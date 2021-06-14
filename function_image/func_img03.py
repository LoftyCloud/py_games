import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

Width, Height = (400, 450)
canvas_size = (300, 300)
button_color = "gray"
button_count = 3
button_list = []
button_text = ["-", "+", "OK"]
button_size = (5, 1)

min_x, max_x = (-10, 10)
func = None
func_str = "x"
STEP = 10

place_list = [  # 画布，标签，输入框，按钮-，按钮+，按钮ok
    ((Width - canvas_size[0]) / 2, 10),
    ((Width - canvas_size[0]) / 2 + 20, canvas_size[1] + button_size[1] + 85),
    ((Width - canvas_size[0]) / 2 + 50, canvas_size[1] + button_size[1] + 85),
    ((Width - canvas_size[0]) / 2, canvas_size[1] + 30),
    ((Width - canvas_size[0]) / 2 + canvas_size[0] - 40, canvas_size[1] + 30),
    ((Width - canvas_size[0]) / 2 + 220, canvas_size[1] + button_size[1] + 80)
]


def button_0_down():
    global min_x, max_x
    min_x += STEP
    max_x -= STEP
    draw_function_img()


def button_1_down():
    global min_x, max_x
    min_x -= STEP
    max_x += STEP
    draw_function_img()


def button_2_down():
    global min_x, max_x
    global func_str
    func_str = entry.get()
    min_x, max_x = (-50, 50)  # 复原
    draw_function_img()


def draw_function_img():
    global func

    x = np.linspace(min_x, max_x, 1000)
    func = eval(func_str)

    f_plot.clear()
    f_plot.plot(x, func)
    can.draw()


def add_components():
    """
    将组件放置在窗体上
    :return:
    """
    can.get_tk_widget().place(x=place_list[0][0], y=place_list[0][1])

    label.place(x=place_list[1][0], y=place_list[1][1])
    entry.place(x=place_list[2][0], y=place_list[2][1])
    # 按钮
    global index
    for index in range(button_count):
        button_list[index].place(x=place_list[index + 3][0], y=place_list[index + 3][1])

    win.geometry(str(Width) + "x" + str(Height))  # 设置窗口大小，geometry参数为字符串


if __name__ == "__main__":
    '''将定义全部提出来'''
    win = tk.Tk()
    # 画布,将matplotlib图表镶嵌入tkinter界面
    figure = plt.Figure(figsize=(3, 3))
    f_plot = figure.add_subplot(111)
    can = FigureCanvasTkAgg(figure, win)
    # 标签和输入框
    label = tk.Label(win, text="y =")
    entry = tk.Entry(win)
    entry.insert(0, func_str)
    # 按钮
    command_list = [button_0_down, button_1_down, button_2_down]
    for index in range(button_count):
        button_index = tk.Button(win,
                                 text=button_text[index],
                                 bg=button_color,
                                 width=button_size[0],
                                 height=button_size[1],
                                 command=command_list[index])
        button_list.append(button_index)

    add_components()

    win.mainloop()
