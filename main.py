import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtQuick import QQuickView
import res

if __name__ == "__main__":
    app = QApplication()
    view = QQuickView()
    view.setSource("view.qml")
    view.show()
    view.resize(400, 300)
    sys.exit(app.exec())
