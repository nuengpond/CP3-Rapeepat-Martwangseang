Esp = 55
Ame = 50
Lat = 60
Moc = 65
username = input("username: ")
password = input("password: ")
if username == "Rapeepat" and password == "1993":
    print("--- Welcome to NP'Coffee Shop (^_^) ---")
    print("1. Espresso", Esp,"THB")
    print("2. Americano", Ame,"THB")
    print("3. Latte", Lat,"THB")
    print("4. Mocha", Moc,"THB")
    Select = int(input(">>"))
    if Select == 1:
        amountEsp = int(input("Amount: "))
        print("Espresso =",Esp,"*",amountEsp)
        print("Total =",amountEsp*Esp,"THB")
    elif Select == 2:
        amountAme = int(input("Amount: "))
        print("Americano =",Ame,"*",amountAme)
        print("Total =",amountAme*Ame,"THB")
    elif Select == 3:
        amountLat = int(input("Amount: "))
        print("Latte =",Lat,"*",amountLat)
        print("Total =",amountLat*Lat,"THB")
    elif Select == 4:
        amountMoc = int(input("Amount: "))
        print("Mocha =",Moc,"*",amountMoc)
        print("Total =",amountMoc*Moc,"THB")
else:
    print("Please try again !")
print("Thank You For Choosing Us")