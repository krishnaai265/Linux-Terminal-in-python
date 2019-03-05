import os
import re
import sys
import atexit

os.chdir('/')

print('$> <starting your application...>')
ulocation = 'PATH: /'
olocation = '/tmp/secret'

def exit_handler():						   # handle halt of the program and wirte "Good bye"
    print('GOOD BYE')

# create initial temparary directory
def create_folder(location):                             
	global olocation
	if not os.path.exists(olocation):
    		os.makedirs('/'+olocation)

#create new folder, called multiple times
def create_folder2(location):                            
	global olocation
	if os.path.exists(olocation):
		print('ERR: DIRECTORY ALREADY EXIST')              # Error if folder is exist
	else:
		os.makedirs(olocation)
		print('SUCC: CREATED')                             # Success if folder is created

#use if you want to create files
'''def create_file(my_file):                                       
	if my_file.is_file():
		print('ERR: DIRECTORY ALREADY EXIST')
'''

# remove location
def rlocation(location):
	global olocation
	os.rmdir(olocation+'/'+location)                           # location + file name(that user enter on console)
	print('SUCC: DELETED')					   # Folder successfully deleted

# modify location
def mlocation(location):
	global olocation
	global ulocation
	olocation = olocation+'/'+location			   # original internal directory
	ulocation = ulocation+'/'+location		           # user display directory

# back to location(you can also use it if you want to implement cd ..)
def blocation():
	global olocation					   
	global ulocation
	olocation="/".join(olocation.split("/")[:-1])	           # split by / and go back to that location
	ulocation = "/".join(ulocation.split("/")[:-1])

# cd command 
def clocation(location):
	if os.path.exists(olocation+'/'+location):		   # check whether directory is exist or not
		mlocation(location)
		print('SUCC: REACHED')				   # Successful if directory found
	else:
		print('ERR: INVALID PATH')

# list all the subdirectories inside current directory(you can use it in loop to display neighbhood folders subdirectories)
def list_directory():
	global olocation
#	a = os.walk(olocation)
	a = os.listdir(olocation)
	print(' '.join(a))

create_folder(olocation) 		                          # create initial temparary directory

atexit.register(exit_handler) 					  # run script when program close

try:								  # handle if any error is occur
	while True:

		name = input("$> ")
		name.replace('/','')						# avoid input display error

		# print current directory on console "pwd"	
		if name == 'pwd':
			print(ulocation.replace("///","/").replace("//","/"))   # print current location and avoid to print double /

		# create directory "mkdir"
		elif ''.join(name.split(" ",1)[:1]) == 'mkdir':		
			for i in name.split(" ")[1:]:				# create folders one by one
				mlocation(i)
				create_folder2(olocation)
				blocation()

		# list all the directories "ls"
		elif name == 'ls':
			list_directory()

		# go to location "cd"
		elif ''.join(name.split(" ",1)[:1]) == 'cd':
			for i in name.split(" ")[1:]:				# get enterred folder name
				clocation(i)

		# remove directory "rm"
		elif ''.join(name.split(" ",1)[:1]) == 'rm':
			for i in name.split(" ")[1:]:				# Remove directory
				rlocation(i)

		elif name == 'session clear':
			ulocation = 'PATH: /'
			olocation = '/tmp/secret'	
			print('SUCC: CLEARED: RESET TO ROOT')	
		
		# exit from application "exit"
		elif name == 'exit':
			sys.exit(0)

		# take help
		elif name == "help":
			print('pwd \t display current directory')
			print('mkdir \t create new directory')
			print('ls \t display subdirectories of current directories')
			print('cd \t change current directory')
			print('rm \t remove current directory')
			print('session clear \t go back to root directory')
			print('exit \t exit')

		else:
			print("ERR: CANNOT RECOGNIZE INPUT.")

except KeyboardInterrupt:						# prevent ctrl - c to display any error 
	print('')

#print(chr(27) + "[2J")                                                 # use if you want to clear console
#print('Welcome to Krishna's Console') 
#print('Phone no=+91-9456611186')
#print('Email=mymitedu.krishna@gmail.com')
#print('Expert in JAVA, GOLANG and PYTHON')
#print('-------------------Solution-----------------------')
