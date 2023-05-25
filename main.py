from PySide6 import QtWidgets, QtCore
import rtmidi   # it's 'python-rtmidi', not 'rtmidi'
import rtmidi.midiutil
import mido
import time
from UI.mi import Ui_Form


class Worker(QtCore.QThread):
    def __init__(self, port):
        super().__init__()
        self.inport = port      # Порт входящего сигнала по стороннему протоколу
    note = QtCore.Signal(str)
    progress = QtCore.Signal(int)
    message = QtCore.Signal(mido.Message)

    def run(self):
        for msg in self.inport:
            print(msg)
            self.note.emit(msg.type)
            self.message.emit(msg)

        for i in range(5):
            time.sleep(1)
            self.progress.emit(i)


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        self.inport = mido.open_input()
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initThreads()
        self.initSignals()
        self.widgetsSetup()

    def initThreads(self) -> None:
        self.thread = Worker(self.inport)

    def widgetsSetup(self):
        self.ui.verticalSlider.setMinimum(0)
        self.ui.verticalSlider.setMaximum(127)
        self.ui.pushButton_4.setCheckable(True)

    def initSignals(self):
        self.ui.pushButton.clicked.connect(self.ShowName)
        self.ui.pushButton.clicked.connect(self.runLongProcess)
        self.ui.pushButton_2.clicked.connect(self.ClearConnection)
        self.ui.pushButton_3.clicked.connect(self.ClearLog)
        self.thread.progress.connect(self.reportProgress)
        self.thread.message.connect(self.printMsg)
        self.thread.message.connect(self.SetSlider)
        self.thread.finished.connect(lambda: self.ui.pushButton.setEnabled(True))

    def ShowName(self):
        try:
            dev_name = self.inport.name
            self.ui.label_2.setText(dev_name)

        except IOError:
            self.ui.label_2.setText('No active connections')

        print(type(self.thread))

    def ClearConnection(self):
        if self.ui.label_2.text != "Device is not defined":
            self.inport.close()
            print(self.inport.closed)
            self.ui.label_2.setText("Device is not defined")
        else:
            pass
        print(type(self.inport))
        self.ui.pushButton.setEnabled(True)

    def runLongProcess(self) -> None:
        """
        Запуск потока обработки входящих MIDI сообщений
        :return: None
        """
        self.ui.pushButton.setEnabled(False)
        self.thread.start()

    def printMsg(self, msg) -> None:
        """
        Приём полного представления сообщения из MIDI потока
        :param msg: Полный текст сообщения для добавления в PlainTextEdit
        :return: None
        """
        self.ui.plainTextEdit.appendPlainText(str(msg))

    def SetSlider(self, msg):
        if msg.type == "control_change":
            self.ui.verticalSlider.setValue(msg.value)
        if msg.type == "note_on":
            self.ui.pushButton_4.setChecked(True)
            self.ui.pushButton_4.setStyleSheet("background-color:rgb(46, 255, 245)")
        if msg.type == "note_off":
            self.ui.pushButton_4.setChecked(False)
            self.ui.pushButton_4.setStyleSheet("background-color:rgb(236, 236, 236)")

    def reportProgress(self, progress):
        print(progress)

    def ClearLog(self):
        self.ui.plainTextEdit.clear()


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
