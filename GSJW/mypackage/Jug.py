class Jug:
    def __init__(self):
        self.value = None
        self.max_value = None
    def __init__(self,max_value,value = 0):
        self.max_value = max_value
        self.value = value
    def __str__(self) -> str:
        return str(self.value)
    def __repr__(self):
        return f" Jug:{str(self.value)}"
    def isEmpty(self):
        if (self.value == 0):
            return True
        else:
            return False
    def isFull(self):
        if (self.value == self.max_value):
            return True
        else:
            return False
    def current_value(self):
        return self.value
    def avail_space(self):
        return (self.max_value - self.value)
    def empty_jug(self):
        self.value = 0
    def pour_Water(self,value):
        try:
            if self.value == value:
                self.value = 0
            elif value <= self.max_value:
                self.value = self.value - value
            else:
                raise ValueError
        except ValueError:
            print("Value Error Exception!!!!!")
    def fill_Water(self,value):
        try:
            if self.value == 0 and value <= self.max_value:
                self.value = self.value + value
            elif (self.value + value) <= self.max_value:
                self.value+= value
            else:
                raise ValueError
        except ValueError:
            print("Value Error!!!!!!!!!!!!!")
    def fill_full_water(self):
        if self.value < self.max_value:
            self.value = self.max_value