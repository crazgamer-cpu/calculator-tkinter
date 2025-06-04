import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(str(screen.get())))
            screen.set(result)
        except Exception as e:
            screen.set("Error")
    elif text == "C":
        screen.set("")
    else:
        screen.set(screen.get() + text)


root = tk.Tk()
root.geometry("300x400")
root.title("Calculator")


screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen, font="Arial 20 bold")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]


for row in buttons:
    btn_row = tk.Frame(button_frame)
    btn_row.pack(expand=True, fill="both")
    for item in row:
        b = tk.Button(btn_row, text=item, font="Arial 18", relief='ridge')
        b.pack(side="left", expand=True, fill="both", padx=2, pady=2)
        b.bind("<Button-1>", click)

root.mainloop()
