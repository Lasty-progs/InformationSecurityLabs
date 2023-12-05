def calculate_checksum(data):
    checksum = sum(data) % 256
    return checksum

def add_checksum(data):
    checksum = calculate_checksum(data)
    data_with_checksum = data + [checksum]
    return data_with_checksum

def verify_checksum(data_with_checksum):
    data = data_with_checksum[:-1]
    checksum = calculate_checksum(data)
    return checksum == data_with_checksum[-1]

# Пример использования:
original_data = [1, 2, 3, 4]
data_with_checksum = add_checksum(original_data)

print("Original Data:", original_data)
print("Data with Checksum:", data_with_checksum)

if verify_checksum(data_with_checksum):
    print("Checksum is valid.")
else:
    print("Checksum is not valid.")
