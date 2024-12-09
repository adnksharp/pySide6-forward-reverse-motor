import sys
from pymata4 import pymata4 as arduino

from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

class Board():
    def __init__(self, *motor):
        self.board = arduino.Pymata4()
        self.motor = motor
        for pin in motor:
            self.board.set_pin_mode_pwm_output(pin)

class Widget(QWidget):
    def __init__(self, parent=None):
        self.status = False
        
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        
        self.ui.pwmSlider.valueChanged.connect(self.updateSpin)
        self.ui.pwmSpin.valueChanged.connect(self.updateSlider)
        self.ui.drive.clicked.connect(self.run)
        self.ui.reverse.clicked.connect(self.reverse)
        self.ui.stop.clicked.connect(self.stop)
        
    def updateSpin(self):
        self.ui.pwmSpin.setValue(self.ui.pwmSlider.value())
        
    def updateSlider(self):
        self.ui.pwmSlider.setValue(self.ui.pwmSpin.value())
        
    def run(self):
        if not self.status:
            self.status = True
            self.ui.lcdNumber.display(round((self.ui.pwmSlider.value() * 0.12), 2))
            
    def reverse(self):
        if not self.status:
            self.status = True
            self.ui.lcdNumber.display(round(-(self.ui.pwmSlider.value() * 0.12), 2))
            
    def stop(self):
        self.status = False
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
