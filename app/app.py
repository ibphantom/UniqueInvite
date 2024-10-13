from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

# Generate RSA keys (use only once for setting up)
key = RSA.generate(4096)
private_key = key.export_key()
public_key = key.publickey().export_key()

# Encrypt with RSA (4096-bit)
def encrypt_rsa(data, public_key):
    rsa_key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    encrypted_data = cipher.encrypt(data.encode('utf-8'))
    return base64.b64encode(encrypted_data).decode('utf-8')

# Example usage for username and password
encrypted_username = encrypt_rsa("admin", public_key)
encrypted_password = encrypt_rsa("supersecretpassword", public_key)

print(f"Encrypted Username: {encrypted_username}")
print(f"Encrypted Password: {encrypted_password}")
