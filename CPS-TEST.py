import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtCore import QTimer, Qt

class CPSWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.click_times = []
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_cps)
        self.label = QLabel('CPS: 0.00', self)
        self.label.move(95, 50)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.resize(100, 20)
        self.button = QPushButton('Click me!', self)
        self.button.move(100, 100)
        self.button.clicked.connect(self.on_click)
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('CPS Test')
        self.show()

    def on_click(self):
        if not self.click_times:
            self.timer.start(1000)
        self.click_times.append(time.time())
        self.update_cps()

    def update_cps(self):
        current_time = time.time()
        self.click_times = [t for t in self.click_times if current_time - t < 1]
        cps = len(self.click_times)
        self.label.setText('CPS: {:.2f}'.format(cps))
        if not self.click_times:
            self.timer.stop()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    cps_widget = CPSWidget()
    sys.exit(app.exec_())
