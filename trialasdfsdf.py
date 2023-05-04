import re
import hash

def fetch_entry():
    print('\033c')
    msg = """google:suru:b"b\x91\x90\xd3z\xa7s6\x182U(\x0f\x17\xd1Mi\x83\tUC\xa86\xb7paS\xe7\x81\xf9\xecI\xb5T\x91\x8bc\x8a(\x8f\xad\x87\x06\x17\xea'\xccCHN\x81\xe5\x17\xda7\x87\x9c-\xe0\xd7\xec\xf2\x17a"
"""
    identifier = input("\t\tsitename/username ")
	#with open("database.txt",mode='rb') as databasefile:
	#	for d in databasefile.readline():
    print(identifier)
    print(msg)
    result = re.findall(r'.{}.'.format(identifier), msg)
    if result:
        print("\n\t\tsearch success")
        print("\n\t\t", result)		
    else:
        print("\n\n\tsearch failure")
	# print("IN PROGRESS")	


fetch_entry()

