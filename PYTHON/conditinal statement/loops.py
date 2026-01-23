# while loop
# performing condition until its true 

# #infinite loop
# while True:
#     print("Hello world")

# #finite loop
# count = 1

# while (count <= 5):
#     print("Hello world!")
#     count += 1
# print("After loop count =", count)

# i = 1 #iterator
# while (i <= 5):
#     print("Hello world!")
#     i += 1
# print("After loop count = ", i)

# # reverse
# i = 5
# while (i >= 1):
#     print("Hello woeld!")
#     i -= 1

# # multiplication table for any number 'n'
# num = int(input("Enter the number: "))
# i = 1
# while (i <= 10):
#     multi = num * i
#     print(num ,"*" ,i, "=" , multi)
#     i += 1

# # break and continue
# i = 1
# while (i <= 10):
#     if (i % 6 == 0):
#         break
#     print(i)
#     i += 1 #updatation
# print("Outside the loop!")

# i = 1
# while (i <= 10):
#     if (i % 3 == 0):
#         i += 1
#         continue
#     print(i)
#     i += 1
# print("outside the loop..")

# # print all odd numbers
# i = 1
# while (i <= 10):
#     i += 1 #here code will run till 11
#     if (i % 2 == 0):
#         continue
#     print(i)
# print("outside the loop")


# for loop
# use for sequential traversal
# for var in string:
#     print(var)
# in is membership operator which checks presence

# string = "hello"
# if 'o' in string:
#     print("o exists in string")

# range function 
# range (n) means 0 to n-1 sequence

# for i in range(5):
#     print(i+1)

# # count the number of i's
# word = "artificial intelligense"

# count = 0
# for ch in word:
#     if (ch == 'i'):
#         count += 1
# print("number of i's :", count)

# # print vowel count of given string
# word = "artifical intelligense"
# count = 0
# for ch in word:
#     if (ch == 'a' or ch =='i' or ch == 'e' or ch =='o' or ch =='u'):
#         count += 1
# print("number of vowels is =", count)

# Range function
# range(start,stop,step)
# if range(5) = 0,1,2,3,4
# if range(1,6) = 1,2,3,4,5
# if range(1,5,2) = 1,3,5

# for i in range (5):
#     print(i)

# for i in range(1,6):
#     print(i)

# for i in range(1,6,2):
#     print(i)


# sum of first 'n' natural numbers
num = int(input("Enter the number: "))
sum = 0
for i in range (1,num+1):
    sum += i
print("sum is", sum)

