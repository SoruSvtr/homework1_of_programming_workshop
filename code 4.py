import turtle

bg_clr = input("Enter your background color : ")
tlt = input("Enter your title : ")

wn = turtle.Screen()

wn.bgcolor(bg_clr)
wn.title(tlt)

srsh = turtle.Turtle()

srsh.shape("turtle")

clr = input("Enter your square color : ")

srsh.color(clr)

sz = int(input("Enter your size : "))

for i in range(4):
    srsh.forward(sz)
    srsh.left(90)
    srsh.stamp()

wn.mainloop()