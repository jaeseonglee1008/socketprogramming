#####################################################
#                                                   #
#       CS453 Socket programming with python        #
#       UDP Client side                             #
#       Author: Jaeseong Lee 11/11/2017             #
#                                                   #
#####################################################

# import socket module 
from socket import *
# time.sleep() Arguments for timeout test
import time
# local host
serverName ='127.0.0.1'
# define port number for server side which value is greater than 50000 to avoid complicit  
serverPort = 50005
# init Status code. 200 for success and 300 for fail
Status_Code = 0
again = "Y"
#set d value for timeout testing
d = 0.1

try:
    while (again =="y") | (again =="Y"):
        if d<2:
            # creating client socket
            clientSocket = socket(AF_INET, SOCK_DGRAM)
            print("\nEnter an Operation Code (OC) in between two numbers")
            print("OC can be: Addition (+), Subtraction (-), Multiplication (*), and Division (/)")
            print("==>>Example: 3*5 or 3 * 5 .")
            print("Invalid input will return fail code 300")
            print("d value is " + str(d) + ". program will be terminated if d value is bigger than 2")
            message = input("\nInput : ")
            print("\n<<== At Client message to send out: '"+ message)
            # sending out the input string to server
            clientSocket.sendto(message.encode(),(serverName,serverPort))
            # receiving modifiedMessage string and serverAddress
            modifiedMessage, serverAddress =  clientSocket.recvfrom(2048)
            #decode and store status code
            Status_Code = int(modifiedMessage.decode())
            # decode and display status code in console
            print("Status_Code received : "+ str(Status_Code))
            # receiving the 2nd return values which is either answer or -1 for failure.
            modifiedMessage, serverAddress =  clientSocket.recvfrom(2048)
            
            # wait for d seconds
            time.sleep(d)
            # increase the d value as twice for next request.
            d *= 2
            # if client receives success code
            if Status_Code == 200:
                # decode and display the result in console
                print("Result received! ==>> " + message + ": "+ modifiedMessage.decode())
            # if client receives fail code, notify it to users
            else:
                print("Invalid input!!!")
            again = input("Try again? (Y/N)")
        else:
            raise TimeoutError('Timeout error')
except TimeoutError as e:
    print(e + "occured. Server is DEAD")

print ("\n***Client Program Ends***")
clientSocket.close()
