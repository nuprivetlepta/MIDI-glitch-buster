from PySide6 import QtWidgets, QtCore
import mido
from UI.mi import Ui_Form


class Worker(QtCore.QThread):
    """
    Main thread of our application, it's responsible for receiving MIDI notes from devices
    and output them into window.
    """
    def __init__(self, port=None):
        """
        Initialisation of the thread
        :param port: Input port of third party protocol, "None" by default,
        mido.open_input after action in method below.
        """
        super().__init__()
        self.inport = port
        self.is_running = True
    note = QtCore.Signal(str)
    progress = QtCore.Signal(int)
    message = QtCore.Signal(mido.Message)

    def run(self):
        """
        Workflow of our thread, receives messages from port, emits it into application.
        :return: None
        """
        if self.inport is None:
            return None
        else:
            for msg in self.inport:
                print(msg)
                self.note.emit(msg.type)
                self.message.emit(msg)

    def stop(self):
        """
        Method is responsible for stop of messages flow emitting in our app. Can be used infinite amount of times
        with no impact on the thread which can be restarted again.
        :return: None
        """
        self.is_running = False
        self.terminate()


class Window(QtWidgets.QWidget):

    def __init__(self):
        """
        Initialisation of Main Window.
        """
        super().__init__()
        self.thread = None
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initThreads()
        self.initSignals()
        self.widgetsSetup()

    def initThreads(self) -> None:
        """
        Method assigns instance of Worker Class as a thread in app's workflow.
        :return: None
        """
        self.thread = Worker()

    def widgetsSetup(self):
        """
        In MIDI protocol lower and upper limit for each note have values of 0 and 127. That method adapts our UI
        slider from 0-100 to 0-127 for mapping of our notes in visualisation of fader.
        Also, there is a virtual button for visualisation of notes which are emitted by buttons on device.
        :return: None
        """
        self.ui.verticalSlider.setMinimum(0)
        self.ui.verticalSlider.setMaximum(127)
        self.ui.pushButton_4.setCheckable(True)

    def initSignals(self):
        """
        Overall initialisation of signals in application.
        :return: None
        """
        self.ui.pushButton.clicked.connect(self.ShowName)
        self.ui.pushButton.clicked.connect(self.runLongProcess)
        self.ui.pushButton_2.clicked.connect(self.ClearConnection)
        self.ui.pushButton_3.clicked.connect(self.ClearLog)
        self.thread.message.connect(self.printMsg)
        self.thread.message.connect(self.SetSlider)
        self.thread.finished.connect(lambda: self.ui.pushButton.setEnabled(True))

    def ShowName(self):
        """
        Method gets the name of connected device and set it into label. In case when there is no
        connection name will be replaced by "No active connections" string.
        Assigns "inport" of our thread as mido.open_input(), thread is starting to receive signals from device.
        :return: None
        """
        try:
            self.thread.inport = mido.open_input()
            self.ui.label_2.setText(self.thread.inport.name)
        except IOError:
            self.ui.label_2.setText('No active connections')

    def ClearConnection(self):
        """
        Method closes our inport and since then program won't receive signals from device. After that
        it closes thread because it's no longer needed and name of label will tell user that there is no devices.
        When there is no active threads method will pass.
        :return: None
        """
        if self.thread.inport is not None:
            self.thread.inport.close()
            self.ui.label_2.setText("Device is not defined")
        else:
            pass

        self.ui.pushButton.setEnabled(True)
        self.thread.stop()

    def runLongProcess(self) -> None:
        """
        Method starts our thread and process of receiving and handling MIDI messages starts.
        Push button which is responsible for connecting device will be deactivated.
        :return: None
        """
        self.ui.pushButton.setEnabled(False)
        self.thread.start()

    def printMsg(self, msg) -> None:
        """
        Receives full information about note from MIDI message
        :param msg: adds information into PlainTextEdit
        :return: None
        """
        self.ui.plainTextEdit.appendPlainText(str(msg))

    def SetSlider(self, msg):
        """
        Method changes value in our slider in case of signal from fader on device("control_change"),
        otherwise message will be "note_on" and method will affect visualisation of button.
        :param msg: gives information about type of signal and helps app to show user which remote he is testing.
        :return: None
        """
        if msg.type == "control_change":
            self.ui.verticalSlider.setValue(msg.value)
        if msg.type == "note_on":
            self.ui.pushButton_4.setChecked(True)
            self.ui.pushButton_4.setStyleSheet("background-color:rgb(46, 255, 245)")
        if msg.type == "note_off":
            self.ui.pushButton_4.setChecked(False)
            self.ui.pushButton_4.setStyleSheet("background-color:rgb(236, 236, 236)")

    def ClearLog(self):
        """
        Method clears a log of actions added into plainTextEdit.
        :return: None
        """
        self.ui.plainTextEdit.clear()


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
