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
To request data from the microservice you will set up the communicaiton channel using zeroMQ and send a string to the microservice requesting a random ingredient be generated. 
Example:

            context = zmq.Context()
            socket = context.socket(zmq.REQ)
            socket.connect("tcp://localhost:5560")
            socket.send_string("Generate random recipe ingredient")

## How to programmatically RECEIVE data from the microservice
To receive data from the microservice you will set up the communicaiton channel using zeroMQ and when the microservice receives a string from the main program, it will process the request and send back a random ingredient in the form of a string back to the main program.
Example:

            socket = context.socket(zmq.REP)
            socket.bind("tcp://localhost:5560")
            if message.decode() == "Generate random recipe ingredient":
                        random_ingredient = random.choice(available_ingredients)
                        socket.send_string(random_ingredient)


## UML sequence diagram

![UML](https://github.com/user-attachments/assets/cbfb6f3d-9fb3-482e-9fae-4ccbbc239ad7)
