"""
File: quiz.py
Author: Sarah Kim
Date: 2024-03-05
Description: this program is a multiple choice game that
calculates the use's score
"""
#introduce programm 
print("Math multiple Choice Quiz!")

#print the first question and choices
print(" ")
print("1. What is the sum of 4 + 25 + 9?")
print("(a) 38")
print("(b) 34")
print("(c) 62")

#recieve answer for question 1
first_answer = input("> ")

#determine if user is right or wrong 
if first_answer == "a" or first_answer == "A":
    print("Correct!")
    score = 1
else:
    print("Incorrect.")
    score = 0

#print the second question and choices
print(" ")
print("2. What is the result of 4 x 25 + 9?")
print("(a) 108")
print("(b) 100")
print("(c) 109")

#recieve answer for question 2
second_answer= input(">")

#determine if user is right or wrong 
if second_answer == "c" or second_answer == "C":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect")

#print the third question and choices
print(" ")
print("3. What is the sum of 24 + 25 + 9?")
print("(a) 38")
print("(b) 57")
print("(c) 58")

#recieve answer for question 3
third_answer = input(">")

#determine if user answer is right or wrong
if third_answer == "c" or third_answer == "C":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect.")

#calculate grade
grade = round(score/3 * 100, 2)

#Tell user the quiz is complete and their score & grade
print(" ")
print("Quiz Complete!")
print(" ")
print("You got " + str(score) + " questions correct out of 3!")
print("Your grade percentage is: " + str(grade) + "%")

