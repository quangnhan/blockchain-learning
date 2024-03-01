from solathon import Client, PublicKey

client = Client("https://api.devnet.solana.com")
public_key = PublicKey("B3BhJ1nvPvEhx3hq3nfK8hx4WYcKZdbhavSobZEA44ai")
balance = client.get_balance(public_key)

print(balance)
