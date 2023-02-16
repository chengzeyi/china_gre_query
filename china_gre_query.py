#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import io
import time
import random
from selenium import webdriver


CONFIG_FILE = './config.json'
BROWSER_WAIT_TIME = 5

HOST = 'gre.etest.net.cn'
FRONT_PAGE_URL = f'https://{HOST}'
BASE_LOGIN_URL = f'https://{HOST}/login.do'
BASE_QUERY_URL = f'https://{HOST}/testSites.do'


class UserInfo(object):

    def __init__(self, config_file):
        with open(config_file, 'r') as fp:
            obj = json.load(fp)
            self.neea_id = obj['neea_id']
            self.password = obj['password']
            self.ym = obj['ym']
            self.cities = obj['cities']
            self.cities_names = obj['cities_names']
            self.full_result = obj['full_result']
            self.query_interval = obj['query_interval']
            self.query_interval_error = obj['query_interval_error']


def login(browser, user_info):
    # dcap = dict(DesiredCapabilities.PHANTOMJS)
    # dcap['phantomjs.page.settings.userAgent'] = (
    #     'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    # )

    browser.get(FRONT_PAGE_URL)
    browser.implicitly_wait(BROWSER_WAIT_TIME)

    neea_id_input = browser.find_element_by_id('neeaId')
    neea_id_input.clear()
    neea_id_input.send_keys(user_info.neea_id)
    password_input = browser.find_element_by_id('password')
    password_input.clear()
    password_input.send_keys(user_info.password)

    check_image_code_input = browser.find_element_by_id('checkImageCode')
    check_image_code_input.click()
    check_image_code_input.clear()
    input('Enter check code then press the <ENTER> key to continue...')
    browser.execute_script('login();')
    time.sleep(BROWSER_WAIT_TIME)


def query(browser, user_info):
    req_url = BASE_QUERY_URL
    req_url += '?p=testSites'
    req_url += '&m=ajax'
    req_url += f'&ym={user_info.ym}'
    req_url += f'&neeaID={user_info.neea_id}'
    req_url += f"&cities={'%3B'.join(user_info.cities)}"
    req_url += f"&citiesNames={'%3B'.join(user_info.cities_names)}"
    req_url += '&whichFirst=AS'
    req_url += '&isFilter=0'
    req_url += '&isSearch=1'
    browser.get(req_url)
    raw_json = browser.find_element_by_id('json').text
    obj = json.loads(raw_json)

    has_seat_list = []
    no_seat_list = []
    for item in obj:
        for date in item['dates']:
            for site in date['sites']:
                if not user_info.full_result and site['realSeats'] == 0:
                    continue
                bjtime = site['bjtime']
                province = site['province']
                city = item['city']
                site_name = site['siteName']
                if site['realSeats'] == 0:
                    no_seat_list.append(f'[{bjtime}|{province}|{city}|{site_name}]')
                else:
                    has_seat_list.append(f'[{bjtime}|{province}|{city}|{site_name}]')

    if user_info.full_result:
        if no_seat_list:
            print('<No Seat>:')
            print('\n'.join(no_seat_list))
        else:
            print('<The query result of sites without available seats is empty>')
    if not has_seat_list:
        print('<The query result of sites with available seats is empty>')
    else:
        print('<Has Seat>:')
        print('\n'.join(has_seat_list))


def main():
    browser = webdriver.Firefox()
    user_info = UserInfo(CONFIG_FILE)
    login(browser, user_info)
    while True:
        try:
            query(browser, user_info)
        except Exception as e:
            print(e)
            login(browser, user_info)
            continue
        print('Query again after %d second(s)' % user_info.query_interval)
        time.sleep(user_info.query_interval + random.randint(
            -user_info.query_interval_error, user_info.query_interval_error))


if __name__ == '__main__':
    main()

