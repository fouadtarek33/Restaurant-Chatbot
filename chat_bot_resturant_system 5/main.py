import pandas as pd 
from datetime import datetime
import os
import time
import random
from chat_bot import ai_assistant
df = pd.read_csv("Menu.csv")


typing_messages = [
    "🤖 Bot is typing...",
    "🤖 One moment...",
    "🤖 Let me check...",
    "🤖 Preparing your request..."
]

cart=[]
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def weather_recommendation(df):
    print("Hello before you place an order, tell me......")

    print("How's the weather treating you today?\n1-Hot🔥\n2-Cold❄️\n3-Normal🌸")
    weather = input("1/2/3: ")

    if "1" in weather:
        print("\nI advise you to order some cold drinks🥤🧊")

        print("\n        Here are our drinks😊❄️")

        drinks = df[df["Category"] == "Drink"]

        for _, row in drinks.iterrows():
            print(f"\nID:{row["ID"]} -> {row["Name"]:<10} | {row["Price"]}EGP  | Quantity:{row["Quantity"]}")

        print("\n"+"-"*15)
        print("\nWould you like to place an order🍔💯")
        order = input("(Y/N): ").strip().lower()
        if order == "y":
            order_food(df, cart)
        else:
            print("\nWelcome😊!, You light up the  Resturant\nFeel free to order anything you'd like🍔😊😋")
            time.sleep(5)
            clear()
    elif "2" in weather:
        print("\nYou're in the right place👍, \nWe have food that will warm you up🔥😊")
        print("\nHere's are our Food😋🍔🍕\n")

        food = df[df["Category"] == "Food"]

        for _, row in food.iterrows():
            print(f"ID:{row["ID"]} -> {row["Name"]:<10} | {row["Price"]}EGP | Quantity:{row["Quantity"]}")
        
        print("\n"+"-"*15)
        print("\nWould you like to place an order🍔💯")
        order = input("(Y/N): ").strip().lower()
        if order == "y":
            order_food(df, cart)
        else:
            print("Welcome😊!, You light up the  Resturant\nFeel free to order anything you'd like🍔😊😋")
            time.sleep(5)
            clear()

    else:
        print("Welcome😊!, You light up the  Resturant\nFeel free to order anything you'd like🍔😊😋")
        time.sleep(5)
        clear()

def welcome_massage(df):
    print("=" * 50)
    print("""\n

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

          \n""")

def show_menu(df):
    print("=" * 50)
    print("""
            🍔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🍕
                Here's The Menu For You 😋
             🍰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🍹
        """)
    for category in df["Category"].unique():

        if category == "Food":
            print("          ========== Food🍕 ==========\n")


        elif category == "Desert":
            print("\n          ========== Desert🍰 ==========\n")
        elif category == "Drink":
            print("\n          ========== Drinks🍵 ==========\n")

        else:
            print(f"\n {category}")

        category_items = df[df["Category"] == category]

        for _, row in category_items.iterrows():
            print(
                f"ID:{row['ID']} -> "
                f"{row['Name']:<20} | "
                f"{row["Price"]} EGP |"
                f"Quantity:{row["Quantity"]:<20}"
            )

    print("\n" + "=" * 50)

def show_options(df):
    print("1-order food🍔")
    print("2-Show cart🛒")
    print("3-Remove item from cart🛒❌")
    print("4-Search by ID🔍")
    print("5-Search by Name🔍")
    print("6-Chat with AI assistant🤖")
    print("7-Exit👋")

# رساله بعد ما يخلص الطلب بتسأله عايز يعمل ايه بعد كده
def what_next(df, cart):
    print("\n🤖 Bot: What would you like to do next?\n")
    print("1- Order more food 🍔")
    print("2- View your cart 🛒")
    print("3- Finish order 👋")

    user_choice = input("\n🧑🏻 You : ").strip().lower()

    if user_choice in ["1", "order"]:
        order_food(df, cart)
    elif user_choice in ["2", "cart"]:
        show_cart(df, cart)
        input("Press Enter...")
        what_next(df, cart)
    elif user_choice in ["3", "finish"]:
        exit_program(df)
    else:
        print("\n🤖 Invalid option, try again.❌🔃")
        time.sleep(2)
        clear()

