# Variables
sales=[]
saleStatus=True
addProducts=True
totalSales=0
validation=True
input_validation=True

# Program
print()
print("Welcome to the inventory management system")  #Welcome message
print("--------------------------------")
while saleStatus:   #Loop to add products to the sale
    while input_validation:
        name=input("Please, Enter the product name: ")  #Enter the product name
        if name:
            break
        else: print("Error! You must enter a product.")

    while validation:   #Loop to validate the price and quantity inputs
        try:
            price=float(input("Please, Enter the product value: ")) #Enter the product price
            break 
        except ValueError:
            print()
            print("Error: Please enter a valid numeric value")
            print()

    while validation:   #Loop to validate the price and quantity inputs
        try:
            quantity=float(input("Please, Enter the quantity of the product: "))    #Enter the product quantity
            if quantity<=0:
                print("The quantity must be greater then zero")
                continue
            break 
        except ValueError:
            print()
            print("Error: Please enter a valid numeric value")
            print()

    print("product added successfully!")

    sale=[name, price, quantity]    #Create a list with the product name, price and quantity
    sales.append(sale)  #Add the product to the sales list
    print()

    while addProducts:  
        addProduct=input("Want add more product? (Yes) or (No): ").lower()  #Ask the user if they want to add more products to the sale
        print()
        if addProduct == "yes":
            addProducts=False
        elif addProduct == "no":
            saleStatus=False
            addProducts=False
        else:
            print("--------------------------------")
            print("Invalid option, try again, type (yes) or (no)")  #If the user enters an invalid option, it will ask again
    addProducts=True

print()
print("--------------------------------")

#Print the products added to the sale and calculate the total sale
for sale in sales:  
    number = sales.index(sale) + 1
    subTotalSale=sale[1] * sale[2]
    print(f"Product {number}: {sale[0]} | Value: ${sale[1]} | Quantity: {sale[2]} | Total: ${subTotalSale}")   #
    totalSales= totalSales + subTotalSale
    
#Print the total sale    
print(f"Total sale is: ${totalSales}")
print("--------------------------------")
print("Thank you for your purchase!")

#qué pasa con los valores negativos (corregido. Solo pasa con la cantidad)
#qué pasa si el usuario no ingresa nada en las opciones (Corregido)