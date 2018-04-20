#####################################################
#                                                   #
#       CS453 Socket programming with python        #
#       TCP Server side                             #
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

while True:
    # Server creates a socket
    serverSocket = socket(AF_INET,SOCK_STREAM)
    # Server binds the socket with port number   
    serverSocket.bind(('',serverPort))
    # Socket starts to receive packets from client
    serverSocket.listen(2)
    # printing out the message that the server is awaiting for packets receiving from the client side
    print ("The TCP server is ready to receive")
    # receiving client socket info and address and storing them
    connectionSocket, addr = serverSocket.accept()
    # decode the message received and store it
    message = connectionSocket.recv(1024).decode()
    # display the message received to console for users
    print ("==>> At Server receved message is: '" + message)
    print ("==>> clientAddress is: " , str(addr[0]) + "/" + str(addr[1]))
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
                connectionSocket.send(str(Success_Code).encode())
                # send back the result to the client
                connectionSocket.send(str(First_Number+Second_Number).encode())
            # elif the Operator is subtraction
            elif Operator=="-":
                # print out the result that will send to the client
                print ("<<== Server send back the result: '" + str(First_Number-Second_Number) + "'")
                # send back the success code to the client
                connectionSocket.send(str(Success_Code).encode())
                # send back the result to the client
                connectionSocket.send(str(First_Number-Second_Number).encode())
            # elif the Operator is multiplication
            elif Operator=="*":
                # print out the result that will send to the client
                print ("<<== Server send back the result: '" + str(First_Number*Second_Number) + "'")
                # send back the success code to the client
                connectionSocket.send(str(Success_Code).encode())
                # send back the result to the client
                connectionSocket.send(str(First_Number*Second_Number).encode())
            # if the Operator is devision
            elif Operator=="/":
                # print out the result that will send to the client
                print ("<<== Server send back the result: '" + str(First_Number/Second_Number) + "'")
                # send back the success code to the client
                connectionSocket.send(str(Success_Code).encode())
                # send back the result to the client
                connectionSocket.send(str(First_Number/Second_Number).encode())
            #technically this else for returning fail code wont be run but in case
            else:
                # print out the result that will send to the client
                print ("<<-- Server send back the result: '" + "-1" + "'\n")
                # send back the fail code to the client
                connectionSocket.send(str(Fail_Code).encode())
                # send back the result to the client
                connectionSocket.send(str(-1).encode())

        else:
            # print out the result that will send to the client
            print ("<<-- Server send back the result: '" + "-1" + "'\n")
            # send back the fail code to the client
            connectionSocket.send(str(Fail_Code).encode())
            # send back the result to the client
            connectionSocket.send(str(-1).encode())
    #Throwing the exception for Value Error
    except ValueError:
        # print out the result that will send to the client
        print ("<<-- Server send back the result: '" + "-1" + "'\n")
        # send back the fail code to the client
        connectionSocket.send(str(Fail_Code).encode())
        # send back the result to the client
        connectionSocket.send(str(-1).encode())
    #Throwing the exception for zero division error
    except ZeroDivisionError:
        # print out the result that will send to the client
        print ("<<-- Server send back the result: '" + "-1" + "'\n")
        # send back the fail code to the client
        connectionSocket.send(str(Fail_Code).encode())
        # send back the result to the client
        connectionSocket.send(str(-1).encode())
    # reset variables for next request.
    Operator = None
    modifiedMessage = None
    First_Number = None
    Second_Number = None
    # after sending out the status code, result and reset the variables, close the socket
    connectionSocket.close()
