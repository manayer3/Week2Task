import sys
listAccounts=[]
while True:
    selection = input("Enter your name with family name: \nQ: Quit \n")
    if selection is "Q" or selection is "q":
        print("Quitting")
    if len(listAccounts)>0:
        for i,name in enumerate(listAccounts):
            print(f"{i+1} : Account Name : {name}")
            break
    elif len(selection.split(" ")) > 0 :
        firstName = selection.split(" ")[0][0]
        familyName = selection.split(" ")[1]
        userAccountName = firstName + "." + familyName
        listAccounts.append(userAccountName)
    else:
        print("please enter your name with family name")


