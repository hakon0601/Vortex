

class Action():
    def __init__(self, variables=[], values=[]):
        self.variables = variables
        self.values = values

    def perform_action(self):
        for i in range(len(self.variables)):
            self.variables[i].set(self.variables[i].get() + self.values[i])
