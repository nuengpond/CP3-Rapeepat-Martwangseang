def vatCalculate(totalPrice = float(input("Price ="))):
    result = totalPrice+(totalPrice*7/100)
    return result

print(vatCalculate())
