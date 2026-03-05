# Description: TaskPY200_T2: 
# Write python program to check if number is positive, negative, or zero.
#  Using formatted string printing show message like : 
# “Your entered number {} was negative , how ever positive value of your number is {}

num = int(input("Enter a number : "))

if num < 0:
    print(f"Your entered number {num} was negative , how ever positive value of your number is {abs(num)}")
elif num > 0:
    print(f"Your entered number {num} is positive")
else:
    print(f"Your entered number {num} is zero")