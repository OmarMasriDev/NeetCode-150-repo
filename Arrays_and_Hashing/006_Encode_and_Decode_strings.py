class StrCodec:
    def encode(self, strs):
        # Encodes a list of string to a single string
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + ":" + s # Store length and string
        return encoded_string
    
    def decode(self, s):
        # Decodes a single string to a list of strings
        i = 0
        decoded_string =[]

        while i < len(s):
            j = s.find(":", i) # Find position of colon
            length = int(s[i:j]) # Get length of next string
            i = j + 1 # Move past the colon
            decoded_string.append(s[i:i+length])
            i += length # Move to the next encoded sec
        return decoded_string
    
# Example:
codec = StrCodec()
original = ["hello", "world", "python", "1234"]
encoded = codec.encode(original)
decoded = codec.decode(encoded)

print("Encoded:", encoded)
print("Decoded:", decoded)
