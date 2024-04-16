# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # 下一个文件按钮
        # self.next_button = QtWidgets.QPushButton(self.centralwidget)
        # self.next_button.setGeometry(QtCore.QRect(320, 490, 100, 40))
        # self.next_button.setObjectName("next_button")
        # self.next_button.setText("下一个")

        # 上一个文件按钮
        # self.pre_button = QtWidgets.QPushButton(self.centralwidget)
        # self.pre_button.setGeometry(QtCore.QRect(520, 490, 100, 40))
        # self.pre_button.setObjectName("pre_button")
        # self.pre_button.setText("上一个")

        #“激光品牌”
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(620, 45, 67, 17))
        self.label_3.setObjectName("label_3")

        #使用帮助
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(35, 290, 800, 500))
        self.label_4.setText(
            "工作流程:\n"
            "选择文件—>确定品牌—>自动标定—>调整标定数据—>手动标定—>效果展示—>保存数据\n\n"
            "提示:\n"
            "标定时尽量选择没有车辆的数据以确保标定数据的准确性。\n"
            "如果标定数据不理想，可以尝试同车道的其他的.dat文件再次自动标定。也可以进一步修改参数手动标定。\n"
            "当标定信息栏已经有参数时，若再次点击会覆盖先前标定数据。\n"
            "保存标定信息将存入./data/biaoding_file/中。\n")
        # 切换扫描模式
        self.switchUp2Down = QtWidgets.QRadioButton(self.centralwidget)
        self.switchUp2Down.setGeometry(QtCore.QRect(620, 10, 150, 31))
        self.switchUp2Down.setText("从上向下")
        self.switchUp2Down.setCheckable(True)

        # 品牌
        self.brand_selection = QtWidgets.QComboBox(self.centralwidget)
        self.brand_selection.setGeometry(QtCore.QRect(670, 40, 50, 31))
        self.brand_selection.addItems(["dg", "as"])

        # 自动标定按钮
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(620, 90, 100, 40))
        self.pushButton.setObjectName("pushButton")

        # 手动标定显示按钮
        self.shoudong_button = QtWidgets.QPushButton(self.centralwidget)
        self.shoudong_button.setGeometry(QtCore.QRect(620, 145, 100, 40))
        self.shoudong_button.setObjectName("shoudong_button")
        self.shoudong_button.setText("手动标定")

        # 最终效果显示按钮
        self.result_show_button = QtWidgets.QPushButton(self.centralwidget)
        self.result_show_button.setGeometry(QtCore.QRect(620, 200, 100, 40))
        self.result_show_button.setObjectName("result_show_button")
        self.result_show_button.setText("最终效果展示")

        # 存储标定信息按钮
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(620, 255, 100, 40))
        self.save_button.setObjectName("save_button")
        self.save_button.setText("保存标定信息")


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 340, 67, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 400, 67, 17))
        self.label_2.setObjectName("label_2")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 514, 28))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menubar.addAction(self.menu.menuAction())

        #输入栏
        self.filePath_editline = QtWidgets.QLineEdit(self.centralwidget)
        self.filePath_editline.setGeometry(QtCore.QRect(120, 335, 600, 31))
        self.filePath_editline.setPlaceholderText("请输入原文件：")

        #输入保存路径
        self.savePath_editline = QtWidgets.QLineEdit(self.centralwidget)
        self.savePath_editline.setGeometry(QtCore.QRect(120, 395, 600, 31))
        self.savePath_editline.setPlaceholderText("保存路径自动生成：")

        #显示当前地址
        self.address= QtWidgets.QLabel(self.centralwidget)
        self.address.setText("当前文件夹路径:")
        self.address.setGeometry(QtCore.QRect(30, 3, 800, 19))

        self.file_list = QtWidgets.QListWidget(self.centralwidget)
        self.file_list.setGeometry(30, 30, 420, 280)

        #显示标定信息
        self.biaoding_edit_word = QtWidgets.QLabel(self.centralwidget)
        self.biaoding_edit_word.setGeometry(QtCore.QRect(460, 3, 65, 19))
        self.biaoding_edit_word.setText("标定信息：")

        self.biaoding_angle_edit = QtWidgets.QTextEdit(self.centralwidget)
        self.biaoding_angle_edit.setGeometry(QtCore.QRect(520, 35, 60, 31))
        self.biaoding_angle_edit.setPlaceholderText("Angle")
        h_step = 34
        self.biaoding_height_edit = QtWidgets.QTextEdit(self.centralwidget)
        self.biaoding_height_edit.setGeometry(QtCore.QRect(520, 35 + h_step, 60, 31))
        self.biaoding_height_edit.setPlaceholderText("Height")

        self.biaoding_max_l_edit = QtWidgets.QTextEdit(self.centralwidget)
        self.biaoding_max_l_edit.setGeometry(QtCore.QRect(520, 35 + 2 * h_step, 60, 31))
        self.biaoding_max_l_edit.setPlaceholderText("Max_l")

        self.biaoding_min_l_edit = QtWidgets.QTextEdit(self.centralwidget)
        self.biaoding_min_l_edit.setGeometry(QtCore.QRect(520, 35 + 3 * h_step, 60, 31))
        self.biaoding_min_l_edit.setPlaceholderText("Min_l")

        self.biaoding_max_h_edit = QtWidgets.QTextEdit(self.centralwidget)
        self.biaoding_max_h_edit.setGeometry(QtCore.QRect(520, 35 + 4 * h_step, 60, 31))
        self.biaoding_max_h_edit.setPlaceholderText("Max_h")

        self.biaoding_min_h_edit = QtWidgets.QTextEdit(self.centralwidget)
        self.biaoding_min_h_edit.setGeometry(QtCore.QRect(520, 35 + 5 * h_step, 60, 31))
        self.biaoding_min_h_edit.setPlaceholderText("Min_h")
        # 安全岛宽度
        self.refuge_island_width = QtWidgets.QTextEdit(self.centralwidget)
        self.refuge_island_width.setGeometry(QtCore.QRect(520, 35 + 6 * h_step, 60, 31))
        self.refuge_island_width.setPlaceholderText("Isle_l")
        # 安全岛高度
        self.refuge_island_height = QtWidgets.QTextEdit(self.centralwidget)
        self.refuge_island_height.setGeometry(QtCore.QRect(520, 35 + 7 * h_step, 60, 31))
        self.refuge_island_height.setPlaceholderText("Isle_h")

        self.biaoding_label = QtWidgets.QLabel(self.centralwidget)
        self.biaoding_label.setGeometry(QtCore.QRect(460, 40, 60, 300))
        self.biaoding_label.setText("Angle:\n\nHeight:\n\nMax_l:\n\nMin_l:\n\nMax_h:\n\nMin_h:\n\nIsle_l:\n\nIsle_h:")
        self.biaoding_label.setAlignment(QtCore.Qt.AlignTop)


        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "标定工具 v_1.05"))
        self.pushButton.setText(_translate("MainWindow", "自动标定"))

        self.label.setText(_translate("MainWindow", "filePath:"))
        self.label_2.setText(_translate("MainWindow", "savePath:"))
        self.label_3.setText(_translate("MainWindow", "品牌："))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.action.setText(_translate("MainWindow", "打开"))
        self.action_2.setText(_translate("MainWindow", "打开文件夹"))
