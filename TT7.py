fullName = input("enter your name with family name :")
if len(fullName.split(" "))>0:
    firstName = fullName.split(" ")[0][0]
    familyName = firstName.split(" ")[1]
    userAccountName = firstName + "." + familyName
    print(f"user Account Name is :{userAccountName}") 
else:
    print("please enter your name with family name")