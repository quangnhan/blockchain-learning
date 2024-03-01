from solathon import Client, Keypair

client = Client("https://api.devnet.solana.com")

new_account = Keypair()
print(new_account.public_key, new_account.private_key)
amount = 10000  # This is the amount in lamports

res = client.request_airdrop(new_account.public_key, amount)
print("Airdrop response: ", res)
