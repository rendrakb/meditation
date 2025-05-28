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
        self.root = self.interface.root
        
    def init_layout(self):
        self._buttons_frame()
        self._progress_bar_frame()

    def _buttons_frame(self):
        frame = ttk.Frame(self.root)
        frame.pack(pady=10)

        self.interface.start_button = ttk.Button(frame, text="Start")
        self.interface.stop_button = ttk.Button(frame, text="Stop")
        self.interface.pause_button = ttk.Button(frame, text="Pause")

        self.interface.start_button.pack(side="left", padx=5)
        self.interface.stop_button.pack(side="left", padx=5)
        self.interface.pause_button.pack(side="left", padx=5)

    def _progress_bar_frame(self):
        frame = ttk.Frame(self.root)
        frame.pack(pady=10)

        self.interface.progress_bar = ttk.Progressbar(frame, orient="horizontal", length=200, mode="determinate")
        self.interface.progress_bar.pack(pady=10)

def run():
    root = tk.Tk()

    root.title("Meditation")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"400x300+{(screen_width - 400) // 2}+{(screen_height - 300) // 2}")

    app = MeditationInterface(root)

    root.mainloop()

if __name__ == "__main__":
    run()