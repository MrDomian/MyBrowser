import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView


class Browser(QWidget):
    def __init__(self):
        super().__init__()
        icon = QIcon("icon.png")
        self.setWindowIcon(icon)

        self.setWindowTitle("MyBrowser4Fun")
        self.setGeometry(50, 50, 1600, 900)

        self.webview = QWebEngineView()
        self.webview.load(QUrl("https://www.google.com/"))

        self.address_bar = QLineEdit()
        self.address_bar.returnPressed.connect(self.browse)

        self.browse_btn = QPushButton("Search")
        self.browse_btn.clicked.connect(self.browse)

        self.back_btn = QPushButton("<")
        self.back_btn.clicked.connect(self.webview.back)

        self.forward_btn = QPushButton(">")
        self.forward_btn.clicked.connect(self.webview.forward)

        self.reload_btn = QPushButton("Refresh")
        self.reload_btn.clicked.connect(self.webview.reload)

        address_layout = QHBoxLayout()
        address_layout.addWidget(self.back_btn)
        address_layout.addWidget(self.forward_btn)
        address_layout.addWidget(self.reload_btn)
        address_layout.addWidget(self.address_bar)
        address_layout.addWidget(self.browse_btn)

        layout = QVBoxLayout()
        layout.addLayout(address_layout)
        layout.addWidget(self.webview)

        self.setLayout(layout)

    def browse(self):
        url = QUrl(self.address_bar.text())
        self.webview.load(url)


app = QApplication(sys.argv)
browser = Browser()
browser.show()
sys.exit(app.exec_())

