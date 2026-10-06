import random
from datetime import datetime

quotes = [
    "Believe in yourself and keep learning!",
    "Every expert was once a beginner.",
    "Small steps every day lead to big results.",
    "Don't give up. Keep trying!",
    "Your hard work will pay off."
]

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why was the computer cold? It left its Windows open!",
    "What do programmers say when they make a mistake? It was a feature!"
]


def calculator():
    print("\n--- Simple Calculator ---")

    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                print("Chatbot: Cannot divide by zero.")
                return
            result = num1 / num2
        else:
            print("Chatbot: Invalid operator.")
            return

        print("Chatbot: Result =", result)

    except ValueError:
        print("Chatbot: Please enter valid numbers.")


def chatbot():

    print("=" * 45)
    print("        🤖 PYTHON CHATBOT")
    print("=" * 45)

    print("Chatbot: Hello! I am your Python chatbot.")
    print("Chatbot: Type 'help' to see what I can do.")
    print("Chatbot: Type 'bye' to end the conversation.")

    name = input("\nChatbot: What is your name? ")

    if name.strip() == "":
        name = "Friend"

    print(f"Chatbot: Nice to meet you, {name}! 😊")

    while True:

        user_input = input(f"\n{name}: ").lower().strip()

        # Exit
        if user_input in ["bye", "exit", "quit"]:
            print(f"Chatbot: Goodbye, {name}! Have a wonderful day! 👋")
            break

        # Greetings
        elif user_input in ["hello", "hi", "hey", "hii", "hai"]:
            responses = [
                f"Hello {name}! 😊",
                f"Hi {name}! How can I help you?",
                f"Hey {name}! Nice to chat with you!"
            ]
            print("Chatbot:", random.choice(responses))

        # How are you
        elif "how are you" in user_input:
            print("Chatbot: I'm doing great! Thanks for asking. 😄")

        # Chatbot name
        elif "your name" in user_input or "who are you" in user_input:
            print("Chatbot: I'm PythonBot, a simple rule-based chatbot!")

        # User name
        elif "my name" in user_input:
            print(f"Chatbot: Your name is {name}. 😊")

        # Time
        elif "time" in user_input:
            current_time = datetime.now().strftime("%I:%M:%S %p")
            print("Chatbot: The current time is", current_time)

        # Date
        elif "date" in user_input or "today" in user_input:
            current_date = datetime.now().strftime("%d-%m-%Y")
            print("Chatbot: Today's date is", current_date)

        # Calculator
        elif "calculate" in user_input or "calculator" in user_input:
            calculator()

        # Motivation
        elif "motivate me" in user_input or "motivation" in user_input:
            print("Chatbot: 💡", random.choice(quotes))

        # Joke
        elif "joke" in user_input:
            print("Chatbot: 😂", random.choice(jokes))

        # Thank you
        elif "thank you" in user_input or "thanks" in user_input:
            print("Chatbot: You're welcome, " + name + "! 😊")

        # Python
        elif "python" in user_input:
            print(
                "Chatbot: Python is a beginner-friendly programming language "
                "used in AI, web development, automation, and data science."
            )

        # AI
        elif user_input == "ai" or "artificial intelligence" in user_input:
            print(
                "Chatbot: AI stands for Artificial Intelligence. "
                "It allows computers to perform tasks that normally require "
                "human intelligence."
            )

        # Fun
        elif "fun" in user_input or "happy" in user_input:
            print("Chatbot: 😄 I'm always ready for a fun conversation!")

        # Help
        elif user_input == "help":
            print("\nChatbot: Here are some things you can ask me:")
            print("  • hello")
            print("  • how are you?")
            print("  • what is your name?")
            print("  • what is my name?")
            print("  • what is the time?")
            print("  • what is today's date?")
            print("  • calculate")
            print("  • motivate me")
            print("  • tell me a joke")
            print("  • tell me about Python")
            print("  • what is AI?")
            print("  • thank you")
            print("  • bye")

        # Unknown input
        else:
            unknown_responses = [
                "I'm still learning. Try asking something from the help menu.",
                "Interesting! I don't understand that yet.",
                "Sorry, I don't have a response for that.",
                "Could you try asking that in a different way?"
            ]

            print("Chatbot:", random.choice(unknown_responses))


if __name__ == "__main__":
    chatbot()