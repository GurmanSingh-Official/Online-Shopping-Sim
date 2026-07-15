def user_inp():
    print("Hey")
    print("What do you want to do?")
    print("1. View Products")
    print("2. Add Product")
    print("3. View Cart")
    print("4. Exit")
    inp = input("").strip().lower()
    return inp

user_inp()