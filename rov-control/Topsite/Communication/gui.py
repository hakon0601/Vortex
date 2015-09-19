__author__ = 'hakon0601'

import Tkinter as tk

import tcpclient
import action
import ps3controller
import threading
import xinterface
import ctrl_model
import time


class Gui(tk.Tk):
    def __init__(self, host, port, use_controller=False, *args, **kwargs):

        self.client = tcpclient.TCPClient(host, port)

        tk.Tk.__init__(self, *args, **kwargs)
        self.title("VortexNTNU")
        self.create_buttons()
        self.create_sliders()
        self.set_key_bindings()
        self.command_action_dict = self.create_command_action_dict()

        control_model = ctrl_model.Model()
        # Init input thread
        input_thread = threading.Thread(target=xinterface.get_input, args=(control_model,))
        input_thread.start()

        while True:
            print str(control_model.control_model)
            time.sleep(0.5)


        '''
        if use_controller:
            self.controller = ps3controller.PS3Controller()
            # Allows the gui to set up before starting the controller transmissions
            t = threading.Timer(5, self.start_listening_to_controller)
            t.start()
        '''


    def create_buttons(self):
        self.info1 = tk.Label(self, text="WASD/Arrows")
        self.info1.grid(row=0, column=0)
        self.v = tk.StringVar()
        self.btn_forward = tk.Button(self, text="Forward", width=15, command=lambda:self.send_dir(dir="Forward"))
        self.btn_backward = tk.Button(self, text="Backward", width=15, command=lambda:self.send_dir(dir="Backward"))
        self.btn_right = tk.Button(self, text="Right", width=15, command=lambda:self.send_dir(dir="Right"))
        self.btn_left = tk.Button(self, text="Left", width=15, command=lambda:self.send_dir(dir="Left"))
        self.btn_asc = tk.Button(self, text="Ascend", width=15, command=lambda:self.send_dir(dir="Ascend"))
        self.btn_dec = tk.Button(self, text="Descend", width=15, command=lambda:self.send_dir(dir="Descend"))
        self.btn_forward.grid(row=1, column=1)
        self.btn_backward.grid(row=3, column=1)
        self.btn_right.grid(row=2, column=2)
        self.btn_left.grid(row=2, column=0)
        self.btn_asc.grid(row=1, column=2)
        self.btn_dec.grid(row=1, column=0)

    def create_sliders(self):
        self.horizontal_slider_1 = tk.Scale(self, length=600, from_=-1000, to=1000, orient=tk.HORIZONTAL)
        self.horizontal_slider_1.grid(row=5, column=0, columnspan=3)
        self.vertical_slider_1 = tk.Scale(self, length=600, from_=-1000, to=1000, orient=tk.VERTICAL)
        self.vertical_slider_1.grid(row=4, column=3, rowspan=3)

    def set_key_bindings(self):
        self.bind('<Up>', lambda event, dir="Forward" : self.send_dir(self, dir))
        self.bind('w', lambda event, dir="Forward" : self.send_dir(self, dir))
        self.bind('<Down>', lambda event, dir="Backward" : self.send_dir(self, dir))
        self.bind('s', lambda event, dir="Backward" : self.send_dir(self, dir))
        self.bind('<Right>', lambda event, dir="Right" : self.send_dir(self, dir))
        self.bind('d', lambda event, dir="Right" : self.send_dir(self, dir))
        self.bind('<Left>', lambda event, dir="Left" : self.send_dir(self, dir))
        self.bind('a', lambda event, dir="Left" : self.send_dir(self, dir))
        self.bind('e', lambda event, dir="Ascend" : self.send_dir(self, dir))
        self.bind('q', lambda event, dir="Descend" : self.send_dir(self, dir))

    def send_dir(self, event=None, dir=None):
        print "Sending dir: " + dir
        self.do_action(dir)
        self.client.send(dir)

    def do_action(self, dir):
        action = self.command_action_dict[dir]
        action.perform_action()

    def create_command_action_dict(self):
        dict = {}
        dict["Forward"] = action.Action(variables=[self.vertical_slider_1], values=[10])
        dict["Backward"] = action.Action(variables=[self.vertical_slider_1], values=[-10])
        dict["Right"] = action.Action(variables=[self.horizontal_slider_1], values=[10])
        dict["Left"] = action.Action(variables=[self.horizontal_slider_1], values=[-10])
        return dict

    def start_listening_to_controller(self):
        while True:
            axis = self.controller.get_axis_array()
            #print axis
            self.horizontal_slider_1.set(round(axis[0] * 1000, 0))
            self.vertical_slider_1.set(round(axis[1] * 1000, 0))
            self.client.send(str(axis))

if __name__ == "__main__":
    app = Gui(host="178.62.193.33", port=12000, use_controller=True)
    app.mainloop()
