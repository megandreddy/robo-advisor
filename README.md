# Robo-advisor Project

A tool which accepts stcok inputs, accesses lives data, and gives a recommendation as to whether one should purchase a stock. Automates the process of making stock recommendations.

# prerequisites


Anaconda 3.7+
Python 3.7+
Pip


# Installation instructions:


Navigate from the command line and then create and activate an anaconda environment called stocks-env:

cd my-first-python-app

conda create -n stocks-env python=3.8 # (first time only) -->
conda activate stocks-env

Next, install required packages:

pip install -r requirements.txt


# Setup instructions:


Obtain free API key from https://www.alphavantage.co/
create a your own .env file in the root directory of local repository and set an environmental variable called ALPHAVANTAGE_API_KEY
place ALPHAVANTAGE_API_KEY = your API key in your .env fil


# Usage instructions:


Input a valid stock symbol between 1-5 characters


# Run the program to recieve recommendation of whether to buy, sell, or hold the selected stock:


python app/robo_advisor.py 

