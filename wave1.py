"""
Concert venue soundwaves
"""
import turtle
import time
import math

# list of tuples that stores location of all objects
from typing import List, Any

objects = []

# the speed of sound is a constant
speed_of_sound = 340

# distance from speaker to audience
direct_distance = 0

# each tuple in waves list has a list of points where it bounces off the wall
reflect_points = []

# keeps track of how many times the waves bounce off the wall
reflects = 0

# the average distance of the waves that bounce off the wall once from the speaker
bounce_once_avg = 0

# the average distance of the waves that bounce off the wall twice from the speaker
bounce_twice_avg = 0

# length and width initially set as 0, user is asked to enter them
width = 0
length = 0

# angle of wave coming out of the speaker is initially 0
angle = 0

# constant speed of waves
speed = 1

# list of tuples that stores the ((speaker_x,speaker_y,speaker_x,speaker_y,vx,vy, reflects, reflect_points))
waves = []

# x and y position of the speaker
speaker_x = 10
speaker_y = 0


def pressed_keys():
    """
    sig: () -> NoneType
    function for when the user presses the up, down, left, right, 'j', 'i', 'k', or 'l' key
    """
    turtle.color("black")
    global waves
    objects.clear()
    global length
    global width
    global bounce_once_avg
    global bounce_twice_avg
    bounce_once_avg = 0
    bounce_twice_avg = 0
    turtle.clear()
    store_objects()
    turtle.listen()
    init_waves()
    store_objects()
    waves.clear()
    draw_speaker()
    draw_audience()
    turtle.color("black")
    draw_wall()
    turtle.up()
    turtle.goto(-turtle.window_width() / 2 + 10, turtle.window_height() / 2 - 200)
    turtle.down()
    msg = "Press 's' when ready to see new sound waves"
    turtle.write(msg, font=("Arial", 20, "normal"))
    draw_wall()


def key_y():
    """
    sig: ()-> NoneType
    Asks user to re-enter dimensions of concert venue when they press the 'y' key
    """
    global waves
    global bounce_once_avg
    global bounce_twice_avg
    update_input()
    display()
    turtle.clear()
    angle = 0
    waves = []
    bounce_once_avg = 0
    bounce_twice_avg = 0
    turtle.clear()
    draw_wall()
    draw_speaker()
    draw_audience()
    turtle.up()
    turtle.color("black")


def key_s():
    """
    sig: ()-> NoneType
    Re-draws soundwaves when user presses 's'
    """

    global waves
    waves = []
    turtle.clear()
    objects.clear()
    global length
    global width
    store_objects()
    turtle.listen()
    init_waves()
    while len(waves) > 0:
        turtle.clear()
        draw_frame()
        update_waves()
        turtle.update()
        time.sleep(0.1)


# These functions allow user to change the speaker's position

def key_up():
    """
    sig: ()-> NoneType
    Moves speaker up when up arrow is pressed
    """
    global length
    global width
    global speaker_y
    global speaker_init
    draw_wall()
    speaker_init += 5
    speaker_y += 5
    pressed_keys()


def key_left():
    """
    sig: ()-> NoneType
    Moves speaker left when left arrow is pressed
    """
    global length
    global width
    global speaker_x
    global speaker_init
    # speaker_init+=5
    speaker_x -= 5
    pressed_keys()


def key_right():
    """
    sig: ()-> NoneType
    Moves speaker right when right arrow is pressed
    """
    global length
    global width
    global speaker_x
    global speaker_init
    speaker_x += 5
    pressed_keys()


def key_down():
    """
    sig: ()-> NoneType
    Moves speaker down when down arrow is pressed
    """
    global length
    global width
    global speaker_y
    global speaker_init
    speaker_init += 5
    speaker_y -= 5
    pressed_keys()


# These functions allow the user to change audiences location

def key_i():
    """
    sig: ()-> NoneType
    Moves audience up when 'i'is pressed
    """
    global length
    global width
    global audience_y
    global speaker_init
    audience_y += 5
    pressed_keys()


def key_k():
    """
    sig: ()-> NoneType
    Moves audience down when 'k' is pressed
    """
    global length
    global width
    global audience_y
    global speaker_init
    audience_y -= 5
    pressed_keys()


