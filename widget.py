import sys
from pymata4 import pymata4 as arduino

from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

M1 = 2
M2 = 3

class Board():
    def __init__(self, *motor):
        self.board = arduino.Pymata4()
        self.motor = motor
        for pin in motor:
            self.board.set_pin_mode_pwm_output(pin)

class Widget(QWidget):
    def __init__(self, parent=None):
        self.status = False
        self.mode = True
        
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        
        self.ui.pwmSlider.valueChanged.connect(self.updateSpin)
        self.ui.pwmSpin.valueChanged.connect(self.updateSlider)
        self.ui.drive.clicked.connect(lambda x: self.run(0))
        self.ui.reverse.clicked.connect(lambda x: self.run(1))
        self.ui.stop.clicked.connect(self.stop)
        
        self.ino = Board(M1, M2)
        
    def updatePWM(self, mode = 0):
        if mode == 1:
            self.ui.pwmSpin.setValue(self.ui.pwmSlider.value())
        elif mode == 2:
            self.ui.pwmSlider.setValue(self.ui.pwmSpin.value())
        if self.status:
            if self.mode:
                self.ui.lcdNumber.display(round((self.ui.pwmSlider.value() * 0.12), 2))
                self.ino.board.pwm_write(self.ino.motor[0], 0)
                self.ino.board.pwm_write(self.ino.motor[1], int(self.ui.pwmSlider.value() * 2.55))
            else:
                self.ui.lcdNumber.display(round(-(self.ui.pwmSlider.value() * 0.12), 2))
                self.ino.board.pwm_write(self.ino.motor[1], 0)
                self.ino.board.pwm_write(self.ino.motor[0], int(self.ui.pwmSlider.value() * 2.55))
        
    def updateSpin(self):
        self.updatePWM(1)
        
    def updateSlider(self):
        self.updatePWM(2)
        
    def run(self, by):
        if not self.status:
            self.status = True
            self.mode = by == 0
            self.updatePWM()
            
    def stop(self):
        self.status = False
        for i in self.ino.motor:
            self.ino.board.pwm_write(i, 0)
            
    def closeEvent(self, event):
        self.ino.board.shutdown()
        event.accept()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
