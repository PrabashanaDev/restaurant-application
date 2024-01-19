#order_menu()- Will display the menu
#order_process()- Will ask the user to order
#customer_order()- Will display the order
#order_quanity()- Will ask the user to enter the quantity
#order_time()- Will display the order time
#order_confirm- Will ask the user to confirm the order


def order_menu():
    print("1. 🍔Burger - $5.99")
    print("2. 🍕 Pizza - $7.99")
    print("3. 🍗Chicken - $6.99")
    print("4. 🍟Fries - $2.99")
    print("5. 🥤Drink - $1.99")
    print("6. 🍦Ice Cream - $3.99")
    print("7. 🥗Salad - $4.99")
    print("8. 🍝Pasta - $8.99")
    print("9. 🍱Sushi - $9.99")
    print("10. 🍣Sashimi - $10.99")

 

  
def order_process():
    order = input("What would you like to order?🤔 (Tell us order number) ")
    if order == "1":
        customer_order(order)
        order_quanity()
    elif order == "2":
            customer_order(order)
            order_quanity()
    elif order == "3":
            customer_order(order)
            order_quanity()
    elif order == "4":
            customer_order(order)
            order_quanity()
    elif order == "5":
            customer_order(order)
            order_quanity()
    elif order == "6":
            customer_order(order)
            order_quanity()
    elif order == "7":
            customer_order(order)
            order_quanity()
    elif order == "8":  
            customer_order(order)
            order_quanity()
    elif order == "9":
            customer_order(order)
            order_quanity()
    elif order == "10":
            customer_order(order)
            order_quanity()
            


def customer_order(order):
   if order == "1":
     print("Great choice, You selected 🍔 Burger ")
   elif order == "2":
     print("Great choice, You selected 🍕 Pizza ")
   elif order == "3":
     print("Great choice, You selected 🍗 Chicken ")
   elif order == "4":
     print("Great choice, You selected 🍟 Fries ")
   elif order == "5":
     print("Great choice, You selected 🥤 Drink ")
   elif order == "6":
     print("Great choice, You selected 🍦 Ice Cream ")
   elif order == "7":
     print("Great choice, You selected 🥗 Salad ")
   elif order == "8":
     print("Great choice, You selected 🍝 Pasta ")
   elif order == "9":
     print("Great choice, You selected 🍱 Sushi ")
   elif order == "10":
     print("Great choice, You selected 🍣 Sashimi ")
  
  
           
def order_quanity():
    quantity = int(input("How many do you like to order?🤔 "))
    print(f"You ordered {quantity}. Is that correct?🤔 (yes/no)")
    confirm = input()
    if confirm == "yes":
        order_time(quantity)
    elif confirm == "no":
        print("Please re-order")
        order_process()
        

def order_time(quantity):
  time= 2*quantity
  print(f"Your order will be ready in {time} minutes")


order_confirm = input("Hello👋, Welcome to The Golden Corral, Best food in town😋 \nDo you ready to order?🙄 (yes/no)")
if order_confirm == "yes":
  order_menu()
  order_process()
elif order_confirm == "no":
  print("Okay, See you next time👋")
else:
  print("Sorry, We don't understand it😔")
