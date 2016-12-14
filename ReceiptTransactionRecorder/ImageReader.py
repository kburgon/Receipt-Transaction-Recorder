#! /bin/env python

""" Kevin Burgon -- 12/07/2016
    Last Edit 12/12/2016

    This module creates the main window for the receipt transaction recorder
    and handles UI events as the central object of the application.  This file
    serves as the executable for the project.
"""

import sys
from PyQt4 import QtCore, QtGui
from ImageReaderGui import Ui_MainWindow
import TextExtraction
import ChargeFilter

class ApplicationWindow(QtGui.QMainWindow):
    """ Main window of application. """
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.imageScene = QtGui.QGraphicsScene()
        QtCore.QObject.connect(self.ui.readImageButton, QtCore.SIGNAL("clicked()"), self.readImageButtonClicked)

    def readImageButtonClicked(self):
        openFileDialog = QtGui.QFileDialog(self)
        filePath = openFileDialog.getOpenFileName()
        from os.path import isfile
        if isfile(filePath):
            print('Get filepath')
            self.ui.filePathInput.setText(filePath)
            extractedText = TextExtraction.extractText(filePath)
            self.displayImageText(extractedText)
            self.displayFilteredText(extractedText)
            newImage = QtGui.QPixmap(filePath).scaled(QtCore.QSize(511, 581), QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
            self.displayImage(newImage)

    def displayImageText(self, extractedText):
        self.ui.outputTextView.setPlainText('Loading...')
        self.ui.outputTextView.setPlainText(extractedText)

    def displayFilteredText(self, extractedText):
        self.ui.matchedTextView.setPlainText('Loading...')
        self.ui.matchedTextView.setPlainText(str(ChargeFilter.findCharges(extractedText)))

    def displayImage(self, currentImage):
        self.imageScene.clear()
        self.imageScene.addPixmap(currentImage)
        self.ui.inputImageView.setScene(self.imageScene)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    readerWindow = ApplicationWindow()
    readerWindow.show()
    sys.exit(app.exec_())
