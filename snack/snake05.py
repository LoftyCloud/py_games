import random
import tkinter as tk
from tkinter import messagebox

FPS = 75
R = 30
C = 50
cell_size = 10

win = tk.Tk()
canvas = tk.Canvas(win, width=C * cell_size, height=R * cell_size)
snack_list = [(0, 0), (1, 0), (2, 0)]
snack_color = "green"
head_color = "orange"
food_color = "red"
broad_color = "black"
food = None
direction = [1, 0]
SCORE = 0


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
    canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline=broad_color, width=1)


def draw_broad(canvas):
    """
    draw background
    :return:
    """
    for ri in range(R):
        for ci in range(C):
            draw_single_cell(canvas, ci, ri)


def draw_snack(color=snack_color):
    """
    draw the snack by snack_list with a orange head
    :param color:to repaint the snack
    :return:
    """
    head_c, head_r = snack_list[-1]
    draw_single_cell(canvas, head_c, head_r, head_color)

    for i in range(2, 4):  # i in [2, 3]
        cell = snack_list[-i]
        cell_c, cell_r = cell
        draw_single_cell(canvas, cell_c, cell_r, color)


def check_move():
    """
    to confirm whether the snack can move to the direction or not
    check the wall and the snack itself
    :return:
    """
    snack_c, snack_r = snack_list[-1]
    dc, dr = direction
    new_c = snack_c + dc
    new_r = snack_r + dr
    if new_c >= C or new_r >= R or new_c < 0 or new_r < 0:
        return False
    elif (new_c, new_r) in snack_list:
        return False
    return True


def game_over():
    messagebox.showinfo("GameOver", "SCORE: %s" % SCORE)
    win.destroy()
    return


def draw_snack_move():
    dc, dr = direction
    head_c, head_r = snack_list[-1]
    new_block = (head_c + dc, head_r + dr)

    if check_move():
        # cover the snack's tail with the broad_color to hide it
        tail_c, tail_r = snack_list[0]
        draw_single_cell(canvas, tail_c, tail_r)
        # update the snack_list
        del (snack_list[0])
        snack_list.append(new_block)
        # repaint the snack after moving
        draw_snack()
        # draw_single_cell(canvas, head_c, head_r, head_color)
    else:
        game_over()


def generate_new_food():
    """
    from a food which is not over the snack
    and draw it out
    :return:
    """
    food_c = random.randint(0, C - 1)
    food_r = random.randint(0, R - 1)
    new_food = (food_c, food_r)
    if new_food in snack_list:
        generate_new_food()
    else:
        draw_single_cell(canvas, food_c, food_r, food_color)
        return new_food


def check_eat():
    """
    check whether the snack eat the food or not
    and update the SCORE
    :return:
    """
    if food in snack_list:
        global SCORE
        SCORE += 10
        win.title("GoodWind - SCORE: %s" % SCORE)
        return True
    return False


def snack_grow_up():
    head_c, head_r = snack_list[-1]
    dc, dr = direction
    new_c = head_c + dc
    new_r = head_r + dr
    snack_list.append((new_c, new_r))


def move_snack(event):
    """
    move the snack with the keyboard
    :param event:
    :return:
    """
    global direction
    if event.keysym == "Left" and direction != [1, 0]:
        direction = [-1, 0]
    elif event.keysym == "Right" and direction != [-1, 0]:
        direction = [1, 0]
    elif event.keysym == "Up" and direction != [0, 1]:
        direction = [0, -1]
    elif event.keysym == "Down" and direction != [0, -1]:
        direction = [0, 1]
    else:
        return

    draw_snack_move()


def game_loop():
    win.update()
    global food

    if food is None:
        # from a new food
        food = generate_new_food()
    elif check_eat():
        # check whether the snack eat the food or not
        snack_grow_up()
        food = None
    else:
        draw_snack_move()
    win.after(FPS, game_loop)


def main():
    canvas.pack()  # put the canvas into win
    draw_broad(canvas)

    canvas.focus_set()
    canvas.bind("<KeyPress-Left>", move_snack)
    canvas.bind("<KeyPress-Right>", move_snack)
    canvas.bind("<KeyPress-Up>", move_snack)
    canvas.bind("<KeyPress-Down>", move_snack)

    win.update()
    win.after(FPS, game_loop)
    win.title("GoodWind - SCORE: %s" % SCORE)
    win.mainloop()


if __name__ == '__main__':
    main()
