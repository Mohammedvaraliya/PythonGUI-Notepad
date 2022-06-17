from tkinter import *
from tkinter import font
from tkinter.messagebox import CANCEL, askyesno, showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import askyesnocancel
import os
import sys
from datetime import *

if __name__ == '__main__':
    root = Tk()
    root.geometry("744x500+800+200")
    root.title("*Untitled - Notepad By Varaliya")
    root.wm_iconbitmap("Notepad.ico")
    # root.config(color="white")

    font1 = ["Consolas", 12, "normal"]

    def newFile(event=""):
        global file
        root.title("Untitled - Notepad")
        statusvar.set("New File(Untitled)  ")
        file = None
        TextArea.delete(1.0, END)

    def openFile(event=""):
        global file
        file = askopenfilename(defaultextension="*.txt",
                               filetypes=[("Text Documents('*.txt')", "*.txt"), ("HTML File('*.html')", "*.html"), ("Python File('*.py')", "*.py"),
                                          ("Configuration File('*.cfg')", "*.cfg"), ("CSS File('*.css')", "*.css"), ("CSV File('*.csv')", "*.csv"), ("All Files('*.*')", "*.*")])
        # updating status bar
        name = file
        statusvar.set(f'{name}  ')

        if file == "":
            file = None

        else:
            root.title(os.path.basename(file) + "- Notepad")
            TextArea.delete(1.0, END)
            f = open(file, "r")
            TextArea.insert(1.0, f.read())
            f.close()
            # updating status bar
            name = file
            statusvar.set(f'{name}  ')

    def saveFile(event=""):
        global file
        if file == None:
            file = asksaveasfilename(initialfile="untitled.txt", defaultextension="*.txt",
                                     filetypes=[("Text Documents('*.txt')", "*.txt"), ("HTML File('*.html')", "*.html"), ("Python File('*.py')", "*.py"), ("Configuration File('*.cfg')", "*.cfg"),
                                                ("CSS File('*.css')", "*.css"), ("CSV File('*.csv')", "*.csv"), ("All Files('*.*')", "*.*")])
            # updating status bar
            name = file
            statusvar.set(f'saved - {name}  ')

            if file == "":
                file = None

            else:
                # save as a new file
                f = open(file, "w")
                f.write(TextArea.get(1.0, END))
                f.close()

                root.title(os.path.basename(file) + " - Notepad")
                print("File Saved")
                # updating status bar
                name = file
                statusvar.set(f'saved - {name}  ')

        else:
            # save The new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()
            # updating status bar
            name = file
            statusvar.set(f'saved - {name}  ')

    def save_as(event=""):
        global file

        file = asksaveasfilename(initialfile="untitled.txt", defaultextension=".*", title="Save File",
                                 filetypes=[("Text Documents('*.txt')", "*.txt"), ("HTML File('*.html')", "*.html"), ("Python File('*.py')", "*.py"), ("Configuration File('*.cfg')", "*.cfg"),
                                            ("CSS File('*.css')", "*.css"), ("CSV File('*.csv')", "*.csv"), ("All Files('*.*')", "*.*")])
        # updating status bar
        name = file
        statusvar.set(f'saved - {name}  ')

        if file == "":
            file = None

        else:
            # save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
            # updating status bar
            name = file
            statusvar.set(f'saved - {name}  ')

    def exit(event=""):
        global file

        ans = askyesnocancel("Notepad", "Do you want to save this file!")

        if ans == YES:
            file = asksaveasfilename(initialfile="untitled.txt", defaultextension="*.txt",
                                     filetypes=[("Text Documents('*.txt')", "*.txt"), ("HTML File('*.html')", "*.html"), ("Python File('*.py')", "*.py"),
                                                ("Configuration File('*.cfg')", "*.cfg"), ("CSS File('*.css')",
                                                                                           "*.css"), ("CSV File('*.csv')", "*.csv"),
                                                ("All Files('*.*')", "*.*")])

            if file == "":
                file = None

            else:
                # save as a new file
                f = open(file, "w")
                f.write(TextArea.get(1.0, END))
                f.close()

                root.title(os.path.basename(file) + " - Notepad")
                print("File Saved")

        elif ans == NO:
            root.destroy()

    def cut(event=""):
        TextArea.event_generate(("<<Cut>>"))

    def copy(event=""):
        TextArea.event_generate(("<<Copy>>"))

    def paste(event=""):
        TextArea.event_generate(("<<Paste>>"))

    def about():
        showinfo("Notepad", "Notepad By Varaliya")

    def new_window():
        global file
        root.title("Untitled - Notepad")
        statusvar.set("New Window(Untitled)  ")
        file = None
        TextArea.delete(1.0, END)

    def my_func1(event=""):
        font1[1] = font1[1] + 2
        TextArea.config(font=font1)

    def my_func2(event=""):
        font1[1] = font1[1] - 2
        TextArea.config(font=font1)

    def Datetime(event=""):
        date = datetime.now()
        # Create Label to display the Date
        label = Label(sbar, text=f"{date:%A, %B %d, %Y}  | ", font="cambria 10",
                      background="white", foreground="black", relief="flat")
        label.grid(row=0, column=0)
        # Create Label to display the time
        import time
        time_string = time.strftime('%I:%M %p')
        label = Label(sbar, text=time_string, font="cambria 10",
                      background="white", foreground="black", relief="flat")
        label.grid(row=0, column=1)

    # creating the shortcuts for every menus and sub menu
    root.bind("<Control-n>", newFile)
    root.bind("<Control-o>", openFile)
    root.bind("<Control-s>", saveFile)
    root.bind("<Control-q>", exit)
    root.bind("<Control-x>", cut)
    root.bind("<Control-c>", copy)
    root.bind("<Control-v>", paste)
    root.bind("<Control-Shift-S>", save_as)
    root.bind("<Control-plus>", my_func1)
    root.bind("<Control-minus>", my_func2)
    root.bind("<Control-d>", Datetime)

    my_frame = Frame(root)
    my_frame.pack(fill=BOTH, expand=True)

    # Add text area
    TextArea = Text(my_frame, font=font1)
    file = None
    TextArea.pack(expand=True, fill=BOTH, padx=0.3, pady=0.3, ipadx=5)
    TextArea.configure(bg="White", foreground="black")

    # Lets create a menu bar
    MenuBar = Menu(root)
    # File Menu starts
    FileMenu = Menu(MenuBar, tearoff=0, background="white")

    # To open new file
    FileMenu.add_command(label="New", accelerator='Ctrl+N',
                         command=newFile, font="cambria 12")

    # To Open New Window
    FileMenu.add_command(label="New Window", accelerator='Ctrl+Shift+N',
                         command=new_window, font="cambria 12")

    # To open already existing file
    FileMenu.add_command(label="Open", accelerator='Ctrl+O',
                         command=openFile, font="cambria 12")

    # To save the current file
    FileMenu.add_command(label="Save", accelerator='Ctrl+S',
                         command=saveFile, font="cambria 12")
    FileMenu.add_command(label="Save as", accelerator='Ctrl+Shift+S',
                         command=save_as, font="cambria 12")
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", accelerator='Ctrl+Q',
                         command=exit, font="cambria 12")
    MenuBar.add_cascade(label="File", menu=FileMenu)
    # File Menu Ends

    # Edit Menu Starts
    EditMenu = Menu(MenuBar, tearoff=0, background="white")

    # To give a feature of cut, copy and paste
    EditMenu.add_command(label='Cut', accelerator='Ctrl+X',
                         command=cut, font="cambria 12")
    EditMenu.add_command(label='Copy', accelerator='Ctrl+C',
                         command=copy, font="cambria 12")
    EditMenu.add_command(label='Paste', accelerator='Ctrl+V',
                         command=paste, font="cambria 12")
    EditMenu.add_separator()
    EditMenu.add_command(label='Date/Time', accelerator='Ctrl+D',
                         command=Datetime, font="cambria 12")
    MenuBar.add_cascade(label="Edit", menu=EditMenu)
    # Edit Menu Ends

    # Format Menu start
    FormatMenu = Menu(MenuBar, tearoff=0, background="white")
    FormatMenu.add_command(
        label="Fonts", font="cambria 12")
    MenuBar.add_cascade(label="Format", menu=FormatMenu)

    sub_menu = Menu(FormatMenu, tearoff=0)
    sub_menu.add_command(label='Lucida Console      Regular      10',
                         font="cambria 12", background="white")
    FormatMenu.add_cascade(label="Default", menu=sub_menu,
                         font="cambria 12", background="white")


    # Format Menu start
    ViewMenu = Menu(MenuBar, tearoff=0, background="white")
    MenuBar.add_cascade(label="View", menu=ViewMenu)

    sub_menu = Menu(ViewMenu, tearoff=0)
    sub_menu.add_command(label='Zoom In', accelerator='Ctrl+Plus',
                         font="cambria 12", background="white", command=lambda:my_func1())
    sub_menu.add_command(label='Zoom Out', accelerator='Ctrl+Minus',
                         font="cambria 12", background="white", command=lambda:my_func2())
    ViewMenu.add_cascade(label="Zoom", menu=sub_menu,
                         font="cambria 12", background="white")

    # Help Menu starts
    AboutMenu = Menu(MenuBar, tearoff=0, background="white")
    AboutMenu.add_command(label="About Notepad",
                          font="cambria 12", command=about)
    MenuBar.add_cascade(label="Help", menu=AboutMenu)

    # Help Menu Ends

    root.config(menu=MenuBar)

    # Adding scroll bar
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)

    # Add Statua bar to bottom of App
    statusvar = StringVar()
    statusvar.set("Untitled  ")

    sbar = Label(root, textvariable=statusvar, relief=SUNKEN, bd=1,
                 bg="white", fg="black", anchor=E, font="cambria 10", background="white")
    sbar.pack(side=BOTTOM, fill=X)


root.protocol("WM_DELETE_WINDOW", exit)

root.mainloop()
