from PyQt6.QtWidgets import QComboBox
from .widgets import main_frame, main_frame_layout

combo_box = QComboBox(parent=main_frame)
combo_box.addItems(["Option 1"])
combo_box.addItems(["Option 2"])
combo_box.addItems(["Option 3"])
combo_box.addItems(["Option 4"])
combo_box.addItems(["Option 5"])