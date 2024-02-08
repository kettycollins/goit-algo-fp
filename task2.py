import turtle

def draw_pythagoras_tree(t, branch_len, level):
    if level == 0:
        return
    t.forward(branch_len)
    t.right(45)  # Змінено лівий поворот на правий
    draw_pythagoras_tree(t, branch_len * 0.7, level - 1)
    t.left(90)   # Змінено правий поворот на лівий
    draw_pythagoras_tree(t, branch_len * 0.7, level - 1)
    t.right(45)  # Змінено лівий поворот на правий
    t.backward(branch_len)

def main():
    window = turtle.Screen()
    window.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(0, -250)
    t.pendown()
    t.left(90)
    level = int(input("Введіть рівень рекурсії для фракталу: "))
    draw_pythagoras_tree(t, 100, level)
    window.mainloop()

if __name__ == "__main__":
    main()
