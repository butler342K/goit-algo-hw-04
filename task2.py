import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_curve(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()

    koch_curve(t, order, size)
    t.right(120)
    koch_curve(t, order, size)
    t.right(120)
    koch_curve(t, order, size)
    window.mainloop()

# Виклик функції
input_order = input("Enter the order of the Koch curve (non-negative integer): ")
try:
    order = int(input_order)
    if order < 0:
        raise ValueError
    draw_koch_curve(order)
    
except ValueError:
    print("Please enter a valid non-negative integer.")
