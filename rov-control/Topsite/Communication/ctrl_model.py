import threading
import time

class Model():

    def __init__(self):
        self.control_model = {
            'leftThumbStick' : {
                'Y' : 0.0,
                'X' : 0.0,
            },
            'rightThumbStick' : {
                'Y' : 0.0,
                'X' : 0.0,
            },
            'Dpad' : {
                'north' : 0,
                'west' : 0,
                'east' : 0,
                'south' : 0,
            },
            'hardTrigger' : {
                'left' : 0,
                'rigth' : 0,
            },
            'softTrigger' : {
                'left' : 0.0,
                'rigth' : 0.0,
            }
        }