# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ImageReaderGui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1004, 671)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.outputTextView = QtGui.QPlainTextEdit(self.centralwidget)
        self.outputTextView.setGeometry(QtCore.QRect(530, 10, 461, 581))
        self.outputTextView.setObjectName(_fromUtf8("outputTextView"))
        self.readImageButton = QtGui.QPushButton(self.centralwidget)
        self.readImageButton.setGeometry(QtCore.QRect(870, 600, 121, 31))
        self.readImageButton.setObjectName(_fromUtf8("readImageButton"))
        self.filePathInput = QtGui.QLineEdit(self.centralwidget)
        self.filePathInput.setGeometry(QtCore.QRect(450, 600, 411, 31))
        self.filePathInput.setObjectName(_fromUtf8("filePathInput"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 600, 131, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.inputImageView = QtGui.QGraphicsView(self.centralwidget)
        self.inputImageView.setGeometry(QtCore.QRect(10, 10, 511, 341))
        self.inputImageView.setObjectName(_fromUtf8("inputImageView"))
        self.matchedTextView = QtGui.QPlainTextEdit(self.centralwidget)
        self.matchedTextView.setGeometry(QtCore.QRect(10, 360, 511, 231))
        self.matchedTextView.setObjectName(_fromUtf8("matchedTextView"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Image Reader", None))
        self.readImageButton.setText(_translate("MainWindow", "Read Image Text", None))
        self.label.setText(_translate("MainWindow", "Image File Location:", None))
