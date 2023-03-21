 #python project


# customer order and billing system


# welcome message :


print("HI , WELCOME TO OUR STORE  ")  # welcome message :


print("we have the following stores in our complex   : ")    # STORES

# STORES

print(" 1 HOODIES SECTION")      # STORE 1

print(" 2 SHOES AND SNEAKERS")       # STORE 2



# taking input from user


n = int(input("SELECT THE STORE YOU WANT TO ORDER FROM "))

if n == 1:

    print("This is a clothing store : PRESENTED BY ,BURBERRY,RALPH LAUREN,PRADA,NIKE,ADIDAS")
    clothes_size = input("Enter the size you want :")
    clothes_colour = input("Enter the colour you want")
    print("YOU HAVE SELECTED ", clothes_size, "of", clothes_colour, "colour")
    c = input("SELECT YOUR BRAND : ")
    if c == "burberry":
        c_price="4000₹"
        a_price="10000₹"
        print("YOU HAVE SELECTED BURBERRY")


    elif c=="ralph lauren":
        c_price = "5000₹"
        a_price = "11000₹"
        print("YOU HAVE SELECTED RALPH LAUREN")



    elif c == "prada":
        c_price = "8200₹"
        a_price = "14200₹"

        print("YOU HAVE SELECTED PRADA")



    elif c == "nike":
        c_price = "12000₹"
        a_price = "18000₹"
        print("YOU HAVE SELECTED NIKE")


    elif c == "adidas":
        c_price = "13000₹"
        a_price = "19000₹"

        print("YOU HAVE SELECTED ADIDAS")

    else:
        print("Sorry we don't have that brand")





    customer = str(input("Customer's Name:"))
    phone=int(input("enter your phone number"))

    print("YOU HAVE SELECTED",c,"HOODIE OF",clothes_colour,"COLOUR")
    print("size : ",clothes_size)
    print("THIS ITEM WILL COST YOU ",c_price,"₹" )

# BILL
    print("YOUR BILL :")
    print("order id : ", id(n))
    print(customer)
    print("PHONE NUMBER :", phone)
    print("YOUR ITEM :"  ,c,"HOODIE")
    print("COLOUR : " ,clothes_colour,)
    print("SIZE : ",clothes_size,)
    print("ACTUAL PRICE :", a_price)
    print("DISCOUNT : 6000₹")
    print("ITEM PRICE ",c_price)
    print("Thank you for shopping, HAVE A GOOD DAY")






if n == 2:



    print("THIS IS OUR SHOE AND SNEAKER SECTION : PRESENTED BY NIKE,ADIDAS,PUMA,HRX,BATA ")
    shoe_size=int(input("Please enter your size : "))
    shoe_colour=input("Select the colour you want ")
    brand = (input("SELECT THE BRAND YOU WANT TO BUY :  "))




    if brand == "nike":




        shoe_price = "14000₹"
        actual_price="20000₹"
        print("you have selected NIKE")



    elif brand == "adidas":

        shoe_price="17000₹"
        actual_price = "23000₹"
        print("you have selected ADIDAS")

    elif brand == "puma":

        shoe_price = "12000₹"
        actual_price = "18000₹"

        print("you have selected PUMA ")

    elif brand == "hrx":
        shoe_price = "2000₹"
        actual_price = "10000₹"
        print("you have selected HRX")

    elif brand == "bata":
        shoe_price = "6000₹"
        actual_price = "12000₹"
        print("you have selected BATA")

    else:
        print("Sorry we don't have that brand")




    customer = str(input("Customer's Name:"))
    phone=int(input("enter your phone number"))

    print("YOU HAVE SELECTED",brand,"SHOES OF",shoe_colour,"COLOUR",shoe_size,"SIZE")
    print("THIS ITEM WILL COST YOU ", shoe_price )


# BILL
    print("YOUR BILL :")
    print("order id : ", id(n))
    print(customer)
    print("PHONE NUMBER :", phone)
    print("YOUR ITEM :"  ,brand,"SHOES")
    print("COLOUR : " ,shoe_colour,)
    print("SIZE : ",shoe_size,)
    print("ACTUAL PRICE :", actual_price)
    print("DISCOUNT : 6000₹")
    print("ITEM PRICE ", shoe_price)
    print("Thank you for shopping, HAVE A GOOD DAY")


