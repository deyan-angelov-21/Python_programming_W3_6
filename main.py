def main():
    print("Program starting.")
    print("Welcome to the unit converter program!")
    print("Follow the menu instructions below.")
    print()

    print("Options:")
    print("1 -- Length")
    print("2 -- Weight")
    print("0 -- Exit")
    
    choice = float(input("Your choice: "))
    print()

    if choice == 1:
        print("Length options:")
        print("1 -- Meters to kilometers")
        print("2 -- Kilometers to meters")
        print("0 -- Exit")
        l_choice = float(input("Your choice: "))
        
        if l_choice == 1:
            m = float(input("Insert meters: "))
            km = m / 1000.0
            print(f"{round(m, 1)} m is {round(km, 1)} km")
        elif l_choice == 2:
            km = float(input("Insert kilometers: "))
            m = km * 1000.0
            print(f"{round(km, 1)} km is {round(m, 1)} m")
        elif l_choice == 0:
            pass
        else:
            print("Unknown option.")
            
    elif choice == 2:
        print("Weight options:")
        print("1 -- Grams to pounds")
        print("2 -- Pounds to grams")
        print("0 -- Exit")
        w_choice = float(input("Your choice: "))
        
        conversion_factor = 453.59237
        
        if w_choice == 1:
            g = float(input("Insert grams: "))
            lbs = g / conversion_factor
            print(f"{round(g, 1)} g is {round(lbs, 1)} lb")
        elif w_choice == 2:
            lbs = float(input("Insert pounds: "))
            g = lbs * conversion_factor
            print(f"{round(lbs, 1)} lb is {round(g, 1)} g")
        elif w_choice == 0:
            pass
        else:
            print("Unknown option.")
            
    elif choice == 0:
        pass
    else:
        print("Unknown option.")

    print()
    print("Program ending.")

if __name__ == "__main__":
    main()
