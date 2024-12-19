import pandas as pd
import yfinance as yf
import os
import csv

# User data file
USER_DATA_FILE = "users.csv"

# Register a new user
def register_user(email, password):
    if not os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Email", "Password"])

    with open(USER_DATA_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([email, password])
    print("Registration successful!")

# Authenticate user
def authenticate_user(email, password):
    if not os.path.exists(USER_DATA_FILE):
        print("No users registered yet. Please register first.")
        return False
    
    with open(USER_DATA_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Email'] == email and row['Password'] == password:
                print("Login successful!")
                return True
    print("Invalid email or password.")
    return False

# Fetch closing prices
def get_closing_prices(ticker, start_date, end_date):
    try:
        data = yf.download(ticker, start=start_date, end=end_date)
        closing_prices = data['Close']
        print(f"Closing prices for {ticker}:\n{closing_prices}")
        return closing_prices
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

# Analyze closing prices
def analyze_closing_prices(data):
    average = data.mean()
    percentage_change = ((data[-1] - data[0]) / data[0]) * 100
    highest = data.max()
    lowest = data.min()
    results = {
        "Average Closing Price": average,
        "Percentage Change": percentage_change,
        "Highest Closing Price": highest,
        "Lowest Closing Price": lowest
    }
    return results

# Save data to CSV
def save_to_csv(data, filename):
    df = pd.DataFrame([data])
    if not os.path.exists(filename):
        df.to_csv(filename, index=False)
    else:
        df.to_csv(filename, mode='a', header=False, index=False)
    print("Data saved successfully!")

# Read from CSV
def read_from_csv(filename):
    if not os.path.exists(filename):
        print("No data available.")
        return
    data = pd.read_csv(filename)
    print("Saved Data:")
    print(data)
