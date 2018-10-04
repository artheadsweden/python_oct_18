import tkinter as tk


def main():
    window = tk.Tk()

    def callback_btn1():
       print("Button1 clicked")

    def callback_btn2():
       print("Button2 clicked")

    btn1 = tk.Button(window, text="Click me", command=callback_btn1)
    btn1.pack()
    btn2 = tk.Button(window, text="Click me too", command=callback_btn2)
    btn2.pack()

    window.mainloop()


if __name__ == '__main__':
    main()
