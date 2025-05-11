from PyQt6 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)

widget = QtWidgets.QWidget()

widget.setWindowTitle('Hello QT6')
widget.resize(400,300)

label = QtWidgets.QLabel(widget)
label.setText('TEST')


widget.show()

sys.exit(app.exec())