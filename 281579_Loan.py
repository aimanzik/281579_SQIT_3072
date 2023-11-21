import os

# List to store loan calculations
House_loan_calculations = []

# Set Debt Service Ratio(DSR) threshold
dsr_threshold = 70.0

# Function to calculate monthly installment
def calculate_monthly_installment(principal, annual_interest_rate, loan_term):
    monthly_interest_rate = (annual_interest_rate / 100) / 12
    num_payments = loan_term * 12
    monthly_installment = (principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -num_payments)
    return monthly_installment

# Function to calculate total amount payable
def calculate_total_amount_payable(monthly_installment, loan_term):
    return monthly_installment * loan_term * 12

# Function to calculate Debt Service Ratio(DSR)
def calculate_dsr(housing_loan, other_commitments, monthly_income):
    total_commitments = housing_loan + other_commitments
    dsr = (total_commitments / monthly_income) * 100
    return dsr

# Function to show previous calculation
def display_previous_calculations():
    print("\nPrevious Loan Calculations:")
    for i, calculation in enumerate(House_loan_calculations, start=1):
        print(f"{i}. Principal: ${calculation['principal']}, "
              f"Interest Rate: {calculation['annual_interest_rate']}%, "
              f"Loan Term: {calculation['loan_term']} years, "
              f"Monthly Installment: ${calculation['monthly_installment']:.2f}, "
              f"Total Payable: ${calculation['total_amount_payable']:.2f}, "
              f"DSR: {calculation['dsr']:.2f}%")

# Function to delete previous calculation
def delete_calculation(index):
    if 1 <= index <= len(House_loan_calculations):
        del House_loan_calculations[index - 1]
        print("Calculation deleted.")
    else:
        print("Invalid index.")

# Function to modify Debt Service Ratio(DSR) threshold
def modify_dsr_threshold():
    global dsr_threshold
    new_dsr_threshold = float(input("Enter the new DSR threshold (e.g., 70.0): "))
    if 0 <= new_dsr_threshold <= 100:
        dsr_threshold = new_dsr_threshold
        print(f"DSR threshold updated to {dsr_threshold}%.")
    else:
        print("Invalid DSR threshold. Please enter a value between 0 and 100.")

# Function to define main menu
def main():
    while True:
        print("\nMenu:")
        print("1. Calculate a new loan")
        print("2. Display previous loan calculations")
        print("3. Delete a previous calculation")
        print("4. Modify DSR threshold")
        print("5. Exit")

        choice = input("Enter your choice (Option 1-5): ")

        if choice == '1':
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen
            print("Calculate a New Loan:")
            try:
                principal = float(input("Enter the principal loan amount: $"))
                annual_interest_rate = float(input("Enter the annual interest rate: "))
                loan_term = int(input("Enter the loan term in years: "))
                monthly_income = float(input("Enter the applicant's monthly income: $"))
                other_commitments = float(input("Enter any other monthly financial commitments: $"))
            except ValueError:
                print("Invalid input. Please enter valid numerical values.")
                continue

            monthly_installment = calculate_monthly_installment(principal, annual_interest_rate, loan_term)
            total_amount_payable = calculate_total_amount_payable(monthly_installment, loan_term)
            dsr = calculate_dsr(monthly_installment, other_commitments, monthly_income)

            House_loan_calculations.append({
                'principal': principal,
                'annual_interest_rate': annual_interest_rate,
                'loan_term': loan_term,
                'monthly_installment': monthly_installment,
                'total_amount_payable': total_amount_payable,
                'dsr': dsr
            })

            print("\nLoan Calculation Results:")
            print(f"Monthly Installment: ${monthly_installment:.2f}")
            print(f"Total Amount Payable: ${total_amount_payable:.2f}")
            print(f"DSR: {dsr:.2f}%")

            if dsr <= dsr_threshold:
                print("Congratulations! You are eligible for the loan.")
            else:
                print("Sorry, you are not eligible for the loan based on the Debt Service Ratio (DSR).")

        elif choice == '2':
            display_previous_calculations()

        elif choice == '3':
            display_previous_calculations()
            try:
                index_to_delete = int(input("Enter the number of loan of the calculation to delete: "))
                delete_calculation(index_to_delete)
            except ValueError:
                print("Invalid input. Please enter a valid numerical index.")

        elif choice == '4':
            modify_dsr_threshold()

        elif choice == '5':
            print("Exiting the program.")
            input("Press Enter to exit..... BYE-BYE ^_^")
            os._exit(0)

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()