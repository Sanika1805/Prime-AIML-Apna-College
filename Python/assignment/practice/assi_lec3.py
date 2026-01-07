##Q1
# #check string is palindrome or not
# str= input("Enter a sting:")
# rev=str[:: -1]

# if str == rev:
#     print("It is a palindrome")
# # else:
# #     print("It is not a palindrome")

# #hint : using loop to reverse the string
# str=input("Enter the string :")
# rev=""
# for ch in str:
#     rev= ch + rev
# if rev==str:
#     print("String is a palindrome")
# else:
#     print("String is not a palindrome")


##Q2
# # list of integers , compute avg of int
# list=[0,2,4,5,6,7]
# print(list)
# print(type(list))

# sum=0
# for val in list:
#     sum+= val
# print("avg is", sum/6)

#Q3
#take two list from user , merge them and sort the result

# list1 = list(map(int , input("Enter the list 1: ").split()))
# list2 = list(map(int , input("Enter the list 2: ").split()))

# merged_list = list1 + list2

# merged_list.sort()

# print("Merged and sorted list : ", merged_list)


# # #Q4
# # #Given tuple of integers,create : tuple of all even numbers and tuple of all odd numbers
# t = tuple(map(int, input ("Enter the values in the tuple : ").split())) #split() uses to split the string into list
#  #for eg. i/p=2 3 4 , o/p= ['2' , '3' , '4']
#  #map(int,..) convert each string into an integer eg= 2, 3, 4
# even = () 
# odd = ()

# for x in t:
#     if x % 2 == 0:
#         even += (x,)

#     else :
#         odd += (x, )

# print("Even Tuple : ", even)
# print("Odd Tuple : ", odd)


# # Q5
# students = {}

# while True: #to rune program until infinity loop untile user choose exit
#     print("\nA. Add student")
#     print("\nB. update marks")
#     print("\nC. Search student")
#     print("\nD. Display All student")
#     print("\nE. Exit")

#     choice = input("Enter your choice: ").upper() #upper convert input to 

#     if choice == 'A':
#        name = input("Enter the name of the student: ")
#        marks = int(input("Enter the marks of the student: "))
#        students[name] = marks
#        print("Student added succesgully!")

#     elif choice == 'B':
#       name = input("Enter the name of the student: ")
#       if name in students:
#          marks = int(input("Entervthe new marks: "))
#          students[name] = marks
#          print("Marks of", name , "updated succesfully")

#       else:
#          print("Student not found!")

#     elif choice == 'c':
#          name = input("Enter the name of the student: ")
#          if name in students:
#             print("Marks : ", students[name])

#          else:
#             print("Student not found!")

#     elif choice == 'D':
#        if not students:
#           print("Students are not available!")
#        else:
#           for name , marks in students.items
#           print(name , ":" , marks)

#     elif choice == 'E':
#        break
    

#     else:
#        print("Invalid choice")

#Q6
# words = ["apple", "banana" , "kiwi" , "cherry" , "mango"]

# word_length = {}

# for word in words:
#     word_length[word]= len(word)

# print(word_length)

# #modified taking input from user
# words = str(input("Enter word of your choice: ")).split()
# word_length = {}

# for word in words:
#     word_length[word]= len(word)

# print(word_length)


# #Q7
# # Write a program that takes a string from the user and print the number of spaces in the string.
# string = input("Enter a string: ")
# count = 0

# for ch in string:
#     if ch == ' ':
#         count += 1

# print("Number of spaces: ", count)


# #Q 8
# #program to check whether two list have common elements also printing them
# list1 = input("Enter the First list : ").split()
# list2 = input("Enter the second list : ").split()

# set1=set(list1)
# set2=set(list2)
# common = set1.intersection(set2)
# if set1.intersection(set2):
#     print("list have common elements and common elements are:")
#     for item in common:
#         print(item)

# else:
#     print("Given two list do not have comman elements.")

# Q 9
# given list , print all elements that appers more than once in the list
# #without using sets
# lst = input("Enter elements of the list: ").split()

# count = {}

# for item in lst:
#     if item in count:
#         count[item] += 1
#     else:
#         count[item] = 1

# print("Elements appearing more than once:")
# for key in count:
#     if count[key] > 1:
#         print(key)


## using sets
# lst = input("Enter the list:").split()

# duplicates = set()
# seen = set()

# for item in lst:
#     if item in seen:
#         duplicates.add(item)
#     else:
#         seen.add(item)

# if duplicates:
#     print("Elements appering more than once: ")
#     for x in duplicates:
#         print(x)

# else:
#     print("No duplicate elemets found")

#Q 10 
# all unique characters and unique characters
lst = input("Enter the list : ")
seen = set()
duplicate = set()
unique = set()

for item in lst:
    if item in seen:
        duplicate.add(item)
        unique.discard(item)

    else:
        seen.add(item)
        unique.add(item)

print("Unique characters:",unique)
print("Duplicate characters:", duplicate)
