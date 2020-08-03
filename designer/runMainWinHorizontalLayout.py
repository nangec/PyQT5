import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

import MainWinHorizontalLayout

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = QMainWindow()

    # 创建ui的实例
    ui = MainWinHorizontalLayout.Ui_MainWindow()
    ##  向主窗口上添加空间
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec())
