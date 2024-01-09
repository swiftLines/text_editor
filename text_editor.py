from tkinter import *

def main():
  window = tk.Tk()
  window.title('Text Editor')

  text_edit = tk.Text(window, font='Helvetica 18')
  text_edit.grid(row=0, column=1)

  window.mainloop()

main()
