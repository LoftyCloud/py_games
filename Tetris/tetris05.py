import tkinter as tk
import random
from tkinter import messagebox

FPS = 200
R = 20  # 格子个数
C = 12
cell_size = 20  # 格子大小
score = 0

win = tk.Tk()
canvas = tk.Canvas(win, width=C * cell_size, height=R * cell_size)

SHAPES = {  # 方块格子的相对坐标
    'O': [(-1, -1), (0, -1), (-1, 0), (0, 0)],
    'Z': [(-1, -1), (0, -1), (0, 0), (1, 0)],
    'S': [(0, -1), (1, -1), (-1, 0), (0, 0)],
    'T': [(-1, -1), (0, -1), (1, -1), (0, 0)],
    'I': [(0, -2), (0, -1), (0, 0), (0, 1)],
    'L': [(-1, -2), (-1, -1), (-1, 0), (0, 0)],
    'J': [(0, -2), (0, -1), (0, 0), (-1, 0)],
    'A': [(0, 0)]
}

SHAPES_COLOR = {
    'O': "blue",
    'Z': "orange",
    'S': 'green',
    'T': 'purple',
    'I': 'red',
    'L': 'yellow',
    'J': '#CCCCCC',
    'A': 'gray'
}

# block_list记录已经固定的方块
block_list = []
for i in range(R):
    i_row = ['' for j in range(C)]
    block_list.append(i_row)

current_block = None


def draw_cell_by_cr(canvas, c, r, color="black"):
    """
    画一个方格，默认黑色
    :param canvas:画板
    :param c: 方格所在列
    :param r: 方格所在行
    :param color: 颜色
    :return:
    """
    x0 = c * cell_size
    y0 = r * cell_size

    x1 = x0 + cell_size
    y1 = y0 + cell_size
    canvas.create_rectangle(x0, y0, x1, y1, fill=color, width=2)


def draw_board(canvas, block_list):
    """
    重绘画布和方块
    :param canvas:画板
    :param block_list:已经放置好的方块
    :return:
    """
    for ri in range(R):
        for ci in range(C):
            cell_type = block_list[ri][ci]
            if cell_type:
                draw_cell_by_cr(canvas, ci, ri, SHAPES_COLOR[cell_type])
            else:
                draw_cell_by_cr(canvas, ci, ri)


def draw_cells(canvas, c, r, cell_list, color='black'):
    """
    绘制指定形状和颜色的方块
    :param canvas: 画板
    :param c:该形状设定的原点的列
    :param r:该形状设定的原点的行
    :param cell_list:形状内方格相对于自身原点的位置坐标
    :param color:颜色
    :return:
    """
    for cell in cell_list:
        cell_c, cell_r = cell
        ci = cell_c + c
        ri = cell_r + r
        if 0 <= c < C and 0 <= r < R:
            draw_cell_by_cr(canvas, ci, ri, color)


