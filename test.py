def calculate_transactions(initial_amount, num_transactions):
    transactions = []
    factor = 1.25

    for i in range(num_transactions):
        transaction_amount = initial_amount * (factor ** i)
        transactions.append(transaction_amount)

    return transactions

def main():
    total_amount = 1000
    num_transactions = 5

    # Calculate the initial transaction amount
    initial_transaction = total_amount / sum([1.25 ** i for i in range(num_transactions)])

    # Calculate all transactions
    transactions = calculate_transactions(initial_transaction, num_transactions)

    # Print the result
    for i, amount in enumerate(transactions, start=1):
        print(f"Transaction {i}: ${amount:.2f}")

if __name__ == "__main__":
    main()
