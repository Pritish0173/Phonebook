
class Contact:
    def __init__(self, name, phno, email):
        self.name = name
        if phno.isdigit():
            self.phno = phno
        else:
            self.phno = None
        if email.isspace() or email == "":
            self.email = None
        else:
            self.email = email

    def __str__(self):
        s = "{Name: "+self.name
        if self.phno != None:
            s += ", Phone: "+ self.phno
        if self.email != None:
            s += ", Email: "+ self.email
        s += "}"
        return s

def menu():
    print("Please select one of the following options:")
    print("1. Add Contact")
    print("2. Display Contacts")
    print("3. Exit")
    print()

    option = int(input("Enter the option number: "))
    return option

def addcontact(pb):
    print()
    print("Contacts will be stored in the format [Name, Contact number, Email id]")
    print()
    name = input("Enter the name: ")
    if name == " " or name == "":
        print("Please enter name of the contact")
        return
    phno = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    contact = Contact(name, phno, email)
    temp = [contact.name, contact.phno, contact.email]
    pb.append(temp)

def display(pb):
    print("Contacts will be displayed in the format [Name, Contact number, Email id]")
    for i in pb:
        print(i)    

def phonebook():
    
    print("--------------------------------")
    print("Phonebook Application 1.0")
    print("--------------------------------")
    
    pb = []
    while True:
        option = menu()
        if option == 1:
            addcontact(pb)
            print()
        elif option == 2:
            display(pb)
            print()
        elif option == 3:
            print("thanks")   
            break
        else:
            print("Invalid option") 
            print()

phonebook()