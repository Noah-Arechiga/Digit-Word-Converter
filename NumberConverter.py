# Main function
def main():
    # Display the menu and get the user's choice
    printMenu()
    choice = inputMenuNumber()

    while choice != 3:
        if choice == 1:
            number = inputNumber()
            print(convertNumberToWord(number))
            main()
        elif choice == 2:
            word = inputWord()
            print(convertWordToNumber(word))
            main()
        else:
            print("Invalid menu choice. Please try again.")
            main()
    if choice == 3:
        print("Goodbye, thanks for using this program!")
        exit()

# Function to display the menu
def printMenu():
    print(" ")
    print("--------------------------------")
    print("1. Convert a Number to a Word")
    print("2. Convert a Word to a Number")
    print("3. Quit")
    print("--------------------------------")
    print(" ")

# Function to get the user's menu choice
def inputMenuNumber():
    number = int(input("Enter a menu number choice: "))

    # Check if the user's choice is valid
    if number < 1 or number > 3 or number != int(number):
        print("Invalid menu choice. Please try again.")
        printMenu()
        inputMenuNumber()
    return number

# Function to get the user's number input in digit form
def inputNumber():
    print("Make sure to enter a positive number that is less than 1,000,000. Example: 1120")
    number = int(input("Enter a number in digit form: "))

    # Check if the user's number is valid
    if number < 0 or number >= 1000000 or number != int(number):
        print(" ")
        print("Invalid number. The number you chose is either negative, greater than 1,000,000, or is not a digit. Please try again.")
        print(" ")
        inputNumber()
    return number

# Function to get the user's number input in word form
def inputWord():
    print("Make sure to enter a number in word form that is less than 1,000,000. Example: five hundred thirty six")
    word = input("Enter a number in word form: ").lower()
    print(" ")

    # Check if the user's word is valid
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    wordList = word.split()
    
    if wordList[0] in ones or wordList[0] in teens or wordList[0] in tens:
        return word
    else:
        print(" ")
        print("Invalid number. The number you chose is not a valid number. Make sure to also check your spelling. Please try again.")
        print(" ")
        inputWord
    
# Function to convert a number in digit form to a number in word form
def convertNumberToWord(number):
    word = ""
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if number == 0:
        word = "zero"
    elif number < 10:
        word = ones[number]
    elif number < 20:
        word = teens[number - 10]
    elif number < 100:
        word = tens[number // 10] + " " + ones[number % 10]
    elif number < 1000:
        word = ones[number // 100] + " hundred " + tens[(number % 100) // 10]
        + " " + ones[number % 10]
    elif number < 10000:
        word = ones[number // 1000] + " thousand " + ones[(number % 1000) // 100]
        + " hundred " + tens[(number % 100) // 10] + " " + ones[number % 10]
    elif number < 100000:
        word = tens[number // 10000] + " " + ones[(number % 10000) // 1000]
        + " thousand " + ones[(number % 1000) // 100] + " hundred "
        + tens[(number % 100) // 10] + " " + ones[number % 10]
    elif number < 1000000:
        word = ones[number // 100000] + " hundred " + tens[(number % 100000) // 10000]
        + " " + ones[(number % 10000) // 1000] + " thousand " + ones[(number % 1000) // 100]
        + " hundred " + tens[(number % 100) // 10] + " " + ones[number % 10]
    else:
        print("Invalid number. Make sure to enter a digit. Please try again.")
        inputNumber()
    return word

# Function to convert a number in word form to a number in digit form
def convertWordToNumber(words):
    word = words.lower()
    number = 0
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    if word == "zero":
        number = 0
    elif word in ones:
        number = ones.index(word)
    elif word in teens:
        number = teens.index(word) + 10
    elif word in tens:
        number = (tens.index(word)) * 10
    else:
        wordList = word.split(" ")
        if len(wordList) == 2:
            if wordList[0] in ones:
                if wordList[1] == "hundred":
                    number = ones.index(wordList[0]) * 100
                elif wordList[1] == "thousand":
                    number = ones.index(wordList[0]) * 1000
            if wordList[0] in teens:
                if wordList[1] == "hundred":
                    number = (teens.index(wordList[0]) + 10) * 100
                elif wordList[1] == "thousand":
                    number = (teens.index(wordList[0]) + 10) * 1000
            if wordList[0] in tens:
                if wordList[1] in ones:
                    number = (tens.index(wordList[0]) * 10) + ones.index(wordList[1])
                elif wordList[1] == "thousand":
                    number = tens.index(wordList[0]) * 10000
        else:
            print("Invalid format. Make sure to check the spelling of your words. Please try again.")
            inputWord()
    return number

# Call the main function
main()
