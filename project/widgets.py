from PyQt6.QtWidgets import QWidget, QVBoxLayout, QFrame, QLabel
from .window import main_window

main_frame = QFrame(parent= main_window)
main_frame.setFixedSize(400, 500)

main_frame.setStyleSheet("background-color:gray")

main_frame_layout = QVBoxLayout()
main_frame.setLayout(main_frame_layout)






