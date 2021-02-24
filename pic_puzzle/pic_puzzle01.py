import tkinter as tk
from PIL import Image, ImageTk

win = tk.Tk()
Pic_path = "img5.jpg"
im = Image.open(Pic_path)  # 读取图片
tkImage_list = []

depth = 3
width, height = im.size


def cut_image(Pic):  # 分割图片
    global tkImage_list
    w = int(width/depth)
    h = int(height/depth)
    for i in range(depth):
        for j in range(depth):
            box = (w*j, h*i, w*(j+1), h*(i+1))  # 需要切割的矩形区域
            image = Pic.crop(box)
            tkImage_list.append(ImageTk.PhotoImage(image))
            label = tk.Label(win, image=tkImage_list[i*depth + j])
            """
            Tk.photoImage()显示图片时，
            当把包含该函数放在自定义函数里时，不能正常显示，移出函数又可正常显示，
            所以想到可能是变量不是全局性的缘故，改为全局变量后果然可正常显示
            """
            label.grid(row=i, column=j)
            """ 布局 https://blog.csdn.net/qq_37503890/article/details/90264864"""


if __name__ == '__main__':
    cut_image(im)
    win.mainloop()
