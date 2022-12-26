from PySide6 import QtWidgets, QtCore
import rtmidi
import rtmidi.midiutil
import mido
import time
from UI.mi import Ui_Form

inport = mido.open_input()      # Порт входящего сигнала по стороннему протоколу


class Worker(QtCore.QThread):
    note = QtCore.Signal(str)
    progress = QtCore.Signal(int)

    def run(self):
        # for msg in inport:
        #     print(msg)
        #     self.note.emit(msg.type)

        for i in range(5):
            time.sleep(1)
            self.progress.emit(i)


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initSignals()
        self.initThreads()

    def initThreads(self) -> None:
        self.thread = Worker()


    def initSignals(self):
        self.ui.pushButton.clicked.connect(self.ShowName)
        self.ui.pushButton.clicked.connect(self.runLongProcess)
        self.ui.pushButton_2.clicked.connect(self.ClearConnection)
        self.thread.progress.connect(self.reportProgress)
        self.thread.note.connect(self.getNotes)
        self.thread.finished.connect(lambda: self.ui.pushButton.setEnabled(True))

    def ShowName(self):
        try:
            dev_name = inport.name
            self.ui.label_2.setText(dev_name)
        except IOError:
            self.ui.label_2.setText('No active connections')

        print(type(self.thread))

    def ClearConnection(self):
        if self.ui.label_2.text != "Device is not defined":
            inport.close()
            print(inport.closed)
            self.ui.label_2.setText("Device is not defined")
        else:
            pass
        print(type(inport))
        self.ui.pushButton.setEnabled(True)

    def runLongProcess(self) -> None:
        """
        Запуск потока обработки входящих MIDI сообщений
        :return: None
        """
        self.ui.pushButton.setEnabled(False)
        self.thread.start()

    def getNotes(self, note) -> None:
        """
        Приём данных об входящих сигналах MIDI из потока
        :param note: входящий сигнал
        :return: None
        """
        self.ui.label_3.setText(f"Тип ноты: {note}")

    def reportProgress(self, progress):
        print(progress)



if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
