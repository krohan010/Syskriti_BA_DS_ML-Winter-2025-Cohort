# Description: TaskPY200_T4: Write program to check password strength rules Input a string s 
# (assume lowercase/uppercase/digits may appear) Now check: 
# if the string contains full fills all these and print final output: 
# valid (STRONG) or Invalid password 
# (WEAK) 1. length >= 8 
# 2. has at least 1 digit 
# 3. has at least 1 uppercase 
# 4. has at least 1 lowercase Print “STRONG” else “WEAK”

# Take password input from user
password = input("Enter your password: ")

# Initialize conditions
has_digit = False
has_upper = False
has_lower = False

# Check each character
for char in password:
    if char.isdigit():
        has_digit = True
    elif char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True

# Check all conditions
if len(password) >= 8 and has_digit and has_upper and has_lower:
    print("STRONG")
else:
    print("WEAK")