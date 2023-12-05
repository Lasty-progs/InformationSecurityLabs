def generate_hash(data, key):
    hashed_data = [d ^ k for d, k in zip(data, key)]
    return hashed_data

def encrypt(data, key):
    encrypted_data = generate_hash(data, key)
    return encrypted_data

def decrypt(encrypted_data, key):
    decrypted_data = generate_hash(encrypted_data, key)
    return decrypted_data

# Пример использования:
original_data = [1, 2, 3, 4]
encryption_key = [5, 6, 7, 8]

encrypted_data = encrypt(original_data, encryption_key)
decrypted_data = decrypt(encrypted_data, encryption_key)

print("Original Data:", original_data)
print("Encrypted Data:", encrypted_data)
print("Decrypted Data:", decrypted_data)
