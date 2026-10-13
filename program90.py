"""
create a product class with the product name , price anfd quantity . add an
instance method to calculate the total cost . take these values from the user and
display the product name and cost
"""
class Product:
    def __init__(self,product_name,price,quantity):
        self.product_name=product_name
        self.price=price
        self.quantity=quantity
    def calculate(self):
        return self.price
n=Product("sandwich","100","3")
print("Total cost: ",n.product_name)
print("Total cost: ",n.price)
print("Total cost: ",n.quantity)

    
