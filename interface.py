from tkinter import *
import tkinter as tk
from coffee_detector import CoffeeDetector

class Application(tk.Frame):
    CANVAS_WIDTH = 800
    CANVAS_HEIGHT = 600

    def __init__(self, master=None):
        # master.title("Clasificadora de Cafe")
        super().__init__(master)
        # self.pack()
        # self.canvas = tk.Canvas(master, width=self.CANVAS_WIDTH, height=self.CANVAS_HEIGHT)
        # self.canvas.config(bg="white")
        # self.canvas.pack()
#        self.coffee_detector = CoffeeDetector()
        self.create_widgets()

    def create_widgets(self):

        # create all of the main containers
        top_frame = Frame(root, bg='#fef2cc', width=450, height=50, pady=3)
        center = Frame(root, bg='gray2', width=50, height=40, pady=3)
        btm_frame = Frame(root, bg='white', width=450, height=45, pady=3)
        btm_frame2 = Frame(root, bg='black', width=450, height=60, pady=3)

        # layout all of the main containers
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)

        top_frame.grid(row=0, sticky="ew")
        center.grid(row=1, sticky="nsew")
        btm_frame.grid(row=3, sticky="nsew")
        btm_frame2.grid(row=4, sticky="ew")

        # create the widgets for the top frame
        model_label = Label(top_frame, text='Ceres: Clasificadora de cafe', font="Arial 20 bold", bg='#fef2cc')
        # layout the widgets in the top frame
        model_label.grid(row=0, columnspan=1)

        # create the center widgets
        center.grid_rowconfigure(0, weight=1)
        center.grid_columnconfigure(1, weight=1)

        ctr_left = Frame(center, bg='#fef2cc', width=100, height=190)
        ctr_mid = Frame(center, bg='#fef2cc', width=250, height=190, padx=3, pady=3)
        ctr_right = Frame(center, bg='#fef2cc', width=100, height=190, padx=3, pady=3)

        ctr_left.grid(row=0, column=0, sticky="ns",  padx=3)
        ctr_mid.grid(row=0, column=1, sticky="nsew")
        ctr_right.grid(row=0, column=2, sticky="ns")

        play_icon = tk.PhotoImage(file="img/play.png")
        button1 = Button(ctr_left, text="Raise Frame 2", image=play_icon)
        button1.photo = play_icon
        button1["command"] = self.say_hi
        button1.grid(row=0, columnspan=1)

        title_green_label = Label(ctr_mid, text='Café verde', bg='#fef2cc')
        title_green_label.grid(row=0, columnspan=1)

        green_img = tk.PhotoImage(file="img/green_icon.png")
        green_icon = Label(ctr_mid, image=green_img)
        green_icon.photo = green_img
        green_icon.grid(row=1, columnspan=1)

        green_amount_label = Label(ctr_mid, text='10 frutos', bg='#fef2cc')
        green_amount_label.grid(row=2, columnspan=1)

        # create the bottom widgets
        btm_frame.grid_rowconfigure(0, weight=1)
        btm_frame.grid_columnconfigure(1, weight=1)

        btm_left = Frame(btm_frame, bg='#fef2cc', width=100, height=190)
        btm_mid = Frame(btm_frame, bg='#fef2cc', width=250, height=190, padx=3, pady=3)
        btm_right = Frame(btm_frame, bg='#fef2cc', width=100, height=190, padx=3, pady=3)
        btm_right_off = Frame(btm_frame, bg='#fef2cc', width=100, height=190, padx=3, pady=3)

        btm_left.grid(row=0, column=0, sticky="ns", padx=3)
        btm_mid.grid(row=0, column=1, sticky="nsew")
        btm_right.grid(row=0, column=2, sticky="nsew")
        btm_right_off.grid(row=0, column=3, sticky="ns")

        stop_icon = tk.PhotoImage(file="img/stop.png")
        button2 = Button(btm_left, text="Raise Frame 1", image=stop_icon)  # raises frame 1 on clicking it
        button2.photo = stop_icon
        button2["command"] = self.bye
        button2.grid(row=1, columnspan=1)

        title_ripe_label = Label(btm_mid, text='Café maduro', bg='#fef2cc')
        title_ripe_label.grid(row=0, columnspan=1)

        ripe_img = tk.PhotoImage(file="img/ripe_icon.png")
        ripe_icon = Label(btm_mid, image=ripe_img)
        ripe_icon.photo = ripe_img
        ripe_icon.grid(row=1, columnspan=1)

        ripe_amount_label = Label(btm_mid, text='34 frutos', bg='#fef2cc')
        ripe_amount_label.grid(row=2, columnspan=1)

        ripe_percent_label = Label(btm_right, text='30%', bg='#fef2cc', font="Arial 20 bold")
        ripe_percent_label.grid(row=0, columnspan=1)

        ripe_percent_title_label = Label(btm_right, text='de la cosecha', bg='#fef2cc', font="Arial 10 bold")
        ripe_percent_title_label.grid(row=1, columnspan=1)

        title_weighing_label = Label(btm_right_off, text='1.300 gr', bg='#fef2cc')
        title_weighing_label.grid(row=0, columnspan=1)

        weighing_img = tk.PhotoImage(file="img/weighing.png")
        weighing_icon = Label(btm_right_off, image=weighing_img)
        weighing_icon.photo = weighing_img
        weighing_icon.grid(row=1)


    def create_widgets2(self):
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

        ripe_frame = Frame(bottom_frame, pady=10)
        ripe_frame.pack(side=BOTTOM)

        label2t = Label(ripe_frame, text="Café maduro")
        label2t.pack(side=TOP)

        num_ripe = Label(ripe_frame, text="23 frutos")
        num_ripe.pack(side=BOTTOM)

        ripe_icon = tk.PhotoImage(file="img/ripe_icon.png")
        label2 = Label(ripe_frame, text="Green", image=ripe_icon)
        label2.photo = ripe_icon
        label2.pack(padx=10, pady=10)

        ripe_percent_frame = Frame(bottom_frame, pady=10)
        ripe_percent_frame.pack(side=RIGHT)

        label3t = Label(ripe_percent_frame, text="70%")
        label3t.pack(side=RIGHT)


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

    def test3(self):
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
        print("Stop")
        root.destroy

root = Tk()
root.title('Model Definition')
root.geometry('{}x{}'.format(460, 450))
app = Application(master=root)
app.mainloop()