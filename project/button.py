from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QFont
from .window import main_window
from .widgets import main_frame, main_frame_layout

font = QFont("Arial, 20")
button = QPushButton(main_frame, text = "press")
button.setFont(font)
main_frame_layout.addWidget(button)