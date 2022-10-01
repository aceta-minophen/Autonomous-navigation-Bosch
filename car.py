from shapes import Paper, Triangle, Rectangle, Oval

# Center
a = 300
b = 300

# Colors
sensorColor = "light coral"


def Car():

    paper = Paper()

    body = Rectangle()
    cam = Triangle()
    s1 = Triangle()
    s2 = Triangle()
    s3 = Triangle()
    s4 = Triangle()

    body.set_param(100, 200, a, b, "blue")

    # rect1.set_x(0)
    # rect1.set_y(0)

    #circ1 = Oval()

    #circ1.set_param(100, 100, a, b, "black")

    # trian.draw()

    body.draw()

    # circ1.draw()

    cam.draw(a, b-75, a-50, b-220, a+50, b-220, "light green")
    s1.draw(a-50, b-100, a-50, b-200, a-150, b-100, sensorColor)
    s2.draw(a+50, b-100, a+50, b-200, a+150, b-100, sensorColor)
    s3.draw(a+50, b+100, a+50, b+200, a+150, b+100, sensorColor)
    s4.draw(a-50, b+100, a-50, b+200, a-150, b+100, sensorColor)

    paper.display()


Car()
