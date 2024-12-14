import tkinter as tk
from tkinter import ttk
import datetime
from datetime import date
from tkcalendar import DateEntry
from datetime import datetime
import os


#检查工作目录
directory=os.getcwd()
print(os.getcwd())
#若工作目录不包含schedule，则更改当前目录
if not 'schedule' in directory:
    os.chdir(directory+'/schedule')
    print(os.getcwd())

#检查是否存在date文件，如果不存在，则创建一个新的文件
try:
    with open('date', 'r', encoding='utf-8') as f:
        pass
except:
    with open('date', 'w', encoding='utf-8') as f:
        f.write('')

# 定义一个函数，用于根据date文件中的开始日期和开始时间进行排序
def sort_by_start_date(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    lines=[i for i in lines if i!= '\n']
    if len(lines)==0:
        print("无日程，无需排序")
        return
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
        lines[i] = lines[i].split("/")
    lines.sort(key=lambda x: datetime.strptime(x[0]+'/'+x[1], '%Y-%m-%d/%H:%M'))
    lines= ["/".join([datetime.strptime(item[0], '%Y-%m-%d/%H:%M').strftime('%Y-%m-%d/%H:%M') if '/' in item[0] else item for item in sub_list]) for sub_list in lines]
    for i in range(len(lines)):
        lines[i] = lines[i]+'\n'
    with open(file_name, 'w', encoding='utf-8') as f:
            f.writelines(lines)

DayInMonth=0
schedule_list=[]
# 获取当前日期
current_date = date.today()
print("当前日期:", current_date)
print(type(current_date))
current_date=str(current_date)
print(type(current_date))

class app:
    def __init__(self,year,month):
        self.year=int(year)
        self.month=int(month)
        self.root = tk.Tk()
        
        self.root.minsize(700,530)
        self.root.maxsize(700,530)
        
        self.root.title("日历")
        self.root.grid_rowconfigure(4, weight=1)

        #显示年份
        self.year_minus_button = tk.Button(self.root, text="<", command=self.year_minus)
        self.year_minus_button.grid(row=0, column=0)
        self.year_label = tk.Label(self.root, text=self.year, font=("Arial", 24))
        self.year_label.grid(row=0, column=1, columnspan=2)
        self.year_plus_button = tk.Button(self.root, text=">", command=self.year_plus)
        self.year_plus_button.grid(row=0, column=3)
        #显示月份
        self.month_minus_button = tk.Button(self.root, text="<", command=self.month_minus)
        self.month_minus_button.grid(row=1, column=0)
        self.month_label = tk.Label(self.root, text=self.month, font=("Arial", 20))
        self.month_label.grid(row=1, column=1, columnspan=2)
        self.month_plus_button = tk.Button(self.root, text=">", command=self.month_plus)
        self.month_plus_button.grid(row=1, column=3)
        
        # 创建日历区域
        self.calendar_frame = tk.Frame(self.root, width=40, height=30)
        self.calendar_frame.grid(row=2, column=0, columnspan=4)
        self.create_calendar()
        #创建按钮，点击后触发函数add_schedule
        self.add_schedule_button = tk.Button(self.root, text="添加日程", command=self.add_schedule,font=("Arial", 18))
        self.add_schedule_button.grid(row=100, column=0, columnspan=4)
        #创建框架承接show_all_schedule_button和selected_date_label
        self.frame = tk.Frame(self.root)
        self.frame.grid(row=0, column=4, columnspan=4)
        #创建一个按钮，点击后显示所有日程
        self.show_all_schedule_button = tk.Button(self.frame, text="查看所有日程",command=self.show_all_schedule)
        self.show_all_schedule_button.grid(row=0, column=1,rowspan=2)
        #创建一个标签，用于显示选中日期
        self.selected_date_label = tk.Label(self.frame, text="所有日程")
        self.selected_date_label.grid(row=0, column=0,rowspan=2)
        
        #在窗口右侧创建一个列表框，用于显示选中日期的日程，大小撑满所占位置
        self.schedule_listbox = tk.Listbox(self.root, width=56, height=22)
        self.schedule_listbox.grid(row=0, column=4, rowspan=10)
        #创建一个标签，用于展示警告
        self.warning_label = tk.Label(self.root, text="", fg="red")
        self.warning_label.grid(row=5, column=4, rowspan=4)
        #创建框架，用于容纳两个按钮
        self.button_frame = tk.Frame(self.root)
        self.button_frame.grid(row=100, column=4, rowspan=10)
        #创建按钮，位置在列表框下，窗口的底部，点击后触发函数edit_schedule
        self.edit_schedule_button = tk.Button(self.button_frame, text="编辑日程",font=("Arial", 18), width=10, height=1, command=self.edit_schedule)
        self.edit_schedule_button.grid(row=0, column=0, rowspan=2)
        self.show_all_schedule()
        #创建按钮，位置在列表框下，窗口的底部，点击后触发函数的delete_schedule
        self.delete_schedule_button = tk.Button(self.button_frame, text="删除日程",font=("Arial", 18), width=10, height=1, command=self.delete_schedule)
        self.delete_schedule_button.grid(row=0, column=1, rowspan=2)

    
    def year_minus(self):
        print("年份-")
        self.year-=1
        self.year_label.config(text=self.year)
        print(self.year)
        # 更新日历
        self.create_calendar()
    def year_plus(self):
        print("年份+")
        self.year+=1
        self.year_label.config(text=self.year)
        print(self.year)
        # 更新日历
        self.create_calendar()
    def month_minus(self):
        print("月份-")
        if self.month==1:
            self.year-=1
            self.month=12
            self.year_label.config(text=self.year)
            print(self.year)
        else:
            self.month-=1
        self.month_label.config(text=self.month)
        print(self.month)
        # 更新日历
        self.create_calendar()
    def month_plus(self):
        print("月份+")
        if self.month==12:
            self.year+=1
            self.month=1
            self.year_label.config(text=self.year)
            print(self.year)
        else:
            self.month+=1
        self.month_label.config(text=self.month)
        
        print(self.month)
        # 更新日历
        self.create_calendar()


    def create_calendar(self):
        print("创建日历")
        # 清空日历区域
        for widget in self.calendar_frame.winfo_children():
            widget.destroy()
        # 创建日历区域
        self.calendar_frame = tk.Frame(self.root, width=40, height=30)
        self.calendar_frame.grid(row=2, column=0, columnspan=4)
        # 创建日历标题
        days = ["日", "一", "二", "三", "四", "五", "六"]
        for i in range(7):
            day_label = tk.Label(self.calendar_frame, text=days[i], width=2)
            day_label.grid(row=0, column=i)
        # 创建日历日期（字体大小为30）
        first_day = self.get_first_day_of_month(self.month, self.year)
        days_in_month = self.get_days_in_month(self.month, self.year)
        for i in range(days_in_month):
            day_button = tk.Button(self.calendar_frame, text=str(i + 1), width=2, font=("Arial", 20))
            day_button.grid(row=(i + first_day) // 7 + 1, column=(i + first_day) % 7)
            day_button.bind("<Button - 1>", self.schedule_display)
    def get_first_day_of_month(self, month, year):
        # 计算给定月份的第一天是星期几
        first_day = date(year, month, 1).weekday()
        return first_day
    def get_days_in_month(self, month, year):
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif month in [4, 6, 9, 11]:
            return 30
        elif month == 2:
            if year % 4 == 0 and year % 100!= 0 or year % 400 == 0:
                return 29
            else:
                return 28
            

    #构造函数，显示所有日程
    def show_all_schedule(self):
        #清空schedule_list
        schedule_list.clear()
        print("显示所有日程")
        self.selected_date_label.config(text="所有日程")
        #更新seelf.selected_date_label标签
        self.selected_date_label.update()
        with open("date", "r",encoding='utf-8') as f:
            # 按行读取date文件
            lines=f.readlines()
            for i in range(len(lines)):
                line=lines[i]
                line=line.strip()
                if line=="":
                    continue
                line_list=line.split("/")
                line_list.append(i)
                schedule_list.append(line_list)
        #清空self.schedule_listbox列表框
        self.schedule_listbox.delete(0, tk.END)
        if len(schedule_list)==0:
            self.schedule_listbox.insert(tk.END, "无日程")
            print('无日程')
        else:
            for line in schedule_list:
                #在self.schedule_listbox列表框中显示所有日程
                start_date_list=[i for i in line[0].split("-")]
                end_date_list=[i for i in line[2].split("-")]
                self.schedule_listbox.insert(tk.END, '从'+start_date_list[0]+'年'+start_date_list[1]+'月'+start_date_list[2]+'日'+line[1]+'到'+end_date_list[0]+'年'+end_date_list[1]+'月'+end_date_list[2]+'日'+line[3]+'    '+line[4]+'   '+line[5])
  

    def schedule_display(self, event):
        global DayInMonth
        # 获取被点击按钮年月日
        button = event.widget
        day=button.cget("text")
        DayInMonth=day
        month=self.month_label.cget("text")
        year=self.year_label.cget("text")
        # 显示被点击按钮年月日
        print(year,month,DayInMonth)
        self.selected_date_label.config(text=f"{year}年{month}月{DayInMonth}日日程")
        #更新seelf.selected_date_label标签
        self.selected_date_label.update()
        global schedule_list
        #清空schedule_list
        schedule_list.clear()
        #按行读取date文件
        with open("date", "r",encoding='utf-8') as f:
            # 按行读取date文件
            lines=f.readlines()
            for i in range(len(lines)):
                line=lines[i]
                line=line.strip()
                if line=="":
                    continue
                line_list=line.split("/")
                # 判断被点击按钮日期是否在日程持续时间内
                start_date_list=[int(i) for i in line_list[0].split("-")]
                end_date_list=[int(i) for i in line_list[2].split("-")]
                if start_date_list[0]>int(year) or (start_date_list[0]==int(year) and start_date_list[1]>int(month)) or (start_date_list[0]==int(year) and start_date_list[1]==int(month) and start_date_list[2]>int(DayInMonth)):
                    continue
                elif end_date_list[0]<int(year) or (end_date_list[0]==int(year) and end_date_list[1]<int(month)) or (end_date_list[0]==int(year) and end_date_list[1]==int(month) and end_date_list[2]<int(DayInMonth)):
                    continue
                else:
                    line_list.append(i)
                    schedule_list.append(line_list)
        #清空self.schedule_listbox列表框
        self.schedule_listbox.delete(0, tk.END)
        #判断是否有日程，如果有，则在self.schedule_listbox列表框中显示所有日程
        if len(schedule_list)==0:
            self.schedule_listbox.insert(tk.END, "无日程")
            print('无日程')
        else:
            for line in schedule_list:
                #在self.schedule_listbox列表框中显示所有日程
                start_date_list=[i for i in line[0].split("-")]
                end_date_list=[i for i in line[2].split("-")]
                self.schedule_listbox.insert(tk.END, '从'+start_date_list[0]+'年'+start_date_list[1]+'月'+start_date_list[2]+'日'+line[1]+'到'+end_date_list[0]+'年'+end_date_list[1]+'月'+end_date_list[2]+'日'+line[3]+'    '+line[4]+'   '+line[5])
    
    
    def delete_schedule(self):
        global schedule_list
        if len(schedule_list)==0:
            print("请先添加日程")
            self.warning_label.config(text="请先添加日程")
            return
        del_date = self.schedule_listbox.curselection()
        if len(del_date)==0:
            print("请选择一个日程")
            self.warning_label.config(text="请选择一个日程")
            return
        # 获取被点击列表框中被点击的行号
        self.warning_label.config(text="")
        # 获取被点击列表框中被点击的行号
        line_number=del_date[0]
        # 获取被点击列表框中被点击的行的内容
        LineInList=schedule_list[line_number]
        #创建一个新的窗口，询问是否删除这个日程
        edit_schedule_window = tk.Toplevel(self.root)
        edit_schedule_window.title("删除日程")
        
        # 创建一个标签，询问是否删除这个日程,并居中
        edit_schedule_label = tk.Label(edit_schedule_window, text="确定删除这个日程吗？",font=('', 14))
        edit_schedule_label.pack(side=tk.TOP, pady=10)
        # 创建一个按钮，点击后删除这个日程
        del_schedule_button = tk.Button(edit_schedule_window, text="确定", command=lambda: delete_schedule_confirm(self,LineInList))
        del_schedule_button.pack(side=tk.LEFT, padx=10)
        # 创建一个按钮，点击后关闭这个窗口
        close_schedule_button = tk.Button(edit_schedule_window, text="取消", command=edit_schedule_window.destroy)
        close_schedule_button.pack(side=tk.RIGHT, padx=10)

        def delete_schedule_confirm(self,LineInList):
            with open('date', 'r', encoding='utf-8') as file:
                lines = file.readlines()
                print(lines)
                lines.append('')
                print(lines)
                line=lines.pop(LineInList[-1])
            # 把lines中的内容写入date文件
            with open('date', 'w', encoding='utf-8') as file:
                file.writelines(lines)
            # 对date文件进行排序
            sort_by_start_date('date')
            edit_schedule_window.destroy()
    def edit_schedule(self):

        global schedule_list
        if len(schedule_list)==0:
            print("请先添加日程")
            self.warning_label.config(text="请先添加日程")
            return
        # 获取被点击列表框中被点击的行号
        button = self.schedule_listbox.curselection()
        
        print(button)
        # 如果没有被点击，则返回
        if len(button)==0:
            print("请选择一个日程")
            self.warning_label.config(text="请选择一个日程")
            return
        self.warning_label.config(text="")
        # 获取被点击列表框中被点击的行号
        line_number=button[0]
        # 获取被点击列表框中被点击的行的内容
        LineInList=schedule_list[line_number]
        # 把date文件中的第line_number行删除
        with open('date', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            print(lines)
            lines.append('')
            print(lines)
            line=lines.pop(LineInList[-1])
        #获取开始日期
        print(line)
        start_date=[int(i) for i in (line.split("/"))[0].split("-")]
        set_start_date=date(start_date[0],start_date[1],start_date[2])
        #获取结束日期
        print(line[2])
        end_date=[int(i) for i in (line.split("/"))[2].split("-")]
        set_end_date=date(end_date[0],end_date[1],end_date[2])
        #获取开始时间
        start_time=line.split("/")[1]
        #获取结束时间
        end_time=line.split("/")[3]
        #获取日程类型
        schedule_type=line.split("/")[4]
        #获取日程内容
        schedule=line.split("/")[5]
        # 创建一个新的窗口，用于编辑日程
        edit_schedule_window = tk.Toplevel(self.root)
        edit_schedule_window.title("编辑日程")
        edit_schedule_window.geometry("300x200+100+100")
        edit_schedule_window.minsize(530,150)
        edit_schedule_window.maxsize(530,150)
        # 创建一个标签，提示输入日期
        date_label = tk.Label(edit_schedule_window, text="请输入开始日期:")
        date_label.grid(row=0, column=0)
        #使用DateEntry库创建一个人性化的日期选择器
        date_start_entry = DateEntry(edit_schedule_window, width=12, background='darkblue',foreground='white', borderwidth=2)
        date_start_entry.grid(row=0, column=1)
        date_start_entry.set_date(set_start_date)
        # 创建一个标签，提示输入开始时间
        time_label = tk.Label(edit_schedule_window, text="请输入开始时间(hh:mm):")
        time_label.grid(row=0, column=2)
        # 创建一个文本框，用于输入开始时间
        time_start_entry = tk.Entry(edit_schedule_window)
        time_start_entry.grid(row=0, column=3)
        time_start_entry.insert(0, start_time)
        # 创建一个标签，提示输入结束日期
        date_label = tk.Label(edit_schedule_window, text="请输入结束日期:")
        date_label.grid(row=1, column=0)
        # 使用DateEntry库创建一个人性化的日期选择器
        date_end_entry = DateEntry(edit_schedule_window, width=12, background='darkblue',foreground='white', borderwidth=2)
        date_end_entry.grid(row=1, column=1)
        date_end_entry.set_date(set_end_date)
        # 创建一个标签，提示输入结束时间
        time_label = tk.Label(edit_schedule_window, text="请输入结束时间(hh:mm):")
        time_label.grid(row=1, column=2)
        # 创建一个文本框，用于输入结束时间
        time_end_entry = tk.Entry(edit_schedule_window)
        time_end_entry.grid(row=1, column=3)
        time_end_entry.insert(0, end_time)
        # 创建一个标签，提示输入日程类型
        type_label = tk.Label(edit_schedule_window, text="请输入日程类型:")
        type_label.grid(row=2, column=0)
        # 创建一个文本框，用于输入日程类型
        type_entry = tk.Entry(edit_schedule_window)
        type_entry.grid(row=2, column=1)
        type_entry.insert(0, schedule_type)
        # 创建一个标签，提示输入日程内容
        content_label = tk.Label(edit_schedule_window, text="请输入日程内容:")
        content_label.grid(row=2, column=2)
        # 创建一个文本框，用于输入日程内容
        content_entry = tk.Entry(edit_schedule_window)
        content_entry.grid(row=2, column=3)
        content_entry.insert(0, schedule)
        #创建一个标签，用于展示警告
        warning_label = tk.Label(edit_schedule_window, text="", fg="red")
        warning_label.grid(row=3, column=0, columnspan=4)
        # 创建一个按钮，点击后触发函数add_schedule_to_file
        add_button = tk.Button(edit_schedule_window, text="确认修改", command=lambda: self.edit_schedule_to_file(date_start_entry.get_date(), time_start_entry.get(), date_end_entry.get_date(), time_end_entry.get(), type_entry.get(), content_entry.get(),warning_label,LineInList[-1],edit_schedule_window))
        add_button.grid(row=4, column=0, columnspan=4)
    def edit_schedule_to_file(self, date_start, time_start, date_end, time_end, type, content,warning_label,line_num,window):
        #判断所有输入内容是否合法,如果有一个为空，则把warning_label标签的内容改为"请输入所有内容"
        if date_start == "" or time_start == "" or date_end == "" or time_end == "" or type == "" or content == "":
            print("请输入所有内容")
            warning_label.config(text="请输入所有内容")
            return
        try:
            time_start_list=[int(i) for i in time_start.split(":")]
            time_end_list=[int(i) for i in time_end.split(":")]
        except:
            print("时间格式错误")
            warning_label.config(text="时间格式错误")
            return
        else:
            if len(time_start_list)!=2 or len(time_end_list)!=2:
                print("时间格式错误")
                warning_label.config(text="时间格式错误")
                return
            if time_start_list[0]>23 or time_start_list[1]>59 or time_end_list[0]>23 or time_end_list[1]>59:
                print("时间格式错误")
                warning_label.config(text="时间格式错误")
                return
        if date_start>date_end:
            print("开始日期不能大于结束日期")
            warning_label.config(text="开始日期不能大于结束日期")
            return
        if date_start==date_end:
            if time_start_list[0]>time_end_list[0] or (time_start_list[0]==time_end_list[0] and time_start_list[1]>time_end_list[1]):
                print("开始时间不能大于结束时间")
                warning_label.config(text="开始时间不能大于结束时间")
                return


        # 把date文件中的第line_number行删除
        with open('date', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            print(lines)
            lines.append('')
            print(lines)
            del lines[line_num]
        lines.insert(line_num,str(date_start) + "/" + time_start + "/" + str(date_end) + "/" + time_end + "/" + type + "/" + content + "\n")
        # 把lines中的内容写入date文件
        with open('date', 'w', encoding='utf-8') as file:
            file.writelines(lines)
        # 对date文件进行排序
        sort_by_start_date('date')
        # 关闭窗口
        window.destroy()
        global DayInMonth
        day=DayInMonth
        month=self.month_label.cget("text")
        year=self.year_label.cget("text")
        # 显示被点击按钮年月日
        print(year,month,day)
        self.selected_date_label.config(text=f"{year}年{month}月{day}日日程")
        global schedule_list
        #清空schedule_list
        schedule_list.clear()
        #按行读取date文件
        with open("date", "r",encoding='utf-8') as f:
            # 按行读取date文件
            lines=f.readlines()
            for i in range(len(lines)):
                line=lines[i]
                line=line.strip()
                if line=="":
                    continue
                line_list=line.split("/")
                # 判断被点击按钮日期是否在日程持续时间内
                start_date_list=[int(i) for i in line_list[0].split("-")]
                end_date_list=[int(i) for i in line_list[2].split("-")]
                if start_date_list[0]>int(year) or (start_date_list[0]==int(year) and start_date_list[1]>int(month)) or (start_date_list[0]==int(year) and start_date_list[1]==int(month) and start_date_list[2]>int(day)):
                    continue
                elif end_date_list[0]<int(year) or (end_date_list[0]==int(year) and end_date_list[1]<int(month)) or (end_date_list[0]==int(year) and end_date_list[1]==int(month) and end_date_list[2]<int(day)):
                    continue
                else:
                    line_list.append(i)
                    schedule_list.append(line_list)
        #清空self.schedule_listbox列表框
        self.schedule_listbox.delete(0, tk.END)
        #判断是否有日程，如果有，则在self.schedule_listbox列表框中显示所有日程
        if len(schedule_list)==0:
            self.schedule_listbox.insert(tk.END, "无日程")
        else:
            for line in schedule_list:
                #在self.schedule_listbox列表框中显示所有日程
                start_date_list=[i for i in line[0].split("-")]
                end_date_list=[i for i in line[2].split("-")]
                self.schedule_listbox.insert(tk.END, '从'+start_date_list[0]+'年'+start_date_list[1]+'月'+start_date_list[2]+'日'+line[1]+'到'+end_date_list[0]+'年'+end_date_list[1]+'月'+end_date_list[2]+'日'+line[3]+'    '+line[4]+'   '+line[5])


    def add_schedule(self):
        # 创建一个新的窗口，用于添加日程
        add_schedule_window = tk.Toplevel(self.root)
        add_schedule_window.title("添加日程")
        add_schedule_window.geometry("300x200+100+100")
        add_schedule_window.minsize(530,150)
        add_schedule_window.maxsize(530,150)
        # 创建一个标签，提示输入日期
        date_label = tk.Label(add_schedule_window, text="请输入开始日期:")
        date_label.grid(row=0, column=0)
        #使用DateEntry库创建日期选择器
                # 使用DateEntry库创建一个人性化的日期选择器，并设置日期格式为yyyy/mm/dd
        date_start_entry = DateEntry(add_schedule_window, width=12, background='darkblue',
                        foreground='white', borderwidth=2, date_pattern='yyyy/mm/dd')
        date_start_entry.grid(row=0, column=1)

        # 创建一个标签，提示输入开始时间
        time_label = tk.Label(add_schedule_window, text="请输入开始时间(hh:mm):")
        time_label.grid(row=0, column=2)
        # 创建一个文本框，用于输入开始时间
        time_start_entry = tk.Entry(add_schedule_window)
        time_start_entry.grid(row=0, column=3)
        # 创建一个标签，提示输入结束日期
        date_label = tk.Label(add_schedule_window, text="请输入结束日期:")
        date_label.grid(row=1, column=0)
        # 使用DateEntry库创建一个人性化的日期选择器
        date_end_entry = DateEntry(add_schedule_window, width=12, background='darkblue',
                        foreground='white', borderwidth=2, date_pattern='yyyy/mm/dd')
        date_end_entry.grid(row=1, column=1)
        # 创建一个标签，提示输入结束时间
        time_label = tk.Label(add_schedule_window, text="请输入结束时间(hh:mm):")
        time_label.grid(row=1, column=2)
        # 创建一个文本框，用于输入结束时间
        time_end_entry = tk.Entry(add_schedule_window)
        time_end_entry.grid(row=1, column=3)
        # 创建一个标签，提示输入日程类型
        type_label = tk.Label(add_schedule_window, text="请输入日程类型:")
        type_label.grid(row=2, column=0)
        # 创建一个文本框，用于输入日程类型
        type_entry = tk.Entry(add_schedule_window,width=15)
        type_entry.grid(row=2, column=1)
        # 创建一个标签，提示输入日程内容
        content_label = tk.Label(add_schedule_window, text="请输入日程内容:")
        content_label.grid(row=2, column=2)
        # 创建一个文本框，用于输入日程内容
        content_entry = tk.Entry(add_schedule_window)
        content_entry.grid(row=2, column=3)
        #创建一个标签，用于展示警告
        warning_label = tk.Label(add_schedule_window, text="", fg="red")
        warning_label.grid(row=3, column=0, columnspan=4)
        # 创建一个按钮，点击后触发函数add_schedule_to_file
        add_button = tk.Button(add_schedule_window, text="添加", command=lambda: self.add_schedule_to_file(date_start_entry.get_date(), time_start_entry.get(), date_end_entry.get_date(), time_end_entry.get(), type_entry.get(), content_entry.get(),warning_label,add_schedule_window))
        add_button.grid(row=4, column=0, columnspan=4)


    # 定义一个函数，用于将输入的日程信息写入date文件
    def add_schedule_to_file(self, date_start, time_start, date_end, time_end, type, content, warning_label, window):
        #判断所有输入内容是否合法,如果有一个为空，则把warning_label标签的内容改为"请输入所有内容"
        if date_start == "" or time_start == "" or date_end == "" or time_end == "" or type == "" or content == "":
            print("请输入所有内容")
            warning_label.config(text="目标有点空洞")
            return
        #把ScheduleTime转换为dateti0me格式
        ScheduleTime=str(date_start)+" "+time_start+':00'
        EndDT=str(date_end)+" "+time_end+':00'
        date_startDT=datetime.strptime(ScheduleTime, '%Y-%m-%d %H:%M:00')
        date_endDT=datetime.strptime(EndDT, '%Y-%m-%d %H:%M:00')
        if date_startDT > date_endDT:
            print("开始时间不能晚于结束时间")
            warning_label.config(text="还没开始就结束了？")
            return
        ScheduleLine=str(date_start) + "/" + time_start + "/" + str(date_end) + "/" + time_end + "/" + type + "/" + content + "\n"
        # 将输入的日期、时间、类型、内容写入date文件中
        with open("date", "a",encoding='utf-8') as f:
            f.write(ScheduleLine)
        # 对date文件进行排序
        sort_by_start_date('date')
        #添加成功
        print("添加成功")
        # 关闭窗口
        window.destroy()
        #更新self.schedule_listbox列表框
        month=self.month_label.cget("text")
        year=self.year_label.cget("text")
        global schedule_list , DayInMonth
        #清空schedule_list
        schedule_list.clear()
        #按行读取date文件
        with open("date", "r",encoding='utf-8') as f:
            # 按行读取date文件
            lines=f.readlines()
            for i in range(len(lines)):
                line=lines[i]
                line=line.strip()
                if line=="":
                    continue
                line_list=line.split("/")
                # 判断被点击按钮日期是否在日程持续时间内
                start_date_list=[int(i) for i in line_list[0].split("-")]
                end_date_list=[int(i) for i in line_list[2].split("-")]
                if start_date_list[0]>int(year) or (start_date_list[0]==int(year) and start_date_list[1]>int(month)) or (start_date_list[0]==int(year) and start_date_list[1]==int(month) and start_date_list[2]>int(DayInMonth)):
                    continue
                elif end_date_list[0]<int(year) or (end_date_list[0]==int(year) and end_date_list[1]<int(month)) or (end_date_list[0]==int(year) and end_date_list[1]==int(month) and end_date_list[2]<int(DayInMonth)):
                    continue
                else:
                    line_list.append(i)
                    schedule_list.append(line_list)
        #清空self.schedule_listbox列表框
        self.schedule_listbox.delete(0, tk.END)
        #判断是否有日程，如果有，则在self.schedule_listbox列表框中显示所有日程
        if len(schedule_list)==0:
            self.schedule_listbox.insert(tk.END, "无日程")
        else:
            for line in schedule_list:
                #在self.schedule_listbox列表框中显示所有日程
                start_date_list=[i for i in line[0].split("-")]
                end_date_list=[i for i in line[2].split("-")]
                self.schedule_listbox.insert(tk.END, '从'+start_date_list[0]+'年'+start_date_list[1]+'月'+start_date_list[2]+'日'+line[1]+'到'+end_date_list[0]+'年'+end_date_list[1]+'月'+end_date_list[2]+'日'+line[3]+'    '+line[4]+'   '+line[5])
    
        

    def run(self):
        self.root.mainloop()


# 主程序入口
if __name__ == "__main__":
    sort_by_start_date('date')
    window = app(current_date[:4], current_date[5:7])
    window.run()