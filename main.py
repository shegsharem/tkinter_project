import tkinter as tk
from ctypes import windll

windll.shcore.SetProcessDpiAwareness(1) # Set high dpi for window

def yeth():
        print("YYE")

class Window(tk.Tk):
    def __init__(self, title:str=None, size:str=None) -> None:
        """Create window instance

        :param title: `window title`, defaults to None
        :type title: str, optional
        :param size: ``"width x height + pos_x + pos_y"``, defaults to None
        :type size: str, optional
        """
        super().__init__()
        if title: self.title(title)
        if size: self.geometry(size)
        else: self.geometry("640x390+10+10")

        # Call Toolbar Constructor
        self.toolbar = Toolbar()

        # Bind keyboard shortcuts
        self.bind('<Control-n>',yeth)
    
    

class Toolbar(tk.Frame):
    def __init__(self) -> None:
        super().__init__()
        self.UI() # Process UI
    
    def UI(self) -> None:
        self.master.title("Menu")
        toolbar = tk.Menu(self.master)
        self.master.configure(menu=toolbar)

        filemenu = tk.Menu(toolbar, tearoff='off') # Add new button to toolbar
        filemenu.add_command(label="New",accelerator="Ctrl+N", command=None)
        filemenu.add_command(label="Open", accelerator="Ctrl+O", command=None)

        toolbar.add_cascade(label="File", menu=filemenu) # Pack filemenu and put in toolbar

if __name__ == "__main__":
    window = Window()
    window.mainloop()
