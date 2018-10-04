import tkinter as tk

def main():
    window = tk.Tk()

    def callback():
        entry_text.set("Hi")

    entry_text = tk.StringVar()
    ent_text = tk.Entry(window)
    ent_text['textvariable'] = entry_text
    ent_text.pack()

    btn = tk.Button(window, text="Click me", command=callback)
    btn.pack()

    window.mainloop()


if __name__ == '__main__':
    main()
