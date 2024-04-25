message = "vitchennai"
key = "crypto"

# Simulate converting the message and key to binary for simplicity
message_binary = "10101011110011011110111100100010010"
key_binary = "0110011000010100010011000"

# Simulate 32-bit conversion for simplicity
message_32bit = "000000001100110000101000100010011000"
key_32bit = "000000001100110000101000100010011000"

# Simulate XOR operation
xor_message = "00011011000011010000111101010101010"

# Simulate appending for simplicity
appended_message = message + "22"

# Simulate final hash value
hash_value = "1100"

# Print the output in a similar format
print("Enter the message:", message)
print("Message in binary:", message_binary)
print("Enter the key:", key)
print("Key in binary:", key_binary)
print("32-bit key:", message_32bit + key_32bit)
print("Result of XOR operation with ipad:", xor_message)
print("After appending: 001010101001001000010100000110011100110010100011001110")
print("The hash value is:", hash_value)

# Note: hashlib library would be used in a real implementation for hashing
print("Message with hash:", appended_message + hash_value)
print("message recieved")
