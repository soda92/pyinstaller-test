from PySide6 import QtWidgets
import sys


class LayoutApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        main_widget = QtWidgets.QWidget()  # 实例化一个widget控件
        main_layout = QtWidgets.QVBoxLayout()  # 实例化一个垂直布局层
        main_widget.setLayout(main_layout)  # 设置widget控件布局为水平布局
        # 实例化3个按钮
        button_1 = QtWidgets.QPushButton('按钮一')
        button_2 = QtWidgets.QPushButton('按钮二')
        button_3 = QtWidgets.QPushButton('按钮三')
        # 将按钮添加到水平布局中
        main_layout.addWidget(button_1)
        main_layout.addWidget(button_2)
        main_layout.addWidget(button_3)

        self.setCentralWidget(main_widget)  # 设置窗口的中央部件


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = LayoutApp()
    gui.resize(400, 300)
    gui.show()
    sys.exit(app.exec())
