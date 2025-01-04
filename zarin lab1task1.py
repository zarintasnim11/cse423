

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

# Initial Colors variables
primary_colour = (0, 0, 0)
colour_of_background = (1, 1, 1)

# Rain parameters
rainfall = [] #To store rain co_ordinates
num_drops = 200 #Number of rain drops in the screen
rain_fall_speed = 0.8 #Rain fall speed (used for y)
wind_speed= 1 #Wind speed (used for x)
rain_initialized = False
direction = "straight"
angle_of_rain = 0
size_of_rain = 60

def tri(x1, y1, x2, y2, x3, y3, clr):
    a, b, c = clr
    glColor3f(float(a), float(b), float(c))

    glBegin(GL_TRIANGLES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
    glEnd()

def lines(x1, y1, x2, y2, clr):
    a, b, c = clr
    glColor3f(float(a), float(b), float(c))

    glLineWidth(1.75)
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()


def dark_lines(x1, y1, x2, y2, clr):
    a, b, c = clr
    glColor3f(float(a), float(b), float(c))

    glLineWidth(20)
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()


def points(x1, y1, clr):
    a, b, c = clr
    glColor3f(float(a), float(b), float(c))

    glPointSize(5) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x1,y1) #jekhane show korbe pixel
    glEnd()

def rain(clr):
    a, b, c = clr
    global direction, rainfall, rain_fall_speed, wind_speed, rain_initialized, angle_of_rain, size_of_rain

    if not rain_initialized:
        for i in range(num_drops):
            x = random.randint(0, 1200)
            y = random.randint(0, 800)
            rainfall.append((x, y))
        rain_initialized = True

    new_rainfall = []
    if direction == 'right':
        angle_of_rain = 25
    elif direction == 'left':
        angle_of_rain = -25
    elif direction == 'straight':
        angle_of_rain= 0

    for x, y in rainfall:
        y = y - rain_fall_speed
        if y < 200:
            y = random.randint(800, 2000)

        x_offset = 0
        if direction == 'right':
            x_offset = wind_speed

        elif direction == 'left':
            x_offset = -wind_speed

        x = x + x_offset
        new_rainfall.append((x % 1200, y))

    rainfall = new_rainfall

    for x, y in rainfall:

        lines(x, y + size_of_rain, x + angle_of_rain, y, (a, b, c))


def keyboard_keys(key, x, y):
    global primary_colour, colour_of_background
    if key == b's':
        colour_of_background = (0, 0, 0)
        primary_colour = (1, 1, 1)
    elif key == b'd':
        colour_of_background = (1, 1, 1)
        primary_colour = (0, 0, 0)


def arrow_keys(key, x, y):
    global direction
    if key == GLUT_KEY_RIGHT:
        direction = 'right'
    elif key == GLUT_KEY_LEFT:
        direction = 'left'
    elif key == GLUT_KEY_UP:
        direction = 'straight'
    elif key == GLUT_KEY_DOWN:
        direction = 'straight'


def iterate():
    glViewport(0, 0, 1200, 800)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1200, 0.0, 800, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    global colour_of_background, primary_colour
    a, b, c = colour_of_background
    x, y, z = primary_colour
    glClearColor(a, b, c, 0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()

    rain((x, y, z))
    dark_lines(345, 210,  345, 500, (x, y, z)) #Left line of house
    dark_lines(335, 210, 865, 210, (x, y, z)) #Lower line of house
    dark_lines(855, 210,  855, 500, (x, y, z)) #Right line of house

    tri(345, 210, 345, 510, 855, 210, (a, b, c)) #The  rain not  bypassing through the house
    tri(345, 510, 855, 510, 855, 210, (a, b, c))


    tri(330, 500, 870, 500, 600, 650, (x, y, z)) #Bigger triangle
    tri(360, 508, 840, 508, 600, 640, (a, b, c)) #Smaller Triangle

    lines(400, 210, 400, 380, (x, y, z)) #Door
    lines(400, 380, 500, 380, (x, y, z))
    lines(500, 380, 500, 210, (x, y, z))

    points(490, 295, (x, y, z)) #Doorknob

    lines(650, 350, 750, 350, (x, y, z)) #Window
    lines(750, 350, 750, 450, (x, y, z))
    lines(750, 450, 650, 450, (x, y, z))
    lines(650, 450, 650, 350, (x, y, z))

    lines(700, 350, 700, 450, (x, y, z)) #Window Bar
    lines(650, 400, 750, 400, (x, y, z))

    glutSwapBuffers()


def animate():
    glutPostRedisplay()


# OpenGL initialization
glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1200, 800)
glutInitWindowPosition(0, 0)
glutCreateWindow(b"Rain house: Press s/d for colour change")

