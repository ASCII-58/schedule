import tkinter as tk
from PIL import Image, ImageTk

import os
from PIL import Image, ImageTk

#检查工作目录
directory=os.getcwd()
print(os.getcwd())
#若工作目录不包含schedule，则更改当前目录
if not 'schedule' in directory:
    os.chdir(directory+'/schedule')
    print(os.getcwd())

# 定义的img类
class img:
    def __init__(self, path):
        root = tk.Tk()
        self.root.title("Using img Class in Another Class")
        
        image = Image.open(path)
        self.photo = ImageTk.PhotoImage(image)

    def show_img(self):
        return self.photo


# 定义另一个类，用于创建窗口并展示图片
class WindowWithImage:
    def __init__(self, master, image_path):
        self.master = master
        self.image_loader = img(image_path)  # 创建img类的实例来加载图片
        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(self.master, image=self.image_loader.show_img())
        label.image = self.image_loader.show_img()  # 防止图片被垃圾回收
        label.pack()
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    
    image_path = "ic_public_list_deleted.png"
    app = WindowWithImage(root, image_path)
    root.mainloop()