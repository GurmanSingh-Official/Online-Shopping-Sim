import time

def user_inp(): # Takes user input
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

def quit(): # program for defining exit criteria
    if user_task == "exit" or user_task == "4": 
        print("Exitting....")
        time.sleep(2)
        print("Exitted!")
        exit()
if __name__ == "__main__":
    quit()

products = {"Product": "Price", 
            "apple":    45,
            "milk":     60,
            "mouse":    399}

# List of products, For Demo right now only 3 products are available.
def view_p():
    if user_task == "view products" or user_task == "1":
        print("Fetching products...")
        time.sleep(2)
        print("Here are the available products:-")
        print("")
        for keys, values in products.items():
            print(keys.capitalize(), values)
        print("Prices are in rupees.")
        print("")
if __name__ == "__main__":       
    view_p()

# Conditionals in line 15 and 28 and like these are to be removed,
# since these are for test and a function for user task output will
# be made separately to improve efficiency. 