def order_food(df, cart):
    print("\n🤖 Bot:Tell me What's your budget today? ")
    budget = input("\n🧑🏻 You : ")
    time.sleep(1)
    budget = float(budget)



    print("     I will show you our menu, Take your time and choose your favorite meal😊")
    time.sleep(2)
    # while True:
        #  بتعرضله المينيو المناسب ل المييزانيه بتاعته يعني الي بتساويها او اللي اكبر منها 

    recommended = df[df["Price"] <= budget]

    print(f"""\n🤖 Your budget is {budget} EGP.
Here are the meals that fit your budget:\n""")

    #هنا هتكتبله القسم المخصص لكل عنصر ف المينيو

    for category in recommended["Category"].unique():

        if category == "Food":
            print("\n========== Food🍕 ==========\n")

        elif category == "Desert":
            print("\n========== Desert🍰 ==========\n")

        elif category == "Drink":
            print("\n========== Drinks🍵 ==========\n")

        else:
            print(category)
        #هتخش علي الداتاا المتفلتره الي هي المينيو المخصص علي الكاتيجوري  وتشوف هل هي بتساوي الخليه او العنصر الي انت واقف عليه دلوقتي ولا لا 
        category_items = recommended[recommended["Category"] == category]

        for _, row in category_items.iterrows():
            print(
                f"ID:{row['ID']} -> "
                f"{row['Name']:<20} | "
                f"{row['Price']} EGP | "
                f"Quantity:{row['Quantity']:<20}"
            )
            print("-" * 30)
    start = True

    while start:

            
        print(f"""\n🤖 What do you want:
    1- Order from these meals ✅
    2- Show full menu 📋
                    """)
        user = input("\n🧑🏻 You : ").lower()
        
        if user in ["2", "show"]:
            clear()
            print(random.choice(typing_messages))
            time.sleep(1)
            print("\n🤖 I will show you full menu, Take your time and choose your favorite meal😊")
            # print(random.choice(typing_messages))
            
            show_menu(df)
            start = False
            

        elif user in ["1", "order"]:
            start = False


        else:
            print("\n🤖 Invalid option, try again.❌🔃")
            time.sleep(1)
            input("🤖 Bot: Press Enter to continue...")
            clear()

    
    

    food_id=input("\n🤖 Bot: Enter Food id:")


    if food_id == "":
        print("🤖 Bot is typing...")
        time.sleep(1)
        print("🤖 Bot: You didn't write Food ID❌,Try again🔁")
        time.sleep(1)
        input("🤖 Bot: Press Enter to continue...")
        clear()
        return

    if not food_id.isdigit():
        print("🤖 Bot: Food ID must be a number.")
        return


    food_id = int(food_id)
    food = df[df["ID"] == food_id]

    if food.empty:
        print("🤖 Bot is typing...")
        time.sleep(1)
        print("🤖 Bot: Invalid food id ❌")
        return
        

# عرض تفاصيل العنصر المحدد جديدددد
    name = food.iloc[0]['Name']
    price = food.iloc[0]['Price']
    available_quantity = food.iloc[0]["Quantity"]

    print("\n============ Item Details ============\n")
    print(
        f"Name    : {name}  \n"
        f"Price    : {price}EGP  \n"
        f"Qunatity    : {available_quantity}"
    )
    print("=" * 30)



    Quantity = input("\n🤖 Bot: How much do you want(enter a number):")
    if Quantity == "":
        print("🤖 Bot is typing...")
        time.sleep(1)   
        print("🤖 Bot: You didn't write Quantity❌,Try again🔁")
        time.sleep(1)
        input("🤖 Bot: Press Enter to continue...")
        clear()
        return


    # التحقق مما إذا كانت الكمية المدخلة رقمًا صحيحًا
    if not Quantity.isdigit():
        print("🤖 Bot is typing...")
        time.sleep(1)
        print("🤖 Bot: Quantity must be a number, Try again🔁")
        time.sleep(1)
        input("🤖 Bot: Press Enter to continue...")
        clear()
        return


    
    Quantity = int(Quantity)
    available_quantity = food.iloc[0]["Quantity"]

# التحقق اذا كانت الكميه اصلًا أصغر من 0
    if Quantity <= 0:
        print("🤖 Bot is typing...")
        time.sleep(1)
        print("🤖 Bot: Quantity must be greater than 0.")
        print("🤖 Bot: Try again🔄️")
        time.sleep(1)
        input("🤖 Bot: Press Enter to continue...")
        clear()
        return
# التحقق مما إذا كانت الكمية المدخلة أكبر من الكمية المتاحة
    if Quantity > available_quantity:
        print(f"Sorry, only {available_quantity} item(s) are available🤏")
        print("🤖 Bot: Try again🔄️")
        time.sleep(2)
        input("🤖 Bot: Press Enter to continue...")
        clear()
        return
    


    current_total = 0
