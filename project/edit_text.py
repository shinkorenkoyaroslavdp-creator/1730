from PyQt6.QtWidgets import QLineEdit
from .widgets import main_frame, main_frame_layout

line_edit = QLineEdit(main_frame)
line_edit.setPlaceholderText("Введіть текст")
main_frame_layout.addWidget(line_edit)




