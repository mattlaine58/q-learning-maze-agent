from collections import namedtuple
from random import randint

Point = namedtuple('Point', 'x y')

class Maze:
    REWARD_FOUND_GOAL = 100
    REWARD_CAUGHT = -100
    REWARD_TIME_EXPIRED = 0
    REWARD_OTHER = -1

    MAX_STEPS = 50 # Maximum steps an agent can take before game ends
    MIN_ACTION = 0
    MAX_ACTION = 4

    ACTION_NONE = 0
    ACTION_LEFT = 1
    ACTION_RIGHT = 2
    ACTION_UP = 3
    ACTION_DOWN = 4

    maze_obstacles = None
    MAZE_SIZE = 10
    GOAL_X = 8 # X-pos of the goal
    GOAL_Y = 8 # Y-pos of the goal

    player = None                   # Current position of player
    opponent = None                 # Current position opponent
    goal = Point(GOAL_X, GOAL_Y)    # Position of the goal

    num_steps = 0 # Number of steps that have been taken

    def __init__(self):
        self.__setup()
        return

    '''
    Setup the maze dimension and its obstacles
    '''
    def __setup(self):
        # Create a 10x10 maze, encode obstacles with int 1
        self.maze_obstacles = [[1 for i in range(self.MAZE_SIZE)] for j in range(self.MAZE_SIZE)]

        # Encode empty position with number 0
        for i in range(1, self.MAZE_SIZE - 1):
            for j in range(1, self.MAZE_SIZE - 1):
                self.maze_obstacles[i][j] = 0

        # Setup obstacles
        self.maze_obstacles[2][3] = 1;
        self.maze_obstacles[3][2] = 1;
        self.maze_obstacles[2][6] = 1;
        self.maze_obstacles[3][7] = 1;
        self.maze_obstacles[6][2] = 1;
        self.maze_obstacles[7][3] = 1;
        self.maze_obstacles[6][7] = 1;
        self.maze_obstacles[7][6] = 1;

    '''
    Initialize the maze game. Randomly setup the position of agent and opponent inside the maze
    '''
    def initialize(self):
        self.num_steps = 0;
        self.player = None
        self.opponent = None

        # Player position
        while (self.player is None) or (self.maze_obstacles[self.player.x][self.player.y] == 1) or (self.player.x == self.goal.x and self.player.y == self.goal.y):
            self.player = Point(randint(1, self.MAZE_SIZE - 1), randint(1, self.MAZE_SIZE - 1))

        # Opponent position
        while (self.opponent is None) or (self.maze_obstacles[self.opponent.x][self.opponent.y] == 1) or (self.player.x == self.opponent.x and self.player.y == self.opponent.y):
            self.opponent = Point(randint(1, self.MAZE_SIZE - 1), randint(1, self.MAZE_SIZE - 1))

    '''
    Display the maze in std output
    '''
    def show_maze(self):
        for j in range(self.MAZE_SIZE):
            line = ""
            for i in range(self.MAZE_SIZE):
                if self.maze_obstacles[i][j] == 1:
                    line += "X"
                elif i == self.player.x and j == self.player.y:
                    line += "P"
                elif i == self.opponent.x and j == self.opponent.y:
                    line += "O"
                elif i == self.goal.x and j == self.goal.y:
                    line += "G"
                else:
                    line += " "
            print(line)

    '''
    Get current location of player and opponent
    '''
    def current_locations(self):
        return self.player, self.opponent

    '''
    Execute an action given the current state of the maze. Return rewards
    after taking the action
    '''
    def execute_action(self, action):
        # Agent's turn
        move_result = self.make_player_move(action)
        if move_result == 1:
            return self.REWARD_FOUND_GOAL
        elif move_result == -1:
            return self.REWARD_CAUGHT
        self.num_steps += 1

        # Opponent's turn
        if self.opponent_move() == 1:
            return self.REWARD_CAUGHT

        # Exceed maximum moves
        if self.num_steps >= self.MAX_STEPS:
            return self.REWARD_TIME_EXPIRED

        return self.REWARD_OTHER

    def make_player_move(self, action):
        if (action == self.ACTION_NONE):
            pass
        elif (action == self.ACTION_LEFT):
            if (self.maze_obstacles[self.player.x - 1][self.player.y] == 0):
                self.player = Point(self.player.x - 1, self.player.y)
        elif (action == self.ACTION_RIGHT):
            if (self.maze_obstacles[self.player.x + 1][self.player.y] == 0):
                self.player = Point(self.player.x + 1, self.player.y)
        elif (action == self.ACTION_UP):
            if (self.maze_obstacles[self.player.x][self.player.y - 1] == 0):
                self.player = Point(self.player.x, self.player.y - 1)
        elif (action == self.ACTION_DOWN):
            if (self.maze_obstacles[self.player.x][self.player.y + 1] == 0):
                self.player = Point(self.player.x, self.player.y + 1)
        else:
            print("Unknown action")

        # Check if game ends, e.g. agent runs into opponent or gets to goal
        if (self.player.x == self.GOAL_X) and (self.player.y == self.GOAL_Y):
            return 1
        if (self.player.x == self.opponent.x) and (self.player.y == self.opponent.y):
            return -1
        return 0

    def opponent_move(self):
        best_action = self.ACTION_NONE
        best_dist = ((self.player.x - self.opponent.x) ** 2) + ((self.player.y - self.opponent.y) ** 2)
        the_dist = None

        # Left
        if (self.maze_obstacles[self.opponent.x - 1][self.opponent.y] == 0):
            the_dist = ((self.player.x - (self.opponent.x - 1)) ** 2) + ((self.player.y - self.opponent.y) ** 2)
            if (the_dist < best_dist):
                best_action = self.ACTION_LEFT
                best_dist = the_dist

        # Right
        if (self.maze_obstacles[self.opponent.x + 1][self.opponent.y] == 0):
            the_dist = ((self.player.x - (self.opponent.x + 1)) ** 2) + ((self.player.y - self.opponent.y) ** 2)
            if (the_dist < best_dist):
                best_action = self.ACTION_RIGHT
                best_dist = the_dist

        # Up
        if (self.maze_obstacles[self.opponent.x][self.opponent.y - 1] == 0):
            the_dist = ((self.player.x - self.opponent.x) ** 2) + ((self.player.y - (self.opponent.y - 1)) ** 2)
            if (the_dist < best_dist):
                best_action = self.ACTION_UP
                best_dist = the_dist

        # Down
        if (self.maze_obstacles[self.opponent.x][self.opponent.y + 1] == 0):
            the_dist = ((self.player.x - self.opponent.x) ** 2) + ((self.player.y - (self.opponent.y + 1)) ** 2)
            if (the_dist < best_dist):
                best_action = self.ACTION_DOWN
                best_dist = the_dist

        if (best_action == self.ACTION_NONE):
            pass
        elif (best_action == self.ACTION_LEFT):
            self.opponent = Point(self.opponent.x - 1, self.opponent.y)
        elif (best_action == self.ACTION_RIGHT):
            self.opponent = Point(self.opponent.x + 1, self.opponent.y)
        elif (best_action == self.ACTION_UP):
            self.opponent = Point(self.opponent.x, self.opponent.y - 1)
        elif (best_action == self.ACTION_DOWN):
            self.opponent = Point(self.opponent.x, self.opponent.y + 1)

        if (best_dist == 0.0):
            return 1
        return 0
