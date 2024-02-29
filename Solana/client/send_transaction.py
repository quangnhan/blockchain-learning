from solana.rpc.api import Client
from solders.keypair import Keypair
from solana.transaction import Transaction
from solders.system_program import TransferParams, transfer

LAMPORT_PER_SOL = 1000000000

client: Client = Client("https://api.devnet.solana.com")

# Import private key for sender
sender_private_key = "3Tm9N8aRftTP8ki6c7xw7a378cwqq21qsCzembJfuTifKDi6M1JUzyKJQ9pKGLjoQidCwuFvesHRBbp7QyPWchCR"
sender_pubkey = Keypair.from_base58_string(sender_private_key)

# Wallet address for receiver
receiver_wallet_address = "AhToZmjjLJkP7u1hyNRPeitjgUCHLdpR82P28tecu9An"
receiver_pubkey = receiver_wallet_address

# Amount to send in lamports (0.1 SOL)
amount_to_send = 0.1 * LAMPORT_PER_SOL
client.confirm_transaction(amount_to_send)

# Create transaction
transaction = Transaction().add(transfer(TransferParams(
    from_pubkey=sender_pubkey,
    to_pubkey=receiver_pubkey,
    lamports=1_000_000)
))

# Send transaction
client.send_transaction(transaction)

print("Transaction sent successfully!")
