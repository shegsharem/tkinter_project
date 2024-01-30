import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from ctypes import windll

windll.shcore.SetProcessDpiAwareness(1) # Set high dpi for window

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
        else: self.geometry("1020x640+10+10")

        # Call Toolbar Constructor
        self.toolbar = Toolbar(self)
        self.editor = Editor(self)

class Toolbar(ttk.Frame):
    def __init__(self, master, **kwargs) -> None:
        super().__init__(master, **kwargs)
        window = self.master

        # Toolbar
        toolbar = tk.Menu(window)
        window.configure(menu=toolbar)

        # Bind keyboard shortcuts
        window.bind('<Control-n>',self.new_file)
        window.bind('<Control-o>',self.open_file)

        # File
        filemenu = tk.Menu(toolbar, tearoff='off')
        filemenu.add_command(label="New",accelerator="Ctrl+N", command=self.new_file)
        filemenu.add_command(label="Open", accelerator="Ctrl+O", command=self.open_file)

        toolbar.add_cascade(label="File", menu=filemenu) # Pack filemenu and put in toolbar
    
    def new_file(self, *args) -> None:
        print("New File Request")

    def open_file(self, *args) -> None:
        filename = filedialog.askopenfilename(parent=self)
        if filename != '': return filename

class Editor(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        window = self.master
        open_button = ttk.Button(window, text="Cancel")
        open_button.pack(side='bottom',anchor='se',padx=10,pady=15,ipadx=5, expand=False)
        new_button = ttk.Button(window, text="Save")
        new_button.pack(side='bottom',anchor='se',padx=10,pady=15,ipadx=5,after=open_button,)

        sep = ttk.Separator(window)
        sep.pack(padx=10,pady=10,fill=tk.X,side='right',anchor='center')
        self.pack()



if __name__ == "__main__":
    window = Window(title="Pixel Sprite Editor")
    
    window.mainloop()
