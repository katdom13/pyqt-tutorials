# Form implementation generated from reading ui file 'employee.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(616, 472)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.dateEdit = QtWidgets.QDateEdit(parent=Dialog)
        self.dateEdit.setObjectName("dateEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.dateEdit)
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.comboBox = QtWidgets.QComboBox(parent=Dialog)
        self.comboBox.setObjectName("comboBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.comboBox)
        self.label_4 = QtWidgets.QLabel(parent=Dialog)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.comboBox_2 = QtWidgets.QComboBox(parent=Dialog)
        self.comboBox_2.setObjectName("comboBox_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.comboBox_2)
        self.label_5 = QtWidgets.QLabel(parent=Dialog)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_5)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(parent=Dialog)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.doubleSpinBox)
        self.label_6 = QtWidgets.QLabel(parent=Dialog)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_6)
        self.textEdit = QtWidgets.QTextEdit(parent=Dialog)
        self.textEdit.setObjectName("textEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textEdit)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok|QtWidgets.QDialogButtonBox.StandardButton.Reset)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.label.setBuddy(self.lineEdit)
        self.label_2.setBuddy(self.dateEdit)
        self.label_3.setBuddy(self.comboBox)
        self.label_4.setBuddy(self.comboBox_2)
        self.label_5.setBuddy(self.doubleSpinBox)
        self.label_6.setBuddy(self.textEdit)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        self.buttonBox.clicked['QAbstractButton*'].connect(self.lineEdit.clear) # type: ignore
        self.buttonBox.clicked['QAbstractButton*'].connect(self.dateEdit.clear) # type: ignore
        self.buttonBox.clicked['QAbstractButton*'].connect(self.comboBox.clear) # type: ignore
        self.buttonBox.clicked['QAbstractButton*'].connect(self.comboBox_2.clear) # type: ignore
        self.buttonBox.clicked['QAbstractButton*'].connect(self.doubleSpinBox.clear) # type: ignore
        self.buttonBox.clicked['QAbstractButton*'].connect(self.textEdit.clear) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.lineEdit, self.dateEdit)
        Dialog.setTabOrder(self.dateEdit, self.comboBox)
        Dialog.setTabOrder(self.comboBox, self.comboBox_2)
        Dialog.setTabOrder(self.comboBox_2, self.doubleSpinBox)
        Dialog.setTabOrder(self.doubleSpinBox, self.textEdit)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Employee &name"))
        self.label_2.setText(_translate("Dialog", "&Employment date"))
        self.label_3.setText(_translate("Dialog", "&Department"))
        self.label_4.setText(_translate("Dialog", "&Postition"))
        self.label_5.setText(_translate("Dialog", "Annual &salary"))
        self.label_6.setText(_translate("Dialog", "&Job description"))
