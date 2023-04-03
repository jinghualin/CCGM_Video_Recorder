"""GUI based video recorder for CCGM internal usage"""

import sys
from pathlib import Path

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine


def main() -> int:
    app: QGuiApplication = QGuiApplication(sys.argv)
    engine: QQmlApplicationEngine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)

    engine.load("Modules/view/main.qml")
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
