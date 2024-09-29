import hashlib

def generate_sha256_hash(data):
  """Generates the SHA-256 hash of the given data."""

  # Create a SHA-256 hash object
  hash_object = hashlib.sha256()

  # Update the hash object with the data
  if isinstance(data, str):
    data = data.encode('utf-8')
  hash_object.update(data)

  # Return the hexadecimal representation of the hash
  return hash_object.hexdigest()

if __name__ == "__main__":
  data_to_hash = input("Enter the data to hash: ")
  hash_value = generate_sha256_hash(data_to_hash)
  print("SHA-256 Hash:", hash_value)