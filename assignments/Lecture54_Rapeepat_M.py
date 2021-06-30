def Login():
    usernameInput = input("username: ")
    passwordInput = input("password: ")
    if usernameInput == "admin" and passwordInput == "01234":
        return ShowMenu()
    else:
        print("Please try again !")
        return Login()
def ShowMenu():
    print("----Pond's----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    print("3. Finish")
    return MenuSelect()
def MenuSelect():
    userSelected = int(input(">>"))
    if userSelected == 1:
        return vatCalculate()
    elif userSelected == 2:
        return PriceCalculate()
    elif userSelected == 3:
        print("-------------------------")
        print("Bye Bye (^_^)/")
    else:
        print("Please Select Menu")
        return ShowMenu()
def vatCalculate():
    totalPrice = int(input("TotalPrice ="))
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    print("VAT =",result)
    return ShowMenu()
def PriceCalculate():
    price1 = int(input("1st Product Price :"))
    price2 = int(input("2nd Product Price :"))
    result = str((price1+price2)+((price1+price2)*7/100))
    print("Total Price =",result)
    return ShowMenu()

print(Login())

