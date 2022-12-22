
# ======== The beginning of the class ==========
from tabulate import tabulate


class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        ''' Returns the cost of the shoe in this method. '''
        cost = self.cost
        return cost

    def get_quantity(self):
        ''' Returns the quantity of the shoes in this method. '''
        quantity = self.quantity
        return quantity

    def __str__(self):
        '''Returns a string representation of a class. '''
        country = self.country
        code = self.code
        product = self.product
        cost = self.cost
        quantity = self.quantity

        obj_list = [country, code, product, cost, quantity]

        return obj_list


#==========Functions outside the class==============
def read_shoes_data(shoe_list):
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''

    # Use a try block to catch an error if the file is not located
    # Use an If Loop to make sure to skip the first line in the text file
    try:
        f = open('inventory.txt', 'r+')
        x = 0

        for line in f:
            # Use an If Loop to make sure the first line (menu) in the text file is not added

            if x > 0:
                # Add an instance of the object Shoe for each line added to the shoe_list
                # Make sure that an empty space is not added to the list by using an If Loop 
                line = line.strip("\n")
                line = line.split(",")

                if len(line) > 3:
                    # Add each line to shoe_list and create an instance for each
                    shoe_list.append(Shoe(line[0], line[1], line[2], line[3], line[4]))

                else:
                    pass

            else:
                pass

            x+=1

    except FileNotFoundError:
        print("An error has occured when trying to open the textfile in the function - read_shoes_data")
    
    return shoe_list


def capture_shoes(shoe_list):
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''

    # Get the info from the user to create a new instance of the object
    print("\nTo add data please follow the next steps:\n")
    country = input("Enter the country: ")
    code = input("Enter the product code: ")
    product = input("Enter the product name: ")

    # Make sure they enter an int value
    cost = ""
    while cost.isdigit() == False:
        cost = input("Enter the cost: R ")
    cost = int(cost)

    # Make sure they enter an int value
    quantity = ""
    while quantity.isdigit() == False:
        quantity = input("Enter the quantity available: ")
    quantity = int(quantity)


    # Create instance of the new object then add it to the list
    shoe_list.append(Shoe(country, code, product, cost, quantity))

    # Add new show data to Text File inventory.txt using a try block
    try:
        f = open('inventory.txt', 'w+')

        for x in range(0, len(shoe_list)):

            f.write("{},{},{},{},{}\n".format(shoe_list[x].country, shoe_list[x].code, shoe_list[x].product, shoe_list[x].cost, shoe_list[x].quantity))

            print("\nData for the new shoe has been successfully captured!\n")
    
    except FileNotFoundError:
        print("Can't locate the text file. Please make sure that the inventory.txt file exists and is in the right folder.")

    f.close()

    
