
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n9823361
#    Student name: Nathan Thai
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  FOUR PIECE JIGSAW PUZZLE
#
#  This assignment tests your skills at defining functions, processing
#  data stored in lists and performing the arithmetic calculations
#  necessary to display a complex visual image.  The incomplete
#  Python script below is missing a crucial function, "draw_attempt".
#  You are required to complete this function so that when the
#  program is run it produces a picture of a jigsaw puzzle whose
#  state of completion is determined by data stored in a list which
#  specifies the locations of the pieces.  You are also required to
#  provide a solution to your particular puzzle.  See the instruction
#  sheet accompanying this file for full details.
#
#  Note that this assignment is in two parts, the second of which
#  will be released only just before the final deadline.  This
#  template file will be used for both parts and you will submit
#  your final solution as a single file, whether or not you
#  complete both parts of the assignment.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.

from turtle import *
from math import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

size_of_pieces = 300 # pixels (excluding any protruding "tabs")
half_piece_size = size_of_pieces / 2
max_tab_size = 100 # pixels
box_size = size_of_pieces + (max_tab_size * 2)
half_box_size = box_size / 2
left_border = max_tab_size
gap = max_tab_size
top_bottom_border = max_tab_size
canvas_height = (top_bottom_border + size_of_pieces) * 2
canvas_width = (size_of_pieces * 2 + left_border) * 2
template_centres = [[-(size_of_pieces + half_piece_size), -half_piece_size], # bottom left
                    [-half_piece_size, -half_piece_size], # bottom right
                    [-(size_of_pieces + half_piece_size), half_piece_size], # top left
                    [-half_piece_size, half_piece_size]] # top right
box_centre = [gap + (box_size / 2), 0]

#
#--------------------------------------------------------------------#



#-----Functions for Drawing the Background---------------------------#
#
# The functions in this section are called by the main program to
# draw the background for the puzzle, i.e., the template for the
# pieces and the box they're kept in.  You should not change any of
# the code in this section.  Note that each of these functions
# leaves the turtle's pen up and at its standard width and colour.
#


# Draw the box that contains unused puzzle pieces.  (The box is
# larger than the puzzle pieces to allow for tabs sticking out on
# any of their four sides.)
def draw_box():

    # Determine the position of the box's bottom-left corner
    bottom_left = [box_centre[0] - half_box_size,
                   box_centre[1] - half_box_size]

    # Go to the bottom-left corner and get ready to draw
    penup()
    goto(bottom_left)
    width(5)
    color('black')
    pendown()
    
    # Walk around the box's perimeter
    setheading(0) # point east
    for side in [1, 2, 3, 4]:
        forward(box_size)
        left(90)

    # Reset the pen
    width(1)
    penup()
 

# Draw the individual squares of the jigsaw's template
def draw_template(show_template = False):

    # Only draw if the argument is True
    if show_template:

        # Set up the pen
        width(3)
        color('grey')

        # Draw a box for each centre coordinate
        for centre_x, centre_y in template_centres:
            
            # Determine the position of this square's bottom-left corner
            bottom_left = [centre_x - half_piece_size,
                           centre_y - half_piece_size]

            # Go to the bottom-left corner and get ready to draw
            penup()
            goto(bottom_left)
            pendown()
        
            # Walk around the square's perimeter
            setheading(0) # point east
            for side in [1, 2, 3, 4]:
                forward(size_of_pieces)
                left(90)

        # Reset the pen
        width(1)
        color('black')
        penup()


# As a debugging aid, mark the coordinates of the centres of
# the template squares and the box
def mark_coords(show_coords = False):

    # Only mark the coordinates if the argument is True
    if show_coords:

        # Don't draw lines between the coordinates
        penup()

        # Go to each coordinate, draw a dot and print the coordinate
        color('black')
        for x_coord, y_coord in template_centres + [box_centre]:
            goto(x_coord, y_coord)
            dot(4)
            write(str(x_coord) + ', ' + str(y_coord),
                  font = ('Arial', 12, 'normal'))

    # Reset the pen
    width(1)
    penup()
               
#
#--------------------------------------------------------------------#



