from database import Database
from models import Customer, Currency, CurrencyExchange

def menu():
    print("\n==== Currency Exchange System ====")
    print("1. Create Customer")
    print("2. View Customers")
    print("3. Create Currency")
    print("4. View Currencies")
    print("5. Create Currency Exchange")
    print("6. View Exchange Records")
    print("9. Exit !")

def main():
    database = Database()
    database.create_tables()

    menu()

    while(1):
        choice = input("Enter a number to select the menu (1 - 9): ")

        if choice == '1':
            name = input("Enter customer name: ")
            email = input("Enter email address: ")
            phone = input("Enter phone number:")

            customer = Customer()
            customer.create_customer(name, email, phone)

        elif choice == '2':
            customer = Customer()
            customers = customer.view_customers()

            for customer in customers:
                print(customer)

        elif choice == '3':
            code = input("Enter currency code: ")
            name = input("Enter currency name: ")
            ex_rate = input("Enter exchange rate: ")

            currency = Currency()
            currency.create_currency(code, name, ex_rate)

        elif choice == '4':
            currency = Currency()
            currencies = currency.view_currencies()

            for currency in currencies:
                print(currency)

        elif choice == '5':
            customer_id = input("Enter customer ID: ")
            from_value = input("Enter currency amount for exchange (Eg: USD 100): ")
            to_currency_code = input("Enter currency code to exchange (Eg: NZD): ")

            from_currency_code, from_amount = from_value.split()

            currency = Currency()
            rows = currency.view_currency_by_code(from_currency_code)
            from_exchange_rate = rows[0][3]

            currency = Currency()
            rows = currency.view_currency_by_code(to_currency_code)
            to_exchange_rate = rows[0][3]

            to_amount = (float(from_amount) * from_exchange_rate) / to_exchange_rate
            
            currency_exchange = CurrencyExchange()
            currency_exchange.create_currency_exchange(customer_id, from_currency_code, to_currency_code, from_amount, to_amount)

            print(f"Converted Amount: {to_currency_code} {to_amount} \n")

        elif choice == '6':
            currency_exchange = CurrencyExchange()
            rows = currency_exchange.view_currency_exchange()

            for row in rows:
                print(row)

        elif choice == '9': # Exit
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


            

if __name__ == "__main__":
    main()