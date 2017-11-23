from tkinter import *
import tkinter as tk
#from coffee_detector import CoffeeDetector

class Application(tk.Frame):
    CANVAS_WIDTH = 800
    CANVAS_HEIGHT = 600

    def __init__(self, master=None):
        master.title("Clasificadora de Cafe")
        super().__init__(master)
        self.pack()
        # self.canvas = tk.Canvas(master, width=self.CANVAS_WIDTH, height=self.CANVAS_HEIGHT)
        # self.canvas.config(bg="white")
        # self.canvas.pack()
#        self.coffee_detector = CoffeeDetector()
        self.test3()

    def test3(self):
        m = PanedWindow(height=self.CANVAS_HEIGHT, width=self.CANVAS_WIDTH, orient=HORIZONTAL)
        m.pack(fill=BOTH, expand=1)

        # top frame has two buttons which switches the bottom frames
        topFrame = Frame(m, bg="gray")
        m.add(topFrame)

        play_icon = tk.PhotoImage(file="img/play.png")
        button1 = Button(topFrame, text="Raise Frame 2", image=play_icon)  # raises frame 2 on clicking it
        button1.photo = play_icon
        button1.pack()

        stop_icon = tk.PhotoImage(file="img/stop.png")
        button2 = Button(topFrame, text="Raise Frame 1", image=stop_icon)  # raises frame 1 on clicking it
        button2.photo = stop_icon
        button2.pack()

        right_frame = Frame(m, bg="#FFFFFF")
        m.add(right_frame)

        top_frame = Frame(right_frame)
        top_frame.pack(side=TOP, pady=10)

        label1t = Label(top_frame, text="Café verde")
        label1t.pack(side=TOP)

        num_green = Label(top_frame, text="23 frutos")
        num_green.pack(side=BOTTOM)

        green_icon = tk.PhotoImage(file="img/green_icon.png")
        label1 = Label(top_frame, text="Green", image=green_icon)
        label1.photo = green_icon
        label1.pack(padx=10, pady=10, side=BOTTOM)

        center_frame = Frame(right_frame, bg="#000000")
        center_frame.pack(fill=BOTH, expand=1)

        bottom_frame = Frame(right_frame, pady=10)
        bottom_frame.pack(side=BOTTOM)

        label2t = Label(bottom_frame, text="Café maduro")
        label2t.pack(side=TOP)

        num_ripe = Label(bottom_frame, text="23 frutos")
        num_ripe.pack(side=BOTTOM)

        ripe_icon = tk.PhotoImage(file="img/ripe_icon.png")
        label2 = Label(bottom_frame, text="Green", image=ripe_icon)
        label2.photo = ripe_icon
        label2.pack(padx=10, pady=10)





    def create_panes(self):
        m1 = PanedWindow()
        m1.pack(fill=BOTH, expand=1)

        left = Label(m1, text="left pane")
        m1.add(left)

        hi_there = tk.Button(m1, text='Inicio', fg='green')
        hi_there["command"] = self.say_hi
        m1.pack(hi_there)

        quit = tk.Button(m1, text="Salir", fg="red")
        quit["command"] = self.bye
        m1.pack(quit)

        m2 = PanedWindow(m1, orient=VERTICAL)
        m1.add(m2)

        top = Label(m2, text="top pane")
        m2.add(top)

        bottom = Label(m2, text="bottom pane")
        m2.add(bottom)

    def create_widgets(self):
        left_frame = PanedWindow()
        left_frame.pack(fill=BOTH, expand=1)

        self.hi_there = tk.Button(left_frame, text='Inicio', fg='green')
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(left_frame, text="Salir", fg="red")
        self.quit["command"] = self.bye
        self.quit.pack(side="bottom")

        right_frame = PanedWindow(left_frame, orient=VERTICAL)
        left_frame.add(right_frame)

        self.green_icon = tk.PhotoImage(file="img/green_icon.png")
        self.canvas.create_image(50, 360, anchor=tk.NW, image=self.green_icon)


    def say_hi(self):
        print("Start")
#        self.coffee_detector.start_capture()


    def bye(self):
#        self.coffee_detector.release_capture()
        root.destroy


root = tk.Tk()
app = Application(master=root)
app.mainloop()