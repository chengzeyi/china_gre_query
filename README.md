# china_gre_query.py

This is a python script program to query all available seats of ETS' GRE Test in China.

## Usage

1. Run `install.sh` or mannual install all the dependencies.
2. Rename `config_example.json` to `config.json` and modify it to set your NEEA ID, password, etc.
    - Filter out the cities you choose (just add or remove items in that list, the default list contains all).
    - Choose out the month you desire.
    - Choose what kind of result you require: full (with sites of no seat) or not (without sites of no seat).
    - Choose the interval of each query (too short may result into the blacklist).
    - Choose the error of the interval (disguise as a human).
3. Execute `china_gre_query.py` and follow the information it prints.

## Warning

When the script prompt you to enter the check code in the web browser, you are only alowed to
enter the check code in the input text area. Do not press your `ENTER` key on that web page.
Instead, back to the CLI and press `ENTER` there and everything will be just fine.