def key_l():
    """
    sig: ()-> NoneType
    Moves audience left when 'l' is pressed
    """
    global length
    global width
    global audience_x
    global speaker_init
    audience_x += 5
    pressed_keys()


def key_j():
    """
    sig: ()-> NoneType
    Moves audience left when 'j' is pressed
    """
    global length
    global width
    global audience_x
    global speaker_init
    # speaker_init+=5
    audience_x -= 5
    pressed_keys()


# These functions draw the concert venue
def draw_wall():
    """
    sig: () -> NoneType
    Draws the wall from length and width entered by user
    """
    y = 0
    x = 0
    global length
    global width
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(length)
        turtle.left(90)


def draw_speaker():
    """
    sig: ()-> NoneType
    draws the speaker
    """
    global speaker_init
    global speaker
    turtle.penup()
    turtle.left(90)
    turtle.color("pink")
    global speaker_x
    global speaker_y
    turtle.forward(speaker_init)
    turtle.right(90)
    turtle.goto(speaker_x - 10, speaker_y)
    turtle.begin_fill()
    for i in range(4):
        turtle.pendown()
        turtle.forward(20)
        turtle.right(90)
    turtle.end_fill()


def draw_audience():
    """
    sig: ()-> NoneType
    draws the audience
    """
    global audience_x
    global audience_y
    turtle.penup()
    turtle.goto(audience_x, audience_y)
    turtle.pendown()
    turtle.color("blue")
    turtle.begin_fill()
    for i in range(4):
        turtle.pendown()
        turtle.forward(20)
        turtle.right(90)
    turtle.end_fill()


def store_objects():
    """
    sig: ()-> NoneType
    Stores location of the walls, speaker, and audience
    """
    global waves
    global xinc
    global yinc
    global speaker_x
    global speaker_y
    global audience_x
    global audience_y
    global length
    global width
    global objects
    objects.append(("Top wall", 0, width, length, length + 1))
    objects.append(("Side wall", width, width + 1, 0, length))
    objects.append(("Top wall", 0, length, 0, 1))
    objects.append(("Side wall", 0, 1, 0, width))
    objects.append(("Audience", audience_x, audience_x + 20, audience_y - 20, audience_y))
    objects.append(("Speaker", 10 + speaker_x, speaker_y, 0, 0))


# These functions draw the soundwaves

def draw_direct_sound():
    """
    sig: ()-> NoneType
    Draws the soundwave from speaker to audience
    """
    global direct_distance
    turtle.color("red")
    turtle.penup()
    turtle.goto(speaker_x, speaker_y)
    turtle.pendown()
    turtle.goto(audience_x, audience_y)


def draw_in_progress_waves():
    """
    sig: () -> NoneType
    Draw all the current soundwaves
    """
    turtle.color("black")
    for (x, y, startx, starty, vx, vy, reflects, reflecting_points) in waves:
        turtle.up()
        turtle.goto(speaker_x, speaker_y)
        turtle.down()
        item = reflecting_points.copy()
        item.insert(0, (startx, starty))
        item.append((x, y))
        for i in range(0, len(item)):
            if item[i] == (0, 0):
                continue
            turtle.goto(item[i])


def update_input():
    """
    sig: ()-> NoneType
    Aks user for length and width, and stores the initial location of the speaker and audience accordingly
    """
    global length
    global width
    global speaker_y
    global speaker_init
    global audience_x
    global audience_y
    # Will multiple length and width by 40 for the purpose of turtle graphics
    turtle.clear()
    length = int(turtle.textinput("length", "Please enter the length of the venue in meters: ")) * 10
    width = int(turtle.textinput("length", "Please enter the width of the venue in meters: ")) * 10
    turtle.listen()
    speaker_y = (width / 2) + 5
    speaker_init = (width / 2) + 5
    audience_x = (length / 2) + 5
    audience_y = (width / 2) + 5


