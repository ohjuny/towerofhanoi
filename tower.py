from disc import Disc

# Define Tower class
class Tower:
    # Initialize tower with discs (if required)
    # If height entered, initialize tower of height in decreasing order
    def __init__(self, height=0):
        assert(type(height) == int)

        # self.discs is stack with first item being bottom, last being top
        self.discs = []
        
        if height:
            for size in range(height, 0, -1):
                self.discs.append(Disc(size))

    # Returns height of tower
    def get_height(self):
        return len(self.discs)

    # Return tower as oredered list of disc size
    def get_list(self):
        return [disc.get_size() for disc in self.discs]

    # Returns size of top disc
    def get_top_size(self):
        return self.discs[-1].get_size()

    # Returns true if tower has no discs
    def empty(self):
        return len(self.discs) == 0

    # Returns true if size is smaller than top disc
    def check_smaller(self, size):
        # Returns True if empty to avoid IndexError 
        if self.empty():
            return True
        return size < self.discs[-1].get_size()

    # Add given disc to top of tower
    # Return True if successful, False if input disc is larger than top disc
    def add(self, disc):
        # If empty, should always add
        if self.empty():
            self.discs.append(disc)
            return True
        # Ensure that larger disc cannot be placed above smaller disc
        elif disc.get_size() > self.discs[-1].get_size():
            return False
        else:
            self.discs.append(disc)
            return True
    
    # Remove top disc
    # Returns removed disc
    def remove(self):
        return self.discs.pop(-1)

    # # Print tower to screen, with whitespace relative to base size
    # def print(self, base):
    #     return