# Description: TaskPY200_T6: Find the Smallest Number With “Digit Constraints” Input: N Find smallest number x in 1..N such that: 
# • sum of digits of x is divisible by 7 
# • x contains exactly two 3s • 
# x does not contain digit 0 If none, print -1.

# function to sum all of its digits
def digit_sum(x):
    return sum(int(d) for d in str(x))

# Check that number containe - no of 3s
def has_three(x):
    return str(x).count('3')

# function to check that a number has zero or not.
def has_zero(x):
    return '0' in str(x)

# Find Smallest Number : 
def small_number(n):
    for x in range(1, n+1):
        if(
            (digit_sum(x) % 7 == 0) and
            has_three(x) == 2 and
            not has_zero(x)
        ):
            return x
    return -1
    
# Get user Input :
n = int(input("Enter a value : "))
result = small_number(n)

# Final Output 
if result == -1:
    print(f"\nNot valid number found in range o to {n}. Output : -1")
else:
    print(f"\nSmallest Valid Number : {result}")
    print(f"Digits      : {' + '.join(list(str(result)))}")
    print(f"Digit Sum   : {digit_sum(result)} (Divisible by 7)")
    print(f"Count of 3s : {has_three(result)} (Exactly two)")
    print(f"Contains 0? : {'Yes x' if has_zero(result) else 'No'}")