from solders.keypair import Keypair

secret_key = "3Tm9N8aRftTP8ki6c7xw7a378cwqq21qsCzembJfuTifKDi6M1JUzyKJQ9pKGLjoQidCwuFvesHRBbp7QyPWchCR"
keypair = Keypair.from_base58_string(secret_key)
message = b"The quick brown fox jumps over the lazy dog"
signature = keypair.sign_message(message)
verify_sign = signature.verify(keypair.pubkey(), message)

print(verify_sign) # bool
