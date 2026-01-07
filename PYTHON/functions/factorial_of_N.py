# def calc_fact(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     return fact
# print(calc_fact(5))


n = int(input("Enter the number: "))
def calc_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact
print(calc_fact(n))