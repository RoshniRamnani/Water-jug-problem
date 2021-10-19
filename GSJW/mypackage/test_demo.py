class hello:
    def __init__(self):
        self.x = 0
    def set_x(self):
        self.x = 4
    def display(self):
        print(self.x)
    

h = hello()
h.display()
h.set_x()
h.display()