# هنا انت بتحسب اجمالي السله خليك فهمان
    for item in cart:
        current_total += item["Total"]


    new_order_total = price * Quantity
    new_total = current_total + new_order_total

    if new_total > budget:
        print(random.choice(typing_messages))
        time.sleep(1)
        print("\n🤖 This order exceeds your budget.❌")
        print(f"    Your budget is {budget} EGP, and your current total is {current_total} EGP.")
        print(f"    The total for this order would be {new_total} EGP.")
        print("     Try again🔄️")
        print(random.choice(typing_messages))
        input("\n\n🤖 Bot: Press Enter to continue...")
        clear()
        return

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


    df.loc[df["ID"] == food_id, "Quantity"] = available_quantity - Quantity
    print("\n🤖 Bot is typing...")
    time.sleep(1)
    print("Added to cart ✅🛒")
    time.sleep(1)
    input("🤖 Bot: Press Enter to continue...")



# حساب المبلغ المتبقي بعد الطلب
    
    rest = budget - new_total
    if rest > 0:
        print("""🤖 Bot: 
        Do you want to see your resept? (Y / N)
        """)
        user = input("\n🧑🏻 You : ").lower()
        if user in ["y", "yes"]:


            time.sleep(1)
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

                # new_total += item["Total"]

            if new_total >= 500:

                new_total *= 0.9

                print("\n        10% Discount Aplplied🎉")

            vat = new_total * 0.10

            grand_total = new_total + vat

            print("\n")

            print(f"Subtotal = {new_total:.2f}EGP")

            print(f"\nVAT = {vat:.2f}EGP")

            print(f"\nTotal = {grand_total:.2f}EGP")

            print("\nDate :", datetime.now().strftime("%d/%m/%Y"))

            print("Time :", datetime.now().strftime("%H:%M:%S"))
            print("\n" + "=" * 10 + " Receipt " + "=" * 10 + "\n")
            time.sleep(5)
            input("🤖 Bot: Press Enter to continue...")
            what_next(df, cart)














def show_cart(df, cart):
        if not cart:
            print("\nCart is empty 🛒❌")
            print("\n"+"-"*15)
            print("\nWould you like to place an order🍔💯") 
            order = input("(Y/N): ").strip().lower()
            if order == "y":
                order_food(df, cart)

            else:
                print("\nno problem😊")
                print("\nOur Resturant is Always at your Service!!😊❤️")
                time.sleep(5)
                clear()

        else:
            print("\n===== YOUR CART =====\n")
            total = 0
            for item in cart:
                print(
                    f"{item['Name']:<20}"
                    f"x{item['Qty']:<7}"
                    f"{item['Price']}EGP"
                )

            print("\n" + "=" *10+" Receipt " + "=" *10 + "\n")

            print( 
                f"{'Name':<15}"
                f"{'Qty':<10}"
                f"{'Price':<10}"
                f"{'Total':<10}"
                )
            print("-"*50+"\n")
            for item in cart:
                print(
                    f"{item['Name']:<15} "
                    f"{item['Qty']:<10} "
                    f"{item['Price']:<10}"
                    f"{item['Total']:<10}"
                )
                total += item["Total"]
            if total >= 500:
                total *=0.9
                print("\n        10% Discount Aplplied🎉")    
            vat = total * 0.10
            grand_total = total + vat
            
            print("\n")
            print(f"Subtotal : {total: .2f}EGP")
            print(f"\nVAT : {vat:.2f}EGP")
            print(f"\nTotal : {grand_total:.2f}EGP")
            print("\nDate : " , datetime.now().strftime("%d/%m/%Y"))
            print("Time : ",datetime.now().strftime("%H:%M:%S"))   

            checkout(cart, vat, total, grand_total)                 

def remove_item(df, cart):
        if not cart:
            print("Cart is empty🛒❌")
            time.sleep(2)
            clear()
            return
        
        print("\n===== YOUR CART =====\n")

        for item in cart:
            print(f"ID:{item["ID"]} -> {item["Name"]} x{item["Qty"]}")

        remove_item = int(input("\nEnter item id to remove❌: "))
        found = False

        for item in cart:
            if item["ID"] == remove_item:
                removed_Qty = int(input("How many do you want to remove? "))

                if removed_Qty <= 0:
                    print("Invaild Qunatity!❌")
                    print("Try again🔄️")
                    found = True
                    time.sleep(3)
                    clear()
                    break
                
                if removed_Qty > item["Qty"]:
                    print("The quantity of item is more than what's in your cart🛒❌")
                    print("Try again🔄️")
                    found = True
                    time.sleep(5)
                    clear()
                    break

                df.loc[df["ID"] == remove_item,
                "Quantity"] += removed_Qty
                
                item["Qty"] -= removed_Qty

                item["Total"] = item["Qty"] * item["Price"]

                if item["Qty"] == 0:
                    cart.remove(item)
                print("Item updeted Successfuly✅🛒")
                found = True
                time.sleep(2)
                clear()
                break
        if not found:
            print("Item not found in your Cart❌")
            print("Try again🔄️")
            time.sleep(2)
            clear()