def generate_new_block():
    # 随机生成新的方块
    # choice(seq)：从非空列表中选取随机元素
    kind = random.choice(list(SHAPES.keys()))
    cr = [C // 2, 0]  # 坐标
    new_block = {
        'kind': kind,
        'cell_list': SHAPES[kind],
        'cr': cr
    }
    return new_block


def check_move(block, direction=[0, 1]):
    """
    判断俄罗斯方块是否可以朝指定方向移动
    :param block: 方块对象
    :param direction: 移动方向
    :return:
    """
    cc, cr = block['cr']
    cell_list = block['cell_list']

    for cell in cell_list:
        cell_c, cell_r = cell
        c = cell_c + cc + direction[0]
        r = cell_r + cr + direction[1]
        # 判断左右边界以及下边界
        if c < 0 or r >= R or c >= C:
            return False

        if r > 0 and block_list[r][c]:
            return False

    return True


def draw_block_move(canvas, block, direction=[0, 0]):
    """
    绘制方块的移动
    :param canvas:画板
    :param block: 方块对象
    :param direction: 移动方向
    :return:
    """
    shape_type = block['kind']
    c, r = block['cr']
    cell_list = block['cell_list']

    # 用背景绘制原有位置的方块以达到清除的目的
    draw_cells(canvas, c, r, cell_list)

    dc, dr = direction
    new_c, new_r = c + dc, r + dr
    block['cr'] = [new_c, new_r]
    # 在新位置绘制方块
    draw_cells(canvas, new_c, new_r, cell_list, SHAPES_COLOR[shape_type])


def save_to_block_list(block):
    shape_type = block['kind']
    cc, cr = block['cr']
    cell_list = block['cell_list']

    for cell in cell_list:
        cell_c, cell_r = cell
        c = cell_c + cc
        r = cell_r + cr

        block_list[r][c] = shape_type


def horizontal_move_block(event):
    """
    左右移动俄罗斯方块
    :param event: 键盘鼠标事件
    :return:
    """
    direction = [0, 0]
    if event.keysym == 'Left':
        direction = [-1, 0]
    elif event.keysym == 'Right':
        direction = [1, 0]
    else:
        return

    global current_block
    if current_block is not None and check_move(current_block, direction):
        draw_block_move(canvas, current_block, direction)


def game_loop():
    win.update()
    global current_block  # global获取全局变量

    down = [0, 1]

    if current_block is None:
        # 生成一个新的方块
        new_block = generate_new_block()
        draw_block_move(canvas, new_block)
        current_block = new_block

        if not check_move(current_block):
            messagebox.showinfo("GameOver", "Your score is %s" % score)
            win.destroy()
            return

    else:
        # 移动当前的方块
        if check_move(current_block, [0, 1]):
            draw_block_move(canvas, current_block, down)
        else:
            save_to_block_list(current_block)
            current_block = None

    check_and_clear()

    win.after(FPS, game_loop)


def rotate_block(event):
    """
    旋转方块
    :param event:键鼠事件
    :return:
    """
    global current_block
    if current_block is None:
        return

    cell_list = current_block['cell_list']
    rotate_list = []
    for cell in cell_list:
        cell_c, cell_r = cell
        rotate_cell = [cell_r, -cell_c]
        rotate_list.append(rotate_cell)

    block_after_rotate = {
        'kind': current_block['kind'],
        'cell_list': rotate_list,
        'cr': current_block['cr']
    }

    if check_move(block_after_rotate):
        cc, cr = current_block['cr']
        draw_cells(canvas, cc, cr, current_block['cell_list'])
        draw_cells(canvas, cc, cr, block_after_rotate['cell_list'], SHAPES_COLOR[current_block['kind']])
        current_block = block_after_rotate


def land(event):
    global current_block
    if current_block is None:
        return

    cell_list = current_block['cell_list']
    cc, cr = current_block['cr']
    min_height = R
    for cell in cell_list:
        cell_c, cell_r = cell
        c, r = cell_c + cc, cell_r + cr

        if block_list[r][c]:
            return

        h = 0
        for ri in range(r + 1, R):
            if block_list[ri][c]:
                break
            else:
                h += 1

        if h < min_height:
            min_height = h

    down = [0, min_height]
    if check_move(current_block, down):
        draw_block_move(canvas, current_block, down)


def check_row_complete(row):
    """
    检查一行是否已满
    :param row: 行
    :return:
    """
    for cell in row:
        if cell == '':
            return False
    return True


def check_and_clear():
    """
    检查并清除一整行
    :return:
    """
    has_complete_row = False
    for ri in range(len(block_list)):
        if check_row_complete(block_list[ri]):
            has_complete_row = True
            if ri > 0:
                for cur_ri in range(ri, 0, -1):
                    block_list[cur_ri] = block_list[cur_ri - 1][:]
                block_list[0] = ['' for i in range(C)]
            else:
                block_list[ri] = ['' for i in range(C)]

            global score
            score += 10

    if has_complete_row:
        draw_board(canvas, block_list)
        win.title("SCORES: %s" % score)


def main():
    canvas.pack()

    draw_board(canvas, block_list)
    canvas.focus_set()
    canvas.bind("<KeyPress-Left>", horizontal_move_block)
    canvas.bind("<KeyPress-Right>", horizontal_move_block)
    canvas.bind("<KeyPress-Up>", rotate_block)
    canvas.bind("<KeyPress-Down>", land)

    win.update()
    win.after(FPS, game_loop)
    win.title("SCORES: %s" % score)
    win.mainloop()


if __name__ == '__main__':
    main()
