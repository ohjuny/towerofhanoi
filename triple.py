from tower import Tower

# Define Triple class
class Triple:
    # Initialize Triple with 3 towers
    # Tower 1 has height 'height', rest have height 0
    def __init__(self, height):
        assert(type(height) == int)

        self.towers = [Tower(height), Tower(), Tower()]
        self.height = height
        # For solve method
        self.move_counter = 0

    # Returns height of Triple
    def get_height(self):
        return self.height

    # Returns if given tower is empty
    def empty(self, tower):
        return self.towers[tower-1].empty()

    # Move top disc in '_from' tower to 'to' tower
    # _from and to must be between 0 and 2 (inclusive)
    # Return True if successful, False if _from disc is larger than to disc
    def move(self, _from, to):
        assert(type(_from) == int)
        assert(type(to) == int)

        if self.towers[to].check_smaller(self.towers[_from].get_top_size()):
            return self.towers[to].add(self.towers[_from].remove())
        else:
            return False
    
    # Return whether all discs are in tower 3
    def complete(self):
        return len(self.towers[0].get_list()) == 0 and len(self.towers[1].get_list()) == 0

    # Print 3 towers as 3 lists
    def print_lists(self):
        print('Tower 1: {}'.format(self.towers[0].get_list()))
        print('Tower 2: {}'.format(self.towers[1].get_list()))
        print('Tower 3: {}'.format(self.towers[2].get_list()))

    # Pads _list with 0s to make its length length
    def pad_zero(self, _list, length):
        while len(_list) < length:
            _list.append(0)
        return _list

    # Print 3 towers graphically side by side
    def print(self):
        base = self.height
        # Create list of tuples of each layer of tower, in DESCENDING order
        # So first item is top, last item is bottom
        # Each tuple is length self.height
        # eg. [5, 3, 1], [2], [4] becomes [(1, 0, 0, 0, 0), (3, 0, 0, 0, 0), (5, 2, 4, 0, 0)]
        a = self.towers[0].get_list()
        b = self.towers[1].get_list()
        c = self.towers[2].get_list()
        
        # Pad lists with 0 to make them length _max
        a = self.pad_zero(a, self.height)
        b = self.pad_zero(b, self.height)
        c = self.pad_zero(c, self.height)

        # Create tuple
        stage = list(zip(a, b, c))
        stage.reverse()

        # Print each layer
        for layer in stage:
            for disc_size in layer:
                print(' '*(base - disc_size), end='')
                print('-'*disc_size, end='')
                print('|', end='')
                print('-'*disc_size, end='')
                print(' '*(base - disc_size), end='')
                print(' '*2, end='')
            print()
        
        # Print platform
        print('_'*(base*2*3 + 3 + 6))
    
    # Recursively moves n discs from tower _from to tower to
    # aux is the "middle"/"unused" tower
    def move_n(self, n, _from, to, aux):
        # Base case
        if n == 1:
            self.move(_from-1, to-1)

            # Print current state to screen
            print()
            # self.print_lists() # For testing
            self.print()
            self.move_counter += 1
            print('Moves: {}'.format(self.move_counter))

            return

        # Recursive step
        self.move_n(n-1, _from, aux, to)
        self.move(_from-1, to-1)

        # Print current state to screen
        print()
        # self.print_lists() # For testing
        self.print()
        self.move_counter += 1
        print('Moves: {}'.format(self.move_counter))

        self.move_n(n-1, aux, to, _from)

    # Solves triple, printing every move to screen
    def solve(self):
        # Print starting state to screen
        print('Let\'s begin!')
        print()

        # self.print_lists() # For Testing
        self.print()
        print('Moves: {}'.format(self.move_counter))

        self.move_n(self.height, 1, 3, 2)