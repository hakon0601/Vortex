import xinterface
import threading
import time

status = {
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

input_thread = threading.Thread(target=xinterface.get_input, args=(status,))
input_thread.start()

while 1:
    time.sleep(0.1)
    print status