#-----Test data------------------------------------------------------#
#
# These are the data sets you will use to test your code.
# Each of the data sets is a list specifying the locations of
# jigsaw puzzle pieces:
#
# 1. The name of the piece, from 'Piece A' to 'Piece D'
# 2. The place to put the piece, either in the template, denoted
#    'Top left', 'Top right', 'Bottom left' or 'Bottom right', or
#    in the unused pieces box, denoted 'In box'
# 3. An optional mystery value, 'X', whose purpose will be
#    revealed only in the second part of the assignment
#
# Each data set does not necessarily mention all pieces.  Also notice
# that several pieces may be in the box at the same time, in which
# case they should just be drawn on top of each other.
#
# You can create further data sets, but do not change any of the
# given ones below because they will be used to test your submission.
#
# Most importantly, you must write your own data set at the end
# to provide the correct solution to your puzzle.
#

# The following data set doesn't require drawing any jigsaw pieces
# at all.  You may find it useful as a dummy argument when you
# first start developing your "draw_attempt" function.

attempt_00 = []

# Each of the following data sets put just one piece in the box.
# You may find them useful when creating your individual pieces.

attempt_01 = [['Piece A', 'In box']]
attempt_02 = [['Piece B', 'In box']]
attempt_03 = [['Piece C', 'In box']]
attempt_04 = [['Piece D', 'In box']]

# Each of the following data sets put just one piece in a
# location in the template.

attempt_05 = [['Piece A', 'Top left']]
attempt_06 = [['Piece B', 'Bottom right']]
attempt_07 = [['Piece C', 'Top right']]
attempt_08 = [['Piece D', 'Bottom left']]
attempt_09 = [['Piece A', 'Bottom left']]
attempt_10 = [['Piece B', 'Top left']]
attempt_11 = [['Piece C', 'Bottom right']]
attempt_12 = [['Piece D', 'Top right']]

# Each of the following data sets put all four pieces in the
# box, but in different orders.

attempt_13 = [['Piece A', 'In box'], ['Piece B', 'In box'],
              ['Piece C', 'In box'], ['Piece D', 'In box']]
attempt_14 = [['Piece D', 'In box'], ['Piece C', 'In box'],
              ['Piece B', 'In box'], ['Piece A', 'In box']]
attempt_15 = [['Piece C', 'In box'], ['Piece D', 'In box'],
              ['Piece A', 'In box'], ['Piece B', 'In box']]

# Each of the following data sets uses between two and four pieces,
# either in the template or in the box

attempt_16 = [['Piece A', 'Top right'], ['Piece B', 'Bottom left']]
attempt_17 = [['Piece D', 'Bottom right'], ['Piece C', 'In box']]
attempt_18 = [['Piece C', 'Bottom right'], ['Piece A', 'Bottom right']]
attempt_19 = [['Piece B', 'In box'], ['Piece D', 'Top left'],
              ['Piece C', 'In box']]
attempt_20 = [['Piece C', 'Top left'], ['Piece D', 'Top right'],
              ['Piece A', 'Bottom left']]
attempt_21 = [['Piece A', 'In box'], ['Piece D', 'Bottom left'],
              ['Piece C', 'Top right']]
attempt_22 = [['Piece A', 'Bottom left'], ['Piece B', 'Top right'],
              ['Piece C', 'Bottom right'], ['Piece D', 'In box']]
attempt_23 = [['Piece D', 'Bottom right'], ['Piece C', 'In box'],
              ['Piece B', 'Top right'], ['Piece A', 'Top left']]
attempt_24 = [['Piece C', 'Bottom right'], ['Piece D', 'Top left'],
              ['Piece A', 'In box'], ['Piece B', 'In box']]
attempt_25 = [['Piece D', 'Bottom left'], ['Piece B', 'In box'],
              ['Piece C', 'Bottom right'], ['Piece A', 'Top right']]
attempt_26 = [['Piece C', 'Bottom left'], ['Piece B', 'In box'],
              ['Piece A', 'Bottom right'], ['Piece D', 'Top right']]
