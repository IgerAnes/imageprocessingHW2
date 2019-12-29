import tkinter as tk
from hw2_2 import Background_Subtraction

BS = Background_Subtraction() #need be instantiate or will have self argument 

MainWindow = tk.Tk()
MainWindow.title("Graghic User Interface")
MainWindow.geometry("400x300")
# ------------------------------ frame -------------------------------------
Frame_P1 = tk.Frame(MainWindow)
Frame_P1.grid(column = 0, row = 0, sticky = "wn")

Frame_P2 = tk.Frame(MainWindow)
Frame_P2.grid(column = 0, row = 1, sticky = "wn")

Frame_P3 = tk.Frame(MainWindow)
Frame_P3.grid(column = 1, row = 0, sticky = "wn")

Frame_P4 = tk.Frame(MainWindow)
Frame_P4.grid(column = 1, row = 1, sticky = "wn")
# ------------------------------ label -------------------------------------
Label_title01 = tk.Label(Frame_P1, text = "1. Stereo")
Label_title01.grid(row = 0, column = 0, padx = 10, pady = 5, sticky = "W")

Label_title02 = tk.Label(Frame_P2, text = "2. Back Subtractor")
Label_title02.grid(row = 0, column = 0, padx = 10, pady = 5, sticky = "W")

Label_title03 = tk.Label(Frame_P3, text = "3. Feature Tracking")
Label_title03.grid(row = 0, column = 0, padx = 10, pady = 5, sticky = "W")

Label_title04 = tk.Label(Frame_P4, text = "4. Augmented Reality")
Label_title04.grid(row = 0, column = 0, padx = 10, pady = 5, sticky = "W")
# ----------------------------- bottum --------------------------------------
Button_Displarity = tk.Button(Frame_P1, text = "1.1 Displarity", 
# command = lambda:IPF.ChooseAndLoadImage(),
width = "20", height = "1")
Button_Displarity.grid(row = 1, column = 0, padx = 8, pady = 8)

Button_BackSubtraction = tk.Button(Frame_P2, text = "2.1 BackGround Subtraction",
command = lambda:BS.Start_Process(),
width = "25", height = "1")
Button_BackSubtraction.grid(row = 1, column = 0, padx = 8, pady = 8)

Button_Preprocessing = tk.Button(Frame_P3, text = "3.1 Preprocessing",
# command = lambda:IPF.ImageFlipping(),
width = "20", height = "1")
Button_Preprocessing.grid(row = 1, column = 0, padx = 8, pady = 8)

Button_Videotracking = tk.Button(Frame_P3, text = "3.2 Video tracking",
# command = lambda:IPF.ImageFlipping(),
width = "20", height = "1")
Button_Videotracking.grid(row = 2, column = 0, padx = 8, pady = 8)

Button_Augmented = tk.Button(Frame_P4, text = "4.1 Augmented Reality",
# command = lambda:IPF.ColorConversion(),
width = "20", height = "1")
Button_Augmented.grid(row = 1, column = 0, padx = 8, pady = 8)

if __name__ == '__main__':
    MainWindow.mainloop()