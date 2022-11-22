
#function for display title
def display_title():
  print("Department Store Sales Tax and Grand Total Application")
  print()
  print("Data Entries: Enter 0 to end your input")

#function which gets the cost of all the items
def get_all_items_total():
  cost_total = 0
  while True:
    cost_of_item = float(input("Cost of Item: "))
    if cost_of_item == 0:
      break
    cost_total += cost_of_item
  return cost_total

#function that calculates the discount on the item
def get_discount(total, promo_code):
  discount = 0
  if total >= 100:
    discount = total*0.1
    return discount
  if promo_code == 123:
    discount = 1
  elif promo_code == 456:
    discount = 2
  elif promo_code == 789:
    discount = 3
  elif promo_code == 0:
    discount = 0
  return discount

#function to get the sales tax
def get_sales_tax(subtotal, tax_rate):
  sales_tax = subtotal * (tax_rate/100)
  sales_tax = round(sales_tax, 2)
  return sales_tax

# a main function to run everything in
def main():
  display_title() # calls display title
  choice = "y"
  while choice.lower()  == "y": # loop to re run code if user wants to use the application again
    total = get_all_items_total()
    print("All items total: $" + str(total))
    print()

    #while loop to calculate sales tax
    while True:
      tax_rate = float(input("Sales tax rate (from 6%-10%): "))
      if tax_rate >= 6 and tax_rate <= 10:
        break
      else:
        print("Tax rate should be from 6 to 10")
    # while loop for the promo code
    print("If purchase is $100 or great an automatic 10% discount will be applied instead of promotion code.")
    while True:
      promo_code = int(input("Promotion Code (123 = $1 off, 456 = $2, 789 = $3): "))
      if promo_code == 123 or promo_code == 456 or promo_code == 789:
        break
      else:
        print("Invalid promotion code. Try again")

    #calls all the functions and prints out the values for each thing
    print()
    discount = get_discount(total, promo_code)
    print("Discount amount: $" + str(discount))
    subtotal = total - discount
    print("Subtotal: $" + str(subtotal))
    
    sales_tax = get_sales_tax(subtotal, tax_rate)
    print("Sales tax amount: $" + str(sales_tax))
    grand_total = subtotal + sales_tax
    print("Grand total: $" + str(grand_total))

    choice = input("Continue? y/Y/n/N: ") # sees if user wants to run code again
    print()
    
# calls main
main()  



