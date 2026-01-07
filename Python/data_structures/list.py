#  Topic : List in python
# Author : Sanika Jagtap
# Description : Basic list operations and examples


marks= [99,89,100,65,92]
# marks[2]=70
# print(marks)

# #slicing
# print(marks[:4])

##append
#print(marks)

#loops
x=65
idx=0
for val in marks:
    if(val==x):
        print(f"{x} found at idx={idx}") # linear search
        break
    idx +=1