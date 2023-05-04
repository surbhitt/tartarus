import uuid
import hashlib
import sys

def hashText(text):
    """
        Basic hashing function for a text using random unique salt.  
    """
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + text.encode()).hexdigest() + ':' + salt
    
def matchHashedText(hashedText, providedText):
    """
        Check for the text in the hashed text
    """
    _hashedText, salt = hashedText.split(':')
    return _hashedText == hashlib.sha256(salt.encode() + providedText.encode()).hexdigest()


if sys.argv[1] == "-e":
	f = open("master.txt", "w")
	hashed = hashText(sys.argv[2])
	f.write(hashed)
	print(hashed)

elif sys.argv[1] == "-c":
	n = open("master.txt", "r")
	for l in n:
		res = matchHashedText(l, sys.argv[2])
	print(res)
