from shapes import Paper, Triangle, Rectangle, Oval

a = 200
b = 300


def Car():

    paper = Paper()

    rect1 = Rectangle()

    rect1.set_x(a)
    rect1.set_y(b)

    rect1.set_width(100)
    rect1.set_height(200)
    rect1.set_color("blue")

    circ1 = Oval()

    circ1.set_x(a+50)
    circ1.set_y(b+150)

    circ1.set_height(1)
    circ1.set_width(1)

    circ1.set_color("white")

    rect1.draw()

    circ1.draw()

    paper.display()


Car()
