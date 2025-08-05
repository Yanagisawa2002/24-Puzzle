import sys
import os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                            QLabel, QLineEdit, QPushButton, QTextEdit, QMessageBox)
from PyQt5.QtCore import Qt

# 导入现有的24点求解器功能
import importlib.util

spec = importlib.util.spec_from_file_location("24point", "24point.py")
point24 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(point24)

def format_num(n):
    if n.is_integer():
        return str(int(n))
    else:
        return str(n)

class Point24Solver(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        # 设置窗口标题和大小
        self.setWindowTitle('24点求解器')
        self.setGeometry(100, 100, 500, 400)

    def initUI(self):
        # 创建主窗口部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # 创建主布局
        main_layout = QVBoxLayout(central_widget)

        # 创建输入区域
        input_label = QLabel('输入四个数字:')
        main_layout.addWidget(input_label)
        input_layout = QHBoxLayout()
        self.num_inputs = []
        for i in range(4):
            num_input = QLineEdit()
            num_input.setPlaceholderText(f'数字 {i+1}')
            num_input.setFixedWidth(60)
            num_input.setAlignment(Qt.AlignCenter)
            self.num_inputs.append(num_input)
            input_layout.addWidget(num_input)

        # 创建计算按钮
        self.calc_button = QPushButton('计算')
        self.calc_button.clicked.connect(self.calculate)

        # 创建清除按钮
        self.clear_button = QPushButton('清除')
        self.clear_button.clicked.connect(self.clear)

        # 创建按钮布局
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.calc_button)
        button_layout.addWidget(self.clear_button)

        # 创建结果显示区域
        result_label = QLabel('计算结果:')
        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)

        # 将所有部件添加到主布局
        main_layout.addLayout(input_layout)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(result_label)
        main_layout.addWidget(self.result_text)

        # 添加说明文本
        help_text = QLabel('说明: 输入四个数字，程序将尝试使用加减乘除运算得到24。')
        help_text.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(help_text)

    def calculate(self):
        nums = []
        for i, num_input in enumerate(self.num_inputs):
            text = num_input.text().strip()
            if not text:
                QMessageBox.warning(self, '输入错误', f'请输入数字 {i+1}')
                return
            try:
                nums.append(float(text))
            except ValueError:
                QMessageBox.warning(self, '输入错误', f'数字 {i+1} 不是有效的数字')
                return

        # 格式化初始表达式
        initial_expressions = [format_num(num) for num in nums]

        # 调用求解函数
        solution = point24.solve_24(nums, initial_expressions)

        # 显示结果
        if solution:
            self.result_text.setText(f'可以解决：{solution}')
        else:
            self.result_text.setText('无法解决')

    def clear(self):
        for num_input in self.num_inputs:
            num_input.clear()
        self.result_text.clear()

if __name__ == '__main__':
    # 确保中文显示正常
    os.environ['QT_FONT_DPI'] = '96'
    app = QApplication(sys.argv)
    window = Point24Solver()
    window.show()
    sys.exit(app.exec_())