from PyQt5 import QtWidgets
import sys
from MainPage import MainPage


if __name__ == "__main__":
    """To start the person tracking application."""

    app = QtWidgets.QApplication(sys.argv)
    main_page = MainPage()

    main_page.show()
    sys.exit(app.exec_())