# callback functions
glutKeyboardFunc(keyboard_keys)
glutSpecialFunc(arrow_keys)
glutDisplayFunc(showScreen)
glutIdleFunc(animate) #what you want to do in the idle time (when no drawing is occuring)

# Enter the GLUT event processing loop
glutMainLoop()


#Task 222222222222222222222
# from OpenGL.GL import *
# from OpenGL.GLUT import *
# from OpenGL.GLU import *
# import random

# # Initial balls variables
# balls = []
# speed = 0.05
# speed_temp = 0

# background_color = a, b, c = (random.random(), random.random(), random.random())
# spacebar_flag = False

# # Initial Blinking variables
# leftclick_flag = False
# blink_flag = False
# frame_counter = 0
# blink_frame_interval = 5000  #Blinking speed by frames

# def draw_points():
#     global balls, blink

#     for ball in balls:
#         x, y, color, direction_x_axis, direction_y_axis = ball

#         # For blinking
#         if (spacebar_flag == False) and (leftclick_flag == True) and (blink_flag == True):
#             r, g, b = background_color
#         else:
#             r, g, b = color

#         glPointSize(15)
#         glEnable(GL_POINT_SMOOTH)
#         glBegin(GL_POINTS)
#         glColor3f(r, g, b)
#         glVertex2f(x, y)
#         glEnd()

# def keyboard_keys(key, x, y):
#     global speed, spacebar_flag, speed_temp

#     if key == b' ':
#         if spacebar_flag == False:
#             speed_temp = speed
#             speed = 0
#             spacebar_flag = True
#         else:
#             speed = speed_temp
#             spacebar_flag = False

#     glutPostRedisplay()

# def arrow_keys(key, x, y):
#     global speed

#     if key == GLUT_KEY_UP:
#         if speed < 0.25:
#             speed += 0.01
#             print("Speed increased")
#         else:
#             speed = 0.25
#             print("Maximum speed")
#     if key == GLUT_KEY_DOWN:
#         if speed > 0:
#             speed -= 0.01
#             print("Speed decreased")
#         else:
#             speed = 0
#             print("Minimum speed")

#     glutPostRedisplay()

# def mouse(button, state, x, y):
#     global balls, leftclick_flag

#     if button == GLUT_LEFT_BUTTON:
#         if (state == GLUT_DOWN) and (not spacebar_flag):
#             leftclick_flag = not leftclick_flag

#     if button == GLUT_RIGHT_BUTTON:
#         if (state == GLUT_DOWN) and (not spacebar_flag):
#             direction_x_axis = random.choice([-1, 1])
#             direction_y_axis = random.choice([-1, 1])
#             color = (random.random(), random.random(), random.random())
#             balls.append((x, 500 - y, color, direction_x_axis, direction_y_axis))

# def animate():
#     global balls, speed, frame_counter, blink_flag

#     frame_counter += 1
#     if frame_counter >= blink_frame_interval:
#         frame_counter = 0
#         blink_flag = not blink_flag

#     for ball in range(len(balls)):
#         x, y, color, direction_x_axis, direction_y_axis = balls[ball]

#         x = (x + speed * direction_x_axis)
#         y = (y + speed * direction_y_axis)

#         if y > 500:  # Upper border boundary reflection
#             direction_y_axis = -1
#             y = y - speed
#         elif y < 0:  # Lower border boundary reflection
#             direction_y_axis = 1
#             y = y + speed
#         elif x > 1000:  # Right border boundary reflection
#             direction_x_axis = -1
#             x = x - speed
#         elif x < 0:  # Left border boundary reflection
#             direction_x_axis = 1
#             x = x + speed

#         balls[ball] = x, y, color, direction_x_axis, direction_y_axis

#     glutPostRedisplay()

# def iterate():
#     glViewport(0, 0, 1000, 500)
#     glMatrixMode(GL_PROJECTION)
#     glLoadIdentity()
#     glOrtho(0, 1000, 0, 500, 0, 1)
#     glMatrixMode(GL_MODELVIEW)
#     glLoadIdentity()

# def showScreen():
#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#     glLoadIdentity()
#     iterate()
#     glClearColor(a, b, c, 0)

#     draw_points()

#     glutSwapBuffers()

# # OpenGL initialization
# glutInit()
# glutInitDisplayMode(GLUT_RGBA)
# glutInitWindowSize(1000, 500)
# glutInitWindowPosition(0, 0)
# glutCreateWindow(b"The Amazing Box with random backgrounds")

# # Registering callback functions
# glutMouseFunc(mouse)
# glutKeyboardFunc(keyboard_keys)
# glutSpecialFunc(arrow_keys)
# glutDisplayFunc(showScreen)
# glutIdleFunc(animate) #what you want to do in the idle time (when no drawing is occuring)

# # Enter the GLUT event processing loop
# glutMainLoop()
