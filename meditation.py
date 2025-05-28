import sys
import time

try:
    import tkinter as tk
    from tkinter import ttk, font, messagebox

except (ModuleNotFoundError, ImportError):
    print(
        "Your Python environment does not have the required libraries installed."
    )
    sys.exit(0)

__version__ = "0.0.1"

class MeditationInterface:
    start_button: ttk.Button
    stop_button: ttk.Button
    pause_button: ttk.Button
    time_button: ttk.Button
    progress_bar: ttk.Progressbar

    def __init__ (self, root: tk.Tk):
        self.root = root
        
        self.layout = LayoutManager(self)
        self.layout.init_layout()

class LayoutManager:
    def __init__(self, interface: MeditationInterface):
        self.interface = interface
        
    def init_layout(self):
        self._header_frame()
        self._buttons_frame()
        self._progress_bar_frame()

    