import time
import os
import pandas as pd
from datetime import datetime
df = pd.read_csv("Menu.csv")

cart = []


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")



def weather(weather_choice):
    if weather_choice == "1" or weather_choice == "hot":

        print("\n   I advise you to order some cold drinks🥤🧊")
        print("\n   Here are our drinks😊❄️")

        drinks = df[df["Category"] == "Drink"]

        for _, row in drinks.iterrows():
            print(
                f"\nID:{row['ID']} -> "
                f"{row['Name']:<10} | "
                f"{row['Price']}EGP | "
                f"Quantity:{row['Quantity']}"
            )

    elif weather_choice == "2" or weather_choice == "cold":

        print("     You're in the right place👍,")
        print("     We have food that will warm you up🔥😊")
        print("\n   Here's are our Food😋🍔🍕\n")

        food = df[df["Category"] == "Food"]

        for _, row in food.iterrows():
            print(
                f"ID:{row['ID']} -> "
                f"{row['Name']:<10} | "
                f"{row['Price']}EGP | "
                f"Quantity:{row['Quantity']}"
            )
    elif weather_choice == "3" or weather_choice == "normal":

        print(
            "     You're in the right place👍,"
            "     We have food that will warm you up🔥😊"
        )
        print("\n   Here's are our Food😋🍔🍕\n")

        food = df[df["Category"] == "Food"]

        for _, row in food.iterrows():
            print(
                f"ID:{row['ID']} -> "
                f"{row['Name']:<10} | "
                f"{row['Price']}EGP | "
                f"Quantity:{row['Quantity']}"
            )
    else:

        print(
            "     Welcome😊!, You light up the Resturant\n"
            "Feel free to order anything you'd like🍔😊😋"
        )




def show_menu():

    clear_screen()
    print("\n" + "=" * 10 + " Here's the Mneu for you 😊 " + "=" * 10)

    for category in df["Category"].unique():

        if category == "Food":
            print("\n========== Food🍕 ==========\n")

        elif category == "Desert":
            print("\n========== Desert🍰 ==========\n")

        elif category == "Drink":
            print("\n========== Drinks🍵 ==========\n")

        else:
            print(category)

        category_items = df[df["Category"] == category]

        for _, row in category_items.iterrows():

            print(
                f"ID:{row['ID']} -> "
                f"{row['Name']:<20} | "
                f"{row['Price']} EGP | "
                f"Quantity:{row['Quantity']:<20}"
            )
    

    
    

def order_food(food_id, Quantity):
    
    if food_id == "":
        print("🤖 Bot is typing...")
        time.sleep(1)
        print("🤖 Bot: You didn't write Food ID❌,Try again🔁")
        return

    food_id = int(food_id)

    food = df[df["ID"] == food_id]

    if food.empty:
        print("🤖 Bot is typing...")
        time.sleep(1)
        print("🤖 Bot: Invalid food id ❌")
        return


    if Quantity == "":
        print("🤖 Bot is typing...")
        time.sleep(1)   
        print("🤖 Bot: You didn't write Quantity❌,Try again🔁")
        return

    Quantity = int(Quantity)

    avalid_quantity = food.iloc[0]["Quantity"]

    if Quantity > avalid_quantity:
        print("🤖 Bot is typing...")
        time.sleep(1)
        print("🤖 Bot: Not enough quantity ❌🫤")
        return

    name = food.iloc[0]["Name"]
    price = food.iloc[0]["Price"]

    found = False

    for item in cart:

        if item["ID"] == food_id:

            item["Qty"] += Quantity
            item["Total"] = item["Qty"] * item["Price"]

            found = True
            break

    if not found:

        cart.append({

            "ID": food_id,
            "Name": name,
            "Price": price,
            "Qty": Quantity,
            "Total": price * Quantity

        })

    df.loc[df["ID"] == food_id, "Quantity"] = avalid_quantity - Quantity
    print("🤖 Bot is typing...")
    time.sleep(1)
    print("🤖 Bot: Added to cart ✅🛒")

    



