stock = int(input("Enter the Current stock :")) 
proceed = True

while True:
    if stock == 0:
        a = "Out of Stock!"
        proceed = False 
    elif stock <= 5:
        a = "Low on Stock!"
        
    if proceed == False:        
        print(a, "Please Restock!")
        ask = input("Do you want to Restock? (Press 'o' for yes and 'x' for no)")
        
        if ask == 'o':
            password = input("Enter your password :")
            if password == "Mghr2@3#@vendingmachine":
                stock2 = int(input("Enter the  stock :"))
                stock = stock + stock2
                print("Stock updated!", stock2, "items is/are added to the stock!")
                print("Total stock is :", stock)
            else:
                print("Wrong Password!")
                continue
        else:
            continue
        
    proceed = True
    if stock <= 5:
        a = "Low on Stock!"
    if stock == 1:
        x = "item"
        y = "is"
    else:
        x = "items"
        y = "are"
    if stock <= 5:
        print("Notice!", a,  "Only", stock, x, y, "available!")  
        ask2 = input("Do you want to proceed with buying? (Press 'o' for yes and 'x' for no) :")      
        
        if ask2 == "o":
            pass
        elif ask2 == "Mghr2@3#@vendingmachine":
            proceed = False
            continue    
        else:
            continue
    
    user_want = int(input("How many candies do you want? "))
    i = 1
    
    if user_want > stock:
        print("Sorry! only", stock, x, y, "available in the stock! You can buy only", stock, x, ". Do you want to proceed? ")
        ask3 = input("Press 'o' for yes and 'x' for no :")
        if ask3 == 'o':
            pass
        else:
            continue
    
    while i <= user_want:
        if i > stock + i - 1:
            print("Out of Stock!")
            break
        
        else:
            print("Candy")
            i = i + 1
            stock = stock - 1
            
    if i > 1:
        print("Enjoy")
        
    print("Come again!")
    continue

        
    
        