import hash
"""
f = open("trial1.txt","r")
a, b = f.read().split()
print(a+"\n"+ b)
"""

"""
publicKey, privateKey = "trial1", "trial2" 
fvar_key = open("trial1.txt", "w")
fvar_key.write(publicKey)
fvar_key.write(privateKey)
# fvar_key.write()

fvar_keyq = open("trial1.txt", "r+")
# a = fvar_keyq.readlines()
print(fvar_keyq.read())
"""
p = b'0\xc4\x8b\xcc\xfeWN\r\xc6\x04^\n\xfa\xcdd\xe1V\x99\xd6 \xc5q\x8bN\xfeHS\xee,\xde1\x0b\xcaT\x05U\x98\xfc}\xaf\xd8;@\x90R\xf0\xf3Q;\xce<\xdf\xcf\x19Qd\xd2s\x0f^\x89\xcf.^'
print("hte pass is " + hash.decrypt(p))