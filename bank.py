import datetime

class Transaction:
    def __init__(self, amount, transaction_type, date=None):
        if transaction_type not in ["debet", "kredyt"]:
            raise ValueError("Invalid transaction type. Use 'debet' or 'kredyt'.")
        self.amount = amount
        self.type = transaction_type
        self.date = date or datetime.datetime.now()

    def __repr__(self):
        return f"Transaction(amount={self.amount}, type='{self.type}', date='{self.date}')"

class BankAccount:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, amount, transaction_type):
        transaction = Transaction(amount, transaction_type)
        self.transactions.append(transaction)
        print(f"Transaction logged: {transaction}")

    def get_transaction_history(self):
        if not self.transactions:
            return "No transactions found."
        return "\n".join(str(transaction) for transaction in self.transactions)

    def calculate_balance(self):
        balance = 0
        for transaction in self.transactions:
            if transaction.type == "kredyt":
                balance += transaction.amount
            elif transaction.type == "debet":
                balance -= transaction.amount
        return balance

# Example usage
if __name__ == "__main__":
    account = BankAccount()
    account.add_transaction(1000, "kredyt")
    account.add_transaction(200, "debet")
    print("\nTransaction History:")
    print(account.get_transaction_history())
    print(f"\nCurrent Balance: {account.calculate_balance()}")
