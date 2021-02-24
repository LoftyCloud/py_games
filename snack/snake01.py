import tkinter as tk

R = 50
C = 50
cell_size = 10

win = tk.Tk()
canvas = tk.Canvas(win, width=C * cell_size, height=R * cell_size)
snack_list = [(0, 0), (1, 0), (2, 0)]
snack_color = "green"
food_color = "red"


def draw_single_cell(canvas, c, r, color="black"):
    """
    draw black cell with white edge
    :param canvas:
    :param c:
    :param r: cell's location
    :param color: cell's color, default is black
    :return:
    """
    x0 = c * cell_size
    y0 = r * cell_size

    x1 = x0 + cell_size
    y1 = y0 + cell_size
    canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="white", width=1)


def draw_broad(canvas):
    """
    draw background
    :param canvas:canvas
    :return:
    """
    for ri in range(R):
        for ci in range(C):
            draw_single_cell(canvas, ci, ri)


def draw_snack(canvas, snack_list):
    """
    draw the snack by snack_list
    :param canvas:
    :param snack_list: record the every cell's position
    :return:
    """
    for cell in snack_list:
        cell_c, cell_r = cell
        draw_single_cell(canvas, cell_c, cell_r, snack_color)


def draw_food(canvas):
    food = (4, 0)
    food_c, food_r = food
    draw_single_cell(canvas, food_c, food_r, food_color)


def main():
    canvas.pack()  # put the canvas into win
    draw_broad(canvas)

    draw_snack(canvas, snack_list)
    draw_food(canvas)

    win.title("snack")
    win.mainloop()


if __name__ == '__main__':
    main()