def init_waves():
    """
    sig: ()-> NoneType
    stores the location of all waves as a list of tuples
    """
    global waves
    global speed
    global speaker_x
    global speaker_y
    global init_reflect1
    global init_reflect2
    waves = []
    success_waves = []
    for angle in range(0, 360, 10):
        vx = math.cos(math.radians(angle)) * speed
        vy = math.sin(math.radians(angle)) * speed
        reflect_points = []
        waves.append((speaker_x, speaker_y, speaker_x, speaker_y, vx, vy, reflects, reflect_points))


def update_waves():
    """
    sig: ()-> NoneType
    This function moves the soundwaves and tests if they hit a wall or the audience. If a wave hits the wall, it turns the wave around.
    If a wave hits the audience, it stops moving the wave. If a wave bounces off more than 2 walls, it removes the wave from the
    waves list
    """
    global waves
    global objects
    global success_waves
    q = -1
    count = 0
    for (x, y, startx, starty, vx, vy, reflects, reflecting_points) in waves:
        keeps_going = True
        q += 1
        mylst = reflecting_points
        for i in range(len(objects)):
            count += 1
            # if object hits a wall, turn around and increment reflects
            if (objects[i][1]) <= (x) <= (objects[i][2]) and (objects[i][3]) <= (y) <= (objects[i][4]):
                # myList=reflecting_points
                if reflects < 3:
                    # if the object hits a top wall, change the y velocity
                    if objects[i][0] == "Top wall":
                        vy = -(vy)
                        reflects += 1
                        # for the drawing function to work, python needs to know where the wave hit the wall
                        mylst.append((x, y))
                    # if the object hits a side wall, change the x velocity
                    elif objects[i][0] == "Side wall":
                        vx = -(vx)
                        reflects += 1
                        # for the drawing function to work, python needs to know where the wave hit the wall
                        mylst.append((x, y))
                    # if object hits a wall, turn around and increment reflects
                    elif objects[i][0] == "Audience":
                        if reflects > 0:
                            keeps_going = False
                            break
                        elif reflects == 0:
                            keeps_going = False
                            waves.pop(q)
                            break
                elif reflects >= 3:
                    waves.pop(q)
                    keeps_going = False
                    reflects = 0
        # ensures that waves aren't going outside the concert venue
        if x < -2 or y < -2:
            waves.pop(q)
            reflects = 0
        # advances the waves
        elif keeps_going == True:
            waves[q] = (x + vx, y + vy, speaker_x, speaker_y, vx, vy, reflects, mylst)


# these functions find the times of the reflections

def find_distances():
    """
    sig: ()-> NoneType
    Finds the average distances for the waves reflecting off the walls
    """
    global waves
    global speaker_x
    global speaker_y
    global audience_x
    global audience_y
    one_bounce_xvalues = 0
    one_bounce_yvalues = 0
    one_bounce_count = 0
    two_bounce_count = 0
    two_bounce_xvalues = 0
    two_bounce_yvalues = 0
    global bounce_once_avg
    global bounce_twice_avg
    for i in range(len(waves)):
        for x in range(len(waves[i][7])):
            if len(waves[i][7]) == 1:
                one_bounce_xvalues += waves[i][7][x][0]
                one_bounce_yvalues += waves[i][7][x][1]
                one_bounce_count += 1
            elif len(waves[i][7]) == 2:
                two_bounce_xvalues += waves[i][7][x][0]
                two_bounce_yvalues += waves[i][7][x][1]
                two_bounce_count += 1
    if one_bounce_count > 0:
        bounce_once_avg = (math.sqrt((((one_bounce_xvalues / one_bounce_count) - (speaker_x)) ** 2) + (
                    ((one_bounce_yvalues / one_bounce_count) - (speaker_y)) ** 2))) + (math.sqrt(
            (((one_bounce_xvalues / one_bounce_count) - (audience_x)) ** 2) + (
                        ((one_bounce_yvalues / one_bounce_count) - (audience_y)) ** 2)))
    if two_bounce_count > 0:
        bounce_twice_avg = (math.sqrt((((two_bounce_xvalues / two_bounce_count) - (speaker_x)) ** 2) + (
                    ((two_bounce_yvalues / two_bounce_count) - (speaker_y)) ** 2))) + (math.sqrt(
            (((two_bounce_xvalues / two_bounce_count) - (audience_x)) ** 2) + (
                        ((two_bounce_yvalues / two_bounce_count) - (audience_y)) ** 2)))


