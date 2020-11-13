from tkinter import Tk, Canvas
frame=Tk()
canvas=Canvas(bg='black',height=250,width=300)
canvas.create_rectangle(50,25,150,75, fill = 'red')
canvas.create_line(60, 70, 140, 70)
canvas.create_text(100, 60, text = 'Lam Tsz Him')
canvas.pack()
frame.mainloop()