def show_cart():
    clear_screen()
    
    if not cart:
        print("🤖 Bot is typing...")
        time.sleep(1)
        print("\n🤖 Bot: Cart is empty 🛒❌")

    else:
        print("\n🤖 Bot: Sure! Here's your cart 🛒")
        print("\n===== YOUR CART =====\n")

        total = 0

        for item in cart:

            print(
                f"{item['Name']:<20}"
                f"x{item['Qty']:<7}"
                f"{item['Price']}EGP"
            )

        print("\n" + "=" * 10 + " Receipt " + "=" * 10 + "\n")

        print(

            f"{'Name':<15}"
            f"{'Qty':<10}"
            f"{'Price':<10}"
            f"{'Total':<10}"

        )

        print("-" * 50 + "\n")

        for item in cart:

            print(

                f"{item['Name']:<15} "
                f"{item['Qty']:<10} "
                f"{item['Price']:<10}"
                f"{item['Total']:<10}"

            )

            total += item["Total"]

        if total >= 500:

            total *= 0.9

            print("\n        10% Discount Aplplied🎉")

        vat = total * 0.10

        grand_total = total + vat

        print("\n")

        print(f"Subtotal = {total:.2f}EGP")

        print(f"\nVAT = {vat:.2f}EGP")

        print(f"\nTotal = {grand_total:.2f}EGP")

        print("\nDate :", datetime.now().strftime("%d/%m/%Y"))

        print("Time :", datetime.now().strftime("%H:%M:%S"))
    

def remove_item():
    clear_screen()
    if not cart:
        print("🤖 Bot is typing...")
        time.sleep(1)
        print("\n🤖 Bot: Cart is empty 🛒❌")
        
        return

    print("\n===== YOUR CART =====\n")

    for item in cart:
        print(f"ID:{item['ID']} -> {item['Name']} x{item['Qty']}")

    print("🤖 Bot is typing...")
    time.sleep(1)
    remove_item = int(input("\n 🤖 Bot: Enter item id to remove❌: "))

    found = False

    for item in cart:

        if item["ID"] == remove_item:
            print("🤖 Bot is typing...")
            time.sleep(1)
            removed_Qty = int(input("\n 🤖 Bot: How many do you want to remove? "))

            if removed_Qty <= 0:
                print("🤖 Bot is typing...")
                time.sleep(1)
                print("\n🤖 Bot: Invalid quantity!❌")

                found = True

                break

            if removed_Qty > item["Qty"]:

                print("🤖 Bot is typing...")
                time.sleep(1)
                print("\n🤖 Bot: The quantity of item is more than what's in your cart🛒❌")

                found = True

                break

            df.loc[
                df["ID"] == remove_item,
                "Quantity"
            ] += removed_Qty

            item["Qty"] -= removed_Qty

            item["Total"] = item["Qty"] * item["Price"]

            if item["Qty"] == 0:
                cart.remove(item)
            print("🤖 Bot is typing...")
            time.sleep(1)
            print("\n🤖 Bot: Item updated Successfully✅🛒")
            clear_screen()
            found = True

            break

    if not found:
        print("🤖 Bot is typing...")
        time.sleep(1)
        print("\n🤖 Bot: Item not found in your Cart❌")
        


