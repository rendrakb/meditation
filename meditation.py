import sys
import time

try:
    import tkinter as tk
    from tkinter import ttk

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
    time_slider: ttk.Scale
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
        self._time_slider_frame()
        self._progress_bar_frame()

    def _buttons_frame(self):
        frame = ttk.Frame(self.root)
        frame.pack(pady=2)

        self.interface.start_button = ttk.Button(frame, text="Start")
        self.interface.stop_button = ttk.Button(frame, text="Stop")
        self.interface.pause_button = ttk.Button(frame, text="Pause")

        self.interface.start_button.pack(side="left", padx=1)
        self.interface.stop_button.pack(side="left", padx=1)
        self.interface.pause_button.pack(side="left", padx=1)

    def _time_slider_frame(self):
        frame = ttk.Frame(self.root)
        frame.pack(pady=2)

        self.interface.time_label = ttk.Label(frame, text="Time: 1 min")
        self.interface.time_label.pack(pady=2)

        self.interface.time_slider = ttk.Scale(frame, from_=1, to=30, orient="horizontal", length=225, command=self._update_time_label)
        self.interface.time_slider.pack(pady=2)

    def _update_time_label(self, value):
        self.interface.time_label.config(text=f"Time: {int(float(value))} min")

    def _progress_bar_frame(self):
        frame = ttk.Frame(self.root)
        frame.pack(pady=2)

        self.interface.progress_bar = ttk.Progressbar(frame, orient="horizontal", length=225, mode="determinate")
        self.interface.progress_bar.pack(pady=2)

def run():
    root = tk.Tk()

    root.title("Meditation")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"300x125+{(screen_width - 300) // 2}+{(screen_height - 125) // 2}")

    app = MeditationInterface(root)

    root.mainloop()

if __name__ == "__main__":
    run()