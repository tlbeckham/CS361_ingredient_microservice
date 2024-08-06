import zmq


def recipe_storage_app():
    stored_recipes = []

    while True:
        print("\nRECIPE STORAGE APP")
        print("------------------")
        print("Enter an option to proceed:")
        print("1. Store a recipe")
        print("2. Generate random ingredient")
        print("All other keys to Exit app\n")

        user_input = input()

        if user_input == "1":
            print("Enter recipe:")
            recipe_input = input()
            stored_recipes.append(recipe_input)

        elif user_input == "2":

            context = zmq.Context()

            print("Connecting to server")
            socket = context.socket(zmq.REQ)
            socket.connect("tcp://localhost:5560")

            print(f"Sending request for random ingredient")
            socket.send_string("Generate random recipe ingredient")

            message = socket.recv()
            print(f"\nReceived random ingredient: {message.decode()}")

        else:
            break


if __name__ == "__main__":
    recipe_storage_app()
