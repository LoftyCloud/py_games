import random
import tkinter as tk


FPS = 200
R = 50
C = 50
cell_size = 10

win = tk.Tk()
canvas = tk.Canvas(win, width=C * cell_size, height=R * cell_size)
snack_list = [(0, 0), (1, 0), (2, 0)]
snack_color = "green"
food_color = "red"
broad_color = "black"
food = None


def draw_single_cell(canvas, c, r, color=broad_color):
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


def draw_snack(canvas, snack_list, color=snack_color):
    """
    draw the snack by snack_list
    :param color:
    :param canvas:
    :param snack_list: record the every cell's position
    :return:
    """
    for cell in snack_list:
        cell_c, cell_r = cell
        draw_single_cell(canvas, cell_c, cell_r, color)


def check_move(snack_list, direction=[1, 0]):
    """
    to confirm whether the snack can move to the direction or not
    :param direction:
    :param snack_list:
    :return:
    """
    snack_c, snack_r = snack_list[-1]
    dc, dr = direction
    new_c = snack_c + dc
    new_r = snack_r + dr
    if new_c >= C or new_r >= R or new_c < 0 or new_r < 0:
        return False
    return True


def draw_snack_move(canvas, snack_list, direction=[1, 0]):
    dc, dr = direction
    c, r = snack_list[0]
    new_c, new_r = snack_list[-1]
    new_block = [new_c + dc, new_r + dr]

    if check_move(snack_list):
        # cover the snack with the broad_color to hide it
        draw_snack(canvas, snack_list, broad_color)
        # update the snack_list
        del (snack_list[0])
        snack_list.append(new_block)
        # repaint the snack after moving
        draw_snack(canvas, snack_list)


def generate_new_food():
    food_c = random.randint(0, C)
    food_r = random.randint(0, R)
    new_food = (food_c, food_r)
    return new_food


def check_eat(snack_list, food, direction=[1, 0]):
    snack_c, snack_r = snack_list[-1]
    dc, dr = direction
    new_c = snack_c + dc
    new_r = snack_r + dr
    (food_c, food_r) = food
    if new_c == food_c and new_r == food_r:
        return True
    return False


def snack_grow_up(snack_list, food):
    snack_list.append(food)


def game_loop():
    win.update()

    draw_snack_move(canvas, snack_list)

    global food
    if food is None:
        # from a new food
        (food_c, food_r) = generate_new_food()
        draw_single_cell(canvas, food_c, food_r, food_color)
        food = (food_c, food_r)
    elif check_eat(snack_list, food):
        # check whether the snack eat the food or not
        snack_grow_up(snack_list, food)
        food = None

    win.after(FPS, game_loop)


def main():
    canvas.pack()  # put the canvas into win
    draw_broad(canvas)

    win.update()
    win.title("snack")
    win.after(FPS, game_loop)
    win.mainloop()


if __name__ == '__main__':
    main()
