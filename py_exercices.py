celsius = 37.75


farenheit = (celsius *9/5) + 32

print(farenheit)

celsius = 54

print(farenheit)

def converter(celsius):
    farenheit = (celsius *9/5) + 32
    print(farenheit)

converter(10)

def success():
    moi = "je vais réussir"
    print(moi)

success()

def subtract(nb1,nb3):
    total = nb3-nb1
    print(total)

subtract(2,10)

def multiply(nb2,nb4,nb5):
    total1 = nb2*nb4*nb5
    return total1

r =multiply(1,2,3)

print(r)

print("please enter your name ")
name=input()



def converter():
    x = input("degrees Celsius please ? ")
    farenheit = float(x) * 9/5 + 32
    return x + " degrees Celsius is "+ str(farenheit)+ " degrees Farenheit"

print(converter())

secret_number =18
guess = input("donne un nombre: ")
print(secret_number==guess)


secret = 10
guesss = input("guess ")
print(secret==guess)

def Convert():
    x = input("what degrees ?")
    faren = float(x) * 9/5 +32
    if float(x) > 25:
        print("it's fucking hot here")
    return faren




print(Convert())


