# #Q1
# salary = int(input("Enter your salary: "))
# if (salary < 30000):
#     tax_rate = 5

# elif (salary >= 30000 and salary <= 70000):
#     tax_rate = 15

# else:
#     tax_rate = 25

# print("Tax rate on salary is:", tax_rate)

# #Q2
# def even_value(a,b):
    
#     for i in range(a,b+1):
#         if (i%2 == 0 ):
#             print(i)
#     i += 1
#     return(even_value)
# print(even_value(1,10))
    

# #Q3
# n = int(input("Enter the number: "))
# def print_digits(n):
#     while n > 0:
#         digit = n % 10
#         print(digit)
#         n = n //10
# print_digits(n)

# #Q4 
# n = int(input("Enter the number: "))
# def count_digits(n):
#     count = 0
#     while n > 0:
#         count += 1
#         n = n //10
#     return count

# print("count of number of digits in a number is:",count_digits(n))

# #Q5
# n = int(input("Enter the number: "))
# def sum_of_digits(n):
#     sum = 0
#     while n >0:
#         # digit = n % 10
#         # sum += digit
#         sum += n % 10
#         n = n // 10
#     return sum

# print(sum_of_digits(n))


# #Q6
# for i in range(1,100+1):
#     if i % 3 == 0 and i % 5 == 0:
#         print(i)

# #Q7
# while True:
#     user_input = input("Enter a number or Quit: ")
#     if user_input == "Quit":
#         break
    
#     n = int(user_input)
#     if n > 0:
#         print("Number is positive!")

#     elif n < 0:
#         print("Number is negative!")

#     else :
#         print("Number is zero!")

# #Q8
# a = int(input("Enter the value of a: "))
# b = int(input("Enter the value of b: "))
# operation = input("Enter the operation: ")
# def calculator(a,b,operation):
#     if operation == '+':
#         print(a + b)
#     elif operation == '-':
#         print(a - b)
#     elif operation == '*':
#         print(a * b)
#     elif operation == '/':
#         print(a / b)
#     else:
#         print("Invalid!")

# print(calculator(a,b,operation))

#Q9
# num = int(input("Enter the number: "))
# def is_prime(num):
#     for i in range(2,num-1):
#         if num % i == 0:
#             return False
        
#     if num <= 1:
#         return False
#     return True
# print(is_prime(num))

#Q10
secret_num = 18
while True:
    guess = int(input("Guess the number: "))
    if guess > secret_num:
        print("Too high")
    elif guess < secret_num:
        print("Too low")
    else:
        print("correct!!")
    break