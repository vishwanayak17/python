def convert_paisa(price):
    paisa = int(price * 100)
    return paisa


price = float(input("Enter price: "))

paisa = convert_paisa(price)

print("Price in paisa =", paisa)