def search_item():
    clear_screen()
    print("🤖 Bot is typing...")
    time.sleep(1)
    food_id = input("\n 🤖 Bot: Enter item ID: ")

    if food_id == "":
        print("🤖 Bot is typing...")
        time.sleep(1)
        print("\n🤖 Bot: You didn't write an ID❌,Try again🔁")
        return

    if not food_id.isdigit():
        print("🤖 Bot is typing...")
        time.sleep(1)
        print("\n🤖 Bot: ID must be a number❌,Try again🔁")
        return

    food_id = int(food_id)

    food = df[df["ID"] == food_id]

    if food.empty:
        print("🤖 Bot is typing...")
        time.sleep(1)
        print("\n🤖 Bot: Food ID didn't found❌")

        return

    row = food.iloc[0]

    print("\n========== Food Found ==========\n")

    print(
        f"ID :{row['ID']}\n"
        f"Name :{row['Name']}\n"
        f"Category :{row['Category']}\n"
        f"Price :{row['Price']}EGP\n"
        f"Quantity :{row['Quantity']}"
    )



def main():

    weather(weather_choice=input("\n🤖 Bot: How's the weather today? (hot/cold/normal): "))

    while True:

        show_menu()

        user_choise = input("\n 🤖 Bot: Choose an option:")

        if user_choise == "1":

            order_food()

        elif user_choise == "2":

            show_cart()

        elif user_choise == "3":

            remove_item()

        elif user_choise == "4":

            search_item()

        elif user_choise == "5":

            print("\n🤖 Bot: OK, Have a nice day 👋")

            break

        else:

            print("\n🤖 Bot: Invalid option ❌")

        df.to_csv("Menu.csv", index=False)




#شات بوت يعتمد على الدوال اللي فوق عشان يشتغل و يتفاعل مع المستخدم(قواعد و شروط)


