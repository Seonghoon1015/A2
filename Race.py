import graphics # Import the graphics module for drawing
import Dice # Import the custom Dice module for random number generation
from graphics import Point # Import the Point class from graphics

class Horse:
    def __init__(self, speed, y, image, window):
        self.x = 0 # Initialize the x-position to 0 which is starting line
        self.speed = speed # Store the speed which is number of dice sides
        self.y = y # Store the y-position which represents lane position
        self.image = image # Store the image object for the horse
        self.window = window # Store the graphics window for drawing
        self.dice = Dice.Dice(speed) # Create a dice object with 'speed' sides

    def move(self):
        self.x += self.dice.roll() # Move the horse by rolling the dice and adding the result to x

    def draw(self):
        self.image.draw_at_pos(self.window, self.x, self.y) # Draw the horse at the current x and y positions

    def crossed_finish_line(self, x):
        return self.x >= x # Check if the horse's x-position has reached or crossed the finish line

def main():
    win = graphics.GraphWin("Horse", 700, 350, autoflush=False) # Create the graphics window with a specific size

    horse1_img = graphics.Image(Point(100, 100), "simson.png") # Load the first horse image
    horse2_img = graphics.Image(Point(100, 100), "familyguy.png") # Load the second horse image

    horse1 = Horse(12, 100, horse1_img, win) # Create the first Horse object with unique speed and y-position 100
    horse2 = Horse(12, 250, horse2_img, win) # Create the first Horse object with unique speed and y-position 250

    horse1.draw() # Draw the first horse at the starting position
    horse2.draw() # Draw the second horse at the starting position

    finish_line = graphics.Line(Point(600, 0), Point(600, 350)) # Create a vertical finish line at x=600
    finish_line.setFill("white") # Set the finish line color to white
    finish_line.setWidth(3) # Set the finish line width to 3
    finish_line.draw(win) # Draw the finish line in the window

    win.getMouse() # Wait for the user to click before starting the race

    while True: # Infinite loop for the race
        win.clear_win() # Clear the window for redrawing
        finish_line.draw(win) # Redraw the finish line

        horse1.move() # Move the first horse based on dice roll
        horse2.move() # Move the second horse based on dice roll

        horse1.draw() # Redraw the first horse at the new position
        horse2.draw() # Redraw the second horse at the new position

        win.update() # Update the window to display the latest drawings

        # Break the loop if any horse crosses the finish line
        if horse1.crossed_finish_line(600) or horse2.crossed_finish_line(600):
            break

    # Determine and print the race result
    if horse1.crossed_finish_line(600) and horse2.crossed_finish_line(600):
        print("Tie!") # Print "Tie" if both horses cross the finish line at the same time
    elif horse1.crossed_finish_line(600):
        print("Horse 1 is the winner!") # Print if horse 1 wins
    else:
        print("Horse 2 is the winner!") # Print if horse 2 wins

    win.getMouse() # Wait for a final mouse click before closing the window
    win.close() # Close the graphics window

# Run the main function
if __name__ == "__main__":
    main()