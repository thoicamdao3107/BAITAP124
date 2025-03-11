from PyQt6.QtWidgets import QApplication, QMainWindow

from PyQt6.QtWidgets import QApplication, QMainWindow
from excercise_124.ui.MainWindow124EXT import MainWindow124EXT

# Tạo ứng dụng
app = QApplication([])

# Khởi tạo cửa sổ chính
mainwindow = QMainWindow()

# Khởi tạo giao diện người dùng
myui = MainWindow124EXT()

# Cài đặt UI cho cửa sổ chính
myui.setupUi(mainwindow)

# Hiển thị cửa sổ chính
myui.show()  # Sử dụng phương thức show() chuẩn thay vì showWindow()

# Bắt đầu vòng lặp ứng dụng
app.exec()
