d={}
while True:
    print("\t---Phone Book---")
    print("Enter 1 for adding a contact")
    print("Enter 2 for deleting a contact")
    print("Enter 3 for editing a contact")
    print("Enter 4 for searching for a contact")
    print("Enter 5 for viewing all contacts")
    print("Enter 6 for exiting phonebook")

    a=int(input("Enter your operation: "))

    if a not in (1,2,3,4,5,6):
        print("Invalid input")

    elif a in (1,2,3,4,5,6):

        match a:

            case 1:
                name=input("Enter name of contact: ")
                number=int(input("Enter number of contact: "))
                d[name]=number

            case 2:
                name=input("Enter name of contact: ")
                if name in d:
                    del d[name]
                else:
                    print("Contact not found!")

            case 3:
                choice=int(input("Enter 1 for Updating Name, 2 for Number: "))
                if choice == 1:
                    name=input("Enter name of contact: ")
                    if name in d:
                        newname=input("Enter new name: ")
                        d[newname]=d[name]
                        del d[name]
                    else:
                        print("Contact not found")
                elif choice == 2:
                    name = input("Enter name of contact: ")
                    if name in d:
                        newnumber=int(input("Enter new number of contact: "))
                        d[name]=newnumber
                    else:
                        print("Contact not found")


            case 4:
                name=input("Enter name of contact: ")
                names= d.keys()
                if name in names:
                    print(f" {name}", d[name])
                else:
                    print("Invalid contact!")

            case 5:
                for i in d:
                    print(i, d[i])

            case 6:
                print("Thank you for using phonebook")
                break





