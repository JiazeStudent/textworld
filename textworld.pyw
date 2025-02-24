import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QMenu, QFileDialog, QMessageBox
from PyQt5.QtGui import QFont, QKeySequence
from PyQt5.QtCore import Qt 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("文本世界")
        self.setGeometry(50,100,2500,1500)

        # 创建多行文本编辑框
        self.text_edit = QTextEdit(self)
        self.text_edit.setPlaceholderText("请输入多行文本...")
        self.setCentralWidget(self.text_edit)  # 将文本编辑框设置为窗口的中心部件

        
        # 设置整体字体
        font = QFont("微软雅黑", 12)  # 设置字体为微软雅黑，字号为 12
        self.text_edit.setFont(font)
        self.setFont(font)

        # 设置占位文本的样式（通过 QSS）
        self.text_edit.setStyleSheet("""
            QTextEdit {
                border: 1px solid #ccc; /* 边框颜色 */
                padding: 8px; /* 内边距 */
                font-family: '微软雅黑'; /* 字体 */
                font-size: 10pt; /* 字体大小 */
            }
            QTextEdit:placeholder {
                color: #888; /* 占位文本颜色 */
            }
        """)

        self.setStyleSheet("""
            QMainWindow {
                background-color: #ffffff; /* 白色背景 */
            }

            QMenuBar {
                background-color: #f0f0f0; /* 浅灰色背景 */
                font-size: 10pt; /* 菜单栏字体大小 */
                padding: 5px; /* 菜单栏内边距 */
                border: 1px solid #dcdcdc; /* 边框 */
                border-radius: 4px; /* 菜单栏圆角 */
            }

            QMenuBar::item {
                padding: 8px 20px; /* 菜单项内边距 */
                border-radius: 4px; /* 菜单项圆角 */
            }

            QMenuBar::item:selected {
                background-color: #e0e0e0; /* 选中时的背景色 */
            }

            QMenu {
                background-color: #ffffff; /* 白色背景 */
                font-size: 10pt; /* 菜单字体大小 */
                border: 1px solid #dcdcdc; /* 边框 */
                padding: 3px; /* 内边距 */
            }

            QMenu::item {
                padding: 6px 20px; /* 菜单项内边距 */
                border-radius: 4px; /* 菜单项圆角 */
            }

            QMenu::item:selected {
                background-color: #e0e0e0; /* 选中时的背景色 */
            }
        """)

        
        # 屏蔽右键菜单
        self.text_edit.setContextMenuPolicy(Qt.NoContextMenu)

        # 创建菜单栏
        menubar = self.menuBar()

        # 创建文件菜单
        file_menu = menubar.addMenu("文件")
        open_action = QAction("打开", self)
        open_action.setShortcut(QKeySequence.Open)
        save_action = QAction("保存", self)
        save_action.setShortcut(QKeySequence.Save)
        exit_action = QAction("退出", self)

        open_action.triggered.connect(self.on_open)
        save_action.triggered.connect(self.on_save)
        exit_action.triggered.connect(self.close)

        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        file_menu.addSeparator()  # 添加分割线
        file_menu.addAction(exit_action)

        # 创建编辑菜单
        edit_menu = menubar.addMenu("编辑")
        copy_action = QAction("复制", self)
        copy_action.setShortcut(QKeySequence.Copy)
        paste_action = QAction("粘贴", self)
        paste_action.setShortcut(QKeySequence.Paste)
        cut_action = QAction("剪切", self)
        cut_action.setShortcut(QKeySequence.Cut)

        copy_action.triggered.connect(self.on_copy)
        paste_action.triggered.connect(self.on_paste)
        cut_action.triggered.connect(self.on_cut)

        edit_menu.addAction(copy_action)
        edit_menu.addAction(paste_action)
        edit_menu.addAction(cut_action)
        edit_menu.addSeparator()  # 添加分割线
        undo_action = QAction("撤销", self)
        undo_action.setShortcut(QKeySequence.Undo)  # 设置快捷键 Ctrl+Z
        undo_action.triggered.connect(self.text_edit.undo)

        redo_action = QAction("恢复", self)
        redo_action.setShortcut(QKeySequence.Redo)  # 设置快捷键 Ctrl+Y
        redo_action.triggered.connect(self.text_edit.redo)

        edit_menu.addAction(undo_action)
        edit_menu.addAction(redo_action)


        # 创建帮助菜单
        help_menu = menubar.addMenu("帮助")
        about_action = QAction("关于", self)
        about_action.triggered.connect(self.on_about)
        help_menu.addAction(about_action)

    def on_open(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "打开文件", "", "Text Files (*.txt);;All Files (*)")
        if file_path:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                self.text_edit.setPlainText(content)
    
    def on_save(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "保存文件", "", "Text Files (*.txt);;All Files (*)")
        if file_path:
            with open(file_path, "w", encoding="utf-8") as file:
                content = self.text_edit.toPlainText()
                file.write(content)

    def on_copy(self):
        self.text_edit.copy()

    def on_paste(self):
        self.text_edit.paste()

    def on_cut(self):
        self.text_edit.cut()

    def on_about(self):
        print("这是一个简单的多行文本编辑器")
        QMessageBox.about(self, "关于软件", 
                      "软件名称：文本世界\n"
                      "版本：0.1.0 beta\n"
                      "作者：Mr. 树叶\n"
                      "公众号：树叶世界\n"
                      "版权所有：© 2025 树叶世界\n"
                      "感谢您的使用！")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())