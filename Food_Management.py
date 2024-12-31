Favorite_Foods_List = []

while True:
    print("\t\tWelcome To Favorite Foods Manager")
    print("\t\t\t1. Add Foods")
    print("\t\t\t2. Remove Foods")
    print("\t\t\t3. View All Favorite Foods")
    print("\t\t\t0. Exit")

    try:
        option = int(input("Choose an Option : "))
    except ValueError:
        print("Invalid Input! Please Enter a Number From the Option")
        print("\n")
        continue

    if option == 1:
        food_name = input("Enter Favorite Food Name : ")
        food = food_name.capitalize()
        Favorite_Foods_List.append(food)
        print(f"{food} Add Successfully")
        print(Favorite_Foods_List)
        print("\n")

    elif option == 2:
        food_name = input(("Enter a Food Name For Remove : "))
        food = food_name.capitalize()
        try:
            Favorite_Foods_List.remove(food)
            print(f"{food} Remove Successfully")
            print(Favorite_Foods_List)
        except ValueError:
            print(f"{food} is not in the Favorite Food List, Please Check the List")
            print(Favorite_Foods_List)  
            print("\n")

    elif option == 3:
        if Favorite_Foods_List:
            print("Your Favorite Foods : ")
            for _, food in enumerate(Favorite_Foods_List, start=1):
                print(f"{_}.{food}")

        else:
            print("Food List is empty or didn't added yet! ")
            print("\n")

    elif option == 0:
        print("Thanks For Using Favorite Foods Manager")
        break        
    
    else:
        print("Invalid Choice!, Please Enter Again.")
        print("\n")
