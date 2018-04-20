#####################################################
#													#
#		CS453 Socket programming with python		#
#		TCP Client side								#
#		Author: Jaeseong Lee 11/11/2017				#
#													#
#####################################################

# import socket module 
from socket import *
# local host
serverName ='127.0.0.1'
# define port number for server side which value is greater than 50000 to avoid complicit  
serverPort = 50005
# init Status code. 200 for success and 300 for fail
Status_Code = 0
again = "Y"
while (again =="y") | (again =="Y"):
	# creating client socket
	clientSocket = socket(AF_INET, SOCK_STREAM)
	# addressing for connection
	clientSocket.connect((serverName,serverPort))
	print("\nEnter an Operation Code (OC) in between two numbers")
	print("OC can be: Addition (+), Subtraction (-), Multiplication (*), and Division (/)")
	print("==>>Example: 3*5 or 3 * 5 .")
	print("Invalid input will return fail code 300")
	message = input("\nInput : ")
	print("\n==>> At Client message to send out: '"+ message)
	# sending out the input string to server
	clientSocket.send(message.encode())
	# receiving the first return string which is Status code
	modifiedMessage = clientSocket.recv(1024)
	# decoding status code
	Status_Code = int(modifiedMessage.decode())
	# decode and display status code in console
	print("Status_Code received : "+ str(Status_Code))
	# receiving the 2nd return values which is either answer or -1 for failure.
	modifiedMessage = clientSocket.recv(1024)
	# if client receives success code
	if Status_Code == 200:
		# decode and display the result in console
		print("Result received! ==>> " + message + ": "+ modifiedMessage.decode() + "\n")
	# if client receives fail code, notify it to users
	else:
		print("Invalid input!!!")
	again = input("Try again? (Y/N)")
print ("\n***Client Program Ends***")
clientSocket.close()
