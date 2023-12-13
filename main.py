import sys
from PyQt6.QtWidgets import QDialog, QApplication, QMessageBox, QFileDialog
from layout import *

def isValidPesel(pesel):
    if (len(pesel)!=11): # długość
        return False

    if not pesel.isdigit(): # czy same liczby
        return False

    multiply=[1,3,7,9,1,3,7,9,1,3] # liczba kontrolna
    summ=0
    for i in range(10):
        summ+=(int(pesel[i])*multiply[i])%10
    
    if (int(pesel[10]) != (10-summ%10)%10):
        return False

    return True

class MyForm(QDialog):
    def saveData(self):
        name=self.ui.lineEdit_name.text()
        surname=self.ui.lineEdit_surname.text()
        pesel=self.ui.lineEdit_pesel.text()
        phone=self.ui.lineEdit_phone.text()

        if (isValidPesel(pesel)):
            self.ui.lista.addItem(f"{name} {surname}")
        else:
            QMessageBox.warning(self, "mamo zepsuło sie", "błędny numer pesel :(")
    
    def saveFile(self):
        out=""
        for index in range(self.ui.lista.count()):
            out+=self.ui.lista.itemText(index)+"\n"
            with open('lista.txt', 'w') as file:
                file.write(out)
        
        print(out)

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.save.clicked.connect(self.saveData)
        self.ui.saveFile.clicked.connect(self.saveFile)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyForm()
    sys.exit(app.exec())
