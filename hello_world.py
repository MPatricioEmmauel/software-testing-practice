"""This module contains functions to greet the user and the main entry point of the program."""


def greet_user(name):
    """Greet the user with their name.

    Args:
        name (str): The name of the user.

    Returns:
        str: A greeting message for the user.
    """
    return f"Hello, {name}!"


def main():
    """Main function that gets user's name and prints a greeting."""
    name = input("Enter your name: ")
    greeting = greet_user(name)
    print(greeting)


if __name__ == "__main__":
    main()
