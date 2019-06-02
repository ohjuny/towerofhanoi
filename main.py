from triple import Triple

# Define Game class
class Game:
    # Initialize move counter
    def __init__(self):
        self.moves = 0

    # Print welcome message
    def welcome(self):
        print()
        print('Tower of Hanoi')
        print()
        print('Instructions:')
        print('    Move all the discs from the "tower" on the left to the "tower" on the right.')
        print('    You can only move one disc at a time.')
        print('    You cannot move a larger disc on top of a smaller disc')
        print()
        print('Have fun!')
        print()


    # Print congratulation message
    def congratulate(self):
        print('Congratulations!')
        print('You have completed the Tower of Hanoi of height {} in {} moves.'
                                                .format(self.triple.get_height(), self.moves))
        print()
        print('Note that the Tower of Hanoi of height {} is possible in {} moves.'
                            .format(self.triple.get_height(), 2**self.triple.get_height()-1))
        print()
        print('--------------------------------------------------')
        print()

    # Ask for game height between 1 and 10 (inclusive)
    # Create Triple with given height
    def create_triple(self):
        height = 0
        while height < 1 or height > 10:
            height = int(input('Input a height between 1 and 10 (inclusive): '))
        
        self.triple = Triple(height)
        print()

    # Ask for number between 1 and 3 (inclusive)
    # Return given number
    def input_tower(self):
        tower = 0
        while tower < 1 or tower > 3:
            tower = input('Input a number between 1 and 3 (inclusive): ')
            # To make testing easier
            if tower in ['q', 'quit', 'exit']:
                exit()
            tower = int(tower)
        return tower

    # Return list [_from, to]
    # _from and to cannot be the same number
    # _from cannot be empty list
    def input_towers(self):
        valid = False
        while not valid:
            while True:
                try:
                    # Ask for tower to move from
                    print('Tower to move FROM')
                    _from = self.input_tower()
                    print()
                    assert(type(_from) == int)

                    # Ask for tower to move to
                    print('Tower to move TO')
                    to = self.input_tower()
                    print()
                    assert(type(to) == int)

                    break
                # To make testing easier
                except SystemExit:
                    exit()
                except:
                    print()
                    print('Please enter an integer')
                    print('Try again')
                    print()

            if _from == to:
                print('Cannot move from and to same tower.')
                print('Try again.')
                print()
            elif self.triple.empty(_from):
                print('Cannot move from an empty tower.')
                print('Try again.')
                print()
            else:
                valid = True
        return [_from-1, to-1]

    # Check if game is over
    # Game is over when all discs are in tower 3
    def gameover(self):
        return self.triple.complete()

    # Starts game
    def play(self):
        # Prints instructions of game
        self.welcome()
        
        # Create Triple with given height
        self.create_triple()
        print('Tower of Hanoi of height {} is possible in {} moves.'
                    .format(self.triple.get_height(), 2**self.triple.get_height()-1))
        print('Good luck!')
        
        # Game loop
        while not self.gameover():
            # Print visual separator
            print()
            print('--------------------------------------------------')
            print()
            
            # Print current state of towers, and moves so far
            # self.triple.print_lists() # For testing
            self.triple.print()
            print()
            print('Moves so far: {}'.format(self.moves))
            print()

            # Get _from and to
            _from, to = self.input_towers()

            # Move disc
            # Ensure disc is movable (cannot place larger disc above smaller disc)
            while not self.triple.move(_from, to):
                print('Cannot move larger disc above smaller disc.')
                print('Try again.')
                print()
                _from, to = self.input_towers()
        
            # Update move counter
            self.moves += 1

        # Print visual separator
        print()
        print('--------------------------------------------------')
        print()

        # Print current state of towers, and moves so far
        # self.triple.print_lists() # For testing
        self.triple.print()
        print()
        print('Moves so far: {}'.format(self.moves))
        print()
        
        # Print congratulation message
        self.congratulate()
    
    # Solves a game, printing every move to screen
    def solve(self):
        # Create Triple with given height
        self.create_triple()

        # self.triple.print_lists() # For testing

        # Solve triple
        self.triple.solve()
        # self.triple.print_lists() # For testing
        


# Main Program
print()
print('Would you like to play or watch a solution?')
print()
print('1. Play')
print('2. Watch solution')
print()
while True:
    try:
        choice = int(input('Choice: '))
        assert(choice in [1, 2])

        break
    except ValueError:
        print()
        print('Please enter an integer.')
        print('Try again.')
        print()
    except AssertionError:
        print()
        print('Please choose either 1 or 2.')
        print('Try again.')
        print()

if choice == 1:
    Game().play()
else:
    Game().solve()