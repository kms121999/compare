# User prompts
NUM1_PROMPT = "Please, enter the first number: "
NUM2_PROMPT = "Please, enter the second number: "

def main():
    # Get the first number
    firstNumber = getInt(NUM1_PROMPT)
    # Get the second number
    secondNumber = getInt(NUM2_PROMPT)

    # Compare the numbers
    if firstNumber > secondNumber:
        print("num 1 is bigger than num 2")
    elif secondNumber > firstNumber:
        print("num 2 is bigger than num 1")
    elif firstNumber == secondNumber:
        print("num 1 is equal to num 2")


def getInt(prompt):
    # Initialize variables
    userInput = ''

    # While the no valid user input
    while userInput == '':
        try:
            # Prompt for input and attempt to convert to int
            userInput = int(input(prompt))
        except ValueError:
            pass

    # Return the user's input in int form
    return userInput

# Call main
main()
