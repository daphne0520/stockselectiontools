# Stock Selection Tool

The **Stock Selection Tool** is a Python-based application designed to help users retrieve historical stock closing prices and securely store their analysis for future reference. The tool provides an intuitive interface for users to register, log in, and fetch stock data based on a defined date range.

---

## Features

- **User Registration and Authentication**: 
  - Securely register with an email and password.
  - Log in to access the tool’s features.
  
- **Stock Data Retrieval**: 
  - Input a stock ticker (e.g., `1155.KL` for Maybank Malaysia).
  - Specify a start and end date to fetch historical closing prices.

- **Data Storage**: 
  - User interactions and fetched data (email, password, stock ticker, date range, and closing prices) are stored in a CSV file (`users.csv`).
  - View previously saved data for analysis or review.

---

## Requirements
- Python 3.x
- Required Python libraries:
  - `pandas`
  - `yfinance`

---

## Installation

1. Clone the repository:
   git clone https://github.com/yourusername/stock-selection-tool.git
   cd stock-selection-tool

2. Install the required libraries:
pip install pandas yfinance

Run the program:
python main.py

Usage
Register or Log In:

Choose to register with a new email and password or log in with existing credentials.
Fetch Stock Data:

Input the stock ticker symbol, start date, and end date to retrieve historical closing prices.
View Saved Data:

Access previously saved user interactions, including closing prices and associated stock data.
Exit:

Exit the application once your analysis is complete.