def view_all(shoe_list):
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Pythons tabulate module.
    '''
    # Declare headers and print data on the terminal using module tabulate in style 'pipe'
    # Declare tbl_content list
    tbl_headers = ['Country', 'Code', 'Product', 'Cost', 'Quantity']
    tbl_content = []

    # Use For Loop to run through all objects, convert them to string, add them in tbl_content, then print in a table
    for x in range(0, len(shoe_list)):
        tbl_content.append(shoe_list[x].__str__())
    
    print("\n{}\n".format(tabulate(tbl_content, headers = tbl_headers, tablefmt = 'pipe')))


def re_stock(shoe_list):
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''

    # Had to check through the list and get the index of the object with the lowest quantity
    # Website: https://stackoverflow.com/questions/54624235/how-to-search-list-of-objects-for-index-of-minimum
    # https://medium.com/analytics-vidhya/how-to-use-key-function-in-max-and-min-in-python-1fdbd661c59c
    lowest_quant_index = min(range(len(shoe_list)), key=lambda i: shoe_list[i].get_quantity())
    
    # Use While Loop to keep asking user to enter an amount and make sure it's a digit and it's not a negative number
    re_stock_quant = ""
    while re_stock_quant.isdigit == False or re_stock_quant < '0':
        re_stock_quant = input("""\n{} has the lowest quantity with {} items in stock.\nPlease enter the amount you want to re-stock this item with
To return to previous menu enter '-1'
:""".format(shoe_list[lowest_quant_index].product, shoe_list[lowest_quant_index].quantity))

        # If Loop to check if the user wants to return to previous menu
        if re_stock_quant == '-1':
            return

    # Cast values to Integer and update amount in the list
    original_amount = int(shoe_list[lowest_quant_index].quantity)
    re_stock_quant = int(re_stock_quant)
    shoe_list[lowest_quant_index].quantity = re_stock_quant + original_amount

    # Use a try block to make sure the File does exist in the correct folder
    try:
        # Update the text file inventory.txt with the new info
        f = open('inventory.txt', 'w+')

        for x in range(0, len(shoe_list)):
            f.write("{},{},{},{},{}\n".format(shoe_list[x].country, shoe_list[x].code, shoe_list[x].product, shoe_list[x].cost, shoe_list[x].quantity))
        f.close()

        print("\nThe item has been successfully restocked!\n")
    
    except FileNotFoundError:
        print("File not located. Please make sure the file exists and is in the correct folder.")


def search_shoe(shoe_list):
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    while True:
        shoe_selected = input("""
Enter the code of the shoe you want to see
To return to previous menu enter '-1'
: """)

        # If Loop to check if the user wants to return to previous menu
        if shoe_selected == '-1':
            return

        # Use For Loop to run through shoe_list and the If Loop to see if 
        # the code entered matches any of those in the list
        for x in range(0, len(shoe_list)):

            if shoe_list[x].code == shoe_selected:

                print("""
Country: {}
Code: {}
Product: {}
Cost: {}
Quantity: {}
""".format(shoe_list[x].country, shoe_list[x].code, shoe_list[x].product, shoe_list[x].cost, shoe_list[x].quantity))

                False
                break


def value_per_item(shoe_list):
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    # Create list to place in content to print out in a tabular fashion
    tbl_headers = ['Product', 'Total Stock Value']
    tbl_content = []

    # Use For Loop to run through list of shoes, cast values to Integer, calculate and add to tbl_content list
    for x in range(0, len(shoe_list)):
        cost = int(shoe_list[x].cost)
        quantity = int(shoe_list[x].quantity)

        value = round(cost * quantity, 2)

        temp_list = [shoe_list[x].product, value]

        tbl_content.append(temp_list)

    print("\n{}\n".format(tabulate(tbl_content, headers = tbl_headers, tablefmt = 'pipe', stralign = 'center')))
    

def highest_qty(shoe_list):
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    # Get the maximum quantity's index number out of all the objects then print the item as On Sale
    highest_quant_index = max(range(len(shoe_list)), key=lambda i: shoe_list[i].get_quantity())

    print("\nThe following item will be on sale: {}\n".format(shoe_list[highest_quant_index].product))


#==========Main Menu=============
'''
This is the body part of the code
'''

while True:

    shoe_list = []
    read_shoes_data(shoe_list)
    menu = ""

    # Use While Loop to double check if it is a digit and a valid option
    while menu < '1' and menu > '7' or menu.isdigit() == False:
        menu = input("""Welome to your Inventory App

Please select one of the following option:
1. Search an item
2. View all items details
3. View total stock prices for all items
4. Add a new item
5. Re-stock the lowest item
6. Calculate which item is On Sale
7. Exit
: """)

    # Use If Loop to create a menu choice
    if menu == '1':
        search_shoe(shoe_list)
    
    elif menu == '2':
        view_all(shoe_list)
    
    elif menu == '3':
        value_per_item(shoe_list)
    
    elif menu == '4':
        capture_shoes(shoe_list)
    
    elif menu == '5':
        re_stock(shoe_list)
    
    elif menu == '6':
        highest_qty(shoe_list)
    
    elif menu == '7':
        print("Goodbye!")
        exit()
    
    else:
        print("Please make sure that you selected a valid option. Simply enter the number of your choice.")