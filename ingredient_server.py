import zmq
import random

context = zmq.Context()

print("Connecting to server")
socket = context.socket(zmq.REP)
socket.bind("tcp://localhost:5560")

available_ingredients = ["honey", "dill", "cinnamon", "sage", "thyme", "chives", "ginger", "walnuts"]
used_ingredients = []

while True:
    message = socket.recv()
    print(f"Received request: {message.decode()}")

    if message.decode() == "Generate random recipe ingredient":

        if len(available_ingredients) == 0:
            available_ingredients = used_ingredients.copy()
            used_ingredients = []

        random_ingredient = random.choice(available_ingredients)
        used_ingredients.append(random_ingredient)
        available_ingredients.remove(random_ingredient)

        socket.send_string(random_ingredient)

    else:
        socket.send_string("Invalid request received")
      
