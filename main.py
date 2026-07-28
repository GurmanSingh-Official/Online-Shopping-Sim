import time
import add 

def user_inp():  # Takes user input
    print("Hey")
    print("What do you want to do?")
    print("1. View Products")
    print("2. Add Product")
    print("3. View Cart")
    print("4. Exit")
    inp = input("").strip().lower()
    return inp

if __name__ == "__main__":
    user_task = user_inp()

def task_output():
    if user_task == "exit" or user_task == "4": 
        quit()
    elif user_task == "view products" or user_task == "1":
        view_p()
    elif user_task == "add product" or user_task == "2":
        add_to_cart()
    else:
        print("Sorry, Action in development right now.")

def quit(): # program for defining exit criteria 
    print("Exitting....")
    time.sleep(2)
    print("Exitted!")
    exit()

products = {"Product": "Price", 
            "apple":    45,
            "milk":     60,
            "mouse":    399}
# List of products, For Demo right now only 3 products are available.

def view_p():
    print("Fetching products...")
    time.sleep(2)
    print("Here are the available products:-")
    print("")
    for keys, values in products.items():
        print(keys.capitalize(), values)
    print("Prices are in rupees.")
    print("")

def add_to_cart():
    items = add.input_check()
    print(items.prod.capitalize())
    print(items.qty)
    
if __name__ == "__main__":
    task_output()
