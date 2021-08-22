import Recognize
import DigitalSteno
import sys
import os

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView
from docxtpl import DocxTemplate

app = QApplication(sys.argv)  # Новый экземпляр QApplication


class Converter(QMainWindow, DigitalSteno.Ui_MainWindow):
    time = ""
    agenda = ""
    decided = ""

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn1.clicked.connect(self.uploadMP4)
        self.btn2.clicked.connect(self.unloadTXT)
        self.btn3.clicked.connect(self.addWorld)

    def uploadMP4(self):
        # загрузка ФАЙЛА
        self.file = QtWidgets.QFileDialog.getOpenFileName(self, 'Выберите файл', None, "Video Files (*.mp4)")[0]
        self.text = os.path.basename(str(self.file))
        self.NameFile.setText(self.text)
        self.time = self.text[0] + "" + self.text[1] + "" + self.text[2] + "" + self.text[3] + "" + self.text[4] + "" + \
                    self.text[5] + "" + self.text[6] + "" + self.text[7] + "" + self.text[8] + "" + self.text[9]

        Recognize.mp4_to_waw(self.file)

        blank = Recognize.findtrigger(Recognize.recogn())


        self.ag = blank[0]
        self.dec = blank[1]

        self.plainTextEdit.insertPlainText("СЕГМЕНТ: ПОВЕСТКА ДНЯ\n")
        for i in range(len(self.ag)):
            self.plainTextEdit.insertPlainText(self.ag[i][16:] + "\n")

        self.plainTextEdit.insertPlainText("СЕГМЕНТ: РЕШЕНИЯ\n")
        for i in range(len(self.dec)):
            self.plainTextEdit.insertPlainText(self.dec[i][13:] + "\n")

    def unloadTXT(self):
        # выгружать ФАЙЛ TXT
        self.dirlist = QtWidgets.QFileDialog.getSaveFileName(self, "сохранить файл", '/', '.docx')[0]
        if self.dirlist:
            self.protokol = DocxTemplate("Шаблон.docx")

            self.st_ag = ""
            self.st_dec = ""

            for i in range(len(self.ag)):
                self.st_ag = self.st_ag + str(self.ag[i][16:] + "\n")
            for i in range(len(self.dec)):
                self.st_dec = self.st_dec + str(self.dec[i][13:] + "\n\n")

            print(self.st_ag)
            self.context = {'time': self.time, 'agenda': self.st_ag, 'decided': self.st_dec}
            self.protokol.render(self.context)
            # здесь функция прохода по всем строкам plaintextedit

            self.dirlist = self.dirlist + ".docx"
            self.protokol.save(self.dirlist)

            print(2)

    def fillDoc(self):
        for i in range(self.plainTextEdit.blockCount()):
            print(i)

    def addWorld(self):
        # добавить в словарь
        print(3)
        self.fillDoc()


def main():
    window = Converter()  # Создаём объект класса ExampleApp

    window.showMaximized()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
