temperature = 46
if temperature < 25:
    print("It is cold")
elif temperature > 25:
    print("It is hot")
else:
    print("Normal Temperature")

# A simple program to return the largest number among three
first= 90
second= 45
third= 69
if first > second and first > third:
    print(first," is the largest number")
elif second > first and second > third:
    print(second,"is the largest number")
else:
    print(third,"is the largest number")

# Write a simple program that checks whether a number is even or odd
def check_even_odd(num):
    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")

# Taking input from the user
number = int(input("Enter a number: "))

# Calling the function to check even or odd
check_even_odd(number)