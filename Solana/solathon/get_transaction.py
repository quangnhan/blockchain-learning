from solathon import Client

client = Client("https://api.devnet.solana.com")
transaction_signature = "3ufa2bEAA6fFjyDqCNxiZvWjqwzfPiPqwXJrKwtHCHpakndafFyFMGrnVJYSTaxnVYKLczyHexfPGrmfzpZUzvfR"
transaction = client.get_transaction(transaction_signature)

print(dir(transaction))
