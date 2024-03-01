from solathon.core.instructions import transfer
from solathon import Client, Transaction, PublicKey, Keypair

client = Client("https://api.devnet.solana.com")

sender = Keypair().from_private_key("your_private_key")
receiver = PublicKey("B3BhJ1nvPvEhx3hq3nfK8hx4WYcKZdbhavSobZEA44ai")
amount = 10000 # This is the amount in lamports

instruction = transfer(
    from_public_key=sender.public_key,
    to_public_key=receiver, 
    lamports=amount
)
transaction = Transaction(instructions=[instruction], signers=[sender])

result = client.send_transaction(transaction)
print(result)
