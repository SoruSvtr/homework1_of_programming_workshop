cmd = input('type sum, difference, multiple or divide : ')

cmd_pack = ["sum", "difference", "multiple", "divide"]

if cmd not in cmd_pack:
    print("Enter the correct operation !")
    cmd = input('type sum, difference, multiple or divide : ')

a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))

result = 0

if cmd == "sum":
    result = a + b
elif cmd == "difference":
    result = a - b
elif cmd == "multiple":
    result = a * b
else:
    result = a / b
    
print(result)