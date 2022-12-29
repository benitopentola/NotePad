import tkinter as tk
import tkinter.filedialog as filedialog
import os
import codecs

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
        import codecs

        # create a file dialog to select the file to open
        file_dialog = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_dialog:
            # read the contents of the selected file
            with codecs.open(file_dialog, "r", encoding="utf-8") as file:
                contents = file.read()

            # clear the Text widget and insert the contents of the file
            self.text.delete("1.0", "end")
            self.text.insert("1.0", contents)


            # clear the Text widget and insert the contents of the file
            self.text.delete("1.0", "end")
            self.text.insert("1.0", contents)

# create a root window
root = tk.Tk()

# create an instance of the Notepad class
notepad = Notepad(root)

# start the main event loop
root.mainloop()
