import tkinter as tk
from PIL import Image, ImageTk
import random

win = tk.Tk()
Pic_path = "img5.jpg"
im = Image.open(Pic_path)  # 读取图片
tkImage_list = []
index_list = []  # 用来记录下标，通过打乱下标来打乱拼图

depth = 3  # 分割层数
width, height = im.size  # 输入图片的size
w = int(width / depth)
h = int(height / depth)  # 分割后每张图片的size
box_color = (255, 255, 255)  # 空白区域的颜色


def cut_image(Pic):  # 分割图片并存进tkImage_list中
    global tkImage_list
    global index_list
    for i in range(depth):
        for j in range(depth):
            box = (w*j, h*i, w*(j+1), h*(i+1))  # 需要切割的矩形区域
            image = Pic.crop(box)
            tkImage_list.append(ImageTk.PhotoImage(image))
            index_list.append(i*depth+j)
    random.shuffle(index_list)  # 打乱下标的顺序
    print(index_list)


def form_white_box():  # 生成一个白色的区域并添加至tkImage_list中
    global tkImage_list
    (x, y) = int(depth / 2), int(depth / 2)  # 坐标
    list_index = x * depth + y  # 列表下标
    white_box = Image.new('RGB', (w, h), box_color)  # 生成一张空白的图片
    tk_white_box = ImageTk.PhotoImage(white_box)
    tkImage_list.pop(list_index)
    tkImage_list.insert(list_index, tk_white_box)  # 通过索引删除和添加元素


def show_image_list():  # 通过index_list展示image_list中的图片
    i = 0
    for index in index_list:
        label = tk.Label(win, image=tkImage_list[index])
        label.grid(row=int(i/depth), column=int(i % depth))  # 第i张图片的位置
        i += 1


if __name__ == '__main__':
    cut_image(im)
    form_white_box()
    show_image_list()
    win.mainloop()
