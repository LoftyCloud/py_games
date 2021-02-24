import tkinter as tk
from PIL import Image, ImageTk
import random

FPS = 300
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

image_index = 0
index_index = 0  # 白色图片在image_list中的索引和其在index_list中的索引

replaced_img = None  # 记录被替代的图片，游戏结束时还原


def cut_image(Pic):
    """
    # 分割图片并存进tkImage_list中
    :param Pic: 需要被分割的图片
    :return:
    """
    global tkImage_list
    for i in range(depth):
        for j in range(depth):
            box = (w * j, h * i, w * (j + 1), h * (i + 1))  # 需要切割的矩形区域
            image = Pic.crop(box)
            tkImage_list.append(ImageTk.PhotoImage(image))
            index_list.append(i * depth + j)


def shuffle_list():
    """
    打乱index_list并使逆序数一定为偶数
    :return:
    """
    global index_list
    reverseCount = 0
    random.shuffle(index_list)
    for i in range(len(index_list)):  # 从0到num - 2
        for j in range(i):
            if index_list[i] < index_list[j]:
                reverseCount += 1  # 计算逆序数
    if reverseCount % 2 != 0:
        shuffle_list()


def form_white_box():
    """
    # 生成一个白色的区域并添加至tkImage_list中
    :return:
    """
    global tkImage_list
    global image_index
    global replaced_img
    (x, y) = depth-1, depth-1  # 坐标,改为选取最后一个作为空白区域
    image_index = x * depth + y  # 列表下标
    white_box = Image.new('RGB', (w, h), box_color)  # 生成一张空白的图片
    tk_white_box = ImageTk.PhotoImage(white_box)

    replaced_img = tkImage_list[image_index]
    tkImage_list.pop(image_index)
    tkImage_list.insert(image_index, tk_white_box)  # 通过索引删除和添加元素


def show_image_list():
    """
    # 通过index_list展示image_list中的图片
    :return:
    """
    num = 0
    for index in index_list:
        show_single_img(index, num)
        num += 1


def show_single_img(index, i):
    """
    根据索引在位置i处画出单张图片
    :param index:
    :param i:
    :return:
    """
    label = tk.Label(win, image=tkImage_list[index])
    label.grid(row=int(i / depth), column=int(i % depth))  # 第i张图片的位置


def exchange_img(event):
    """
    通过键盘交换白色图片与相邻图片的位置
    :return:
    """
    global index_index
    global index_list
    x = index_index
    if event.keysym == "Left" or event.keysym == "a":
        # 需要实现index_list的交换
        if x % depth != 0:  # 不是在最左边
            index_list[x - 1], index_list[x] = index_list[x], index_list[x - 1]
            index_index -= 1
    elif event.keysym == "Right" or event.keysym == "d":
        if (x+1) % depth != 0:  # 不是在最右边
            index_list[x + 1], index_list[x] = index_list[x], index_list[x + 1]
            index_index += 1
    elif event.keysym == "Up" or event.keysym == "w":
        if x >= depth:  # 不是在最上面
            index_list[x - depth], index_list[x] = index_list[x], index_list[x - depth]
            index_index -= depth
    elif event.keysym == "Down" or event.keysym == "s":
        if x + depth < depth*depth:  # 不是在最下面
            index_list[x + depth], index_list[x] = index_list[x], index_list[x + depth]
            index_index += depth
    else:
        return


def check_list():
    for i in range(depth * depth):
        if index_list[i] != i:
            return False
    return True


def game_over():
    """
    游戏结束时在窗口添加“you win”文字
    将被替代的图片还原
    :return:
    """
    label = tk.Label(win, text="YOU WIN!!!")
    label.grid(row=depth, column=1)
    tkImage_list.pop(depth * depth - 1)
    tkImage_list.append(replaced_img)
    show_image_list()
    win.update()
    return


def game_loop():
    win.update()
    show_image_list()

    if not check_list():
        win.after(FPS, game_loop)
    else:
        game_over()


def main():
    global index_index

    cut_image(im)  # 切割图片
    form_white_box()  # 生成白色区域
    shuffle_list()  # 打乱index_list

    index_index = index_list.index(image_index)  # 获取白色图片在index_list中的位置

    win.focus_set()
    win.bind("<KeyPress-Left>", exchange_img)
    win.bind("<KeyPress-Right>", exchange_img)
    win.bind("<KeyPress-Up>", exchange_img)
    win.bind("<KeyPress-Down>", exchange_img)
    win.bind("<KeyPress-a>", exchange_img)
    win.bind("<KeyPress-d>", exchange_img)
    win.bind("<KeyPress-w>", exchange_img)
    win.bind("<KeyPress-s>", exchange_img)

    win.title("GoodWind")
    game_loop()

    win.mainloop()


if __name__ == '__main__':
    main()
"""
嘤嘤嘤，我拼不出来
攻略：https://jingyan.baidu.com/article/ea24bc392e8d68da63b3317f.html

九宫格拼图的可解性：原数组和随机出来的数组的逆序数的奇偶性一致，那么就是可解的。
如果原数组是[0,1,2,3,4,5,6,7,8], 算出来的逆序数 为 0， 那么只要保证随机出来的数组的 逆序数 为偶数 ，那么拼图就是可解的。

优化：
1、游戏一定会有解
2、刷新机制优化，只重绘空白图和与空白图产生交换的图片
3、游戏结束时的”you win“字体放大，居中
"""