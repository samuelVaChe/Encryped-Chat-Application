from cryptography.fernet import Fernet
import os

# Define the path to the key file as a global variable
key_file = 'encryption_key.key'

def generate_or_load_key():
    # Access the global key_file variable
    global key_file

    # If the key file exists, load the key
    if os.path.exists(key_file):
        with open(key_file, 'rb') as key_file:
            key = key_file.read()
    else:
        # Generate a new key and save it
        key = Fernet.generate_key()
        with open(key_file, 'wb') as key_file:
            key_file.write(key)

    return key

# Use the key
key = generate_or_load_key()
fernet = Fernet(key)

# Rest of your encryption and decryption functions
# ...

# Encrypt and store-Function
def encrypt_file(msg):
    msg=msg.encode()
    encrypted_data = fernet.encrypt(msg)
    print("\nMessage Encrypted\nSending packet for transmission...")
    return encrypted_data

# Decrypt the encrypted data
def decrypt_file(msg):
    decrypted_data = fernet.decrypt(msg)
    decrypted_data = decrypted_data.decode()  # Decode the bytes back to a string
    print("\nDecrypted...")
    return decrypted_data
