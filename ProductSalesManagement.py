#uses monthly_sales.txt

#display title function
def display_title():
    print("Product Sales Management System")
    print()
#displays the menu of commands
def menu():
    print("Command Menu")
    print("view - View a sales amount for a specified month\nhighest - View the highest sales of the year\nlowest - View the lowest sales of the year\nedit - Edit a sales amount for a specified month\naverage - View the sales average for the whole year\nrange - View the sales average for a specified sales amount range\ntotal - View the sales total for the whole year\nexit - Exit the program")
    print()
#read the text file and turns it into a dictionary
def read_file(dictionary):
    with open("monthly_sales.txt") as file:
        for line in file:
            line = line.replace("\n", "")
            dictionary.update({line[0:3]: line[4:]})
    return dictionary
#rewrites the dictionary into the text file
def write_file(dictionary):
    with open("monthly_sales.txt", "w" ) as file:
        for code in dictionary:
            file.write(code + "	" + dictionary[code]+"\n")
    return dictionary
#views a certain value based on the key given
def view_sales_amount(dictionary):
        code = input("Three-letter month: ")        
        code = code.capitalize()
        if code in dictionary:
            amount = int(dictionary[code])
            amount = "{:,.2f}".format(amount)
            print("Sales amount for " + code + " is $" + str(amount) + ".")
            print()
            return
        else:
            print("Invalid month. Try again")
            print()
#looks for the highest value in the dictionary and then prints it
def get_highest_amount(dictionary):
    value = int(dictionary["Jul"])
    month = "x"
    for code in dictionary:
        if value < int(dictionary[code]):
            value = int(dictionary[code])
            month = code
    value = "{:,.2f}".format(value)
    print("The highest sales amount is $" + value + " in " + month + ".")
    print()
    return
#looks for the lowest value in the dictionary and then prints it
def get_lowest_amount(dictionary):
    value = int(dictionary["Jul"])
    month = "x"
    for code in dictionary:
        if value > int(dictionary[code]):
            value = int(dictionary[code])
            month = code
    value = "{:,.2f}".format(value)
    print("The highest sales amount is $" + value + " in " + month + ".")
    print()
    return
#changes the value of the month given with the value given
def edit_sales_amount(dictionary):
        code = input("Three-letter month: ")
        code = code.capitalize()
        if code in dictionary:
            sales_amount = input("Sales amount: ")
            dictionary[code] = sales_amount 
            sales_amount = "{:,.2f}".format(int(sales_amount))
            print("Sales amount of $" + str(sales_amount) + " for " + code + " has been updated.")
            print()
            return
        else:
            print("Invalid month. Try again")
            print()
# adds up all the values in the dictionary and gets average
def get_average(dictionary):
    total = 0
    for code in dictionary:
        total += int(dictionary[code])
    average = total/12
    average = "{:,.2f}".format(average)
    print("Monthly average is $" + str(average) + ".")
    print()
    return

#loops through the list to see if a value fits in the given range and then takes the average
def get_range_average(dictionary):
    low = input("Low: ")
    high = input("High: ")
    total = 0
    i = 0 #counter variable for the average
    for code in dictionary:
        if int(low) <= int(dictionary[code]) <= int(high):
            total += int(dictionary[code])
            i+=1
    average = total/i        
    average = "{:,.2f}".format(average)
    print("Sales average of this range is $" + str(average) + ".")
    print()
    return
    
# adds up all values in dictionary
def get_total(dictionary):
    total = 0
    for code in dictionary:
        total += int(dictionary[code])
    total = "{:,.2f}".format(total)
    print("Yearly total is $" + str(total) + ".")
    print()
    return
#prints a thank you message
def terminate_app():
    print()
    print("Thank you for using my app!")
    return
    

def main():
    dictionary = {}# creates an emprty dictionary
    read_file(dictionary)
    display_title()
    menu()
           
    while True:
        command = input("Command: ")
        if command == "view":
            view_sales_amount(dictionary)
        elif command == "average":
            get_average(dictionary)
        elif command == "total":
            get_total(dictionary)
        elif command == "highest":
            get_highest_amount(dictionary)
        elif command == "lowest":
            get_lowest_amount(dictionary)
        elif command == "edit":
            edit_sales_amount(dictionary)
            write_file(dictionary)
        elif command == "range":
            get_range_average(dictionary)
        elif command == "exit":
            terminate_app()
            break
        else:
          print("Invalid Command. Try again.\n ")
 
main()

