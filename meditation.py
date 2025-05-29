import sys

try:
    import tkinter as tk
    from tkinter import ttk

except (ModuleNotFoundError, ImportError):
    print(
        "Your Python environment does not have the required libraries installed."
    )
    sys.exit(0)

class MeditationInterface:
    start_button: ttk.Button
    stop_button: ttk.Button
    pause_button: ttk.Button
    time_slider: ttk.Scale
    progress_bar: ttk.Progressbar
    breathing_bar: ttk.Progressbar
    breathing_label: ttk.Label

    def __init__ (self, root: tk.Tk):
        self.root = root
        
        self.layout = LayoutManager(self)
        self.layout.init_layout()

        self.start_button.config(command=self.start_timer)
        self.stop_button.config(command=self.stop_timer)
        self.pause_button.config(command=self.pause_timer)
        self.timer_running = False

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.run_timer()
            self.run_breathing()

    def stop_timer(self):
        self.timer_running = False
        self.progress_bar["value"] = 0
        self.breathing_bar["value"] = 0
        self.breathing_label.config(text="Ready")

    def pause_timer(self):
        self.timer_running = False
        self.breathing_bar["value"] = 0
        self.breathing_label.config(text="Ready")

    def run_timer(self):
        if self.timer_running:
            current_time = int(float(self.time_slider.get()))
            self.progress_bar["maximum"] = current_time * 60
            self.progress_bar["value"] += 1

            if self.progress_bar["value"] < self.progress_bar["maximum"]:
                self.root.after(1000, self.run_timer)

    def run_breathing(self):
        if self.timer_running:
            self.breathing_bar["value"] = 0
            self.breathing_bar["maximum"] = 100
            self.breathing_label.config(text="Inhale")

            def update_progress(phase, duration):
                steps = 100
                interval = duration // steps
                
                def step_progress(value=0):
                    if self.timer_running and value <= 100:
                        self.breathing_bar["value"] = value
                        self.root.after(interval, step_progress, value + 1)
                    else:
                        next_phase()
                
                step_progress()

            def next_phase():
                if self.timer_running:
                    if self.breathing_label["text"] == "Inhale":
                        self.breathing_label.config(text="Hold")
                        update_progress("Hold", 4000)
                    elif self.breathing_label["text"] == "Hold":
                        self.breathing_label.config(text="Exhale")
                        update_progress("Exhale", 8000)
                    else:
                        self.breathing_label.config(text="Inhale")
                        self.root.after(0, self.run_breathing)

            update_progress("Inhale", 4000)

class LayoutManager:
    def __init__(self, interface: MeditationInterface):
        self.interface = interface
        self.root = self.interface.root
        
    def init_layout(self):
        self._buttons_frame()
        self._time_slider_frame()
        self._progress_bar_frame()
        self._breathing_bar_frame()

    def _buttons_frame(self):
        frame = ttk.Frame(self.root)
        frame.pack(pady=1)

        self.interface.start_button = ttk.Button(frame, text="Start")
        self.interface.pause_button = ttk.Button(frame, text="Pause")
        self.interface.stop_button = ttk.Button(frame, text="Stop")

        self.interface.start_button.pack(side="left", padx=1)
        self.interface.pause_button.pack(side="left", padx=1)
        self.interface.stop_button.pack(side="left", padx=1)

    def _time_slider_frame(self):
        frame = ttk.Frame(self.root)
        frame.pack(pady=1)

        self.interface.time_label = ttk.Label(frame, text="Time: 0 min")
        self.interface.time_label.pack(pady=1)

        self.interface.time_slider = ttk.Scale(frame, from_=0, to=30, orient="horizontal", length=225, command=self._update_time_label)
        self.interface.time_slider.pack(pady=1)

    def _update_time_label(self, value):
        self.interface.time_label.config(text=f"Time: {int(float(value))} min")

    def _progress_bar_frame(self):
        frame = ttk.Frame(self.root)
        frame.pack(pady=1)

        self.interface.progress_bar = ttk.Progressbar(frame, orient="horizontal", length=225, mode="determinate")
        self.interface.progress_bar.pack(pady=1)

    def _breathing_bar_frame(self):
        frame = ttk.Frame(self.root)
        frame.pack(pady=1)

        self.interface.breathing_label = ttk.Label(frame, text="Ready")
        self.interface.breathing_label.pack(pady=1)

        self.interface.breathing_bar = ttk.Progressbar(frame, orient="horizontal", length=225, mode="determinate")
        self.interface.breathing_bar.pack(pady=1)

def run():
    root = tk.Tk()

    root.title("Meditation")
    root.resizable(False, False)
    root.attributes("-topmost", True)

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"275x175+{(screen_width - 275) // 2}+{(screen_height - 175) // 2}")

    app = MeditationInterface(root)

    root.mainloop()

if __name__ == "__main__":
    run()