from PySide6 import QtWidgets, QtCore
import rtmidi
import rtmidi.midiutil
import mido
from UI.mi import Ui_Form


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initSignals()
        self.inport = None

    def initSignals(self):
        self.ui.pushButton.clicked.connect(self.ShowName)
        self.ui.pushButton.clicked.connect(self.ShowNote)
        self.ui.pushButton_2.clicked.connect(self.ClearConnection)

    def ShowName(self):
        try:
            self.inport = mido.open_input()
            dev_name = self.inport.name
            self.ui.label_2.setText(dev_name)
        except IOError:
            self.ui.label_2.setText('No active connections')


    def ClearConnection(self):
        if self.ui.label_2.text != "Device is not defined":
            self.inport.close()
            self.ui.label_2.setText("Device is not defined")
        else:
            pass

    def ShowNote(self):
        count = 0
        while True:
            if self.inport is not None:
                for msg in self.inport:
                    if msg.type == "note_on":
                        self.ui.label_3.setText(f"{msg.type}")
                    print(msg.type)
            else:
                continue



if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