def search_food_id(df):
        food_id = input("Enter item ID: ")
        if food_id == "":
            print("You didn't write an ID❌,Try again🔁")
            time.sleep(3)
            clear()
            return
        
        if not food_id.isdigit():
            print("ID must be a number❌,Try again🔁")
            time.sleep(3)
            clear()
            return
        food_id = int(food_id)
        food = df[df["ID"] == food_id]

        if food.empty:
            print("Item ID didn't found❌")
            time.sleep(3)
            clear()
            return
        
        else:
            row = food.iloc[0]
            print("\n========== Food Found ==========\n")
            print(
            f"ID : {row['ID']}\n"
            f"Name : {row['Name']}\n"
            f"Category : {row["Category"]}\n"
            f"Price : {row['Price']}EGP\n"
            f"Quantity : {row['Quantity']}"
            )

            print("\nWould you like to place an order🍔💯") 
            order = input("(Y/N): ").strip().lower()
            if order == "y":
                order_food(df, cart)

            else:
                print("\nno problem😊")
                print("\nOur Resturant is Always at your Service!!😊❤️")
                time.sleep(5)
                clear()

def search_food_name(df):
        search = input("Enter Item Name: ").strip()

        if search == "":
            print("You didn't Enter an Item Name❗")
            print("Try again🔄️")
            time.sleep(3)
            clear()
            return
        result = df[df["Name"].str.contains(search,case=False)]
        if result.empty:
            print("Item not Found, Try again🔄️")
            time.sleep(3)
            clear()
            return
        else:
            print("\n============ Search Results ============\n")
            for _, row in result.iterrows():
                print(
                    f"ID:{row['ID']} -> "
                    f"{row['Name']:<20} | "
                    f"{row['Price']}EGP | "
                    f"Qunatity:{row['Quantity']}" 
                )
            print("\nWould you like to place an order🍔💯") 
            order = input("(Y/N): ").strip().lower()
            if order == "y":
                order_food(df, cart)

            else:
                print("\nno problem😊")
                print("\nOur Resturant is Always at your Service!!😊❤️")
                time.sleep(5)
                clear()

def exit_program(df):
    print("Thanks for visiting us ❤️")
    print("OK, Have a nice day 👋")
    return

def checkout(cart, vat, total, grand_total):
    print("\nWould you like To Checkout🛒💯✅")
    checkout = input("(Y/N): ").strip().lower()
    if checkout == "y":
        print("\n"+"="*15 +" PAYMENT RECEIPT "+"="*15)
        print( 
            f"{'Name':<15}"
            f"{'Qty':<10}"
            f"{'Price':<10}"
            f"{'Total':<10}"
            )
        print("-"*50+"\n")
        for item in cart:
            print(
                f"{item['Name']:<15} "
                f"{item['Qty']:<10} "
                f"{item['Price']:<10}"
                f"{item['Total']:<10}"
            )
        print(f"\n\nSubtotal : {total:.2f}EGP")
        print(f"\nVAT : {vat:.2f}EGP")
        print(f"\nTotal : {grand_total:.2f}EGP")
        print("-"*35)
        print("\nPayment Successfull!;✅")
        print("\nThanks for choosing our Resturant😇🍔")
        print("\nWe Hope to see you again soon!!😇❤️")
        cart.clear()
        print("Would you like place anothe Order or Exit!!")
        order = input("1/2: ")
        if order == "1":
            order_food(df, cart)
        elif order == "2":
            exit_program(df)
            exit()
    elif checkout == "n":
        print("\nno problem😊")
        print("\nOur Resturant is Always at your Service!!😊❤️")
        time.sleep(5)
        clear()
    else:
        print("Invaid choise❌")
        print("Try again🔄️")
        time.sleep(5)
        clear()



weather_recommendation(df)

while True: 
    clear()
    welcome_massage(df)   
    # show_menu(df)
    show_options(df)
    user_choise = input("Choise Option:")
    if user_choise == "1":
        order_food(df, cart)
    elif user_choise == "2":
        show_cart(df, cart)

    elif user_choise == "3":
        remove_item(df, cart)
    
    elif user_choise == "4":
        search_food_id(df)

    elif user_choise == "5":
        search_food_name(df)

    elif user_choise == "6":
        clear()
        ai_assistant(df, cart)
    elif user_choise == "7":
        exit_program(df)
        break
    else:
        print("Invalid option ❌")
        print("Try again🔄️")
        time.sleep(1)
        input("🤖 Bot: Press Enter to continue...")
        clear()

    df.to_csv("Menu.csv" , index=False)
