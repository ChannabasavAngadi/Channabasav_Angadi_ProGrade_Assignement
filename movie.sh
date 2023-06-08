#!/bin/bash

# Install required packages
sudo apt update
sudo apt install python3-pip -y
sudo apt install postgresql -y
sudo apt install libpq-dev -y

# Upgrade pip
pip3 install --upgrade pip

# Install Python packages
pip3 install pandas
pip3 install psycopg2