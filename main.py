import tkinter as tk
import win32api
import tkinter.filedialog as filedialog
import tkinter.messagebox as messagebox
import os

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Otterpad")

        self.text = tk.Text(self.root, font=("Arial", 12))
        self.text.pack(expand=True, fill='both')

        scrollbar = tk.Scrollbar(self.root, command=self.text.yview)
        scrollbar.pack(side='right', fill='y')
        self.text['yscrollcommand'] = scrollbar.set

        save_button = tk.Button(self.root, text="Save", command=self.save)
        save_button.pack(side='left')

        open_button = tk.Button(self.root, text="Open", command=self.open)
        open_button.pack(side='left')

        search_button = tk.Button(self.root, text="Search", command=self.search)
        search_button.pack(side='left')

        replace_button = tk.Button(self.root, text="Replace", command=self.replace)
        replace_button.pack(side='left')

    def save(self):

        contents = self.text.get("1.0", "end-1c")

        file_dialog = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_dialog:

            with open(file_dialog, "w") as file:
                file.write(contents)

    def open(self):

        file_dialog = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_dialog:

            with open(file_dialog, "r") as file:
                contents = file.read()


            self.text.delete("1.0", "end")
            self.text.insert("1.0", contents)

    def search(self):

        search_window = tk.Toplevel(self.root)
        search_window.title("Search")


        tk.Label(search_window, text="Search term:").pack()
        search_term = tk.Entry(search_window)
        search_term.pack()

        def do_search():

            term = search_term.get()

            start = "1.0"
            while True:
                start = self.text.search(term, start, stopindex="end")
                if not start:
                    break

                end = self.text.index(f"{start}+{len(term)}c")
                self.text.tag_add("highlight", start, end)
                start = end

        search_button = tk.Button(search_window, text="Search", command=do_search)
        search_button.pack()

    def replace(self):

        replace_window = tk.Toplevel(self.root)
        replace_window.title("Replace")

        tk.Label(replace_window, text="Search term:").pack()
        search_term = tk.Entry(replace_window)
        search_term.pack()

        tk.Label(replace_window, text="Replace term:").pack()
        replace_term = tk.Entry(replace_window)
        replace_term.pack()

        def do_replace():

            search = search_term.get()
            replace = replace_term.get()

            start = "1.0"
            while True:
                start = self.text.search(search, start, stopindex="end")
                if not start:
                    break

                end = self.text.index(f"{start}+{len(search)}c")
                self.text.delete(start, end)
                self.text.insert(start, replace)

        replace_button = tk.Button(replace_window, text="Replace", command=do_replace)
        replace_button.pack()
from PIL import Image, ImageTk

def main():

    root = tk.Tk()
    root.geometry("800x600")

    icon_path = os.path.join("imagenes", "iconoblockdenotas.ico")
    icon_image = Image.open(icon_path)
    icon_image = icon_image.resize((32, 32), Image.ANTIALIAS)
    icon = ImageTk.PhotoImage(icon_image)
    root.call('wm', 'iconphoto', root._w, icon)

    root.title("Otterpad")

    notepad = Notepad(root)
#s
    root.mainloop()

if __name__ == "__main__":
    main()