def chatbot():
    print("""

 █████╗ ██╗         █████╗ ███████╗██████╗ ██╗ ██████╗  █████╗  █████╗
██╔══██╗██║        ██╔══██╗██╔════╝██╔══██╗██║██╔═══██╗██╔══██╗██╔══██╗
███████║██║        ███████║███████╗██║  ██║██║██║   ██║███████║███████║
██╔══██║██║        ██╔══██║╚════██║██║  ██║██║██║▄▄ ██║██╔══██║██╔══██║
██║  ██║███████╗   ██║  ██║███████║██████╔╝██║╚██████╔╝██║  ██║██║  ██║
╚═╝  ╚═╝╚══════╝   ╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝ ╚══▀▀═╝ ╚═╝  ╚═╝╚═╝  ╚═╝

                 🍽️  AL ASDIQAA RESTAURANT  🍴
═══════════════════════════════════════════════════════════════════════
            Fresh Food • Great Taste • Fast Service
═══════════════════════════════════════════════════════════════════════

          """)

    print("🤖 Bot is typing...")
    time.sleep(1)
    

    print("""🤖 Bot:
   Welcome to Al Asdiqaa Restaurant! 🍔\n
   I'm your virtual assistant, and I'm here to help you with your food and drink orders. 🍕🍟🥤

   """)
    while True:
        print("🤖 Bot is typing...")
        time.sleep(2)
        print("""\n 🤖 Bot:
    What would you like to do today? 😊 """)
        
        print("=" * 50)
        print("1-Order food🍔")
        print("2-Show cart🛒"  )
        print("3-Remove item from cart🛒❌")
        print("4-Search by ID🔍")
        print("5-Exit👋")
        print( "=" * 50)
        user = input("\n🧑🏻 You : ").lower()
        
        #clear_screen()
        if user == "1" or "order" in user:
            print("🤖 Bot is typing...")
            time.sleep(1)
            print("\n🤖 Bot: Sure! Let's get started with your order. 🍔🍕")
            
            print("        I will show you our menu, Take your time and choose your favorite meal😊")
            time.sleep(2)
            while True:
                show_menu()
                time.sleep(1)
                print("\n🤖 Bot is typing...")
                time.sleep(1)
                order_food(food_id=input("\n🤖 Bot: Enter Food id:"), Quantity=input("\n🤖 Bot: How much do you want(enter a number):"))
                print("\n🤖 Bot is typing...")
                time.sleep(1)
                print("\n🤖 Bot: Do you want to order more? (yes or no)")
                bot = input("\n🧑🏻 You : ").lower()
                if bot == "yes":
                    continue
                elif bot == "no":
                    print("\n🤖 Bot is typing...")
                    time.sleep(1)
                    print("\n🤖 Bot: Do you want to see your cart? (yes/no):")
                    bot = input("\n🧑🏻 You : ").lower()
                    if bot == "yes":
                        print("\n🤖 Bot is typing...")
                        time.sleep(1)
                        print("\n🤖 Bot: Sure! Here's your cart 🛒")
                        time.sleep(1)
                        show_cart()
                        input("\n🤖 Bot: Press Enter to continue...")
                        clear_screen()
                        break
                    
                    elif bot == "no":
                        print("\n🤖 Bot is typing...")
                        time.sleep(1)
                        print("\n🤖 Bot: Do you want to order more? (yes or no)")
                        bot = input("\n🧑🏻 You : ").lower()
                        if bot == "yes":
                            continue
                        elif bot == "no":
                            print("\n🤖 Bot is typing...")
                            time.sleep(1)
                            print("\n🤖 Bot: OK, Have a nice day 👋")
                            break
                        else :
                            print("\n🤖 Bot is typing...")
                            time.sleep(1)
                            print("\n🤖 Bot: Invalid option ❌")
                            break
                    else:
                        print("🤖 Bot is typing...")
                        time.sleep(1)
                        print("\n🤖 Bot: Invalid option ❌")
                        break
                else:
                    print("\n🤖 Bot is typing...")
                    time.sleep(1)
                    print("\n🤖 Bot: Invalid option ❌")
                    break




        elif user == "2" or "show" in user:
            clear_screen()
            time.sleep(1)
            print("🤖 Bot is typing...")
            time.sleep(2)
           
            show_cart()
            input("\n🤖 Bot: Press Enter to continue...")
            clear_screen()
            time.sleep(1)
            print("🤖 Bot is typing...")
            time.sleep(1)
            print("\n🤖 Bot: Would you like to continue shopping? (yes/no)")
            bot = input("\n🧑🏻 You : ").lower()
            if bot == "yes":
                clear_screen()
                continue
            elif bot == "no":
                print("🤖 Bot is typing...")
                time.sleep(1)
                print("""\n🤖 Bot:
    Thank you for choosing Al Asdiqaa Restaurant ❤️
    We hope to see you again soon!
    Have a wonderful day 👋""")
                print("\nexiting...")
                break




        elif user == "3" or "remove" in user:
            print("🤖 Bot is typing...")
            time.sleep(1)
            print("\n🤖 Bot: Sure! Let's remove an item from your cart 🛒❌")
            time.sleep(1)
            remove_item()



        elif user == "4" or "search" in user:
            print("🤖 Bot is typing...")
            time.sleep(1)
            print("\n🤖 Bot: Sure! Let's search for an item by its ID 🔍")
            time.sleep(1)
            search_item()


        elif user == "5" or "exit" in user:
            clear_screen()
            print("🤖 Bot is typing...")
            time.sleep(1)
            print("""\n🤖 Bot:
    Thank you for choosing Al Asdiqaa Restaurant ❤️
    We hope to see you again soon!
    Have a wonderful day 👋""")
            print("\nexiting...")
            break
        else:
            print("🤖 Bot is typing...")
            time.sleep(1)
            print("\n🤖 Bot: Invalid option ❌, Please try again🔁")
            print("\n🤖 Bot: Do you want to try again? (yes/no): ")
            user = input("\n🧑🏻 You : ").lower()
            if user == "yes":
                continue
            elif user == "no":
                print("🤖 Bot is typing...")
                time.sleep(1)
                print("""\n🤖 Bot:
    Thank you for choosing Al Asdiqaa Restaurant ❤️
    We hope to see you again soon!
    Have a wonderful day 👋""")
                print("\nexiting...")
                break

chatbot()

   
   