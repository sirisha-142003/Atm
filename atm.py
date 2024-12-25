import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class ATM:
    def __init__(self):
        self.balance = 1000  # Initial account balance
        self.pin = 1234  # Default PIN
        self.transaction_history = []  # List to store transaction history

    def check_balance(self):
        """Function to check account balance"""
        self.transaction_history.append("Checked balance")
        return f"Your current balance is: ${self.balance}"

    def deposit_cash(self, amount):
        """Function to deposit cash into the account"""
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited ${amount}")
            return f"${amount} has been deposited into your account."
        else:
            return "Invalid amount. Please enter a positive value."

    def withdraw_cash(self, amount):
        """Function to withdraw cash from the account"""
        if amount <= 0:
            return "Invalid amount. Please enter a positive value."
        elif amount > self.balance:
            return "Insufficient funds."
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")
            return f"${amount} has been withdrawn from your account."

    def change_pin(self, old_pin, new_pin):
        """Function to change PIN"""
        if old_pin == self.pin:
            if len(str(new_pin)) == 4:  # Ensure the new PIN is 4 digits long
                self.pin = new_pin
                self.transaction_history.append("Changed PIN")
                return "Your PIN has been successfully changed."
            else:
                return "New PIN must be 4 digits."
        else:
            return "Incorrect PIN. Unable to change PIN."

    def view_transaction_history(self):
        """Function to view transaction history"""
        if len(self.transaction_history) == 0:
            return "No transactions to display."
        else:
            return "\n".join(self.transaction_history)

class ATMApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM Machine Simulation")
        self.root.geometry("400x500")
        self.atm = ATM()

        self.pin_entry_var = tk.StringVar()
        self.amount_entry_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        """Creates all the widgets for the ATM GUI."""
        # Style for buttons and labels
        style = ttk.Style()
        style.configure('TButton', width=20, padding=10, font=('Arial', 12), relief="flat")
        style.configure('TLabel', font=('Arial', 12))

        self.pin_label = ttk.Label(self.root, text="Enter PIN:")
        self.pin_label.pack(pady=10)

        self.pin_entry = ttk.Entry(self.root, textvariable=self.pin_entry_var, show="*", width=20, font=('Arial', 12))
        self.pin_entry.pack(pady=10)

        # Buttons with custom light colors
        self.check_balance_button = ttk.Button(self.root, text="Check Balance", command=self.check_balance)
        self.check_balance_button.pack(pady=10)

        self.deposit_button = ttk.Button(self.root, text="Deposit Cash", command=self.deposit)
        self.deposit_button.pack(pady=10)

        self.withdraw_button = ttk.Button(self.root, text="Withdraw Cash", command=self.withdraw)
        self.withdraw_button.pack(pady=10)

        self.change_pin_button = ttk.Button(self.root, text="Change PIN", command=self.change_pin)
        self.change_pin_button.pack(pady=10)

        self.view_history_button = ttk.Button(self.root, text="View Transaction History", command=self.view_history)
        self.view_history_button.pack(pady=10)

        # Define custom colors for the buttons
        style.configure('Blue.TButton', background='#A8DADC', foreground='black')
        style.map('Blue.TButton', background=[('active', '#457B9D'), ('pressed', '#1D3557')])

        style.configure('Green.TButton', background='#A8E6CF', foreground='black')
        style.map('Green.TButton', background=[('active', '#56C8A1'), ('pressed', '#3F9F7F')])

        style.configure('Orange.TButton', background='#FFCCBC', foreground='black')
        style.map('Orange.TButton', background=[('active', '#FF7043'), ('pressed', '#F4511E')])

        style.configure('Yellow.TButton', background='#FFF59D', foreground='black')
        style.map('Yellow.TButton', background=[('active', '#FBC02D'), ('pressed', '#F9A825')])

        style.configure('Purple.TButton', background='#D1C4E9', foreground='black')
        style.map('Purple.TButton', background=[('active', '#9575CD'), ('pressed', '#7E57C2')])

        # Apply the colors to each button
        self.check_balance_button.configure(style='Blue.TButton')
        self.deposit_button.configure(style='Green.TButton')
        self.withdraw_button.configure(style='Orange.TButton')
        self.change_pin_button.configure(style='Yellow.TButton')
        self.view_history_button.configure(style='Purple.TButton')

    def check_balance(self):
        """Checks the balance if the pin is correct."""
        pin = self.pin_entry_var.get()
        if pin == str(self.atm.pin):
            result = self.atm.check_balance()
            self.show_custom_popup("Balance", result)
        else:
            self.show_custom_popup("Error", "Incorrect PIN.")

    def deposit(self):
        """Deposits cash into the account."""
        pin = self.pin_entry_var.get()
        if pin == str(self.atm.pin):
            amount = self.ask_amount("Deposit Cash")
            if amount is not None:
                result = self.atm.deposit_cash(amount)
                self.show_custom_popup("Deposit", result)
        else:
            self.show_custom_popup("Error", "Incorrect PIN.")

    def withdraw(self):
        """Withdraws cash from the account."""
        pin = self.pin_entry_var.get()
        if pin == str(self.atm.pin):
            amount = self.ask_amount("Withdraw Cash")
            if amount is not None:
                result = self.atm.withdraw_cash(amount)
                self.show_custom_popup("Withdraw", result)
        else:
            self.show_custom_popup("Error", "Incorrect PIN.")

    def change_pin(self):
        """Changes the PIN."""
        pin = self.pin_entry_var.get()
        if pin == str(self.atm.pin):
            old_pin = self.ask_for_pin("Enter Old PIN:")
            if old_pin:
                new_pin = self.ask_for_pin("Enter New PIN:")
                if new_pin:
                    result = self.atm.change_pin(old_pin, new_pin)
                    self.show_custom_popup("Change PIN", result)
        else:
            self.show_custom_popup("Error", "Incorrect PIN.")

    def view_history(self):
        """Views the transaction history."""
        pin = self.pin_entry_var.get()
        if pin == str(self.atm.pin):
            result = self.atm.view_transaction_history()
            self.show_custom_popup("Transaction History", result)
        else:
            self.show_custom_popup("Error", "Incorrect PIN.")

    def ask_amount(self, action):
        """Prompts the user to enter an amount."""
        amount = self.ask_for_input(action, "Amount ($):")
        try:
            amount = float(amount)
            if amount > 0:
                return amount
            else:
                self.show_custom_popup("Error", "Amount must be positive.")
                return None
        except ValueError:
            self.show_custom_popup("Error", "Invalid amount. Please enter a valid number.")
            return None

    def ask_for_pin(self, action):
        """Prompts the user to enter a PIN."""
        pin = self.ask_for_input(action, "Enter PIN:")
        try:
            pin = int(pin)
            if len(str(pin)) == 4:
                return pin
            else:
                self.show_custom_popup("Error", "PIN must be 4 digits.")
                return None
        except ValueError:
            self.show_custom_popup("Error", "Invalid PIN. Please enter a numeric value.")
            return None

    def ask_for_input(self, action, prompt):
        """Creates a prompt to ask for user input."""
        input_window = tk.Toplevel(self.root)
        input_window.geometry("300x150")
        input_window.title(action)

        label = ttk.Label(input_window, text=prompt)
        label.pack(pady=10)

        entry = ttk.Entry(input_window, width=20, font=('Arial', 12))
        entry.pack(pady=10)

        result = None

        def submit():
            nonlocal result
            result = entry.get()
            input_window.destroy()

        submit_button = ttk.Button(input_window, text="Submit", command=submit, style='Green.TButton')
        submit_button.pack(pady=10)

        self.root.wait_window(input_window)
        return result

    def show_custom_popup(self, title, message):
        """Creates a custom popup window with a stylish design."""
        popup = tk.Toplevel(self.root)
        popup.title(title)
        popup.geometry("300x200")
        popup.config(bg="#F1FAEE")

        label = ttk.Label(popup, text=message, font=('Arial', 12), background="#F1FAEE")
        label.pack(pady=30)

        close_button = ttk.Button(popup, text="Close", command=popup.destroy, style='Light.TButton')
        close_button.pack(pady=10)

        popup.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = ATMApp(root)
    root.mainloop()
