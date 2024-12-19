from functions import *
import getpass
import datetime

# User interaction starts here
def main():
    print("Welcome to the Stock Selection Tool!")
    logged_in = False

    # User Registration or Login
    while not logged_in:
        print("\n1. Register\n2. Login")
        choice = input("Choose an option (1/2): ")
        if choice == '1':
            email = input("Enter your email: ")
            password = getpass.getpass("Enter your password: ")
            register_user(email, password)
        elif choice == '2':
            email = input("Enter your email: ")
            password = getpass.getpass("Enter your password: ")
            logged_in = authenticate_user(email, password)
        else:
            print("Invalid choice. Please try again.")

    # Stock Analysis Menu
    while True:
        print("\n1. Fetch Stock Data\n2. View Saved Data\n3. Exit")
        option = input("Choose an option (1/2/3): ")

        if option == '1':
            ticker = input("Enter stock ticker (e.g., 1155.KL): ")
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")

            try:
                closing_prices = get_closing_prices(ticker, start_date, end_date)
                if closing_prices is not None:
                    results = analyze_closing_prices(closing_prices)
                    print("\nAnalysis Results:")
                    for key, value in results.items():
                        print(f"{key}: {value:.2f}")

                    # Save interaction to CSV
                    user_data = {
                        "Email": email,
                        "Ticker": ticker,
                        "Start Date": start_date,
                        "End Date": end_date,
                        **results
                    }
                    save_to_csv(user_data, "users.csv")
            except Exception as e:
                print(f"Error: {e}")

        elif option == '2':
            read_from_csv("stock_analysis.csv")

        elif option == '3':
            print("Thank you for using the Stock Selection Tool!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