attempt_27 = [['Piece C', 'Bottom left'], ['Piece D', 'In box'],
              ['Piece A', 'Top left'], ['Piece B', 'Top right']]

# Each of the following data sets is a complete attempt at solving
# the puzzle using all four pieces (so there are no pieces left in the box)

attempt_28 = [['Piece A', 'Bottom left'], ['Piece B', 'Bottom right'],
              ['Piece C', 'Top left'], ['Piece D', 'Top right']]
attempt_29 = [['Piece A', 'Top right'], ['Piece B', 'Bottom right'],
              ['Piece C', 'Top left'], ['Piece D', 'Bottom left']]
attempt_30 = [['Piece A', 'Bottom left'], ['Piece B', 'Top left', 'X'],
              ['Piece C', 'Bottom right'], ['Piece D', 'Top right']]
attempt_31 = [['Piece A', 'Bottom right'], ['Piece B', 'Top right'],
              ['Piece C', 'Bottom left', 'X'], ['Piece D', 'Top left']]
attempt_32 = [['Piece D', 'Top right', 'X'], ['Piece A', 'Bottom left', 'X'],
              ['Piece B', 'Top left'], ['Piece C', 'Bottom right']]
attempt_33 = [['Piece A', 'Top right', 'X'], ['Piece B', 'Bottom right'],
              ['Piece C', 'Top left'], ['Piece D', 'Bottom left', 'X']]

# Here you must provide a list which is the correct solution to
# your puzzle.

# ***** Put the solution to your puzzle in this list
solution = [['Piece A', 'Top left'], ['Piece B', 'Top right'], \
               ['Piece C', 'Bottom left'], ['Piece D', 'Bottom right']]


#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "draw_attempt" function.
#

# Draw the jigsaw pieces as per the provided data set


def draw_section(points, a, b, fill_section=True):
    penup()
    width(a)
    color(b)
    goto(points[0])
    pendown()
    if fill_section:
        begin_fill()
    for point in points:
        goto(point)
    end_fill()

def draw_piece_A(coordinate):
    if  coordinate == "Top left":
        x = -599
        y = 1
    elif coordinate == "Top right":
        x = -299
        y = 1
    elif coordinate == "Bottom left":
        x = -599
        y = -299
    elif coordinate == "Bottom right":
        x = -299
        y = -299
    elif coordinate == "In box":
        x = 200
        y = -150

    
    #Color background
    colormode(255) #sets color saturation(255 all colors)
    width(2)
    penup()
    goto(x, y)
    setheading(0)
    pendown()
    begin_fill() 
    color(238, 233, 233) 
    forward(129) #298
    setheading(90)
    forward(39) #1 side only
    setheading(0)
    forward(41) #left and right side(-2 units)
    setheading(270)
    forward(39)
    setheading(0)
    forward(129) #Bottom right corner of piece
    setheading(90)
    forward(129)
    setheading(180)
    forward(39)
    setheading(90)
    forward(41)
    setheading(0)
    forward(39)
    setheading(90)
    forward(128) #Top right corner
    setheading(180)
    forward(298)
    setheading(270)
    forward(296)
    end_fill()

    
    #Image
    draw_section([[x+298, y+183],[x+174, y+183],[x+111, y+78],[x+57, y+78],\
                  [x+145, y+235],[x+298, y+235],[x+298, y+183]], 2,\
                 (105,105,105), True) #Grey Piece

    draw_section([[x+57, y+78],[x+111, y+78],[x+106, y+69],[x+129, y+26],\
                  [x+129, y],[x+92, y],[x+54, y+69],[x+57, y+78]], 2, (0,0,0)) \
                  #Black Piece


    draw_section([[x+298,y+183],[x+174,y+183],[x+106,y+69],[x+128,y+26]], 4,\
                 (49,79,79), False) #Greenish Gray Border

    draw_section([[x+145,y+235],[x+57,y+78]], 4, (206,206,193), False) #Light Grey Border top left

    draw_section([[x+57,y+78],[x+54,y+69],[x+91,y+1]], 4, (112,138,144), False) #Medium Grey Border bottom left
    
    draw_section([[x+298,y+96],[x+298,y+78],[x+269,y+78],[x+258,y+96]], 2, \
                 (105,105,105)) #Grey Piece right
    draw_section([[x+298,y+78],[x+298,y+45],[x+287,y+45],[x+269,y+78]], 2, \
                 (49,79,79)) #Greenish Grey triangle
    draw_section([[x+258,y+94],[x+287,y+46]], 4, (49,79,79), False) #Greenish Grey border right

        
    penup()
    color('black') #PIECE OUTLINE
    goto(x, y)
    width(2)
    setheading(0)
    pendown()
    forward(129) #298
    setheading(90)
    forward(39) #1 side only
    setheading(0)
    forward(41) #left and right side(-2 units)
    setheading(270)
    forward(39)
    setheading(0)
    forward(129) #Bottom right corner of piece
    setheading(90)
    forward(129)
    setheading(180)
    forward(39)
    setheading(90)
    forward(41)
    setheading(0)
    forward(39)
    setheading(90)
    forward(128) #Top right corner
    setheading(180)
    forward(298)
    setheading(270)
    forward(296)
    



    
    
