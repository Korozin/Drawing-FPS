import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QFont


class FPSLabel(QLabel):
    def __init__(self, parent=None):
        super(FPSLabel, self).__init__(parent)
        self.start_time = time.time()
        self.frames = 0
        self.fps = 0
        self.alpha = 0.2  # Smoothing factor
        
        # Set font size
        self.font = QFont()
        self.font.setPointSize(18)
        self.setFont(self.font)        
        
        self.setText("FPS: 0.0")

    def update_fps(self):
        self.frames += 1
        elapsed_time = time.time() - self.start_time
        if elapsed_time > 1.0:
            self.fps = (1 - self.alpha) * self.fps + self.alpha * (self.frames / elapsed_time)
            self.setText(f"FPS: {self.fps:.1f}")
            self.start_time = time.time()
            self.frames = 0
        else:
            self.fps = (1 - self.alpha) * self.fps + self.alpha * (self.frames / elapsed_time)
            self.setText(f"FPS: {self.fps:.1f}")


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        fps_label = FPSLabel()
        layout.addWidget(fps_label)
        self.setLayout(layout)
        self.setWindowTitle('FPS Counter')

        # start timer for 15 milliseconds
        self.timer = self.startTimer(15) # Value is directly correlated to FPS (EX: Lower = Higher FPS)
        self.show()

    def timerEvent(self, event):
        if event.timerId() == self.timer:
            self.findChild(FPSLabel).update_fps()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())