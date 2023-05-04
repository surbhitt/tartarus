import os
import uuid
import hashlib
import rsa
# from rsa.key import PublicKey



#--------------------------------------------------------------for masterpass
def hash_masterpass(masterpswd):
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + masterpswd.encode()).hexdigest() + ':' + salt    

def match_masterpass(hashedText, providedText):
    _hashedText, salt = hashedText.split(':')
    return _hashedText == hashlib.sha256(salt.encode() + providedText.encode()).hexdigest()

def create_masterpass():
    masterpswd = input("\n\n\t\tcreate master password: ")
    masterpassfile = open("./masterpass.txt", "w") 
   
    masterpassfile.write(hash_masterpass(masterpswd))
    masterpassfile.close()
    return 0


#-------------------------------------------------------------------for keys 

# checking the existance of key file
if os.path.exists("./prvkfile.pem"):
    with open('prvkfile.pem', mode='rb') as prvkfile:
        keydata = prvkfile.read()
    privateKey = rsa.PrivateKey.load_pkcs1(keydata)

    with open('pblkfile.pem', mode='rb') as pblkfile:
        keydata = pblkfile.read()
    publicKey = rsa.PublicKey.load_pkcs1(keydata)    


# if key file does not exit create one
else:    
    publicKey, privateKey = rsa.newkeys(512)
    with open("prvkfile.pem","w") as prvkfile:
        prvkfile.write(privateKey.save_pkcs1().decode('utf-8'))
    with open("pblkfile.pem","w") as pblkfile:
        pblkfile.write(publicKey.save_pkcs1().decode('utf-8'))

# function to encrypt the text
def encrypt(password):
    return rsa.encrypt(password.encode(), publicKey)

# function to decrypt the text
def decrypt(password):
    return rsa.decrypt(password, privateKey).decode()
        

