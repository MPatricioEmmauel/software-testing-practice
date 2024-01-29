def greet_user(name):
    """ Function to greet the user """
    return f"Hello, {name}!"

def main():
    name = input("Enter your name: ")

    greeting = greet_user(name)
    print(greeting)

if __name__ == "__main__":
    main()
