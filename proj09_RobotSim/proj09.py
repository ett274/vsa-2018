# proj09: Simulating robots
# Name: Eliza Thornton
# Date:

import math
import random

import proj09_visualize


# import pylab

# === Provided classes

class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """

    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: float representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)


# === Problems 1

class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """

    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        self.width = width
        self.height = height
        room_array = []
        for i in range(self.height):
            row = []
            for x in range(self.width):
                row.append(0)
            room_array.append(row)
        self.layout = room_array
        self.clean_tiles = 0

    def PrintRoom(self):
        for x in self.layout:
            print x

    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        y = int(pos.getY())
        x = int(pos.getX())
        if self.layout[y][x] == 0:
            self.layout[y][x] = 1
            self.clean_tiles += 1

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        layout = self.layout
        y = layout[n]
        x = y[m]
        if x == 1:
            return True
        else:
            return False

    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return self.width * self.height

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        return self.clean_tiles

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        x = random.uniform(0, self.width)
        y = random.uniform(0, self.height)
        return Position(x, y)

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        if pos.getX() < 0 or pos.getX() > self.width or pos.getY() < 0 or pos.getY() > self.height:
            return False
        else:
            return True


class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """

    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.position = room.getRandomPosition()
        self.room = room
        self.room.cleanTileAtPosition(self.position)
        self.direction = random.uniform(0, 360)
        self.speed = speed

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.position

    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.direction

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        self.position = position

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.direction = direction

    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        while True:
            maybe_position = self.position.getNewPosition(self.direction, self.speed)
            if self.room.isPositionInRoom(maybe_position) is True:
                self.position = maybe_position
                self.room.cleanTileAtPosition(self.position)
                break
            else:
                self.setRobotDirection(random.uniform(0, 360))


# === Problem 2
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current direction; when
    it hits a wall, it chooses a new direction randomly.
    """

    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        while True:
            maybe_position = self.position.getNewPosition(self.direction, self.speed)
            if self.room.isPositionInRoom(maybe_position) is True:
                self.position = maybe_position
                self.room.cleanTileAtPosition(self.position)
                break
            else:
                self.setRobotDirection(random.uniform(0, 360))

# === Problem 3

def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type, delay, animate):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. Robot or
                RandomWalkRobot)
    """
    avg = 0
    anim = ''
    for num in range(num_trials):
        time = 0
        room = RectangularRoom(width, height)
        if animate is True:
            anim = proj09_visualize.RobotVisualization(num_robots, width, height, delay)
        robot_list = []
        for x in range(num_robots):
            robot_list.append(robot_type(room, speed))

        num_tiles = float(room.getNumTiles())
        while float(room.getNumCleanedTiles()) / num_tiles < min_coverage:
            for robot in robot_list:
                robot.updatePositionAndClean()
            if animate is True:
                anim.update(room, robot_list)
            time += 1
        if animate is True:
            anim.done()
        avg += time
    return avg / num_trials


# === Problem 4
#
# 1) How long does it take to clean 80% of a 20x20 room with each of 1-10 robots?
#
# 2) How long does it take two robots to clean 80% of rooms with dimensions 
#	 20x20, 25x16, 40x10, 50x8, 80x5, and 100x4?

def showPlot1(delay, animate):
    """
    Produces a plot showing dependence of cleaning time on number of robots.
    """
    for x in range(1, 11):
        print runSimulation(x, 1, 20, 20, .8, 1, StandardRobot, delay, animate)


def showPlot2(delay, animate):
    """
    Produces a plot showing dependence of cleaning time on room shape.
    """
    print runSimulation(2, 1, 20, 20, .8, 1, StandardRobot, delay, animate)
    print runSimulation(2, 1, 25, 16, .8, 1, StandardRobot, delay, animate)
    print runSimulation(2, 1, 40, 10, .8, 1, StandardRobot, delay, animate)
    print runSimulation(2, 1, 50, 8, .8, 1, StandardRobot, delay, animate)
    print runSimulation(2, 1, 80, 5, .8, 1, StandardRobot, delay, animate)
    print runSimulation(2, 1, 100, 4, .8, 1, StandardRobot, delay, animate)


# === Problem 5

class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random after each time-step.
    """

    def updatePositionAndClean(self):
        while True:
            self.direction = random.uniform(0, 360)
            maybe_position = self.position.getNewPosition(self.direction, self.speed)
            if self.room.isPositionInRoom(maybe_position) is True:
                self.position = maybe_position
                self.room.cleanTileAtPosition(self.position)
                break
            else:
                self.setRobotDirection(random.uniform(0, 360))

# === Problem 6

# For the parameters tested below (cleaning 80% of a 20x20 square room),
# RandomWalkRobots take approximately twice as long to clean the same room as
# StandardRobots do.
def showPlot3(delay, animate):
    """
    Produces a plot comparing the two robot strategies.
    """
    print runSimulation(2, 1, 20, 20, .8, 1, StandardRobot, delay, animate)
    print runSimulation(2, 1, 20, 20, .8, 1, RandomWalkRobot, delay, animate)

runSimulation(1, 1, 20, 20, .8, 1, StandardRobot, 0.1, True)