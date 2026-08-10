#calculator project
#meyar meno entekhab kon mitone adad ya shekl bashe
#bar asas entekhab on meno ye kari anjam bede
print(" + | jam")
print(" - | tafriq")
print(" * | zarb")
print(" / | taqsim")
print(" = | exit")
choice = input("enter your choice: ")
while choice != "=" :
    if choice == "+":
        n1 = int(input("enter uour number:"))
        n2 = int(input("enter your number: "))
        print(f" hasel Jam = {n1 + n2} ")
    elif choice == "-":
        n1 = int(input("enter uour number:"))
        n2 = int(input("enter your number: "))
        print(f" hasel Tafriq = {n1 - n2} ")
    elif choice == "*":
        n1 = int(input("enter uour number:"))
        n2 = int(input("enter your number: "))
        print(f" hasel Zarb = {n1 * n2} ")
    elif choice == "/":
        n1 = int(input("enter uour number:"))
        n2 = int(input("enter your number: "))
        print(f" hasel Taqsim = {n1 / n2} ")
    else:
        print("invalid choice: ")
    print("---------Meno---------")      
    print(" + | jam")
    print(" - | tafriq")
    print(" * | zarb")
    print(" / | taqsim")
    print(" = | exit")
    choice = input("enter your choice: ")
    print("---------Meno---------")
print("tanks for your using my app \u2764\uFE0F" )