import pickle
import pathlib


# Class for contact inputs
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
        if self.phno is not None:
            s += ", Phone: " + self.phno
        if self.email is not None:
            s += ", Email: " + self.email
        s += "}"
        return s


# function for menu
def menu():
    print("Please select one of the following options:")
    print("1. Add Contact")
    print("2. Display Contacts")
    print("3. Search Contacts")
    print("4. Delete Contacts")
    print("5. Exit")
    print()

    option = int(input("Enter the option no.: "))
    return option


# function for adding contact details
def addcontact(pb):
    print()
    print("Contacts will be stored in the format [Name, Contact number, Email id]")
    print()
    name = input("Enter the name: ")
    if name.isspace() or name == "":
        print("Please enter name of the contact")
        return
    phno = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    contact = Contact(name, phno, email)
    temp = [contact.name, contact.phno, contact.email]
    pb.append(temp)
    with open('listfile.data', 'wb') as filehandle:
        # store the data as binary data stream
        pickle.dump(pb, filehandle)


# function for displaying contact details
def display(pb):
    print()
    print("Contacts will be displayed in the format [Name, Contact number, Email id]")
    for i in pb:
        print(i)


# function for sorting contact list
def sortcontacts(pb, i):
    copy_pb = []
    for contact in pb:
        if contact[i-1] is not None:
            copy_pb.append(contact)
    return sorted(copy_pb, key = lambda x: x[i-1])


# function for doing exact binary search on contact list
def binarysearch(pb, key, i, lo, hi):
    if lo >= hi:
        return -1
    mid = (hi - lo)//2 + lo
    if pb[mid][i] == key:
        return mid
    if pb[mid][i] > key:
        return binarysearch(pb, key, i, lo, mid-1)
    if pb[mid][i] < key:
        return binarysearch(pb, key, i, mid+1, hi)


# function for doing nearby search on contact list
def nearbysearch(pb, key,i):
    l = []
    for s in pb:
        if key in s[i] and s[i] is not None:
            l.append(s)
    return l


# function for selecting on either exact search or nearby search
def search(pb):
    print("Please select one of search criteria:")
    print("1. By name")
    print("2. By contact no")
    print("3. By email")
    i = int(input("Enter the option Number: "))
    if i not in (1,2,3):
        print("Invalid Option")
    else:
        sorted_pb = sortcontacts(pb, i)
        print()
        print("Please select one of search criteria:")
        print("1. Exact Search")
        print("2. Nearby search")
        j = int(input("Enter the option number: "))
        if j not in (1,2):
            print("Invalid option")
        else:
            if j == 1:
                key = input("Enter your Search key: ")
                res = binarysearch(sorted_pb, key, i-1, 0, len(sorted_pb))
                if res == -1:
                    print("Contact not Found")
                else:
                    print()
                    print("Contact found")
                    print(sorted_pb[res])
            else:
                key = input("Enter your search key: ")
                res = nearbysearch(sorted_pb, key, i-1)
                if res == []:
                    print("Contact not found")
                else:
                    print()
                    print("Nearby results")
                    for k in res:
                        print(k)


# function for deleting a contact
def delete(pb):
    print("Please select one of Delete criteria:")
    print("1. By name")
    print("2. By contact no")
    print("3. By email")
    i = int(input("Enter the option number: "))
    if i not in (1,2,3):
        print("Invalid Option")
    else:
        sorted_pb = sortcontacts(pb, i)
        key = input("Enter your search key: ")
        res = binarysearch(sorted_pb, key, i-1, 0, len(sorted_pb))
        if res == -1:
            print("Contact not found")
        else:
            print()
            print("Contact found")
            print(sorted_pb[res])
            pb.remove(sorted_pb[res])
            with open('listfile.data', 'wb') as filehandle:
                # store the data as binary data stream
                pickle.dump(pb, filehandle)
            print("Contact Deleted")


# main function for phonebook application
def phonebook():
    print("--------------------------------")
    print("Phonebook Application")
    print("--------------------------------")
    pb = []

    file = pathlib.Path("listfile.data")
    if file.exists ():
        with open('listfile.data', 'rb') as filehandle:
            # read the data as binary data stream
            pb = pickle.load(filehandle)
    else:
        with open('listfile.data', 'wb') as filehandle:
            # store the data as binary data stream
            pickle.dump(pb, filehandle)

    while True:
        option = menu()
        if option == 1:
            addcontact(pb)
            print()
        elif option == 2:
            display(pb)
            print()
        elif option == 3:
            search(pb)
            print()
        elif option == 4:
            delete(pb)
            print()
        elif option == 5:
            print("Thanks") 
            break
        else:
            print("Invalid option")
            print()


phonebook()
