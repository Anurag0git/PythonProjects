print("Welcome to Love Calculator !!")
name1 = input("Enter your name: ")
name2 = input("Enter their name: ")
name1.lower()
name2.lower()
name = name1.lower() + name2.lower()

T = str(name.count("t"))
R = str(name.count("r"))
U = str(name.count("u"))
E = str(name.count("e"))
L = str(name.count("l"))
O = str(name.count("o"))
V = str(name.count("v"))
# print(T,R,U,E,L,O,V)
a = int(T + L)
b = int(R + O)
c = int(U + V)
d = int(E + E)
print(f"Your love percentage is {a+b+c+d}")