def draw_piece_B(coordinate):
    if coordinate == "Top left":
        x = -599
        y = 1
    elif coordinate == "Top right":
        x = -299
        y = 1
    elif coordinate == "Bottom left":
        x = -599
        y = -299
    elif coordinate == "Bottom right":
        x = -299
        y = -299
    elif coordinate == "In box":
        x = 200
        y = -150

    colormode(255) #sets color saturation(255 all colors)
    width(2)
    penup()

    goto(x, y) #Color background
    setheading(0)
    pendown()
    color(238, 233, 233)
    begin_fill()
    forward(129)
    setheading(90)
    forward(39)
    setheading(0)
    forward(41)
    setheading(270)
    forward(39)
    setheading(0)
    forward(129) #Bottom right corner
    setheading(90)
    forward(298) #Top right corner
    setheading(180)
    forward(298) #Top left corner
    setheading(270)
    forward(130)
    setheading(180)
    forward(39)
    setheading(270)
    forward(37)
    setheading(0)
    forward(39)
    setheading(270)
    forward(129)
    end_fill()




    draw_section([[x+36,y+235],[x+6,y+183],[x+1,y+183],[x+1,y+235],[x+36,y+235]], 2,\
                 (105,105,105)) #Grey part top

    draw_section([[x+36,y+235],[x+6,y+183],[x+1,y+183]], 4, (49,79,79)) #Greenish Grey part

    draw_section([[x+1,y+95],[x+278,y+95],[x+269,y+78],[x+1,y+78],[x+1,y+95]],\
                 2, (105,105,105,)) #Grey part
    draw_section([[x+1,y+78],[x+1,y+45],[x+27,y+45],[x+35,y+78],[x+1,y+78]], 2,\
                 (49,79,79)) #Greenish Grey Border left bottom
    draw_section([[x+35,y+78],[x+267,y+78],[x+249,y+45],[x+117,y+45],[x+90,y+1],\
                  [x+35,y+1],[x+65,y+45],[x+27,y+45],[x+35,y+78]], 2, (0,0,0)) #Black
    draw_section([[x+278,y+95],[x+249,y+45],[x+117,y+45],[x+92,y+1]],\
                 4, (105,105,105), False) #Grey Border right bottom
    draw_section([[x+65, y+45],[x+37,y+1]], 4, (49,79,79), False) #Greenish 

    penup()
    color('black') #Outline
    goto(x, y)
    width(2)
    setheading(0)
    pendown()
    forward(129)
    setheading(90)
    forward(39)
    setheading(0)
    forward(41)
    setheading(270)
    forward(39)
    setheading(0)
    forward(129) #Bottom right corner
    setheading(90)
    forward(298) #Top right corner
    setheading(180)
    forward(298) #Top left corner
    setheading(270)
    forward(130)
    setheading(180)
    forward(39)
    setheading(270)
    forward(37)
    setheading(0)
    forward(39)
    setheading(270)
    forward(129)



