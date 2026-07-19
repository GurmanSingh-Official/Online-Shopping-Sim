import main 

class Items:
    def __init__(self, prod, qty):
        self.prod = prod
        self.qty = qty 

def input_check():
    product = input("Product Name: ").lower().strip()
    if product not in main.products.keys():
        print("We are Sorry, This Product is not available right now.")
        input_check()
    else:
        print("Product is available.")
        quantity = int(input("Product Quantity: "))
        prod = Items(product, quantity) 
        return prod      
input_check()






    

    
