import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

Width, Height = (400, 450)
canvas_size = (300, 300)
COLOR = "gray"
LINE_COLOR = "green"
button_count = 5
button_list = []
button_text = ["-", "+", "OK", "left", "right"]
button_size = (5, 1)

min_y, max_y = (-10, 10)
min_x, max_x = (-10, 10)
func = None
func_str = "x*x*x"
STEP = 5

# 画布，标签，输入框，按钮-，按钮+，按钮ok，按钮left，按钮right在窗体上的位置
PLACE_LIST = [(50, 10),
              (110, 346),
              (140, 346),
              (50, 330),
              (310, 330),
              (185, 380),
              (50, 380),
              (310, 380)]


def button_reduce_down():  # 缩减x的范围
    global min_x, max_x
    if max_x > min_x + 2 * STEP:  # 修改控制幅度的条件，修复因左右移动图形的功能而导致的bug
        min_x += STEP
        max_x -= STEP
    else:  # 控制缩减的幅度
        min_x = min_x / 2
        max_x = max_x / 2
    draw_function_img()


def button_add_down():  # 增加x的范围
    global min_x, max_x
    if abs(max_x) < STEP and abs(min_x) < STEP:  # 修改控制幅度的条件，修复因左右移动图形的功能而导致的bug
        min_x = min_x * 2
        max_x = max_x * 2
    else:
        min_x -= STEP
        max_x += STEP
    draw_function_img()


def button_ok_down():  # 重绘输入框函数的图像
    global min_x, max_x
    global func_str
    func_str = entry.get()
    min_x, max_x = (-10, 10)  # 按下ok键时复原x的范围

    draw_function_img()


def button_left_down():  # 将函数图像向左移
    global min_x, max_x
    min_x += STEP
    max_x += STEP
    draw_function_img()


def button_right_down():  # 将函数图像向右移
    global min_x, max_x
    min_x -= STEP
    max_x -= STEP
    draw_function_img()


def draw_function_img():  # 重绘函数图像
    global func

    x = np.linspace(min_x, max_x, 1000)
    try:
        func = eval(func_str)
    except Exception as e:
        tk.messagebox.showinfo('ERROR', 'ERROR:' + str(e))
    else:
        f_plot.clear()
        f_plot.set_xlim(min_x, max_x)
        f_plot.set_ylim(min_y, max_y)  # y范围不固定图形变化起来会只移动坐标轴的位置和比例，图案看起来没变化Orz
        f_plot.plot(x, func, c=LINE_COLOR)
        can.draw()


def add_components():
    """
    将组件放置在窗体上
    :return:
    """
    can.get_tk_widget().place(x=PLACE_LIST[0][0], y=PLACE_LIST[0][1])

    label.place(x=PLACE_LIST[1][0], y=PLACE_LIST[1][1])
    entry.place(x=PLACE_LIST[2][0], y=PLACE_LIST[2][1])
    # 按钮
    global index
    for index in range(button_count):
        button_list[index].place(x=PLACE_LIST[index + 3][0], y=PLACE_LIST[index + 3][1])

    win.geometry(str(Width) + "x" + str(Height))  # 设置窗口大小，geometry参数为字符串


if __name__ == "__main__":
    '''将定义全部提出来'''
    win = tk.Tk()
    win.title("GoodWind")
    # 画布,将matplotlib图表镶嵌入tkinter界面
    figure = plt.Figure(figsize=(3, 3), facecolor=COLOR)
    f_plot = figure.add_subplot(111)
    can = FigureCanvasTkAgg(figure, win)

    # 标签和输入框
    label = tk.Label(win, text="y =")
    entry = tk.Entry(win)
    entry.insert(0, func_str)
    # 按钮
    command_list = [button_reduce_down, button_add_down, button_ok_down, button_left_down, button_right_down]
    for index in range(button_count):
        button_index = tk.Button(win,
                                 text=button_text[index],
                                 bg=COLOR,
                                 width=button_size[0],
                                 height=button_size[1],
                                 command=command_list[index])
        button_list.append(button_index)

    add_components()
    draw_function_img()

    win.mainloop()
