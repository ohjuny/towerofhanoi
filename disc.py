# Define Disc class
class Disc:
    # Initialize disc size
    def __init__(self, size):
        assert(type(size) == int)

        self.size = size

    # Return size
    def get_size(self):
        return self.size

    # # Print disc to screen
    # def print(self):
    #     print('-'*self.size*2)