# This Python file uses the following encoding: utf-8
from PySide6 import QtCore
from PySide6 import QtQuick
from Pyside6 import QtDeclarative


class windowConnect(QtQuick.QQuickItem):
    def __init__(self):
        pass

    @QtCore.SLOT(str)
    def outputStr(self, s):
        print(s)
