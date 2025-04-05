class POS:
    def __init__(self):
       # Product catalog with product identification (number),prices and stock amount
       self.product_dict={
         1:{'Name':'Toothpaste','Price':300,'Stock':35},
         2:{'Name':'Handsoap','Price':200,'Stock':20},
         3:{'Name':'Mop','Price':350,'Stock':5},
         4:{'Name':'Water','Price':100,'Stock':50},
         5:{'Name':'Juice','Price':150,'Stock':42},
         6:{'Name':'Jasmine Rice','Price':1050,'Stock':30},
         7:{'Name':'Flour','Price':750,'Stock':20},
         8:{'Name': '1lb Chicken','Price':350,'Stock':10},
         9:{'Name':'Ketchup','Price':220,'Stock':6},
         10:{'Name':'Vinegar','Price':300,'Stock':18}
         }
       #Initializes shopping cart for future using
       self.shopping_cart={}

    #Stock validation displaying product information
    def display_productsfromdict(self):
        for product_identification, details in self.product_dict.items():
            print (f"{product_identification}, {details['Name']}, {details['Price']} ,(Stock:{details['Stock']})")

    #Alert used to indicate low stock        
    def display_lowstock_alert(self):
        for product_identification, details in self.product_dict.items():
            #Check stock amount and make decision if less than or equal to five
            if details['Stock']< 5:
              print(f"Low Stock Alert:{details['Name']} is low.The available stock is less than five.")

    # Allows product(s) to be added to the shopping cart         
    def add_item_to_cart(self):
        #Displays all product from catalog(dictionary)
        self.display_productsfromdict()
        # Enters product in cart using product identification (number)
        product_identification=int(input('Enter the product number to add to the shopping cart:'))
        # Checks for product in product dictionary
        if product_identification in self.product_dict:
            # Enters the amount of a product in shopping cart
            product_quantity=int(input('Enter the quantity of product to add to the cart:'))
            #Validates if the required amount is in stock
            if product_quantity <= self.product_dict[product_identification]['Stock']:
           # Adds new product to cart
             self.shopping_cart[product_identification]={
                   'Name':self.product_dict [product_identification]['Name'],
                   'Price':self.product_dict[product_identification]['Price'],
                   'Quantity':product_quantity
                }
             # Updates stock in shopping cart if product is already in cart
            self.shopping_cart[product_identification]['Quantity'] += product_quantity
            # Reduce stock in product catalog for POS system
            self.product_dict[product_identification]['Stock']-= product_quantity
            print(f"{self.product_dict[product_identification]['Name']} x {product_quantity} added to cart successfully ")
            self.display_lowstock_alert()
        else:
         print('Invalid!Enter valid product or quantity')

    # Removes product from the cart
    def remove_product_from_cart(self):
        #Allows viewing of shopping cart
          self.view_cart()
        #Enter product identification that should be removed from shopping cart
          product_identification=int(input('Enter product to be removed from shopping cart:'))
        #Validates if product is actually in product catalog
          if product_identification in self.shopping_cart:
           # Enter the amount of a product to be removed from the shopping cart
           product_quantity=int(input('Enter the quantity to be removed from shopping cart:'))
           # Checks if the quantity entered is actually in cart
           if product_quantity <= self.shopping_cart[product_identification]['Quantity']:
            # Update the product quantity in cart by subtracting
            self.shopping_cart[product_identification]['Quantity']-=product_quantity
            # Updates and add the product quantity removed back to stock in product catalog
            self.product_dict[product_identification]['Stock']+=product_quantity
            # Removes product if the quantity is now zero after removal
            if self.shopping_cart[product_identification]['Quantity']==0:
                del self.shopping_cart[product_identification]
            print (f"{self.product_dict[product_identification]} x {product_quantity} was removed from cart ")
          else:
           print('Invalid! Please enter a product or quantity already found in shopping cart')
          # Checks if the cart contains product or if it is empty
          if not self.shopping_cart:
             print('The shopping cart is empty.Returning to main menu')
    #Showcases all items in the shopping cart       
    def view_cart (self):
        print('Shopping cart:')
        # Check if the cart contains items or it is empty
        if not self.shopping_cart:
          print('No products found in shopping cart')
          return 0
        else:
          total_price=0
          # Checks through cart and ensure an amount is present for products
          for details in self.shopping_cart.values():
             # Calculates the price per item
             total_item=details['Price'] * details['Quantity']
             print(f"{details['Name']}: {details['Quantity']} x ${details['Price']}=${total_item}")
             total_price += total_item
          print(f"Total:${total_price}")
          return total_price
    # Checking out process for products
    def checkout (self):
        #Captures the subttal from shopping cart
        subtotal=self.view_cart()
        if subtotal==0 :
           print('Checkout can only be done if item/items is in shopping cart')
           return
        # Calculating and adding tax to products
        sales_tax= subtotal * 0.10
        # Calculating the final total
        final_price=subtotal+sales_tax
        # Calculating discount
        if final_price > 5000:
           discount_apply=final_price * 0.05
           final_price-=discount_apply
           print(f"Discount applied to cart:- ${discount_apply:.2f}")
        print(f"Sales Tax (10%): ${sales_tax:.2f}")
        print(f"The overall total is: ${final_price:.2f}")
        # Loop
        while True:
           # Enters the amount of money received from customer
           given_amount=int(input('Enter the amount given by customer:'))
           # Validates if amount recieved can cover the cost of shopping cart products
           if given_amount>= final_price:
              # Calculating change for customer
              customer_change=given_amount-final_price
              print(f"Customer's change:${customer_change:.2f}")
              # Creation and output of receipt
              self.generate_customer_receipt(subtotal,sales_tax,final_price,given_amount,customer_change)
              # Clears shopping cart for next transaction
              self.shopping_cart.clear()
              break
           else:
             print('Insufficent amount. Please request more to finalize payment.')
             return
    # Generation of receit for customers       
    def generate_customer_receipt(self,subtotal,sales_tax,final_price,given_amount,customer_change):
        print('---Customer Receipt---')
        print('Best Buy Retail Store 🛒')
        print('3 Main Street, May Pen')
        for details in self.shopping_cart.values():
            total_items=details['Price']* details['Quantity']
            print(f"{details['Name']}:{details['Quantity']} x ${details['Price']} = ${total_items}")
        print(f"Subtotal:${subtotal:.2f}")
        print(f"10% Sales tax: ${sales_tax:.2f}")
        print(f"Final Total: ${final_price}")
        print(f"Amount paid by customer:{given_amount:.2f}")
        print(f"Customer change:{customer_change:.2f}")
        print(f"Absolutely no exchange of opened food items or products bought over three days ")
        print(f"Thank you for shopping with us. Have a great day ☺!")
        print(f"------------------------------------------------")
    # Loop for the Point of Sale 
    def cashingsystem (self):
        while True:
             print('WELCOME TO BEST BUY RETAIL STORE POINT OF SALE SYSTEM')
             print()
             print('Point of Sale Menu')
             print('1.View product catalog')
             print('2.Add to shopping cart')
             print('3.Remove from shopping cart')
             print('4.View shopping cart')
             print('5.Checkout shopping cart')
             print('6.Exit')
             print()
             pos_choice=input('Enter your choice from point of sale menu:')
             if pos_choice=='1':
                 self.display_productsfromdict()
             elif pos_choice=='2':
              self.add_item_to_cart()
             elif pos_choice=='3':
              self.remove_product_from_cart()
             elif pos_choice=='4':
              self.view_cart()
             elif pos_choice=='5':
              self.checkout()
             elif pos_choice=='6':
              print(' Exiting Point of Sale System.')
              break
             else:
              print('Invalid choice. Select choice from 1-6.')
#Operates the Point of Sale enabling it to start             
pos_system=POS()
pos_system.cashingsystem()
