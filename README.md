# china_gre_query.py

This is a Python script program to query all available seats of ETS' GRE Test in China.

## Usage

1. Run `install.sh` or mannually install all the dependencies.
    - Mannual installation is recommended, since the environment of the systems varies.
    - Prerequisites include Python3, Selenium, Firefox and a driver (geckodriver).
2. Rename `config_example.json` to `config.json` and modify it to set your NEEA ID, password, etc.
    - Filter out the cities you choose (just add or remove items in that list, the default list contains all).
    - Choose the month you desire.
    - Choose what kind of result you require: full (with sites of no seat) or not (without sites of no seat).
    - Choose the interval of each query (or too short may result into being blocked).
    - Choose the error of the interval (to disguise as a human).
3. Execute `china_gre_query.py` and follow the information it prints.

## Warning

When the script prompts you to enter the check code in the web browser, you are only alowed to
enter the check code in the input text area. Do not press your `ENTER` key on that web page.
Instead, go back to the CLI and press `ENTER` there and everything will be just fine.

