import pygame

class PS3Controller():
	def __init__(self):
		pygame.init()
		self.joystick = pygame.joystick.Joystick(0)
		self.joystick.init()
		print self.joystick.get_name()


	def get_axis_array(self):
		pygame.event.pump()
		return [self.joystick.get_axis(0),self.joystick.get_axis(1),self.joystick.get_axis(2),self.joystick.get_axis(3)]

'''
c = PS3Controller()

while True:
	print c.get_axis_array()
'''
