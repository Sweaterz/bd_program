# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import os
import sys
from PyQt5 import QtWidgets
from class_biaoding import Biaoding
import newGUI


class Window(newGUI.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.have_opened_files = []
        self.file_point = 0
        self.directory1 = ""
        self.biaoding_data = ""
        self.filePath = ""
        self.savePath = ""
        self.up2down = self.switchUp2Down.isChecked()
        self.pushButton.clicked.connect(self.zidong_biaoding_270mini)
        self.action.triggered.connect(self.open_new_file)
        self.action_2.triggered.connect(self.open_new_folder)
        # self.next_button.clicked.connect(self.next_file)
        # self.pre_button.clicked.connect(self.pre_file)
        self.save_button.clicked.connect(self.save_biaoding_info)
        self.shoudong_button.clicked.connect(self.shoudong_biaoding_270mini)
        self.result_show_button.clicked.connect(self.result_show)
        self.file_list.itemSelectionChanged.connect(self.select_file)
        self.file_list.doubleClicked.connect(self.quick_show)
        self.action_4.triggered.connect(self.help_info)
        self.action_3.triggered.connect(self.about)
        # self.brand_selection.currentIndexChanged.connect(self.brand_change)

    def about(self):
        QtWidgets.QMessageBox.information(self, "提示框",
                                          "工作流程:\n"
                                          "选择文件—>确定品牌—>自动标定—>调整标定数据—>手动标定—>效果展示—>保存数据\n\n"
                                          "提示:\n"
                                          "标定时尽量选择没有车辆的数据以确保标定数据的准确性。\n"
                                          "如果标定数据不理想，可以尝试同车道的其他的.dat文件再次自动标定。也可以进一步修改参数手动标定。\n"
                                          "当标定信息栏已经有参数时，若再次点击会覆盖先前标定数据。\n"
                                          "保存标定信息将存入./data/biaoding_file/中。\n")

    def help_info(self):
        QtWidgets.QMessageBox.information(self, "关于",
                                          "标定软件  v1.05\n"
                                          "2023.9.5\n\n"
                                          "中储恒科物联网有限公司")

    def quick_show(self):
        if self.biaoding_angle_edit.text() == "" and self.biaoding_height_edit.text() == "":
            self.zidong_biaoding_270mini()
            return
        else:
            self.shoudong_biaoding()
            return

    def select_file(self):
        if self.file_list.count() == 0:
            return
        if len(self.file_list.selectedItems()) == 0:
            return
        self.filePath = self.directory1 + '/' + self.file_list.selectedItems()[0].text()
        self.savePath = self.filePath[:-4].replace("data_file", "bin_file") + ".bin"
        self.savePath_editline.setText(self.savePath)
        self.filePath_editline.setText(self.filePath)
        self.file_point = self.file_list.currentRow()

    # def brand_change(self):
    #     self.brand_selection.currentText()
    #     self.brand
    def next_file(self):
        if self.filePath_editline.text() == "":
            QtWidgets.QMessageBox.information(self, "提示框", "还没有选中文件")
            return
        self.file_point = (self.file_point + 1) % len(self.have_opened_files)
        self.file_list.setCurrentRow(self.file_point)
        self.filePath_editline.setText(self.directory1 + "/" + self.have_opened_files[self.file_point])
        self.filePath = self.filePath_editline.text()
        self.savePath = self.filePath[:-4].replace("data_file", "bin_file") + ".bin"
        self.savePath_editline.setText(self.savePath)

    def pre_file(self):
        if self.filePath_editline.text() == "":
            QtWidgets.QMessageBox.information(self, "提示框", "还没有选中文件")
            return
        self.file_point = (self.file_point - 1) % len(self.have_opened_files)
        self.file_list.setCurrentRow(self.file_point)
        self.filePath_editline.setText(self.directory1 + "/" + self.have_opened_files[self.file_point])
        self.filePath = self.filePath_editline.text()
        self.savePath = self.filePath[:-4].replace("data_file", "bin_file") + ".bin"
        self.savePath_editline.setText(self.savePath)

    def save_biaoding_info(self):
        dir_name = "data/biaoding_file"
        biaoding_savePath = dir_name + '/' + self.filePath_editline.text().split('/')[-1][:-4] + ".txt"

        if not os.path.isdir(dir_name):
            os.makedirs(dir_name)
        self.biaoding_data = "Angle:{}\nHeight:{}\nMax_l:{}\nMin_l:{}\nMax_h:{}\nMin_h:{}\nIsle_h{}\nIsle_l:{}" \
            .format(self.biaoding_angle_edit.text(), self.biaoding_height_edit.text(),
                    self.biaoding_max_l_edit.text(), self.biaoding_min_l_edit.text(),
                    self.biaoding_max_h_edit.text(), self.biaoding_min_h_edit.text(),
                    self.refuge_island_height.text(), self.refuge_island_width.text())
        with open(biaoding_savePath, 'w') as f:
            f.write(self.biaoding_data)
            f.close()
        QtWidgets.QMessageBox.information(self, "提示框", "保存成功:<br>%s" % biaoding_savePath)

    def open_new_file(self):
        self.directory1 = "./data/data_file/"
        file_urls, _ = QtWidgets.QFileDialog.getOpenFileNames(self, "选取文件", "./data/data_file/",
                                                              "(*.dat);;All files(*.*)")
        # _, _ = QFileDialog.getOpenFileName(self, "选取文件", '/home/zhy/下载/', '12 (*.jpg *.gif *.png *.jpeg)')
        # print(filename)
        if not file_urls:
            return

        for file_url in file_urls:
            file_name = file_url.split('/')[-1]
            self.have_opened_files.append(file_name)
            self.file_list.addItem(file_name)
        # self.filePath_editline.setText(self.file_url)
        # self.filePath = self.filePath_editline.text()
        self.directory1 = '/'.join(file_urls[0].split('/')[:-1])
        if self.have_opened_files:
            self.filePath_editline.setText(file_urls[0])
            QtWidgets.QMessageBox.information(self, "提示框", "打开文件夹:<br>%s" % self.directory1)
            self.address.setText(self.directory1)
            # self.filePath = self.filePath_editline.text()

    def open_new_folder(self):

        self.directory1 = QtWidgets.QFileDialog.getExistingDirectory(self, "选取文件夹", "./data/data_file/")
        if self.directory1 == "":
            return
        if self.file_list.count() != 0:
            self.file_list.itemSelectionChanged.disconnect(self.select_file)
            self.file_list.clear()
            self.file_list.itemSelectionChanged.connect(self.select_file)
            self.file_point = 0
            self.have_opened_files.clear()

        QtWidgets.QMessageBox.information(self, "提示框", "打开文件夹:<br>%s" % self.directory1)
        # self.address.setText(self.directory1)
        files = os.listdir(self.directory1)
        files.sort()
        for file in files:
            if file.split('.')[-1] == "dat":
                self.have_opened_files.append(file)
                self.file_list.addItem(file)
        if self.have_opened_files:
            self.filePath_editline.setText(self.directory1 + "/" + self.have_opened_files[self.file_point])
            # self.file_list.setCurrent(5)
            # self.msg.setStyleSheet("background-color: yellow; color: black;")
            # self.filePath = self.filePath_editline.text()
            # self.savePath = self.filePath[:-4].replace("data_file", "bin_file") + ".bin"
            # self.savePath_editline.setText(self.savePath)

    def zidong_biaoding(self):
        try:
            if self.filePath == "":
                QtWidgets.QMessageBox.information(self, "提示框", "请先选择文件！")
                return
            self.up2down = self.switchUp2Down.isChecked()

            self.filePath = self.filePath_editline.text()
            self.savePath = self.filePath[:-4].replace("data_file", "bin_file") + ".bin"
            self.savePath_editline.setText(self.savePath)
            self.mayavi_widget1.clearAll()

            if self.brand_selection.currentText() == "杜格":
                temp = Biaoding(self.filePath, self.savePath, "dg")
                flag = temp.readDatDG(up2down=self.up2down)
                if not flag:
                    QtWidgets.QMessageBox.information(self, "提示框", "数据错误，请检查品牌是否正确或者更换数据重试。")
                    return
                # temp.biaoding_show()
                temp.integrate_show(self.mayavi_widget1.visualization.scene.mayavi_scene)
            elif self.brand_selection.currentText() == "傲视":
                temp = Biaoding(self.filePath, self.savePath, "as")
                flag = temp.justreadDatAS()
                if not flag:
                    QtWidgets.QMessageBox.information(self, "提示框", "数据错误，请检查品牌是否正确或者更换数据重试。")
                    return
                # temp.biaoding_show()
                temp.integrate_show(self.mayavi_widget1.visualization.scene.mayavi_scene)

            else:
                temp = Biaoding(self.filePath, self.savePath, "dg")
                flag = temp.justreadDatAS()
                if not flag:
                    QtWidgets.QMessageBox.information(self, "提示框", "数据错误，请检查品牌是否正确或者更换数据重试。")
                    return
                # temp.biaoding_show()
                temp.integrate_show(self.mayavi_widget1.visualization.scene.mayavi_scene)

            # QMessageBox.information(MainWindow, "提示框","标定成功")
            self.biaoding_angle_edit.setText("{:.2f}".format(temp.iHorizontalAngle))
            self.biaoding_height_edit.setText(str(temp.iHorizontalHeight))
            self.biaoding_max_l_edit.setText(str(temp.max_l))
            self.biaoding_min_l_edit.setText(str(temp.min_l))
            self.biaoding_max_h_edit.setText(str(temp.max_h))
            self.biaoding_min_h_edit.setText(str(temp.min_h))
        except Exception as e:
            QtWidgets.QMessageBox.information(self, "错误！", "标定出错,请检查数据或更换数据重试\n" + str(e))
            return

    def zidong_biaoding_270mini(self):
        if self.filePath == "":
            QtWidgets.QMessageBox.information(self, "提示框", "请先选择文件！")
            return
        self.up2down = self.switchUp2Down.isChecked()

        self.filePath = self.filePath_editline.text()
        self.savePath = self.filePath[:-4].replace("data_file", "bin_file") + ".bin"
        self.savePath_editline.setText(self.savePath)
        self.mayavi_widget1.clearAll()

        if self.brand_selection.currentText() == "杜格":
            temp = Biaoding(self.filePath, self.savePath, "dg")
            flag = temp.readDatDG_270mini(up2down=self.up2down)
            if not flag:
                QtWidgets.QMessageBox.information(self, "提示框", "数据错误，请检查品牌是否正确或者更换数据重试。")
                return
            # temp.biaoding_show()
            temp.integrate_show(self.mayavi_widget1.visualization.scene.mayavi_scene)
        elif self.brand_selection.currentText() == "傲视":
            temp = Biaoding(self.filePath, self.savePath, "as")
            flag = temp.justreadDatAS()
            if not flag:
                QtWidgets.QMessageBox.information(self, "提示框", "数据错误，请检查品牌是否正确或者更换数据重试。")
                return
            # temp.biaoding_show()
            temp.integrate_show(self.mayavi_widget1.visualization.scene.mayavi_scene)

        else:
            temp = Biaoding(self.filePath, self.savePath, "dg")
            flag = temp.justreadDatAS()
            if not flag:
                QtWidgets.QMessageBox.information(self, "提示框", "数据错误，请检查品牌是否正确或者更换数据重试。")
                return
            # temp.biaoding_show()
            temp.integrate_show(self.mayavi_widget1.visualization.scene.mayavi_scene)

        # QMessageBox.information(MainWindow, "提示框","标定成功")
        self.biaoding_angle_edit.setText("{:.2f}".format(temp.iHorizontalAngle))
        self.biaoding_height_edit.setText(str(temp.iHorizontalHeight))
        self.biaoding_max_l_edit.setText(str(temp.max_l))
        self.biaoding_min_l_edit.setText(str(temp.min_l))
        self.biaoding_max_h_edit.setText(str(temp.max_h))
        self.biaoding_min_h_edit.setText(str(temp.min_h))

    def shoudong_biaoding(self):
        try:
            if self.filePath == "":
                QtWidgets.QMessageBox.information(self, "提示框", "请先选择文件！")
                return
            if self.biaoding_angle_edit.text() == '':
                QtWidgets.QMessageBox.information(self, "提示框", "请先自动标定！")
                return
            self.up2down = self.switchUp2Down.isChecked()

            self.savePath = self.filePath[:-4].replace("data_file", "bin_file") + ".bin"
            self.savePath_editline.setText(self.savePath)
            temp = Biaoding(self.filePath, self.savePath, self.brand_selection.currentText())
            temp.iHorizontalAngle = float(self.biaoding_angle_edit.text())
            temp.iHorizontalHeight = int(self.biaoding_height_edit.text())
            temp.max_l = int(self.biaoding_max_l_edit.text())
            temp.min_l = int(self.biaoding_min_l_edit.text())
            temp.max_h = int(self.biaoding_max_h_edit.text())
            temp.min_h = int(self.biaoding_min_h_edit.text())
            self.mayavi_widget1.clearAll()

            if self.brand_selection.currentText() == "杜格":
                flag = temp.readDatDG2(up2down=self.up2down)
                if not flag:
                    QtWidgets.QMessageBox.information(self, "提示框", "数据错误，请检查品牌是否正确或者更换数据重试。")
                    return
            elif self.brand_selection.currentText() == "傲视":
                flag = temp.justreadDatAS2()
                if not flag:
                    QtWidgets.QMessageBox.information(self, "提示框", "数据错误，请检查品牌是否正确或者更换数据重试。")
                    return
            # temp.biaoding_show()
            temp.integrate_show(self.mayavi_widget1.visualization.scene.mayavi_scene)
        except Exception as e:
            QtWidgets.QMessageBox.information(self, "错误！", "标定出错,请检查数据或更换数据重试\n" + str(e))
            return

    def shoudong_biaoding_270mini(self):
        try:
            if self.filePath == "":
                QtWidgets.QMessageBox.information(self, "提示框", "请先选择文件！")
                return
            if self.biaoding_angle_edit.text() == '':
                QtWidgets.QMessageBox.information(self, "提示框", "请先自动标定！")
                return
            self.up2down = self.switchUp2Down.isChecked()

            self.savePath = self.filePath[:-4].replace("data_file", "bin_file") + ".bin"
            self.savePath_editline.setText(self.savePath)
            temp = Biaoding(self.filePath, self.savePath, self.brand_selection.currentText())
            temp.iHorizontalAngle = float(self.biaoding_angle_edit.text())
            temp.iHorizontalHeight = int(self.biaoding_height_edit.text())
            temp.max_l = int(self.biaoding_max_l_edit.text())
            temp.min_l = int(self.biaoding_min_l_edit.text())
            temp.max_h = int(self.biaoding_max_h_edit.text())
            temp.min_h = int(self.biaoding_min_h_edit.text())
            temp.lidarAngleStep = 0.25
            self.mayavi_widget1.clearAll()

            if self.brand_selection.currentText() == "杜格":
                flag = temp.readDatDG2_270mini(up2down=self.up2down)
                if not flag:
                    QtWidgets.QMessageBox.information(self, "提示框", "数据错误，请检查品牌是否正确或者更换数据重试。")
                    return
            elif self.brand_selection.currentText() == "傲视":
                flag = temp.justreadDatAS2()
                if not flag:
                    QtWidgets.QMessageBox.information(self, "提示框", "数据错误，请检查品牌是否正确或者更换数据重试。")
                    return
            # temp.biaoding_show()
            temp.integrate_show(self.mayavi_widget1.visualization.scene.mayavi_scene)
        except Exception as e:
            QtWidgets.QMessageBox.information(self, "错误！", "标定出错,请检查数据或更换数据重试\n" + str(e))
            return
    def result_show(self):
        if self.refuge_island_height.text() == '':
            self.refuge_island_height.setText('0')
        if self.refuge_island_width.text() == '':
            self.refuge_island_width.setText('0')
        temp = Biaoding(self.filePath, self.savePath, self.brand_selection.currentText())
        temp.iHorizontalAngle = float(self.biaoding_angle_edit.text())
        temp.iHorizontalHeight = int(self.biaoding_height_edit.text())
        temp.max_l = int(self.biaoding_max_l_edit.text())
        temp.min_l = int(self.biaoding_min_l_edit.text())
        temp.max_h = int(self.biaoding_max_h_edit.text())
        temp.min_h = int(self.biaoding_min_h_edit.text())
        temp.isle_l = int(self.refuge_island_width.text())
        temp.isle_h = int(self.refuge_island_height.text())
        self.mayavi_widget1.clearAll()
        try:
            temp.final_integrate_show(fig=self.mayavi_widget1.visualization.scene.mayavi_scene, up2down=self.up2down)
        except Exception as e:
            QtWidgets.QMessageBox.information(self, "错误！", "标定出错,请检查数据或更换数据重试\n" + str(e))
            return


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mywindow = Window()
    mywindow.show()
    sys.exit(app.exec())
