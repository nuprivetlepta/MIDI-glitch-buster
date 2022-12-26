from PySide6 import QtWidgets, QtCore
import rtmidi
import rtmidi.midiutil
import mido
from UI.mi import Ui_Form

inport = None


class Worker(QtCore.QThread):
    progress = QtCore.Signal(str)


    def run(self):
        count = 0
        while True:
            if inport is not None:
                for msg in inport:
                    if msg.type == "note_on":
                        self.progress.emit(msg.type)

            else:
                continue



class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initSignals()


    def initSignals(self):
        self.ui.pushButton.clicked.connect(self.ShowName)
        # self.ui.pushButton.clicked.connect(self.ShowNote)
        self.ui.pushButton_2.clicked.connect(self.ClearConnection)

    def ShowName(self):
        try:
            inport = mido.open_input()
            dev_name = inport.name
            self.ui.label_2.setText(dev_name)
        except IOError:
            self.ui.label_2.setText('No active connections')


    def ClearConnection(self):
        if self.ui.label_2.text != "Device is not defined":
            inport.close()
            self.ui.label_2.setText("Device is not defined")
        else:
            pass





if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
