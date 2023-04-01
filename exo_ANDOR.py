L1 = input("L1 ? ")
L2 = input(" L2 ? ")
N = input("number ? ")
Color = input("color ? ")

if L1 == "python" and L2 == "python" or L1 =="java" and L2 == "java":
     print("its good")
elif L1 == "python" and L2 == "java" or L1 == "java" and L2 == "python":
     print("its better")
elif N > 10 and Color =="blue":
     print("true")
elif N < 10 and Color != "blue":
     print("not good")
