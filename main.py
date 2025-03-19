def select_dish(foods, selected_food):
     if selected_food < 0:
         raise ValueError("Invalid Input!")  # This is Error detection
    # Select_dish  notices there's something wrong, but doesn't know the best way to handle it. But the menu driver does know how to report that to the user.

     print(f"Ah, {foods[selected_food]}! An excellent choice!")

def your_menu(foods):
    try:
        index = 1
        for dish in foods:
            print(f"{index}. {dish}")
            index += 1
    
        selected_choice = int(input("Your order number? "))
        # We usually seperate error detection from error fix.
        # if selected_choice < 1:
        #     raise IndexError("Enter a value between 1 and {len(foods)}")
        select_dish(foods, selected_choice - 1)

    except (IndexError, ValueError) as error:
        print(f"{error} was entered.")  # it didn't show error in case of negative entry
        print("Next time try entering something on the menu!")


menu_items = [
    "Yakisoba",
    "Pho Tai Nam Gan",
    "Chile Verde",
    "Swiss & Mushroom Burger",
    "Saag Paneer",
]

your_menu(menu_items)
print("Yum!")