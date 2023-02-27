# print("hello world")

#Use a variable to store a number, then write a condition that prints -1 if the number is less than 10, prints 1 if the number is greater than 10, and prints 0 if the number is equal to 10.


# var = 9
# if var < 10:
#   print (-1)
# elif var > 10:
#   print(1)
# else:
#   print(0)

#Use variables to store two numbers, then write a condition that prints 1 if the numbers are both less than 10, and prints 0 otherwise.
# digit1 = 9
# digit2 = 11
  
# if ((digit1< 10) and (digit2< 10)):
#     print(-1)
# else:
#     print(0)

# 4. Use a variable to store a number, then write a condition that prints 1 if the number is over 9000, and prints -1 otherwise.
# var = 900

# if (var>9000):
#     print(1)
# else:
#     print(-1)

 # 5. Use a variable to store a number, then write a condition that prints 9 if the number is less than 10, prints 19 if the number is less than 20, prints 29 if the number is less than 30, and prints -1 otherwise (only one print statement should occur).

# var = 28

# if (var < 10):
#      print(9)
# elif(var < 20):
#      print(19)
# elif(var <30):
#     print(29)
# else:
#     print(1)

# 6. Use variables to store two numbers, then write a condition that prints 100 if either number is greater than 10, and prints -100 otherwise.

# var1 = 9
# var2 = 8
# if (var1>10) or (var2>10):
#     print(100)
# else:
#     print(-100)

# 7. Use a variable to store a number, then write a condition that prints 1776 if the number is less than 0, and prints 1979 otherwise.
# var = 1
# if (var<0):
#     print(1776)
# else:
#     print(1979)
# 8. Use a variable to store a number, then write a condition that prints 100 if the number equals 100, prints 99 if the number is equal to 99, and prints 0 otherwise.
# var = 99
# if (var == 100):
#     print (100)
# elif (var == 99):
#     print (99)
# else:
#     print (0)

# 9. Use variables to store two numbers, then write a condition that prints 1 if the first number is less than zero and the second number is greater than 0, and prints 0 otherwise.
# var1 = -100
# var2 = 100
# if (var1 < 0) and (var2 > 0):
#     print (1)
# else:
#     print (0)
# 10. Use a variable to store a number, then write a condition that prints 5 if the number is greater than 80, prints 4 if the number is greater than 60, prints 3 if the number is greater than 40, prints 2 if the number is greater than 20, and prints 1 otherwise (only one print statement should occur).



# 1. Write a program that uses variables to store a first and last name, then prints the full name in one line using string concatenation (the + operator).
# first_name = input("What is your first name?")
# last_name = input("What is your last name?")
# print("Your first name is " + first_name +" and your last name is " + last_name)
# 2. Write a program that uses variables to store a first and last name, then prints the full name in one line using string interpolation (the #{} operator).
# first_name = input("What is your first name?")
# last_name = input("What is your last name?")
# print(f'Your first name is {first_name} and your last name is {last_name}')

# 3. Write a program that asks the user to input a word. If the word is "marco", print "polo".
# word = input("Please input a word: ")
# if (word == "marco") or (word == "Marco"):
#   print ("Polo!")
# else:
#   print(word)

# 4. Write a program that uses variables to store three different colors, then prints out a sentence using the colors with string concatenation (the + operator).
# color1 = input("What is your first color?")
# color2 = input("now what is your second color?")
# color3 = input(" lastly what is the last color?")
# print ("Your first color is " + color1 + "your second color is " + color2 + " and your last color is "+ color3)

# 5. Write a program that uses variables to store three different colors, then prints out a sentence using the colors with string interpolation (the #{} operator).
# print (f"Your first color is {color1} your second color is {color2} and lastly your third color is {color3}.")

# 6. Write a program that asks the user to enter a name. If the name is not "Santa", print "You're not Santa."
# name = input("What is your name?")
# if(name != "Santa"):
#   print("You're not Santa")
# else:
#   print(name)

# 7. Write a program that uses variables to store a book's title and author, then prints out a sentence using that information with string concatenation (the + operator).
# title = "Harry Potter"
# author = "J.K. Rowling"
# print("The Title of this novel is " + title + " by bestselling author " + author)

# 8. Write a program that uses variables to store a book's title and author, then prints out a sentence using that information with string interpolation (the #{} operator).
# print (f"the title of this novel is {title} by bestselling author {author}")
# 9. Write a program that asks the user to enter a password. If the password is "Joshua", the program responds "Shall we play a game?". For any other password, the program responds "Access denied"
# password = input("Please enter a password: ")
# if (password == "Joshua"):
#   print("Shall we play a game?")
# else:
#   print("Access Denied")

# 10. Write a program that uses variables to store the names of three cities, then prints out a sentence using that information with string concatenation (the + operator).
# city1 = "New York"
# city2 = "Chicago"
# city3 = "Denver"
# print ("last week i started off in " + city1 + " then went over to " + city2 + " and finally threw a party at " + city3 )

# 1. Write a program that asks the user to enter a word, then prints that word with all capital letters.
# string = 'My name is ayush'
# print(string.upper())

# 2. Write a program that asks the user to enter a number, then prints "That's a big number" if the number is greater than 100.
# number = int(input("Please enter a big number: "))
# # number = int(number)
# if (number > 100):
#   print("That's a big number!")
# else:
#     print("that's a tiny number, think bigger!")

# 3. Write a program that asks the user to enter two numbers, then prints the numbers added together.
# number1 = int(input("Please enter the first number: "))
# number2 = int(input("please enter the second number: "))
# print(number1+number2)


# 4. Write a program that asks the user to enter a word, then prints that word in reverse order.
# string = input("please put a word or phrase: ")
# reverse_string = string[::-1]
# print(reverse_string)

# 5. Write a program that asks the user to enter a number, then prints the number times 10.
number = int(input("Please enter a number and i'll multiply it times 10: "))
number = number*10
print(number)

# 6. Write a program that asks the user to enter two words, then prints both words on the same line in all capital letters.

# 7. Write a program that asks the user to enter a word, then prints the number of letters in the word.

# 8. Write a program that asks the user to enter a number, then prints "That's a negative number" if the number is less than 0.

# 9. Write a program that asks the user to enter two numbers, then prints the two numbers multiplied together.

# 10. Write a program that asks the user to enter a word, then prints "That's a long word" if the word has more than 5 letters.



