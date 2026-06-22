#Caesar Cipher
def encrypt_name(full_name,key): 
    encrypted=""
    for char in full_name:
        if char.isupper():
            shifted=(ord(char)-ord("A")+key)%26
            encrypted+=chr(shifted+ord("A"))
        elif char.islower():
            shifted=(ord(char)-ord("a")+key)%26
            encrypted+=chr(shifted+ord("a"))
        else:
            encrypted+=char
    if key%2==0:
       encrypted="".join(reversed(encrypted))
    return encrypted

def decrypt_name(encrypted_text,key):
    if key%2==0:
        encrypted_text="".join(reversed(encrypted_text))
    decrypted=""
    for char in encrypted_text:
        if char.isupper():
            shifted=(ord(char)-ord("A")-key)%26
            decrypted+=chr(shifted+ord("A"))
        elif char.islower():
            shifted=(ord(char)-ord("a")-key)%26
            decrypted+=chr(shifted+ord("a"))
        else:
            decrypted+=char
    return decrypted
full_name="Chimemela Chidinma Uchechukwu."
firstname=full_name.split()[0]
key=len(firstname)
encrypted=encrypt_name(full_name,key)
decrypted=decrypt_name(encrypted,key)
print("Original:",full_name)
print("encrypted:",encrypted)
print("decrypted:",decrypted)

full_name=input("Enter Your Name.")
firstname=full_name.split()[0]
key=len(firstname)
encrypted=encrypt_name(full_name,key)
decrypted=decrypt_name(encrypted,key)
print("Original:",full_name)
print("encrypted:",encrypted)
print("decrypted:",decrypted)