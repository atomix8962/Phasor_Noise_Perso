# Run the GUI
import tkinter as tk
import os
import application.GUI.window as Application

root = tk.Tk()
gui = Application.Window(root)
root.mainloop()
PATH = ["src/tmp/noise_reshape.png", "src/tmp/noise.png", "src/tmp/noise_psd.png", "src/tmp/noise_psd_reshape.png", "src/tmp/noise_hist.png", "src/tmp/noise_hist_reshape.png"]
for p in PATH:
    try: 
        os.remove(p)
    except:
        pass
