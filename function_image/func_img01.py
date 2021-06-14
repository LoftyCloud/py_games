import tkinter as tk

Width, Height = (400, 400)
canvas_size = (int(Width * .75), int(Height * .5))
canvas_color = "gray"
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
    print(2)


command_list = [button_0_down, button_1_down, button_2_down]


def add_components(Tk):
    """
    在Tk对象上添加组件
    :param Tk:
    :return:
    """
    # 画布
    can = tk.Canvas(Tk, width=canvas_size[0], height=canvas_size[1], background=canvas_color)
    can.place(x=place_list[0][0], y=place_list[0][1])
    # 标签
    label = tk.Label(Tk, text="y=")
    label.place(x=place_list[1][0], y=place_list[1][1])
    entry = tk.Entry(Tk)
    entry.place(x=place_list[2][0], y=place_list[2][1])
    # 按钮
    for i in range(button_count):
        button_i = tk.Button(Tk,
                             text=button_text[i],
                             bg=button_color,
                             width=button_size[0],
                             height=button_size[1],
                             command=command_list[i])
        button_list.append(button_i)
        button_list[i].place(x=place_list[i + 3][0], y=place_list[i + 3][1])


def main():
    win = tk.Tk()
    win.geometry(str(Width) + "x" + str(Height))  # 设置窗口大小，geometry:形状，参数为字符串
    add_components(win)
    win.mainloop()


if __name__ == "__main__":
    main()
