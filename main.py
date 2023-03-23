# Run the GUI
import tkinter as tk
import os
import app.application as Application

root = tk.Tk()
gui = Application.GUI(root)
root.mainloop()
PATH = ["tmp/noise_reshape.png", "tmp/noise.png", "tmp/noise_psd.png", "tmp/noise_psd_reshape.png", "tmp/noise_hist.png", "tmp/noise_hist_reshape.png"]
for p in PATH:
    try: 
        os.remove(p)
    except:
        pass
