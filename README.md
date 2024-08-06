# CS362_ingredient_microservice

This microservice will generate a random ingredient from a pre-defined list of ingredients.

### Install ZeroMQ (Python)
To get started you should install ZeroMQ. Using a terminal, install the package by typing the following command:

_pip install pyzmq_

### Run the Microservice
Using a terminal, type the following command:

_python ingredient_test_program.py_

Using a second terminal, type the following command:

_python run ingredient_server.py_


## How to programmatically REQUEST data from the microservice
To request data from the microservice you will connect to the server via the port and send a string to the microservice requesting a random ingredient be generated. 

            socket = context.socket(zmq.REQ)
            socket.connect("tcp://localhost:5560")

            print(f"Sending request for random ingredient")
            socket.send_string("Generate random recipe ingredient")

## How to programmatically RECEIVE data from the microservice

## UML sequence diagram

![UML](https://github.com/user-attachments/assets/cbfb6f3d-9fb3-482e-9fae-4ccbbc239ad7)
