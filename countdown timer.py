import tkinter as tk

class OverlayCountdown:
    def __init__(self, duration=45):
        self.duration = duration
        self.remaining = duration
        self.running = False

        self.root = tk.Tk()
        self.root.geometry("200x80+100+100")
        self.root.overrideredirect(True)
        self.root.wm_attributes("-topmost", True)
        self.root.wm_attributes("-transparentcolor", "white")
        self.root.configure(bg="white")

        self.label = tk.Label(self.root, text="", font=("Consolas", 32), fg="black", bg="white")
        self.label.pack(expand=True)

        self.root.bind("<space>", self.toggle_timer)
        self.update_display()

    def update_display(self):
        mins, secs = divmod(self.remaining, 60)
        time_str = f"{mins:02}:{secs:02}"
        self.label.config(text=time_str)

        if self.remaining <= 10:
            self.label.config(fg="red")
        else:
            self.label.config(fg="black")

        if self.running and self.remaining > 0:
            self.remaining -= 1
            self.root.after(1000, self.update_display)
        elif self.remaining == 0:
            self.running = False

    def toggle_timer(self, event=None):
        if not self.running:
            self.remaining = self.duration
            self.running = True
            self.update_display()

    def launch(self):
        self.root.mainloop()


if __name__ == "__main__":
    timer = OverlayCountdown(duration=45)
    timer.launch()
