import tkinter as tk
import tkinter.filedialog as filedialog
import tkinter.messagebox as messagebox
import os

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Notepad")

        # create a Text widget
        self.text = tk.Text(self.root, font=("Arial", 12))
        self.text.pack(expand=True, fill='both')

        # create a Scrollbar and associate it with the Text widget
        scrollbar = tk.Scrollbar(self.root, command=self.text.yview)
        scrollbar.pack(side='right', fill='y')
        self.text['yscrollcommand'] = scrollbar.set

        # create a Save button
        save_button = tk.Button(self.root, text="Save", command=self.save)
        save_button.pack(side='left')

        # create an Open button
        open_button = tk.Button(self.root, text="Open", command=self.open)
        open_button.pack(side='left')

        # create a Search button
        search_button = tk.Button(self.root, text="Search", command=self.search)
        search_button.pack(side='left')

        # create a Replace button
        replace_button = tk.Button(self.root, text="Replace", command=self.replace)
        replace_button.pack(side='left')

    def save(self):
        # get the contents of the Text widget
        contents = self.text.get("1.0", "end-1c")

        # create a file dialog to select the save location
        file_dialog = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_dialog:
            # write the contents to the selected file
            with open(file_dialog, "w") as file:
                file.write(contents)

    def open(self):
        # create a file dialog to select the file to open
        file_dialog = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_dialog:
            # read the contents of the selected file
            with open(file_dialog, "r") as file:
                contents = file.read()

            # clear the Text widget and insert the contents of the file
            self.text.delete("1.0", "end")
            self.text.insert("1.0", contents)

    def search(self):
        # create a top-level window to input the search term
        search_window = tk.Toplevel(self.root)
        search_window.title("Search")

        # create a label and an entry to input the search term
        tk.Label(search_window, text="Search term:").pack()
        search_term = tk.Entry(search_window)
        search_term.pack()

        # create a Search button
        def do_search():
            # get the search term from the entry
            term = search_term.get()

            # search for the term in the Text widget
            start = "1.0"
            while True:
                start = self.text.search(term, start, stopindex="end")
                if not start:
                    break

                # select the found term and highlight it
                end = f"{start}+{len(term)}c"
                self.text.tag_add("sel", start, end)
                self.text.mark_set("insert", end)

                start = end

        tk.Button(search_window, text="Search", command=do_search).pack()

    def replace(self):
        # create a top-level window to input the search and replace terms
        replace_window = tk.Toplevel(self.root)
        replace_window.title("Replace")

        # create labels and entries to input the search and replace terms
        tk.Label(replace_window, text="Search term:").pack()
        search_term = tk.Entry(replace_window)
        search_term.pack()
        tk.Label(replace_window, text="Replace term:").pack()
        replace_term = tk.Entry(replace_window)
        replace_term.pack()

        # create a Replace button
        def do_replace():
            # get the search and replace terms from the entries
            search = search_term.get()
            replace = replace_term.get()

            # search for the search term in the Text widget
            start = "1.0"
            while True:
                start = self.text.search(search, start, stopindex="end")
                if not start:
                    break

                # replace the found term with the replace term
                end = f"{start}+{len(search)}c"
                self.text.delete(start, end)
                self.text.insert(start, replace)

                start = end

        tk.Button(replace_window, text="Replace", command=do_replace).pack()

def main():
    # create a root window
    root = tk.Tk()
    root.geometry("800x600")

    # create a Notepad object
    notepad = Notepad(root)

    # start the event loop
    root.mainloop()

if __name__ == "__main__":
    main()



