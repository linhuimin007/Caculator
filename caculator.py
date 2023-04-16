from tkinter import *

class Caculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("615x680+400+100")
        self.root.resizable(width = False, height = False)

        self.MainFrame1 = Frame(self.root, bd = 20, relief = RIDGE, width = 605, height = 670, bg = "cadet blue")
        self.MainFrame1.grid()

        self.MainFrame2 = Frame(self.MainFrame1, bd = 20, relief = RIDGE, width = 605, height = 670,bg = "powder blue")
        self.MainFrame2.grid()

        self.display = Label(self.MainFrame2, width = 30, height = 2, bg = "white", font = ('arial', 20, 'bold'), 
                             anchor = "e")
        self.display.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10)

        # Define the input value variable
        self.input_value = ""

        self.create_button("←", 1, 0)
        self.create_button("CE", 1, 1)
        self.create_button("C", 1, 2)
        self.create_button("±", 1, 3)

        self.create_button("7", 2, 0)
        self.create_button("8", 2, 1)
        self.create_button("9", 2, 2)
        self.create_button("+", 2, 3)

        self.create_button("4", 3, 0)
        self.create_button("5", 3, 1)
        self.create_button("6", 3, 2)
        self.create_button("-", 3, 3)

        self.create_button("1", 4, 0)
        self.create_button("2", 4, 1)
        self.create_button("3", 4, 2)
        self.create_button("*", 4, 3)

        self.create_button("0", 5, 0)
        self.create_button(".", 5, 1)
        self.create_button("=", 5, 2)
        self.create_button("/", 5, 3)

    def create_button(self, text, row, column):
        button = Button(self.MainFrame2, text = text, width = 6, height = 2, font=('arial', 20, 'bold'),
                        bd = 4, bg = 'cadet blue', command = lambda: self.button_click(text))
        button.grid(row = row, column = column, padx = 5, pady = 5)
    
    def button_click(self, text):
        if text == "←":
            self.input_value = self.input_value[:-1]
        elif text == "CE":
            self.input_value = ""
        elif text == "C":
            self.input_value = ""
        elif text == "=":
            try:
                self.input_value = str(eval(self.input_value))
            except:
                self.input_value = "Error"
        elif text == "±":
            self.input_value = str(-float(self.input_value))
        else:
            self.input_value += text
        self.display.config(text = self.input_value)

root = Tk()
app = Caculator(root)
root.mainloop()