def draw_piece_C(coordinate):
    if coordinate == "Top left":
        x = -599
        y = 1
    elif coordinate == "Top right":
        x = -299
        y = 1
    elif coordinate == "Bottom left":
        x = -599
        y = -299
    elif coordinate == "Bottom right":
        x = -299
        y = -299
    elif coordinate == "In box":
        x = 200
        y = -150

    colormode(255) #sets color saturation(255 all colors)
    width(2)
    penup()

    goto(x, y) #Background color
    setheading(0)
    pendown()
    color(238, 233, 233)
    begin_fill()
    forward(299) #Bottom right corner
    setheading(90)
    forward(129)
    setheading(180) #Start of interlock
    forward(39)
    setheading(90)
    forward(41)
    setheading(0)
    forward(39)
    setheading(90)
    forward(128)
    setheading(180)
    forward(130)
    setheading(90)
    forward(39)
    setheading(180)
    forward(38)
    setheading(270)
    forward(39)
    setheading(180)
    forward(130)
    setheading(270)
    forward(297)
    end_fill()

    draw_section([[x+130,y+324],[x+175,y+253],[x+298,y+253],[x+298,y+206],\
                  [x+146,y+206],[x+92,y+298],[x+130,y+298],[x+130,y+324]],\
                 2, (0,0,0)) #Black
    draw_section([[x+93, y+297],[x+146,y+206],[x+297,y+206]], 4, \
                 (112,138,144),False) # Light Grey Border left
    draw_section([[x+131,y+322],[x+175,y+253],[x+297,y+253]], 4, \
                 (49,79,79), False) #Greenish Grey Border right

    penup()
    color('black') #Outline
    goto(x, y)
    width(2)
    setheading(0)
    pendown()
    forward(299) #Bottom right corner
    setheading(90)
    forward(129)
    setheading(180) #Start of interlock
    forward(39)
    setheading(90)
    forward(41)
    setheading(0)
    forward(39)
    setheading(90)
    forward(128)
    setheading(180)
    forward(130)
    setheading(90)
    forward(39)
    setheading(180)
    forward(38)
    setheading(270)
    forward(39)
    setheading(180)
    forward(130)
    setheading(270)
    forward(297)


def draw_piece_D(coordinate):
    if position == "Top left":
        x = -599
        y = 1
    elif coordinate == "Top right":
        x = -299
        y = 1
    elif coordinate == "Bottom left":
        x = -599
        y = -299
    elif coordinate == "Bottom right":
        x = -299
        y = -299
    elif coordinate == "In box":
        x = 200
        y = -150
    
    colormode(255) #sets color saturation(255 all colors)
    width(2)
    penup()

    goto(x, y) #Background color
    setheading(0)
    pendown()
    color(238, 233, 233)
    begin_fill()
    forward(299) #Bottom right corner
    setheading(90)
    forward(298) #Top right corner
    setheading(180)
    forward(130)
    setheading(90)
    forward(39)
    setheading(180)
    forward(38)
    setheading(270)
    forward(39)
    setheading(180)
    forward(130)
    setheading(270)
    forward(130)
    setheading(180)
    forward(39)
    setheading(270)
    forward(37)
    setheading(0)
    forward(39)
    setheading(270)
    forward(130)
    end_fill()

    draw_section([[x+1,y+253],[x+8,y+253],[x+35,y+297],[x+90,y+297],\
                  [x+50,y+230],[x+117,y+115],[x+248,y+115],[x+276,y+67],\
                  [x+89,y+67],[x+8,y+206],[x+1,y+206],[x+1,y+253]],\
                 2, (0,0,0)) #Black
    draw_section([[x+1, y+253],[x+8,y+253],[x+35,y+297]], 4, (49,79,79), False)\
                        #Greenish Grey left
    draw_section([[x+1,y+206],[x+8,y+206],[x+89,y+67],[x+276,y+67],\
                  [x+248,y+115],[x+117,y+115],[x+50,y+230],[x+90,y+297]],\
                 4, (105,105,105), False) #Light Grey Border right bottom

    penup() #PIECE_D OUTLINE
    width(2)
    color('black') 
    goto(x, y) 
    setheading(0)
    pendown()
    forward(299) #Bottom right corner
    setheading(90)
    forward(298) #Top right corner
    setheading(180)
    forward(130)
    setheading(90)
    forward(39)
    setheading(180)
    forward(38)
    setheading(270)
    forward(39)
    setheading(180)
    forward(130)
    setheading(270)
    forward(130)
    setheading(180)
    forward(39)
    setheading(270)
    forward(37)
    setheading(0)
    forward(39)
    setheading(270)
    forward(130)


