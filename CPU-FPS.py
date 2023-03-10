import sys
import psutil
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QFont


class FpsWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.fps = QLabel()
        self.fps.setText("FPS: 0.0")
        
        self.font = QFont()
        self.font.setPointSize(18)
        self.fps.setFont(self.font)

        layout = QVBoxLayout()
        layout.addWidget(self.fps)
        self.setLayout(layout)

        # Setup timer to update FPS label every second
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_fps)
        self.timer.start(500) # Set timer to 500 milliseconds

    def update_fps(self):
        # Get current FPS using psutil
        cpu_percent = psutil.cpu_percent()
        num_cores = psutil.cpu_count()
        fps = float(num_cores * (100 - cpu_percent)) # Change to float for Decimal values

        # Update FPS label
        self.fps.setText(f"FPS: {fps}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    fps_widget = FpsWidget()
    fps_widget.show()
    sys.exit(app.exec_())