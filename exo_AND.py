x = input("météo ? ")
y = input("température ? ")

if x == "raining" and y == "cold":
    print("take an umbrella and a warm jacket.")
elif x == "raining" and y == "warm":
    print("take an umbrella and a t-shirt.")
elif x == "sunny" and y == "cold":
      print("take sunglasses and a warm jacket.")
elif x == "sunny" and y == "warm":
      print("take sunglasses and a t-shirt.")
else: print("stay home!")
