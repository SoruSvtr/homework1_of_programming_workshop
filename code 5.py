inp = input("Enter your input : ")

list_pack = ['[', ']', "'", ',']

for i in inp:
    if inp >= '1' and inp <= '9':
        print("consider it as an integer or a float")
        break
    elif (inp >= 'A' and inp <= 'Z') or (inp >= 'a' and inp <= 'z'):
        print("consider it as a string or charactar")
        break
    elif i in list_pack:
        print("consider it as a list")
        break