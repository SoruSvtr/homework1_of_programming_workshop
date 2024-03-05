q = 1
cmd_pack = ["deposit", "withdraw", "balance"]

print("Please insert your card !")
print("Please Enter your password : ")
password = int(input())

balance = 123456789
result = 0

while q != 0:
    cmd = input("Enter deposit, withdraw or balance : ")

    if cmd not in cmd_pack:
        print("Enter the valid operation !")
        cmd = input("Enter deposit, withdraw or balance : ")

    if cmd == cmd_pack[0]:
        dep = int(input("Enter how much : "))
        balance += dep
    elif cmd == cmd_pack[1]:
        withd = int(input("Enter how much : "))
        balance += withd
    else:
        print(balance)

    q = int(input("Enter 0 for quit : "))