def direct_sound_time():
    """
    sig: ()-> NoneType
    Finds the time it takes for direct sound to reach the audience from the speaker
    """
    global audience_x
    global audience_y
    global speaker_x
    global speaker_y
    return (math.sqrt(((speaker_x - audience_x) ** 2) + ((speaker_y - audience_y) ** 2)))


def one_bounce_time():
    """
    sig: ()-> NoneType
    Finds the time of the waves that reflect once
    """
    global bounce_once_avg
    return (bounce_once_avg / 1000) * speed_of_sound


def two_bounces_time():
    """
    sig: ()-> NoneType
    Finds the time of the waves that reflect twice
    """
    global bounce_twice_avg
    return (bounce_twice_avg / 1000) * speed_of_sound


def draw_frame():
    """
    sig: ()-> NoneType
    Draws current frame
    """
    draw_wall()
    draw_speaker()
    draw_audience()
    draw_direct_sound()
    draw_in_progress_waves()
    display()


# displays times of refections and echo warning
def display():
    """
    sig: ()-> NoneType
    Displays the distance time of soundwaves, as well as a potential echo warning. Also displays suggestions to user about how to change sounds
    """
    global bounce_once_avg
    global bounce_twice_avg
    find_distances()
    turtle.up()
    turtle.color("black")
    turtle.goto(-turtle.window_width() / 2 + 10, turtle.window_height() / 2 - 160)
    turtle.down()
    direct = direct_sound_time()
    bounce1 = one_bounce_time()
    bounce2 = two_bounces_time()
    msg1 = "Direct sound time: " + str(direct) + "ms"
    if bounce_once_avg <= 170:
        msg2 = "One bounce soundwaves average distance: " + str(round(bounce_once_avg / 10, 2)) + " m "
    elif bounce_once_avg > 170:
        msg2 = "Echo warning!!!!"
    if bounce_twice_avg <= 170:
        msg3 = "Two bounces soundwaves average distance: " + str(round(bounce_twice_avg / 10, 2)) + " m "
    elif bounce_twice_avg > 170:
        msg3 = "Echo warning!!!!"
    msg4 = "Click y when ready to re-enter dimensions of venue"
    msg11 = "One bounce average time: " + str(round(bounce1, 2)) + " ms"
    msg12 = "Two bounces average time: " + str(round(bounce2, 2)) + "ms"
    msg5 = "Use up, down, left and right arrows to move speaker"
    msg6 = "Use 'i', 'j', 'k', and 'l' keys to move audience"
    msg10 = "Press 's' when ready to see new sound waves"
    msg = "\n".join([msg1, msg2, msg11, msg3, msg12, msg4, msg5, msg6, msg10])
    turtle.write(msg, font=("Arial", 15, "normal"))
    msg8 = "For a richer, fuller sound, adjust venue to increase delay from reflections"
    msg9 = "For a clearer, more direct sound, adjust venue to decrease delay from early reflections"
    msg10 = "To reduce echo, shorten dimensions of the venue"
    msg_2 = "\n".join([msg8, msg9, msg10])
    turtle.up()
    turtle.color("black")
    turtle.goto(-turtle.window_width() / 2 + 10, (-turtle.window_height() / 2) + 10)
    turtle.down()
    turtle.write(msg_2, font=("Arial", 15, "normal"))


def main():
    """
    sig: ()-> NoneType
    Runs program
    """
    update_input()
    store_objects()
    global waves
    init_waves()
    turtle.tracer(0, 0)
    turtle.onkey(key_y, "y")
    turtle.onkey(key_up, "Up")
    turtle.onkey(key_down, "Down")
    turtle.onkey(key_left, "Left")
    turtle.onkey(key_right, "Right")
    turtle.onkey(key_i, "i")
    turtle.onkey(key_k, "k")
    turtle.onkey(key_l, "l")
    turtle.onkey(key_j, "j")
    turtle.onkey(key_s, "s")
    turtle.listen()
    while len(waves) > 0:
        turtle.clear()
        draw_frame()
        update_waves()
        turtle.update()
        time.sleep(0.1)
    turtle.mainloop()


main()
