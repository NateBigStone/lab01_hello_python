import datetime

"""
Write a program that asks for your name and the month you were born in.
Then, your program should print
    A greeting to you, using your name
    A message with the number of letters in your name
    A 'Happy birthday month!' message if you were born in August
"""

def birthday():
    #Get today's date
    today = datetime.datetime.now()
    #Get month as a number
    today_number = str(today.month)
    #Get month as a name and just the first three letters
    today_word = today.strftime("%B").lower()[:3]
    #User enters their name
    name = input("Please enter your name:\n")
    #User enters their birthday month
    birthday_month = input("Please enter your birthday month:\n")
    #Convert birthday input to string and lowercase
    str(birthday_month).lower()
    #Get the length of the user's name
    name_length = len(name)
    #Convert the length of the name to string before printing
    length_string = str(name_length)
    #Print the person's name
    print("Hello " + name + "!")
    #Wish the person a happy birthday if their birthday month is this month
    if today_word in str(birthday_month).lower() or today_number == birthday_month:
        print("Happy Birthday Month!")
    #Print the length of the user's name
    print(f"There are {length_string} letters in your name")


if __name__ == "__main__":
    birthday()
