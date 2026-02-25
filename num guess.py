low = 1
high = 100

print("Think of a number between 1 and 100.")

while low <= high:
    mid = (low + high) // 2
    print("Is your number is",mid,"?")
    
    user = input("Type 'h' if too high, 'l' if too low, 'c' if correct: ")
    
    if user == 'c':
        print("Yay! I guessed your number ")
        break
    elif user == 'h':
        high = mid - 1
    elif user == 'l':
        low = mid + 1
    else:
        print("Invalid input! Please type h, l, or c.")
