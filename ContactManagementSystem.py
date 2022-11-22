
#display title function
def display_title():
  print("CONTACT MANAGEMENT SYSTEM")
  print()
#a function to print all commands
def menu():
  print("COMMAND MENU")
  print("list - Display all contacts\nview - View a contact\nadd - Add a contact\ndel - Delete a contact\nexit - Exit program")
  print()
# this function prints the entire contact list
def display(contact_list):
  if len(contact_list) == 0:
    print("There are no contacts in in the last.\n")
    return
  else:
    i = 1
    for row in contact_list:
      print(str(i) + "." + row[0] + ", " + row[3])
      i += 1
    print()
    return
#prints a certain contact in the list
def view(contact_list):
  num = input("Number(1 - " + (str(len(contact_list))) + "): ")
  if int(num) < 1 or int(num) > len(contact_list):
    print("Invalid number. Try again!")
    print()
    return
  else:
    row = int(num) - 1
    print(contact_list[row][0] + ", " + contact_list[row][3])
    print()
    return
# adds a contact to the list by creating a new list to add to the old list
def add(contact_list):
  name = input("Name: ")
  email = input("email: ")
  phone = input("phone: ")
  ID = input("ID: ")
  contact = []
  
  contact.append(name)
  contact.append(email)
  contact.append(phone)
  contact.append(ID)
  contact_list.append(contact)

  print(contact[0] + ", " + contact[3] + " was added.")
  print()
  return
#deletes a contact from the list
def delete(contact_list):
    num = input("Number(1 - " + (str(len(contact_list))) + "): ")
    if int(num) < 1 or int(num) > len(contact_list):
      print("Invalid number. Try again!")
      print()
      return
      
    else:
      contact = contact_list.pop(int(num)-1)
      print(contact[0] + ", " + contact[3] + " was deleted.")
      
      print()
#a main function that has the list created, and runs a loop which runs the entire program     
def main():
  contact_list = [["Betty Johnson", "betty.johnson@gmail.com", "(408) 111-2222", "3333"], ["Mark Arlington", "mark.arlington@yahoo.com", "(669) 123-4567", "4444"]]
  
  display_title()
  menu()

  while True:
    command = input("Command: ")
    if command == "list":
      display(contact_list)
    elif command == "view":
      view(contact_list)  
    elif command == "add":
      add(contact_list)
    elif command == "delete":
      delete(contact_list)
    elif command == "exit":
      print("Thank you for using my app.")
      break
    else:
      print("Not a valid command. Please try again.\n ")

main()

