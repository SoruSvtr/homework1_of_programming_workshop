print("lower or upper case doesn't matter !")
cmd = input("Enter either F or C : ")
cmd_pack = ["f", "F", "c", "C"]

cmd_pack1 = ["c", "C"]
cmd_pack2 = ["f", "F"]

if cmd not in cmd_pack:
    print("Enter the correct character !")
    print("lower or upper case doesn't matter !")
    cmd = input("Enter either F or C : ")

temp = int(input("Enter the temperature : "))

result = 0

if cmd in cmd_pack1:
    result = 1.8 * temp + 32
elif cmd in cmd_pack2:
    result = ((temp - 32) * 5) / 9

print(result)