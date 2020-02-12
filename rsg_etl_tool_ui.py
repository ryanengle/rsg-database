# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\rsg-etl-tool.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1835, 1315)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.splitter_3 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.frameTopFrame = QtWidgets.QFrame(self.splitter_3)
        self.frameTopFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameTopFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameTopFrame.setObjectName("frameTopFrame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frameTopFrame)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lblSelectedDataFolder = QtWidgets.QLabel(self.frameTopFrame)
        self.lblSelectedDataFolder.setMaximumSize(QtCore.QSize(16777215, 50))
        self.lblSelectedDataFolder.setObjectName("lblSelectedDataFolder")
        self.verticalLayout_3.addWidget(self.lblSelectedDataFolder)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.butOpenFolder = QtWidgets.QPushButton(self.frameTopFrame)
        self.butOpenFolder.setMaximumSize(QtCore.QSize(16777215, 50))
        self.butOpenFolder.setObjectName("butOpenFolder")
        self.horizontalLayout_2.addWidget(self.butOpenFolder)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.splitter = QtWidgets.QSplitter(self.frameTopFrame)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lblFilesInFolder = QtWidgets.QLabel(self.layoutWidget)
        self.lblFilesInFolder.setObjectName("lblFilesInFolder")
        self.verticalLayout_2.addWidget(self.lblFilesInFolder)
        self.lstFilesInFolder = QtWidgets.QListWidget(self.layoutWidget)
        self.lstFilesInFolder.setMinimumSize(QtCore.QSize(0, 200))
        self.lstFilesInFolder.setObjectName("lstFilesInFolder")
        self.verticalLayout_2.addWidget(self.lstFilesInFolder)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblColumnsInSelectedFile = QtWidgets.QLabel(self.layoutWidget1)
        self.lblColumnsInSelectedFile.setObjectName("lblColumnsInSelectedFile")
        self.verticalLayout.addWidget(self.lblColumnsInSelectedFile)
        self.lstColumnsInSelectedFile = QtWidgets.QListWidget(self.layoutWidget1)
        self.lstColumnsInSelectedFile.setObjectName("lstColumnsInSelectedFile")
        self.verticalLayout.addWidget(self.lstColumnsInSelectedFile)
        self.verticalLayout_3.addWidget(self.splitter)
        self.splitter.raise_()
        self.lblSelectedDataFolder.raise_()
        self.frameBottomFrame = QtWidgets.QFrame(self.splitter_3)
        self.frameBottomFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameBottomFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameBottomFrame.setObjectName("frameBottomFrame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frameBottomFrame)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.butNewTable = QtWidgets.QPushButton(self.frameBottomFrame)
        self.butNewTable.setObjectName("butNewTable")
        self.horizontalLayout.addWidget(self.butNewTable)
        spacerItem1 = QtWidgets.QSpacerItem(40, 13, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.splitter_2 = QtWidgets.QSplitter(self.frameBottomFrame)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.layoutWidget2 = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lblTablesInDb = QtWidgets.QLabel(self.layoutWidget2)
        self.lblTablesInDb.setObjectName("lblTablesInDb")
        self.verticalLayout_5.addWidget(self.lblTablesInDb)
        self.lstTablesInDb = QtWidgets.QListWidget(self.layoutWidget2)
        self.lstTablesInDb.setMinimumSize(QtCore.QSize(0, 300))
        self.lstTablesInDb.setObjectName("lstTablesInDb")
        item = QtWidgets.QListWidgetItem()
        self.lstTablesInDb.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lstTablesInDb.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lstTablesInDb.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lstTablesInDb.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lstTablesInDb.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lstTablesInDb.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lstTablesInDb.addItem(item)
        self.verticalLayout_5.addWidget(self.lstTablesInDb)
        self.layoutWidget3 = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lblAttributesInSelectedTable = QtWidgets.QLabel(self.layoutWidget3)
        self.lblAttributesInSelectedTable.setObjectName("lblAttributesInSelectedTable")
        self.verticalLayout_4.addWidget(self.lblAttributesInSelectedTable)
        self.lstAttributesInSelectedTable = QtWidgets.QListWidget(self.layoutWidget3)
        self.lstAttributesInSelectedTable.setEnabled(False)
        self.lstAttributesInSelectedTable.setObjectName("lstAttributesInSelectedTable")
        item = QtWidgets.QListWidgetItem()
        self.lstAttributesInSelectedTable.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lstAttributesInSelectedTable.addItem(item)
        self.verticalLayout_4.addWidget(self.lstAttributesInSelectedTable)
        self.verticalLayout_6.addWidget(self.splitter_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.butPopulate = QtWidgets.QPushButton(self.frameBottomFrame)
        self.butPopulate.setObjectName("butPopulate")
        self.horizontalLayout_3.addWidget(self.butPopulate)
        self.pbProgressBar = QtWidgets.QProgressBar(self.frameBottomFrame)
        self.pbProgressBar.setProperty("value", 24)
        self.pbProgressBar.setObjectName("pbProgressBar")
        self.horizontalLayout_3.addWidget(self.pbProgressBar)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.splitter_2.raise_()
        self.verticalLayout_7.addWidget(self.splitter_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1835, 38))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Resilient Sensor Grid ETL Tool (2020.02.10)"))
        self.lblSelectedDataFolder.setText(_translate("MainWindow", "C:...Projects01 DDDASUMiami_DataFort Lauderdale2007"))
        self.butOpenFolder.setText(_translate("MainWindow", "Open Folder"))
        self.lblFilesInFolder.setText(_translate("MainWindow", "Files in folder"))
        self.lblColumnsInSelectedFile.setText(_translate("MainWindow", "Columns in selected file"))
        self.butNewTable.setText(_translate("MainWindow", "New Table"))
        self.lblTablesInDb.setText(_translate("MainWindow", "Tables in DB"))
        __sortingEnabled = self.lstTablesInDb.isSortingEnabled()
        self.lstTablesInDb.setSortingEnabled(False)
        item = self.lstTablesInDb.item(0)
        item.setText(_translate("MainWindow", "List of Tables (Sensors, etc)"))
        item = self.lstTablesInDb.item(1)
        item.setText(_translate("MainWindow", "..."))
        item = self.lstTablesInDb.item(2)
        item.setText(_translate("MainWindow", "Generators"))
        item = self.lstTablesInDb.item(3)
        item.setText(_translate("MainWindow", "PV Arrays"))
        item = self.lstTablesInDb.item(4)
        item.setText(_translate("MainWindow", "Wind Turbine"))
        item = self.lstTablesInDb.item(5)
        item.setText(_translate("MainWindow", "Load"))
        item = self.lstTablesInDb.item(6)
        item.setText(_translate("MainWindow", "Power Network"))
        self.lstTablesInDb.setSortingEnabled(__sortingEnabled)
        self.lblAttributesInSelectedTable.setText(_translate("MainWindow", "Attributes in Selected Table"))
        __sortingEnabled = self.lstAttributesInSelectedTable.isSortingEnabled()
        self.lstAttributesInSelectedTable.setSortingEnabled(False)
        item = self.lstAttributesInSelectedTable.item(0)
        item.setText(_translate("MainWindow", "List of variables (attributes) in a selected table"))
        item = self.lstAttributesInSelectedTable.item(1)
        item.setText(_translate("MainWindow", "(Work in Progress)"))
        self.lstAttributesInSelectedTable.setSortingEnabled(__sortingEnabled)
        self.butPopulate.setText(_translate("MainWindow", "Populate"))