def draw_X(coordinate):
    if position == "Top left":
        x = -599
        y = 1
    elif coordinate == "Top right":
        x = -299
        y = 1
    elif coordinate == "Bottom left":
        x = -599
        y = -299
    elif coordinate == "Bottom right":
        x = -299
        y = -299
    elif coordinate == "In box":
        x = 200
        y = -150


    colormode(255) #sets color saturation(255 all colors)
    width(2)
    penup()

    goto(x+90,y+60) #BACKGROUND WHITE
    setheading(0)
    pendown()
    begin_fill()
    color(255,255,255)
    forward(120)
    setheading(90)
    forward(180)
    setheading(180)
    forward(120)
    setheading(270)
    forward(180)
    setheading(0)
    end_fill()
    penup()

    goto(x+100,y+85) #MIDDLE RECTANGLE
    setheading(0)
    width(2)
    color(205,201,201)
    pendown()
    forward(100)
    setheading(90)
    forward(130)
    setheading(180)
    forward(100)
    setheading(270)
    forward(130)
    penup()

    goto(x+130,y+130) #CENTRE SQUARE
    setheading(0)
    color(245,245,245)
    pendown()
    forward(40)
    setheading(90)
    forward(40)
    setheading(180)
    forward(40)
    setheading(270)
    forward(40)
    penup()

    goto(x+133,y+133) #X IN THE MIDDLE
    color(255,0,0)
    pendown()
    setheading(45)
    forward(48)
    penup()
    goto(x+167,y+133)
    setheading(135)
    pendown()
    forward(48)
    penup()
    

    goto(x+90,y+60) #OUTER OUTLINE
    width(4)
    setheading(0)
    color(0,0,0)
    pendown()
    forward(120)
    setheading(90)
    forward(180)
    setheading(180)
    forward(120)
    setheading(270)
    forward(180)
    setheading(0)
    
    
  

        
def draw_attempt(pieces):
    for value in pieces:    #value or variable
        if value[-1] == "X":
            draw_X(value[1])
        elif value[0] == "Piece A":
            draw_piece_A(value[1])
        elif value[0] == "Piece B":
            draw_piece_B(value[1])
        elif value[0] == "Piece C":
            draw_piece_C(value[1])
        elif value[0] == "Piece D":
            draw_piece_D(value[1])
        
            




#
#--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# drawing your jigsaw pieces.  Do not change any of this code except
# where indicated by comments marked '*****'.
#
    
# Set up the drawing canvas
setup(canvas_width, canvas_height)

# Give the canvas a neutral background colour
# ***** You can change the background colour if necessary to ensure
# ***** good contrast with your puzzle pieces
bgcolor('light grey')

# Give the window a title
# ***** Replace this title with one that describes the picture
# ***** produced by solving your puzzle
title('Four Piece Jigsaw Puzzle - Describe your picture here')

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** while the cursor moves around the screen
tracer(True)

# Draw the box that holds unused jigsaw puzzle pieces
draw_box()

# Draw the template that holds the jigsaw pieces
# ***** If you don't want to display the template change the
# ***** argument below to False
draw_template(True)

# Mark the centres of the places where jigsaw puzzle pieces must
# be drawn
# ***** If you don't want to display the coordinates change the
# ***** argument below to False
mark_coords(True)

# Call the student's function to display the attempted solution
# ***** Change the argument to this function to test your
# ***** code with different data sets
draw_attempt(attempt_27)

# Exit gracefully by hiding the cursor and releasing the window
tracer(True)
hideturtle()
done()

#
#--------------------------------------------------------------------#

