sales=[]
saleStatus=True
addProducts=True
totalSales=0
validation=True

print()
while saleStatus:
    name=input("Please, Enter the product name: ")
    while validation:
        try:
            price=float(input("Please, Enter the product value: "))
            break 
        except ValueError:
            print("Error: Please enter a valid numeric value")

    while validation:
        try:
            quantity=int(input("Please, Enter the quantity of the product: "))
            break 
        except ValueError:
            print("Error: Please enter a valid numeric value")

    sale=[name, price, quantity]
    sales.append(sale)
    print()

    while addProducts:
        addProduct=input("Want add more product? (Yes) or (No): ").lower()
        if addProduct == "yes":
            addProducts=False
        elif addProduct == "no":
            saleStatus=False
            addProducts=False
        else:
            print("--------------------------------")
            print("Invalid option, try again")
    addProducts=True
print("--------------------------------")

for sale in sales:  
    number = sales.index(sale) + 1
    subTotalSale=sale[1] * sale[2]
    print(f"Product {number}: {sale[0]}, Value: {sale[1]}, Quantity: {sale[2]}, Total: {subTotalSale}")   #
    totalSales= totalSales + subTotalSale
    
print(f"Total sale is: {totalSales}")
