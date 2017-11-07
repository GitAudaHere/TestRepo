import turtle
t = turtle.Pen()
t.speed(1)
num_side = int(input("How many sides do you want? (Choose 6): "))
side_length = int(input("How many pixels do you want each side to be? "))
side_angle = 360 / num_side

for a in range(0, 3):
    for i in range(0, 6):
        t.forward(side_length)
        t.left(side_angle)

    t.forward(side_length)
    t.right(side_angle)

    for i in range(0, 6):
        t.forward(side_length)
        t.left(side_angle)

    t.right(side_angle)

    t.right(side_angle)
    t.forward(side_length)
    t.left(180 - side_angle * 2)
    
    #t.forward(side_length)

#t.speed(1)
#t.right(side_angle)
#t.forward(side_length)
#t.right(side_angle * 2)
#t.forward(side_length / 2)
#t.right(180)

#for num_side in range(0, num_side):
#    t.forward(side_length)
#    t.backward(side_length)
#    t.left(side_angle)

