# Schedule - 日程管理工具

## 简介

这是一个简单的日程管理软件，使用Python的tkinter库开发。它允许用户添加、查看、编辑和删除日程安排，帮助用户更好地管理时间和任务。

## 功能

- [x] 支持添加日程
- [x] 支持查看日程
- [x] 支持编辑日程
- [x] 支持删除日程
- [x] 支持日程排序
- [x] 支持日程分类
- [x] 日历视图

## 安装要求

要运行此程序，您需要安装以下软件和库：

- Python 3.6或更高版本
- tkinter (通常与Python一起安装)
- tkcalendar

可以使用以下命令安装所需的库：

```bash
pip install tkcalendar
```

## 使用方法

1. 克隆或下载此仓库
2. 进入项目目录
3. 运行main.py文件：

```bash
python main.py
```

### 添加日程

1. 点击主界面上的"添加日程"按钮
2. 在弹出的窗口中填写日程信息（开始日期、开始时间、结束日期、结束时间、日程类型和内容）
3. 点击"添加"按钮确认

### 查看日程

- 点击日历上的某一天可以查看该日的所有日程
- 点击"查看所有日程"按钮可以查看所有日程

### 编辑日程

1. 选择要编辑的日程
2. 点击"编辑日程"按钮
3. 在弹出的窗口中修改日程信息
4. 点击"确认修改"按钮保存更改

### 删除日程

1. 选择要删除的日程
2. 点击"删除日程"按钮
3. 在弹出的确认窗口中点击"确定"按钮

## 文件结构

- `main.py` - 主程序文件
- `date` - 存储日程数据的文件
- `ico.ico` - 程序图标

## 截图

### 主界面

![image](https://github.com/xyxy1029/imghub/blob/main/home.png?raw=true)

### 添加日程

![image](https://github.com/xyxy1029/imghub/blob/main/add_schedule.png?raw=true)

### 编辑日程

![image](https://github.com/xyxy1029/imghub/blob/main/edit_schedule.png?raw=true)

### 删除日程

![image](https://github.com/xyxy1029/imghub/blob/main/delete_schedule.png?raw=true)

## 贡献指南

欢迎对本项目进行贡献！如果您想为此项目做出贡献，请：

1. Fork此仓库
2. 创建您的特性分支：`git checkout -b feature/AmazingFeature`
3. 提交您的更改：`git commit -m 'Add some AmazingFeature'`
4. 推送到分支：`git push origin feature/AmazingFeature`
5. 打开一个Pull Request

## 许可证

本项目采用GNU通用公共许可证第3版（GPL-3.0）进行许可。详情请参阅 [LICENSE](LICENSE) 文件。

## 联系方式

如有任何问题或建议，请提交issue或联系项目维护者。
