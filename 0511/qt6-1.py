from PyQt6 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)

widget = QtWidgets.QWidget()

widget.setWindowTitle('Hello QT6')
widget.resize(400,300)

label = QtWidgets.QLabel(widget)
label.setText('TEST')
label.move(30,30)

label2 = QtWidgets.QLabel(widget)
label2.setText('POIUY')
label2.move(30,50)

input1 = QtWidgets.QLineEdit(widget)
input1.move(60, 30)

text1 = QtWidgets.QTextEdit(widget)
text1.move(100, 100)


widget.show()

sys.exit(app.exec())