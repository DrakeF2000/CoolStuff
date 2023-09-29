data = input()

alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
rot13 = ['N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m']
def encrypt(data:str):
    data = list(data)
    output = ""
    for i in range(len(data)):
        if data[i] in alphabet:
            encrypt_location = alphabet.index(data[i])
            output += rot13[encrypt_location]
        else:
            output += data[i]
    return output
print(encrypt(data))