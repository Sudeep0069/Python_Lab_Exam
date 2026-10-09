'''
 Shopping Cart Management 
A customer adds products to a shopping cart. Write a function that 
accepts a list of product names and performs the following 
operations: 
• Add a new product. 
• Remove a purchased or unwanted product. 
• Display the final cart. 
• Count the total number of products. 
'''
cart = ['Toothpaste','Brush','Biscuits','Cookies','Chips']
def cart_management(cart:list):
    while(True):
        choice = int(input(('Enter Choice-\n1. Add Product\n2. Purchase/Remove\n3. Dispaly cart\n4. Count Products\n5. Exit\n')))
        if choice== 1:
            cart.append(input('Enter product name: '))
            print('Product Added!')
        elif choice == 2:
            product=input('Enter which product you want to buy/remove: ')
            if product.title() in cart:
                cart.remove(product.title())
                print('Product Removed!')
            else:
                print('Invalid Product name')
        elif choice == 3:
            print('Available products:')
            for i in cart:
                print(i)
        elif choice == 4:
            print('Number of Products in cart: ',len(cart))
        elif choice == 5:
            break
        else:
            print('Invalid Choice')
cart_management(cart)
        
        