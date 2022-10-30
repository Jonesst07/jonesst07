# Sherena Jones
# CSCI-130

# Program: LoopDrawing.py
# Due:  10/21/2022

from graphics import *

def main():


# Creates window
        win = GraphWin("Loop Drawing",1000,800)
    
        for i in range(5):
            modifier = i * 175
            p1 = Point(50 + modifier, 600)
            p2 = Point(150 + modifier, 700)
            rect = Rectangle(p1, p2)
            rect.setFill('yellow')
            rect.setOutline("black")
            rect.draw(win)
    
        for i in range(5):
            modifier = i * 200
            p1 = Point(50 + modifier, 100)
            p2 = Point(150 + modifier, 200)
            rect = Rectangle(p1, p2)
            rect.setFill('green')
            rect.setOutline("black")
            rect.draw(win)
            
            
    
    
    
        input('Press ENTER to exit')
 
main()
