import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QAction, QMessageBox
)
from PyQt5.QtCore import QTimer, QDateTime, Qt
from PyQt5.QtGui import QIcon


class PyClock(QMainWindow):
    def __init__(self):
        super().__init__()

        self.use_24h = True
        self.dark_mode = True

        self.init_ui()
        self.init_timer()

    def init_ui(self):
        self.setWindowTitle("PyClock")
        self.setWindowIcon(QIcon("pyclock.png"))  # app logo
        self.resize(300, 150)

        self.label = QLabel(alignment=Qt.AlignCenter)
        self.setCentralWidget(self.label)

        self.apply_theme()
        self.create_menu()
        self.update_time()

    def init_timer(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

    def time_format(self):
        return "HH:mm:ss" if self.use_24h else "hh:mm:ss AP"

    def update_time(self):
        now = QDateTime.currentDateTime()
        self.label.setText(now.toString(self.time_format()))

    def apply_theme(self):
        if self.dark_mode:
            self.setStyleSheet("""
                QMainWindow { background: #121212; }
                QLabel {
                    color: #ffffff;
                    font-size: 40px;
                    font-weight: bold;
                }
            """)
        else:
            self.setStyleSheet("""
                QMainWindow { background: #ffffff; }
                QLabel {
                    color: #000000;
                    font-size: 40px;
                    font-weight: bold;
                }
            """)

    def toggle_time_format(self):
        self.use_24h = not self.use_24h
        self.update_time()

    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
        self.apply_theme()

    def create_menu(self):
        menubar = self.menuBar()

        options = menubar.addMenu("Options")

        format_action = QAction("Toggle 12/24 Hour", self)
        format_action.triggered.connect(self.toggle_time_format)
        options.addAction(format_action)

        theme_action = QAction("Toggle Dark/Light Mode", self)
        theme_action.triggered.connect(self.toggle_theme)
        options.addAction(theme_action)

        about_menu = menubar.addMenu("About")
        about_action = QAction("About PyClock", self)
        about_action.triggered.connect(self.show_about)
        about_menu.addAction(about_action)

    def show_about(self):
        QMessageBox.information(
            self,
            "About PyClock",
            "PyClock Version 2\n"
            "Made by NEOX\n"
            "Compatible with all UNIX, NT, and Apple Silicon systems"
        )


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("PyClock")
    window = PyClock()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
