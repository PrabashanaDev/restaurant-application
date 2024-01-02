#Imagine restuarant name= 'The Golden Corral'
#I want to create functin that contains menu

# def menu():
#     print("Here is our menu📜")
#     print("1. 🍔Burger - $5.99")
#     print("2. 🍕Pizza - $7.99")
#     print("3. 🍗Chicken - $6.99")
#     print("4. 🍟Fries - $2.99")
#     print("5. 🥤Drink - $1.99")
#     print("6. 🍦Ice Cream - $3.99")
#     print("7. 🥗Salad - $4.99")
#     print("8. 🍝Pasta - $8.99")
#     print("9. 🍱Sushi - $9.99")
#     print("10. 🍣Sashimi - $10.99")

# menu()
#How to call menu funtion in the main function
# def main():
#     print("Hello👋, Welcome to The Golden Corral, Best food in town😋")
#     print("Do you ready to order?🙄 (yes/no)")
#     order_confirm = input()
#     if order_confirm == "yes":
#         print("Great!👍")
#         menu()
#     elif order_confirm == "no":
#         print("Okay, See you next time👋")
#     else:
#         print("Sorry, We don't understand that😔")


order_confirm = input("Hello👋, Welcome to The Golden Corral, Best food in town😋. \nDo you ready to order?🙄 (yes/no)")
if order_confirm == "yes":
    print("Great!👍")
    print("Here is our menu📜")
    print("1. 🍔Burger - $5.99")
    print("2. 🍕Pizza - $7.99")
    print("3. 🍗Chicken - $6.99")
    print("4. 🍟Fries - $2.99")
    print("5. 🥤Drink - $1.99")
    print("6. 🍦Ice Cream - $3.99")
    print("7. 🥗Salad - $4.99")
    print("8. 🍝Pasta - $8.99")
    print("9. 🍱Sushi - $9.99")
    print("10. 🍣Sashimi - $10.99")

    order= input("What would you like to order?🤔 (Tell us order number) ")
    if order == "1":
        print("Great choice, You selected 🍔 Burger ")
        quantity = int(input("How many Burgers do you like to order?🤔 ")) #add int() to other orders too
        print(f"You ordered {quantity} 🍔 Burger")
        print("Your order will be ready in 10 minutes")
    elif order == "2":
        print("Great choice, You selected 🍕 Pizza ")
        quantity = input("How many Pizza do you like to order?🤔 ")
        print(f"You ordered {quantity} 🍕 Pizza")
        print("Your order will be ready in 10 minutes")
    elif order == "3":
        print("Great choice, You selected 🍗 Chicken ")
        quantity = input("How many do you like to order?🤔 ")
        print(f"You ordered {quantity} 🍗 Chicken")
        print("Your order will be ready in 10 minutes")
    elif order == "4":
        print("Great choice, You selected 🍟 Fries ")
        quantity = input("How many do you like to order?🤔 ")
        print(f"You ordered {quantity} 🍟 Fries")
        print("Your order will be ready in 10 minutes")
    elif order == "5":
        print("Great choice, You selected 🥤 Drink ")
        quantity = input("How many do you like to order?🤔 ")
        print(f"You ordered {quantity} 🥤 Drink")
        print("Your order will be ready in 10 minutes")
    elif order == "6":
        print("Great choice, You selected 🍦 Ice Cream ")
        quantity = input("How many do you like to order?🤔 ")
        print(f"You ordered {quantity} 🍦 Ice Cream")
        print("Your order will be ready in 10 minutes")
    elif order == "7":
        print("Great choice, You selected 🥗 Salad ")
        quantity = input("How many do you like to order?🤔 ")
        print(f"You ordered {quantity} 🥗 Salad")
        print("Your order will be ready in 10 minutes")
    elif order == "8":  
        print("Great choice, You selected 🍝 Pasta ")
        quantity = input("How many do you like to order?🤔 ")
        print(f"You ordered {quantity} 🍝 Pasta")
        print("Your order will be ready in 10 minutes")
    elif order == "9":
        print("Great choice, You selected 🍱 Sushi ")
        quantity = input("How many do you like to order?🤔 ")
        print(f"You ordered {quantity} 🍱 Sushi")
        print("Your order will be ready in 10 minutes")
    elif order == "10":
        print("Great choice, You selected 🍣 Sashimi ")
        quantity = input("How many do you like to order?🤔 ")
        print(f"You ordered {quantity} 🍣 Sashimi")
        print("Your order will be ready in 10 minutes")
    else:
        print("Sorry, We don't have that in our menu😔")
elif order_confirm == "no":
    print("Okay, See you next time👋")
else:
    print("Sorry, We don't understand that😔")

