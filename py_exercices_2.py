
#def degree(celsius):
 #   farenheit = (celsius * 9/5) + 32
 #   return farenheit

#print(degree(21.5))
#print(degree(-7))
#print(degree(11))
#print(degree(0))


#def degree2(cels):
 #   return (cels * 9/5) +32

#print(degree2(2))

def degree2(celsius):
   farenheit = celsius * 9/5 +32
   return str(celsius) + " degrees Celsius are " + str(farenheit) + " degrees Farenheit"

print(degree2(20))

def longueur(cm):
   inch = cm / 2.54
   return inch

print(longueur(185))
