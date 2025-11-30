import csv

def calculate_gross_pay(pay_rate, hours):
    gross_pay = pay_rate * hours
    return gross_pay

def read_file():

    file_name = "SDev120/final/employee_data.csv"
    try:
        with open(file_name, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row['first_name']) # Access data by column name
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}.")

read_file()



