# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'asn8.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_root(object):
    def setupUi(self, root):
        if not root.objectName():
            root.setObjectName(u"root")
        root.resize(500, 300)
        root.setBaseSize(QSize(0, 0))
        self.centralwidget = QWidget(root)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lblFrPerson = QGroupBox(self.centralwidget)
        self.lblFrPerson.setObjectName(u"lblFrPerson")
        self.gridLayout = QGridLayout(self.lblFrPerson)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lblFirst = QLabel(self.lblFrPerson)
        self.lblFirst.setObjectName(u"lblFirst")
        self.lblFirst.setAutoFillBackground(False)
        self.lblFirst.setStyleSheet(u"background-color: blue;\n"
" color: white;")

        self.gridLayout.addWidget(self.lblFirst, 0, 0, 1, 1)

        self.entFirst = QLineEdit(self.lblFrPerson)
        self.entFirst.setObjectName(u"entFirst")

        self.gridLayout.addWidget(self.entFirst, 0, 1, 1, 1)

        self.lblLast = QLabel(self.lblFrPerson)
        self.lblLast.setObjectName(u"lblLast")
        self.lblLast.setAutoFillBackground(False)
        self.lblLast.setStyleSheet(u"background-color: blue;\n"
" color: white;")

        self.gridLayout.addWidget(self.lblLast, 1, 0, 1, 1)

        self.entLast = QLineEdit(self.lblFrPerson)
        self.entLast.setObjectName(u"entLast")

        self.gridLayout.addWidget(self.entLast, 1, 1, 1, 1)

        self.lblEmail = QLabel(self.lblFrPerson)
        self.lblEmail.setObjectName(u"lblEmail")

        self.gridLayout.addWidget(self.lblEmail, 2, 0, 1, 1)

        self.entEmail = QLineEdit(self.lblFrPerson)
        self.entEmail.setObjectName(u"entEmail")

        self.gridLayout.addWidget(self.entEmail, 2, 1, 1, 1)

        self.lblPhone = QLabel(self.lblFrPerson)
        self.lblPhone.setObjectName(u"lblPhone")

        self.gridLayout.addWidget(self.lblPhone, 3, 0, 1, 1)

        self.entPhone = QLineEdit(self.lblFrPerson)
        self.entPhone.setObjectName(u"entPhone")

        self.gridLayout.addWidget(self.entPhone, 3, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.lblFrPerson)

        self.fraButtons = QFrame(self.centralwidget)
        self.fraButtons.setObjectName(u"fraButtons")
        self.fraButtons.setFrameShape(QFrame.Shape.StyledPanel)
        self.fraButtons.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.fraButtons)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnS = QPushButton(self.fraButtons)
        self.btnS.setObjectName(u"btnS")
        self.btnS.setMinimumSize(QSize(80, 0))
        self.btnS.setBaseSize(QSize(80, 0))

        self.horizontalLayout.addWidget(self.btnS)

        self.btnR = QPushButton(self.fraButtons)
        self.btnR.setObjectName(u"btnR")
        self.btnR.setMinimumSize(QSize(80, 0))
        self.btnR.setBaseSize(QSize(80, 0))

        self.horizontalLayout.addWidget(self.btnR)

        self.btnQ = QPushButton(self.fraButtons)
        self.btnQ.setObjectName(u"btnQ")
        self.btnQ.setMinimumSize(QSize(80, 0))
        self.btnQ.setBaseSize(QSize(80, 0))

        self.horizontalLayout.addWidget(self.btnQ)


        self.verticalLayout_2.addWidget(self.fraButtons)

        root.setCentralWidget(self.centralwidget)

        self.retranslateUi(root)

        QMetaObject.connectSlotsByName(root)
    # setupUi

    def retranslateUi(self, root):
        root.setWindowTitle(QCoreApplication.translate("root", u"Form", None))
        self.lblFrPerson.setTitle(QCoreApplication.translate("root", u"Personal Information", None))
        self.lblFirst.setText(QCoreApplication.translate("root", u"*First Name:", None))
        self.lblLast.setText(QCoreApplication.translate("root", u"*Last Name:", None))
        self.lblEmail.setText(QCoreApplication.translate("root", u"Email:", None))
        self.lblPhone.setText(QCoreApplication.translate("root", u"Phone:", None))
        self.btnS.setText(QCoreApplication.translate("root", u"Submit", None))
        self.btnR.setText(QCoreApplication.translate("root", u"Reset", None))
        self.btnQ.setText(QCoreApplication.translate("root", u"Quit", None))
    # retranslateUi

