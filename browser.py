import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QWidget

class Browser(QWidget):
    def __init__(self):
        super().__init__()
        self.web_view = QWebEngineView()
        self.line_edit = QLineEdit()
        self.back_button = QPushButton("Back")
        self.forward_button = QPushButton("Forward")

        self.init_ui()

    def init_ui(self):
        h_layout = QHBoxLayout()
        h_layout.addWidget(self.back_button)
        h_layout.addWidget(self.forward_button)
        h_layout.addWidget(self.line_edit)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(self.web_view)

        self.setLayout(v_layout)

        self.back_button.clicked.connect(self.web_view.back)
        self.forward_button.clicked.connect(self.web_view.forward)
        self.line_edit.returnPressed.connect(self.load_url)

        self.show()

    def load_url(self):
        url = QUrl(self.line_edit.text())
        self.web_view.load(url)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    browser = Browser()
    sys.exit(app.exec_())
