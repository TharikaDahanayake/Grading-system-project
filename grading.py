try:
    mark_input = input("Enter the mark between 0 and 100: ")
    mark = int(mark_input)
    if 0 <= mark <= 100:
        if 75 <= mark <= 100:
            print("Grade A")
        elif 65 <= mark <= 74:
            print("Grade B")
        elif 55 <= mark <= 64:
            print("Grade C")
        elif 35 <= mark <= 54:
            print("Grade S")
        else:
            print("Grade F")
    else:
        print("Invalid mark entered. Please enter a mark between 0 and 100.")
except ValueError:
    print("Invalid input. Please enter a numeric value between 0 and 100.")