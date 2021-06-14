import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

Width, Height = (400, 400)
canvas_size = (int(Width * .75), int(Height * .5))
button_color = "gray"
button_count = 3
button_list = []
button_text = ["-", "+", "OK"]
button_size = (5, 1)


place_list = [  # 画布，标签，输入框，按钮-，按钮+，按钮ok
    ((Width - canvas_size[0]) / 2, 10),
    ((Width - canvas_size[0]) / 2 + 20, canvas_size[1] + button_size[1] + 100),
    ((Width - canvas_size[0]) / 2 + 50, canvas_size[1] + button_size[1] + 100),
    ((Width - canvas_size[0]) / 2, canvas_size[1] + 30),
    ((Width-canvas_size[0])/2+canvas_size[0]-40, canvas_size[1] + 30),
    ((Width - canvas_size[0]) / 2 + 220, canvas_size[1] + button_size[1] + 95)
]


def button_0_down():
    print(0)


def button_1_down():
    print(1)


def button_2_down():
    f_plot.clear()
    x = np.linspace(1, 10, 1000)  # x的取值范围，以及线的精度
    y = x
    f_plot.plot(x, y)
    can.draw()
    print(2)


command_list = [button_0_down, button_1_down, button_2_down]


def add_components(wnd):
    """
    在窗口上添加组件
    :return:
    """
    # 标签
    label = tk.Label(wnd, text="y =")
    label.place(x=place_list[1][0], y=place_list[1][1])
    entry = tk.Entry(wnd)
    entry.place(x=place_list[2][0], y=place_list[2][1])
    # 按钮
    for i in range(button_count):
        button_i = tk.Button(wnd,
                             text=button_text[i],
                             bg=button_color,
                             width=button_size[0],
                             height=button_size[1],
                             command=command_list[i])
        button_list.append(button_i)
        button_list[i].place(x=place_list[i + 3][0], y=place_list[i + 3][1])


if __name__ == "__main__":
    win = tk.Tk()
    # 画布,将matplotlib图表镶嵌入tkinter界面
    figure = plt.Figure(figsize=(3, 2))
    f_plot = figure.add_subplot(111)  # 111代表位置
    can = FigureCanvasTkAgg(figure, win)
    can.get_tk_widget().place(x=place_list[0][0], y=place_list[0][1])

    win.geometry(str(Width) + "x" + str(Height))  # 设置窗口大小，geometry参数为字符串
    add_components(win)
    win.mainloop()


"""
如何将matplotlib绘制的图表镶嵌入tkinter做的界面中:
https://www.cnblogs.com/brightyuxl/archive/2018/10/22/9832248.html
"""