#####################################################
#                                                   #
#       CS453 Socket programming with python        #
#       UDP Server side                             #
#       Author: Jaeseong Lee 11/11/2017             #
#                                                   #
#####################################################

# import socket module 
from socket import *
# define port number for server side which value is greater than 50000 to avoid complicit  
serverPort = 50005
# success code will be sent out to client if the operation is success
Success_Code = 200
# fail code will be sent out to client if the operation is failed
Fail_Code =300
# init Operator
Operator = None
# init modifiedMessage
modifiedMessage = None



# Server creates a socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Server binds the socket with port number  
serverSocket.bind(('', serverPort))
# printing out the message that the server is awaiting for packets receiving from the client side
print ("The UDP server is ready to receive")
while True:
    # receiving client socket info and address and storing them
    message, clientAddress = serverSocket.recvfrom(2048)
    # display the message received and client address on the console for users
    print ("==>> At Server receved message is: '" + message.decode() + "'  ")
    print ("==>> clientAddress is: " , str(clientAddress[0]) + "/" + str(clientAddress[1]))
    #decode the encoded input string to verify operator
    message = message.decode()
    # try - raise - exception
    try:
        # verify and store operator and digits
        if "+" in message:
            modifiedMessage = message.split("+")
            Operator = "+"
        elif "-" in message:
            modifiedMessage=message.split("-")
            Operator = "-"
        elif "*" in message:
            modifiedMessage=message.split("*")
            Operator = "*"
        elif "/" in message:
            modifiedMessage=message.split("/")
            Operator = "/"
       
        # if there is no operator from the string received, return fail code and run again.
        # and the length of modifiedMessage should be 2 or return fail code.
        if Operator != None and len(modifiedMessage) ==2 :
            # storing first value
            First_Number = int(modifiedMessage[0])
            # storing second value
            Second_Number = int(modifiedMessage[1])
            # if the Operator is addition
            if Operator=="+":
                # print out the result that will send to the client
                print ("<<== Server send back the result: '" + str(First_Number+Second_Number) + "'")
                # send back the success code to the client
                serverSocket.sendto(str(Success_Code).encode(), clientAddress)
                # send back the result to the client
                serverSocket.sendto(str(First_Number+Second_Number).encode(), clientAddress)
            # if the Operator is subtraction
            elif Operator=="-":
                # print out the result that will send to the client
                print ("<<== Server send back the result: '" + str(First_Number-Second_Number) + "'")
                # send back the success code to the client
                serverSocket.sendto(str(Success_Code).encode(), clientAddress)
                # send back the result to the client
                serverSocket.sendto(str(First_Number-Second_Number).encode(), clientAddress)
            # if the Operator is multiplication
            elif Operator=="*":
                # print out the result that will send to the client
                print ("<<== Server send back the result: '" + str(First_Number*Second_Number) + "'")
                # send back the success code to the client
                serverSocket.sendto(str(Success_Code).encode(), clientAddress)
                # send back the result to the client
                serverSocket.sendto(str(First_Number*Second_Number).encode(), clientAddress)

            # if the Operator is devision
            elif Operator=="/":
                # print out the result that will send to the client
                print ("<<== Server send back the result: '" + str(First_Number/Second_Number) + "'")
                # send back the success code to the client
                serverSocket.sendto(str(Success_Code).encode(), clientAddress)
                # send back the result to the client
                serverSocket.sendto(str(First_Number/Second_Number).encode(), clientAddress)
            else:
                # print out the result that will send to the client
                print ("<<-- Server send back the result: '" + "-1" + "'\n")
                # send back the fail code to the client
                serverSocket.sendto(str(Fail_Code).encode(), clientAddress)
                # send back the result to the client
                serverSocket.sendto(str(-1).encode(), clientAddress)
        else:
            # print out the result that will send to the client
            print ("<<-- Server send back the result: '" + "-1" + "'\n")
            # send back the fail code to the client
            serverSocket.sendto(str(Fail_Code).encode(), clientAddress)
            # send back the result to the client
            serverSocket.sendto(str(-1).encode(), clientAddress)
    #Throwing the exception for Value Error
    except ValueError:
        # print out the result that will send to the client
        print ("<<-- Server send back the result: '" + "-1" + "'\n")
        # send back the fail code to the client
        serverSocket.sendto(str(Fail_Code).encode(), clientAddress)
        # send back the result to the client
        serverSocket.sendto(str(-1).encode(), clientAddress)
    #Throwing the exception for zero division error
    except ZeroDivisionError:
        # print out the result that will send to the client
        print ("<<-- Server send back the result: '" + "-1" + "'\n")
        # send back the fail code to the client
        serverSocket.sendto(str(Fail_Code).encode(), clientAddress)
        # send back the result to the client
        serverSocket.sendto(str(-1).encode(), clientAddress)
    # reset variables for next request.
    Operator = None
    modifiedMessage = None
    First_Number = None
    Second_Number = None
