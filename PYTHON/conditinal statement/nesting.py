# username = input("Enter username: ")
# passward = input("Enter your Passward: ")

# if (username == "admin" and passward == "pass"):
#     print("Login successful!")
# else:
#     if (username != "admin"):
#         print("Username is wrong!")
#     else:
#         print("wrong passward")


#match case:
color = input("enter color: ")
match color:
    case "Green":
        print("Go")

    case "Red":
        print("Stop")

    case "Yellow":
        print("Look")

#default case use to if value doesn't match
    case _:
        print("Wrong color!")