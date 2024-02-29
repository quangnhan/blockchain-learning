from solders.keypair import Keypair

secret_key = "3Tm9N8aRftTP8ki6c7xw7a378cwqq21qsCzembJfuTifKDi6M1JUzyKJQ9pKGLjoQidCwuFvesHRBbp7QyPWchCR"
keypair = Keypair.from_base58_string(secret_key)
print(f"Created Keypair with public key: {keypair.pubkey()}")