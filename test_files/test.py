from tkinter import *

app = Tk()

part_text = StringVar()
part_label = Label(app, text='Test app', font=('bold', 14), pady=20)
part_label.grid(row=0, column=0)

app.title('Part Manager')
app.geometry('700x350')

app.mainloop()