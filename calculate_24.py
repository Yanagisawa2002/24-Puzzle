import tkinter as tk
from tkinter import messagebox

# 计算函数
def can_form_24(nums, path=""):
    if len(nums) == 1:
        # 基本情况：如果只有一个数字，检查是否等于24，并输出路径
        if abs(nums[0] - 24) < 1e-6:
            # 将数字转换为整数输出
            path = path.replace(" * ", "*").replace(" / ", "/").replace(" + ", "+").replace(" - ", "-")
            return f"Solution: {path} = 24"
        return None

    # 遍历所有数字的两两组合
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                # 选择两个数字，计算它们的结果
                new_nums = [nums[k] for k in range(len(nums)) if k != i and k != j]
                a, b = nums[i], nums[j]
                
                # 尝试所有运算符
                for op in ['+', '-', '*', '/']:
                    if op == '+':
                        result = a + b
                        new_path = f"({a} {op} {b})"
                    elif op == '-':
                        result = a - b
                        new_path = f"({a} {op} {b})"
                    elif op == '*':
                        result = a * b
                        new_path = f"({a} {op} {b})"
                    elif op == '/':
                        if b != 0:
                            result = a / b
                            new_path = f"({a} {op} {b})"
                        else:
                            continue
                    
                    # 递归调用，继续计算
                    result_path = can_form_24(new_nums + [result], path + (" " if path == "" else " ") + new_path)
                    if result_path:
                        return result_path
    return None

# 验证输入是否为数字
def validate_input(*args):
    if all(arg.get() != "" for arg in args):  # 确保所有输入框都有值
        for entry in args:
            try:
                float(entry.get())  # 尝试将输入转化为数字
            except ValueError:
                entry.set('')  # 如果转换失败，清空输入框
                messagebox.showwarning("Invalid Input", "Please enter valid numbers.")
                return

# GUI 回调函数
def on_calculate():
    try:
        # 获取用户输入的四个数字
        nums = [float(entry_1.get()), float(entry_2.get()), float(entry_3.get()), float(entry_4.get())]
        
        # 调用计算函数
        result = can_form_24(nums)
        if result:
            result_label.config(text=result)
        else:
            result_label.config(text="No solution found")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

# 创建主窗口
root = tk.Tk()
root.title("24 Game Solver")

# 创建并布局控件
label = tk.Label(root, text="Enter four numbers:")
label.pack(pady=10)

entry_1 = tk.Entry(root, width=10)
entry_1.pack(side=tk.LEFT, padx=5)
entry_2 = tk.Entry(root, width=10)
entry_2.pack(side=tk.LEFT, padx=5)
entry_3 = tk.Entry(root, width=10)
entry_3.pack(side=tk.LEFT, padx=5)
entry_4 = tk.Entry(root, width=10)
entry_4.pack(side=tk.LEFT, padx=5)

# 验证输入
entry_var_1 = tk.StringVar()
entry_var_2 = tk.StringVar()
entry_var_3 = tk.StringVar()
entry_var_4 = tk.StringVar()

entry_1.config(textvariable=entry_var_1)
entry_2.config(textvariable=entry_var_2)
entry_3.config(textvariable=entry_var_3)
entry_4.config(textvariable=entry_var_4)

entry_var_1.trace("w", lambda *args: validate_input(entry_var_1, entry_var_2, entry_var_3, entry_var_4))
entry_var_2.trace("w", lambda *args: validate_input(entry_var_1, entry_var_2, entry_var_3, entry_var_4))
entry_var_3.trace("w", lambda *args: validate_input(entry_var_1, entry_var_2, entry_var_3, entry_var_4))
entry_var_4.trace("w", lambda *args: validate_input(entry_var_1, entry_var_2, entry_var_3, entry_var_4))

calculate_button = tk.Button(root, text="Calculate", command=on_calculate)
calculate_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=20)

# 运行主事件循环
root.mainloop()
