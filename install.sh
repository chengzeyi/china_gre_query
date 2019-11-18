#!/bin/bash

python3 pip install selenium

sudo apt install firefox
wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz
tar -xvzf geckodriver-v0.24.0-linux64.tar.gz
chmod +x geckodriver
sudo mv geckodriver /usr/bin/
