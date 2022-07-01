import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets, QtGui
import design  # Это наш конвертированный файл дизайна
from pathlib import Path

class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

        self.setWindowIcon(QtGui.QIcon('icon.ico'))
        self.Button1.clicked.connect(self.pushButton1)
        self.Button2.clicked.connect(self.pushButton2)

        self.lineEdit.setStyleSheet("color: blue")
        self.lineEdit_2.setStyleSheet("color: blue")
        self.lineEdit_3.setStyleSheet("color: blue")
        self.lineEdit_4.setStyleSheet("color: blue")
        self.lineEdit_5.setStyleSheet("color: blue")
        self.lineEdit_6.setStyleSheet("color: blue")
        self.lineEdit_7.setStyleSheet("color: blue")
        self.lineEdit_8.setStyleSheet("color: blue")
        self.lineEdit_9.setStyleSheet("color: blue")
        self.lineEdit_10.setStyleSheet("color: blue")
        self.lineEdit_11.setStyleSheet("color: blue")
        self.lineEdit_13.setStyleSheet("color: blue")

        self.lineEdit.setText(str(0.001))
        self.lineEdit_2.setText(str(0.01))
        self.lineEdit_3.setText(str(0.002))
        self.lineEdit_4.setText(str(0.1))
        self.lineEdit_5.setText(str(0.0))
        self.lineEdit_6.setText(str(0.1))
        self.lineEdit_7.setText(str(0.0))
        self.lineEdit_8.setText(str(0.0))
        self.lineEdit_9.setText(str(0.0021))
        self.lineEdit_10.setText(str(0.1))
        self.lineEdit_11.setText(str(5))
        self.lineEdit_13.setText(str(0.009))

        self.lineEdit_17.setStyleSheet("color: blue")
        self.lineEdit_18.setStyleSheet("color: blue")
        self.lineEdit_19.setStyleSheet("color: blue")
        self.lineEdit_14.setStyleSheet("color: blue")
        self.lineEdit_15.setStyleSheet("color: blue")
        self.lineEdit_16.setStyleSheet("color: blue")
        self.lineEdit_20.setStyleSheet("color: blue")

        self.lineEdit_17.setText(str(10.00))
        self.lineEdit_18.setText(str(9.00))
        self.lineEdit_19.setText(str(0.5))
        self.lineEdit_14.setText(str(0.1))
        self.lineEdit_15.setText(str(0.5))
        self.lineEdit_16.setText(str(0.30))
        self.lineEdit_20.setText(str(8.00))

        home = str(Path.home())
        desktop = str("\Desktop")
        file = str("\dataMethod1.dat")
        file1 = str("\dataMethod2.dat")
        path = home + desktop + file
        path1 = home + desktop + file1
        f = open(path, 'a')
        g = open(path1, 'a')
        f.write(('\n' "pH" '\t' "(H+solid),eq/kg"))
        g.write('\n' "pH" '\t' "(OH-)consumed by reference,cmol/kg" '\t' "(OH-)consumed by sample,cmol/kg" '\t' "Surface charge, cmol/kg")


    def pushButton1(self):
        a = float(self.lineEdit.text())
        Vtot = float(self.lineEdit_2.text())
        Vback = float(self.lineEdit_13.text())
        VA = float(self.lineEdit_3.text())
        CA = float(self.lineEdit_4.text())
        VB = float(self.lineEdit_5.text())
        CB = float(self.lineEdit_6.text())
        VBTA = float(self.lineEdit_7.text())
        CBTA = float(self.lineEdit_8.text())
        VBTB = float(self.lineEdit_9.text())
        CBTB = float(self.lineEdit_10.text())
        pH = float(self.lineEdit_11.text())
        amH = 0.1e1 / a * (VA * CA - VB * CB + (VBTA * CBTA - VBTB * CBTB) * Vtot / Vback)
        aH = "%0.6f" %amH
        self.lineEdit_12.setText(str(aH))
        home = str(Path.home())
        desktop = str("\Desktop")
        file = str("\dataMethod1.dat")
        path = home + desktop + file
        f = open(path, 'a')
        f.write('\n' + str(pH) + '\t' + str(aH))

    def pushButton2(self):
        Vo = float(self.lineEdit_17.text())
        Vsn = float(self.lineEdit_18.text())
        Wsoil = float(self.lineEdit_19.text())
        N = float(self.lineEdit_14.text())
        Vsample = float(self.lineEdit_15.text())
        Vreference = float(self.lineEdit_16.text())
        pH1 = float(self.lineEdit_20.text())
        qsample = 100*(N*Vsample/Wsoil)
        qreference = 100*(N*Vreference/Wsoil)*(Vo/Vsn)
        qsurface = qsample-qreference
        qsam = "%0.6f" %qsample
        qref = "%0.6f" %qreference
        qsur = "%0.6f" %qsurface
        self.lineEdit_21.setText(str(qsam))
        self.lineEdit_22.setText(str(qref))
        self.lineEdit_23.setText(str(qsur))
        home = str(Path.home())
        desktop = str("\Desktop")
        file1 = str("\dataMethod2.dat")
        path1 = home + desktop + file1
        g = open(path1, 'a')
        g.write('\n' + str(pH1) + '\t' + str(qsam) + '\t' + str(qref) + '\t' + str(qsur))







def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':
    main()