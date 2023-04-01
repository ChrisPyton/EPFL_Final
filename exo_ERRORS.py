def add(a, b):
    return a + b

def get_result(answer):
    if answer == "a":
        return True
    else:
        return False

print("Do you like programing?")
print("a. Yes")
print("b. No")
result = input("Enter a or b: ")

if get_result(result) ==True:
    print("Awesome! Programming is really fun!")
else: print("Hang in there! It's an acquired taste!")