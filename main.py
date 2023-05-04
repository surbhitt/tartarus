from time import sleep

from attr import has
import hash
import os
import re


def menu():

	while 1:
		# print(chr(27)+'[2j')
		# print('\x1bc')
		print('\033c')
		
		menu = """
		_____________________________

			pass manager

		a. create entry
		b. edit entry
		c. delete entry
		d. fetch entry
		e. exit

				"""

		print(menu)	
		raised = 1

		opt = input("\t\tchoose option: ")
		
		if opt == "a":
			raised = create_entry()
			if not(raised):
				print("\n\t\t--entry created--")
			else:
				print("\n\t\t--error raised--")	
			sleep(3)	

		elif opt == "b":
			a = 0
		
		elif opt == "c":
			a = 0

		elif opt == "d":
			fetch_entry()

		elif opt == "e": 
			print("\t\t--exiting--\n")
			exit()
		else: 
			print("\t--choose a valid option--")
			input("\t--press enter--")

	return 0			

# function to create entry
def create_entry():
	print('\033c')
	site = input("\t\tsite: ")
	username = input("\t\tusername: ")
	password = input("\t\tpass: ")
	
	# encrypting the password
	password = hash.encrypt(password)

	data = f"""{site}:{username}:{password}\n"""
	# if os.path.exists("./database.txt"):
	fvar_database = open("database.txt", "a") 
	fvar_database.write(data)
	fvar_database.close()

# function to edit entry 
def edit_entry():
	print("IN PROGRESS")
	return 0

# function to delete entry
def delete_entry():
	print("IN PROGRESS")	
	return 0

# function to fetch entry 
def fetch_entry():
	print('\033c')
	identifier = input("\t\tsitename/username ")
	with open("database.txt",mode='rb') as databasefile:
		for d in databasefile.readlines():
			result = re.findall(r'[\w*]:'+identifier+':[\w*]', d)
	if result:
		print("\n\t\tsearch success")
		#print("\n\t\tthe site name is [", result[0],"] the username is [", result[1],"] the password is[", hash.decrypt(result[2]),"]")		
	else:
		print("\n\n\tsearch failure")
	# print("IN PROGRESS")	
	return 0


#--------------------------------------------------------------------driver function
def main():
	# here check the masterpass

	print('\033c')
		
	if os.path.exists("./masterpass.txt"):
		providedPass = input("\n\n\t\tenter the mpass: ")
		masterpswdfile = open("./masterpass.txt", "r")
		for l in masterpswdfile:
			if hash.match_masterpass(l, providedPass):
				menu()
				
			else: 
				print("\t\t--pass doesn't match--\n")
				exit()
	else:
		hash.create_masterpass()
		menu()



# boilerplate
if __name__=="__main__":
	main()	