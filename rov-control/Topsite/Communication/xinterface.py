from os import popen
import sys
import re


def get_input(status):

    playstation = False
    subprocess = popen('sudo xboxdrv --detach-kernel-driver')
    for i in range(0, 18):
        line = subprocess.readline()
        print line
        if 'PLAYSTATION' in line:
            playstation = True

    if playstation:
        while (True):
            line = subprocess.readline()
            data = filter(bool, re.split('[ :]', line))

            status['leftThumbStick']['X'] = int(data[1])
            status['leftThumbStick']['Y'] = int(data[3])

            status['rightThumbStick']['X'] = int(data[5])
            status['rightThumbStick']['Y'] = int(data[7])

            status['Dpad']['north'] = int(data[9])
            status['Dpad']['south'] = int(data[11])

            status['Dpad']['east'] = int(data[13])
            status['Dpad']['west'] = int(data[15])

            status['back'] = int(data[17])
            status['start'] = int(data[21])

            status['leftThumbPush'] = int(data[23])
            status['rightThumbPush'] = int(data[25])

            status['A'] = int(data[27])
            status['B'] = int(data[29])
            status['X'] = int(data[31])
            status['Y'] = int(data[33])

            status['hardTrigger']['left'] = int(data[35])
            status['hardTrigger']['rigth'] = int(data[37])

            status['softTrigger']['left'] = int(data[39])
            status['softTrigger']['rigth'] = int(data[41])


    else:
        while (True):
            line = subprocess.readline()
            data = filter(bool, re.split('[ :]', line))

            status['back'] = int(data[17])
            status['start'] = int(data[21])

            status['leftThumbStick']['X'] = int(data[1])
            status['leftThumbStick']['Y'] = int(data[3])

            status['rightThumbStick']['X'] = int(data[5])
            status['rightThumbStick']['Y'] = int(data[7])

            status['Dpad']['north'] = int(data[9])
            status['Dpad']['south'] = int(data[11])

            status['Dpad']['east'] = int(data[13])
            status['Dpad']['west'] = int(data[15])


            status['leftThumbPush'] = int(data[23])
            status['rightThumbPush'] = int(data[25])

            status['A'] = int(data[27])
            status['B'] = int(data[29])
            status['X'] = int(data[31])
            status['Y'] = int(data[33])

            status['hardTrigger']['left'] = int(data[35])
            status['hardTrigger']['rigth'] = int(data[37])

            status['softTrigger']['left'] = int(data[39])
            status['softTrigger']['rigth'] = int(data[41])
