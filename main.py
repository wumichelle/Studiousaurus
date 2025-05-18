from tkinter import *
from time import *
from random import *
from math import *
import os
from time import time, strftime, localtime
from tkinter import colorchooser
from datetime import datetime
import re
from datetime import datetime, timedelta
from collections import defaultdict


root = Tk()

screen = Canvas(root, width=900, height=800, background="#90afe0")
screen.pack()

#stopwatch global variables:

stopwatch_running = False
stopwatch_start_time = 0
stopwatch_elapsed_time = 0
stopwatch_label = None

#Pomodoro global variables:
countdown_job = None
paused_time = None
current_message_id = None
remove_message_job = None
motivational_dino_id = None
pomodoro_countdown_time = 0
dancing_dino_id = None
dancing_animation_job = None
dino_toggle = True

# #calendar global variables:
# calendar_entry=0

def importImages():
    global dino, Bg, coin, timesup, startstudying, timelobby, shop1, motivationaldino, marketBg1, marketBg2, marketBg3, marketBg4, timerbackground, pomodorosettings, pomodoroupdatebg, adancingdino, bdancingdino, regulartimebackground, rewardsScreenI, backB, statsB, shopB, generic, coinBanner, titleScreen
    dino = PhotoImage(file = "dinos.png")
    Bg = PhotoImage(file = "meadows.png")
    timesup = PhotoImage(file="timesup.png")
    startstudying = PhotoImage(file = "startstudying.png")
    timelobby = PhotoImage(file = "timelobby.png")
    shop1 = PhotoImage(file = "shop1.png")
    motivationaldino = PhotoImage(file = "motivationaldino.png")
    marketBg1 = PhotoImage(file = "marketScreen1.png")
    marketBg2 = PhotoImage(file = "marketScreen2.png")
    marketBg3 = PhotoImage(file = "marketScreen3.png")
    marketBg4 = PhotoImage(file = "marketScreen4.png")
    timerbackground = PhotoImage(file = "timerbackground.png")
    pomodorosettings = PhotoImage(file = "pomodorosettings.png")
    pomodoroupdatebg = PhotoImage(file = "pomodoroupdatebg.png")
    regulartimebackground = PhotoImage(file = "regulartimebackground.png")
    adancingdino = PhotoImage(file = "adancingdino.png").subsample(4) # resize by factor of 2
    bdancingdino = PhotoImage(file = "bdancingdino.png").subsample(4)
    rewardsScreenI = PhotoImage(file = "rewardsScreenI.png")
    backB = PhotoImage(file = "backB.png")
    statsB = PhotoImage(file = "statsB.png")
    shopB = PhotoImage(file = "shopB.png")
    generic = PhotoImage(file = "generic.png")
    coinBanner = PhotoImage(file = "coinBanner.png")
    titleScreen = PhotoImage(file = "titleScreen.png")
    
def importMarketImages():
    global marketImages, buyScreen, zzzs, pearls, pinkspikes, witchshat, flowerclip, magichat, bandana, greenspikes, balloons, cowboyhat, partyhat, cactusback, princess, lotus, fairywings, mesozoic, broke, buyI, equip, equipped
    buyScreen = PhotoImage(file = "buyScreen.png")
    zzzs = PhotoImage(file = "zzzs.png")
    pearls = PhotoImage(file = "pearls.png")
    pinkspikes = PhotoImage(file = "pinkspikes.png")
    witchshat = PhotoImage(file = "witchshat.png")
    flowerclip = PhotoImage(file = "flowerclip.png")
    magichat = PhotoImage(file = "magichat.png")
    bandana = PhotoImage(file = "bandana.png")
    greenspikes = PhotoImage(file = "greenspikes.png")
    balloons  = PhotoImage(file = "balloons.png")
    cowboyhat = PhotoImage(file = "cowboyhat.png")
    partyhat = PhotoImage(file = "partyhat.png")
    cactusback = PhotoImage(file = "cactus.png")
    princess = PhotoImage(file = "princess.png")
    lotus = PhotoImage(file = "lotus.png")
    fairywings = PhotoImage(file = "fairywings.png")
    mesozoic = PhotoImage(file = "mesozoic.png")
    broke = PhotoImage(file = "broke.png")
    buyI = PhotoImage(file = "buy.png")
    equip = PhotoImage(file = "equip.png")
    equipped = PhotoImage(file = "equipped.png")
    
    marketImages = [zzzs, pearls, pinkspikes, witchshat, flowerclip, magichat, bandana, greenspikes, balloons, cowboyhat, partyhat, cactusback, princess, lotus, fairywings, mesozoic]

def importDinoImages():
    global dinoImages, zzzs2, pearls2, pinkspikes2, witchshat2, flowerclip2, magichat2, bandana2, greenspikes2, balloon2, cowboyhat2, partyhat2, cactusback2, princess2, lotus2, fairywings2, mesozoic2
    zzzs2 = PhotoImage(file = "zzzs2.png")
    pearls2 = PhotoImage(file = "pearls2.png")
    pinkspikes2 = PhotoImage(file = "pinkspikes2.png")
    witchshat2 = PhotoImage(file = "witchshat2.png")
    flowerclip2 = PhotoImage(file = "flowerclip2.png")
    magichat2 = PhotoImage(file = "magichat2.png")
    bandana2 = PhotoImage(file = "bandana2.png")
    greenspikes2 = PhotoImage(file = "greenspikes2.png")
    balloon2  = PhotoImage(file = "balloon2.png")
    cowboyhat2 = PhotoImage(file = "cowboyhat2.png")
    partyhat2 = PhotoImage(file = "partyhat2.png")
    cactusback2 = PhotoImage(file = "cactus2.png")
    princess2 = PhotoImage(file = "princess2.png")
    lotus2 = PhotoImage(file = "lotus2.png")
    fairywings2 = PhotoImage(file = "fairywings2.png")
    mesozoic2 = PhotoImage(file = "mesozoic2.png")

    dinoImages = [zzzs2, pearls2, pinkspikes2, witchshat2, flowerclip2, magichat2, bandana2, greenspikes2, balloon2, cowboyhat2, partyhat2, cactusback2, princess2, lotus2, fairywings2, mesozoic2]
    
def setInitialValues():
    global coins, color, marketItems, itemsPrice, ownedItems, Accessories, cointext, titleScreen
    importImages()
    try:
        with open("coins.txt", 'r') as file:
            coins = int(file.read() or 0)
    except FileNotFoundError:
        # If file doesn't exist, start at 0 coins and create the file
        coins = 0
        with open("coins.txt", 'w') as file:
            file.write(str(coins))
    # coins=
    color = "pink"
    marketItems = ["ZZZs","Pearls", "Pink Spikes", "Witch's Hat", "Flower Clip", "Magic Hat", "Bandana", "Green Spikes", "Balloons", "Cowboy Hat", "Party Hat", "Cactus Back", "Princess Ensemble", "Lotus Flower", "Fairy Wings", "Mesozoic Era"]
    ownedItems = []
    itemsPrice = [3,5,7,8,9,9,10, 10,12,15,15,25,30,35,40,45]
    Accessories = False
    cointext = screen.create_text(72, 90, text = str(coins), fill = "#521b66", font = "MS 16", anchor = CENTER)
    title = screen.create_image(450,400, image = titleScreen)
    screen.update()
    sleep(2)
    screen.delete(title)
    startScreen()
    

dinocoordinates = [355, 398, 355, 411, 355, 425, 356, 439, 358, 450, 362, 460, 369, 468, 378, 475, 388, 481, 380, 475, 388, 481, 394, 484, 400, 486, 409, 486, 417, 487, 424, 487, 434, 486, 443, 487, 451, 487, 458, 487, 465, 486, 474, 486, 484, 486, 493, 486, 502, 487, 511, 487, 518, 487, 525, 486, 535, 487, 543, 488, 553, 493, 560, 498, 564, 504, 569, 511, 573, 520, 574, 520, 577, 530, 580, 537, 583, 545, 587, 554, 591, 561, 596, 568, 600, 574, 607, 578, 615, 584, 622, 586, 631, 588, 637, 591, 641, 592, 638, 598, 634, 605, 628, 608, 620, 612, 613, 615, 607, 618, 600, 618, 593, 617, 585, 614, 578, 611, 574, 608, 569, 604, 567, 598, 564, 597, 562, 592, 557, 597, 556, 605, 556, 607, 554, 617, 553, 624, 551, 632, 550, 639, 549, 645, 548, 651, 547, 658, 544, 670, 544, 678, 542, 681, 540, 685, 536, 690, 531, 694, 525, 695, 520, 697, 515, 693, 510, 688, 509, 684, 509, 679, 509, 672, 508, 664, 508, 659, 507, 653, 505, 651, 501, 657, 497, 660, 493, 667, 488, 672, 484, 673, 480, 673, 474, 667, 473, 664, 471, 659, 470, 654, 470, 648, 470, 644, 470, 638, 469, 631, 463, 626, 455, 624, 444, 624, 438, 624, 430, 625, 422, 625, 416, 625, 411, 625, 413, 637, 413, 644, 413, 651, 410, 658, 409, 668, 405, 677, 402, 681, 398, 686, 396, 692, 388, 694, 377, 694, 374, 685, 369, 677, 367, 667, 365, 663, 360, 671, 355, 677, 348, 681, 340, 679, 334, 673, 331, 666, 329, 657, 330, 646, 329, 635, 329, 624, 328, 613, 328, 604, 328, 595, 329, 588, 330, 580, 330, 573, 330, 570, 327, 564, 323, 560, 321, 552, 318, 545, 316, 537, 315, 531, 315, 524, 315, 517, 314, 511, 315, 503, 315, 495, 315, 485, 314, 478, 315, 466, 315, 454, 316, 443, 315, 437, 315, 427, 316, 414, 316, 406, 315, 403, 315, 394, 314, 388, 313, 383, 310, 379, 310, 377, 303, 380, 297, 384, 291, 385, 287, 387, 281, 387, 274, 387, 268, 386, 264, 383, 260, 375, 258, 367, 258, 359, 260, 352, 261, 346, 264, 338, 269, 330, 271, 324, 278, 317, 287, 310, 295, 305, 304, 301, 307, 300, 314, 300, 321, 301, 328, 306, 335, 311, 340, 317, 345, 321, 351, 330, 355, 337, 357, 343, 357, 350, 358, 358, 357, 367, 357, 374, 357, 381, 356, 390, 355, 398, 355, 406,]

def startScreen():
    #stopDancingDino()
    importImages()
    importDinoImages()
    
   
    global dino_polygon_id, Accessories, accessories, coins, cointext, color, rewardsScreenI
    screen.delete(rewardsScreenI)
    screen.create_image(450, 400, image = mesozoic2)
    
    dino_polygon_id = screen.create_polygon(dinocoordinates , fill=color, width=0)
    screen.create_image(450, 500, image = dino)
    
    screen.create_image(55,325, image = shopB)
    #screen.create_image(55,405, image = statsB)
    
    screen.create_image(55, 90, image = coinBanner)

    
###### Colour picker 
    screen.create_rectangle(700, 50, 850, 100, fill="DarkSeaGreen1", outline="black", tags="color_picker")
    screen.create_text(775, 75, text="Pick Colour", font=("Arial", 14), tags="color_picker_text")
    
###### 
    root.bind("<Button-1>", startScreenClick)
    
    screen.create_image(450,400, image = startstudying)
    if Accessories == True:
        if accessories != mesozoic2:
            #print(accessories)
            screen.create_image(450,500, image = accessories)
    
    # # GRID LINES
    # spacing = 25

    # for x in range(25, 1000, spacing): 
    #     screen.create_line(x, 25, x, 1000, fill="white")
    #     screen.create_text(x, 5, text=str(x), font="Times 5", anchor = N, fill="black")
    
    # for y in range(25, 1000, spacing):
    #     screen.create_line(25, y, 1000, y, fill="white")
    #     screen.create_text(5, y, text=str(y), font="Times 5", anchor = W, fill="black")
    
    
      #cointext and banner
    screen.delete (cointext)
    cointext = screen.create_text(72, 90, text = str(coins), fill = "#521b66", font = "MS 16", anchor = CENTER)
    
    
    
def startScreenClick(event):
    xMouse = event.x
    yMouse = event.y
    
    # Check if click is on the "Pick Color" box
    if 700 <= xMouse <= 850 and 50 <= yMouse <= 100:
        open_color_picker(event)
        return
    
    if 200 <= xMouse <= 700 and 150 <= yMouse <= 250:
        timeLobby()
    elif 30 <= xMouse <= 80 and 300 <= yMouse <= 350:
        marketScreen1()
    # elif 30 <= xMouse <= 80 and 380<= yMouse <= 430:
    #     statsScreen()
 
######################################################## 
#dancing dino for pomodoro timer
########################################################       
# def animateDancingDino():
#     global dancing_dino_id, dino_toggle, dancing_animation_job, dino_img
    
    

    # if dancing_dino_id:
    #     screen.delete(dancing_dino_id)

    # # Alternate between the two dino images
    # dino_img = bdancingdino if dino_toggle else adancingdino
    # dino_toggle = not dino_toggle

    # # Display the dino
    # dancing_dino_id = screen.create_image(450, 550, image=dino_img)

    # # Keep animating every 400ms
    # dancing_animation_job = root.after(400, animateDancingDino)
    
# def stopDancingDino():
#     global dancing_dino_id, dancing_animation_job, dino_img
#     screen.delete("dino_img")
#     # if dancing_animation_job:
#     #     root.after_cancel(dancing_animation_job)
#     #     dancing_animation_job = None
#     # if dancing_dino_id:
#     #     screen.delete(dancing_dino_id)
#     #     dancing_dino_id = None
        
######################################################## 
#colour picking for dino
########################################################


def choose_color_from_wheel():
    global color
    color = colorchooser.askcolor(title="Choose a color")  # Returns (RGB tuple, hex string)
    if color[1]:  # color[1] is the hex like "#ff00ff"
        return color[1]
    return None
    
def open_color_picker(event):
    color = colorchooser.askcolor(title="Choose a color")[1]
    if color:
        screen.itemconfig(dino_polygon_id, fill=color)
    
########################################################

def timeLobby():
    #stopDancingDino()
    importImages()
    
    screen.create_image(450,400,image = timelobby)
    # screen.create_rectangle(260, 360, 675, 460, fill = "blue")
    # screen.create_rectangle(220, 500, 560, 600, fill = "red")
    # screen.create_rectangle(160, 155, 250, 260, fill = "yellow")
    # screen.create_rectangle(600, 500, 700, 600, fill = "purple")
    
    
    root.bind("<Button-1>", timeLobbyClick)
    
    
def timeLobbyClick(event):
    global timertype
    xMouse = event.x
    yMouse = event.y
    
    
    if 260 <= xMouse <= 675 and 360 <= yMouse <= 460:
        timertype = "Stopwatch"
        stopwatch()
    elif 225 <= xMouse <= 560 and 480 <= yMouse <= 612:
        timerScreen()
    elif 600 <= xMouse <= 725 and 500 <= yMouse <= 600:
        calendarScreen()
    elif 160 <= xMouse <= 250 and 155 <= yMouse <= 260:
        timertype = "Pomodoro Timer"
        screen.delete("all")
        startScreen()
########################################################
#motivational messages 
########################################################
motivational_messages = [
    "Keep going, Dino-Champ!",
    "You're crushing it like a T-Rex!",
    "Stay sharp like a Velociraptor!",
    "Don't stop now—roar through your goals!",
    "Stomp your stress away!",
    "One fossil step at a time!",
    "Dino-sized effort for dino-sized dreams!",
    "Roaring quietly—your focus is powerful!",
    "Just like fossils—good work takes time!",
    "Making history, one dino-step at a time!",
]

def show_random_message():
    global current_message_id, remove_message_job, motivational_dino_id
    importImages()
    # Remove the old message and dino image if still visible
    if current_message_id:
        screen.delete(current_message_id)
        current_message_id = None
    if motivational_dino_id:
        screen.delete(motivational_dino_id)
        motivational_dino_id = None
    if remove_message_job:
        root.after_cancel(remove_message_job)
        remove_message_job = None

    # Show the dino image and message
    motivational_dino_id = screen.create_image(450, 300, image=motivationaldino)
    message = choice(motivational_messages)
    current_message_id = screen.create_text(530, 610, text=message, font=("Arial", 18, "bold"), fill="darkgreen")

    def remove_message():
        global current_message_id, remove_message_job, motivational_dino_id
        if current_message_id:
            screen.delete(current_message_id)
            current_message_id = None
        if motivational_dino_id:
            screen.delete(motivational_dino_id)
            motivational_dino_id = None
    # 🛠 Restore background if in regular timer
        if timertype == "Timer":
            screen.create_image(450, 400, image=regulartimebackground, tags="regulartimebackground")
            screen.lower("regulartimebackground")
    
        remove_message_job = None

    # Make sure this line is included:
    remove_message_job = root.after(2000, remove_message)

########################################################
#STOPWATCH CODE
########################################################

def stopwatch():
    global stopwatch_label, stopwatch_state, stopwatch_elapsed_time, generic, backB
    
    stopwatch_state = "INIT"
    stopwatch_elapsed_time = 0

    screen.delete("all")
    #screen.create_rectangle(100, 100, 800, 700, fill="white")
    screen.create_image(450, 400, image=generic)
    screen.create_image(110, 95, image = backB)
    screen.create_text(450, 230, text="Stopwatch", font=("Helvetica 20 bold", 28, "bold"), fill="black")

    stopwatch_label = screen.create_text(450, 290, text="00:00:00", font=("Helvetica 20 bold", 40), fill="black")

    # Show the initial big start button
    screen.create_rectangle(300, 400, 600, 470, fill="wheat1", outline="DarkGoldenrod4", width=3, tags="start_btn")
    screen.create_text(450, 435, text="Start", font=("Helvetica", 20), tags="start_btn")

    root.bind("<Button-1>", stopwatchClick)

def stopwatchClick(event):
    global stopwatch_state

    x, y = event.x, event.y
    
    if 80 <= x <= 130 and 80 <= y <= 110:
        screen.delete("all")
        timeLobby()
        return

    if stopwatch_state == "INIT":
        if 300 <= x <= 600 and 400 <= y <= 470:
            startStopwatch()
            showStopwatchControls()

    elif stopwatch_state == "RUNNING":
        if 350 <= x <= 550 and 400 <= y <= 450:  # Pause
            pauseStopwatch()
        elif 350 <= x <= 550 and 470 <= y <= 520:  # End Session
            endStopwatchSession()

    elif stopwatch_state == "PAUSED":
        if 350 <= x <= 550 and 400 <= y <= 450:  # Resume
            resumeStopwatch()
        elif 350 <= x <= 550 and 470 <= y <= 520:  # End Session
            endStopwatchSession()
def showStopwatchControls():
    screen.delete("start_btn")
    # Pause / Resume button
    screen.create_rectangle(350, 400, 550, 450, fill="lightcoral", outline="black", tags="break_resume_btn")
    screen.create_text(450, 425, text="Pause", font=("Helvetica", 16), tags="break_resume_btn")

    # End Session button
    screen.create_rectangle(350, 470, 550, 520, fill="gray", outline="black", tags="end_btn")
    screen.create_text(450, 495, text="End Session", font=("Helvetica", 16), tags="end_btn")

def updateStopwatch():
    global stopwatch_start_time, stopwatch_elapsed_time, update_job

    if stopwatch_state == "RUNNING":
        elapsed = time() - stopwatch_start_time + stopwatch_elapsed_time
        mins = int(elapsed // 60)
        secs = int(elapsed % 60)
        millis = int((elapsed - int(elapsed)) * 100)
        screen.itemconfig(stopwatch_label, text=f"{mins:02}:{secs:02}:{millis:02}")
        update_job = root.after(50, updateStopwatch)
        
def format_time(seconds): #introducing new code
    mins = int(seconds // 60)
    secs = int(seconds % 60)
    millis = int((seconds - int(seconds)) * 100)
    return f"{mins:02}:{secs:02}:{millis:02}"
        
    
def startStopwatch():
    global stopwatch_start_time, stopwatch_state
    stopwatch_state = "RUNNING"
    stopwatch_start_time = time()
    updateStopwatch()

def pauseStopwatch():
    global stopwatch_state, stopwatch_elapsed_time, update_job
    stopwatch_state = "PAUSED"
    stopwatch_elapsed_time += time() - stopwatch_start_time
    if update_job:
        root.after_cancel(update_job)
    screen.itemconfig(stopwatch_label, text="PAUSED")
    # Update button to Resume
    screen.delete("break_resume_btn")
    screen.create_rectangle(350, 400, 550, 450, fill="wheat1", outline="DarkGoldenrod4", width=3, tags="break_resume_btn")
    screen.create_text(450, 425, text="Resume", font=("Helvetica", 16), tags="break_resume_btn")

def resumeStopwatch():
    global stopwatch_start_time, stopwatch_state
    stopwatch_state = "RUNNING"
    stopwatch_start_time = time()
    updateStopwatch()
    # Update button to Pause
    screen.delete("break_resume_btn")
    screen.create_rectangle(350, 400, 550, 450, fill="lightcoral", outline="black", tags="break_resume_btn")
    screen.create_text(450, 425, text="Pause", font=("Helvetica", 16), tags="break_resume_btn")

# def endStopwatchSession():
#     global stopwatch_state, update_job
#     stopwatch_state = "INIT"
#     if update_job:
#         root.after_cancel(update_job)
#     screen.itemconfig(stopwatch_label, text="SESSION ENDED")

def endStopwatchSession():
    global stopwatch_state, update_job, stopwatch_elapsed_time, stopwatch_start_time, total_time

    # Compute total time before resetting state
    if stopwatch_state == "RUNNING":
        total_time = time() - stopwatch_start_time + stopwatch_elapsed_time
    else:
        total_time = stopwatch_elapsed_time

    # Cancel update loop
    if update_job:
        root.after_cancel(update_job)

    # Format and display
    formatted_time = format_time(total_time)
    screen.itemconfig(stopwatch_label, text=f"SESSION ENDED\n{formatted_time}")

    # Save to file
    log_line = f"{strftime('%Y-%m-%d %H:%M:%S', localtime())} - Session Time: {formatted_time}\n"
    with open("stopwatch_log.txt", "a") as file:
        file.write(log_line)

    # Reset state and data
    stopwatch_state = "INIT"
    stopwatch_elapsed_time = 0
    rewardsScreen()

########################################################  
#Code for timer
########################################################

def timerScreen():
    #stopDancingDino()
    screen.delete("all")
    importImages()  # make sure timerbackground is loaded

    global timer_bg_id
    timer_bg_id = screen.create_image(450, 400, image=timerbackground)


    #screen.create_rectangle(100, 100, 800, 700, fill = "sky blue")
    # screen.create_rectangle(225, 300, 400, 400, fill = "blue")
    # screen.create_rectangle(500, 300, 675, 400, fill = "red")
    # screen.create_rectangle(80, 80, 130, 110, fill = "yellow")
    
    root.bind("<Button-1>", timerScreenClick)

def timerScreenClick(event):
    global timertype
    xMouse = event.x
    yMouse = event.y

    if 80 <= xMouse <= 130 and 80 <= yMouse <= 110:
        screen.delete("all")
        timeLobby()
    elif 200 <= xMouse <= 405 and 408 <= yMouse <= 475:
        timertype = "Timer"
        screen.delete("all")
        timerSettings()
    elif 470 <= xMouse <= 750 and 408 <= yMouse <= 475:
        timertype = "Pomodoro Timer"
        screen.delete("all")
        pomodoroSettings()
        
    

def timerSettings():
    global studytime_entry, regulartimebackground
    
    screen.delete("all")
    
    #creen.create_text(450, 180, text="Set Your Timer", font=("Arial", 24, "bold"), fill="white")
    
    
    screen.create_image(450, 400, image=regulartimebackground, tags="regulartimebackground")
    #screen.create_rectangle(100, 100, 800, 700, fill="yellow")
    #screen.create_text(450, 180, text="Set Your Timer", font=("Arial", 24, "bold"))
    screen.create_text(300, 350, text="Subject:", font=("Arial", 16), fill="white")
    screen.create_text(300, 410, text="Study (min):", font=("Arial", 16), fill="white")

    subject_entry = Entry(root)
    studytime_entry = Entry(root)

    screen.create_window(450, 350, window=subject_entry, width=120)
    screen.create_window(450, 410, window=studytime_entry, width=120)
    

    screen.create_rectangle(375, 500, 525, 550, fill="#91734c")# Pink button
    screen.create_text(450, 525, text = "Continue:", font = ("Arial", 20), fill = "white")

    # Back button
    # screen.create_rectangle(80, 80, 130, 110, fill="yellow")
    # screen.create_text(105, 95, text="Back")

    root.bind("<Button-1>", timerSClick)
    
    # global study_minutes
    # 
        
    root.bind("<Button-1>", timerSClick)

def timerSClick(event):
    global timertype, study_time, studytime_entry, timerStart

    xMouse = event.x
    yMouse = event.y

    if 410 <= xMouse <= 525 and 525 <= yMouse <= 650:
        if timertype == "Timer":
            screen.delete("all")
            study_time = int(studytime_entry.get())  
            timerStart = "OFF"
            timer()
            # try:
            # except:
            #     screen.create_text(450, 430, text="Please enter a valid number", fill="red")
        elif timertype == "Pomodoro Timer":
            screen.delete("all")
            pomodoro()
    elif 80 <= xMouse <= 130 and 80 <= yMouse <= 110:
        screen.delete("all")
        timerScreen()


#code for timer
def timer():
    global countdown_time, timer_label, study_time, timerStart, regulartimebackground
    screen.delete("all")
    screen.create_image(450, 400, image=regulartimebackground, tags="regulartimebackground")
    #screen.lower("regulartimebackground")  # This makes sure it's behind all other elements

  #  screen.create_rectangle(100, 100, 800, 700, fill="sky blue")
    #screen.create_rectangle(80, 80, 130, 110, fill="yellow")
    
    # GRID LINES
    spacing = 25
    
    # for x in range(25, 1000, spacing): 
    #     screen.create_line(x, 25, x, 1000, fill="white")
    #     screen.create_text(x, 5, text=str(x), font="Times 5", anchor = N, fill="black")
    
    # for y in range(25, 1000, spacing):
    #     screen.create_line(25, y, 1000, y, fill="white")
    #     screen.create_text(5, y, text=str(y), font="Times 5", anchor = W, fill="black")
    #screen.create_text(450, 200, text="Timer Running", font=("Arial", 24, "bold"), fill="white")

    # Set countdown_time ONCE here
    countdown_time = study_time #* 60
    
    if timerStart == "OFF":
        screen.create_rectangle(350, 300, 550, 350, fill = "white")
        screen.create_text(400, 325, text = "START", font = ("Arial", 15, "bold"), fill = "hot pink")
    # else:
    #     screen.create_rectangle(350, 300, 550, 350, fill = "white")
    #     screen.create_text(400, 325, text = "STOP", font = ("Arial", 15, "bold"), fill = "pink")
    #     screen.create_rectangle(350, 370, 550, 420, fill = "white")
    #     screen.create_text(400, 395, text = "BREAK", font = ("Arial", 15, "bold"), fill = "pink")

    # Show the time immediately before clicking start
    mins = countdown_time // 60
    secs = countdown_time % 60
    global timer_label
    timer_label = screen.create_text(450, 470, text=f"{mins:02}:{secs:02}", font=("Helvetica", 30), fill="black")

    screen.tag_bind("back_button", "<Button-1>", lambda e: timeLobby())
    screen.tag_bind("start_button", "<Button-1>", lambda e: startCountdown())
    root.bind("<Button-1>", timerClick)
    
def timerClick(event):
    xMouse = event.x
    yMouse = event.y
    if 80 <= xMouse <= 130 and 80 <= yMouse <= 110:
        screen.delete("all")
        timeLobby()
    elif 350 <= xMouse <= 550 and 300 <= yMouse <= 350:
        if timerStart == "OFF":
            startCountdown()
        else:
            stopCountdown()
    elif 350 <= xMouse <= 550 and 370 <= yMouse <= 420:
        if timerStart == "ON":
            breakCountdown()
        
# def startCountdown():
#     global countdown_job, paused_time, timerStart
#     try:
#         paused_time = None
#         if countdown_job is not None:
#             root.after_cancel(countdown_job)
#         timerStart = "ON"
#         updateCountdown()
#     except:
#         screen.itemconfig(timer_label, text="Invalid input")

def startCountdown():
    global countdown_job, paused_time, timerStart, timer_start_time
    try:
        paused_time = None
        if countdown_job is not None:
            root.after_cancel(countdown_job)
        timerStart = "ON"
        timer_start_time = time()  # <- RECORD the start time
        updateCountdown()
    except:
        screen.itemconfig(timer_label, text="Invalid input")

        
#new code save to same file (hopefully)
def log_session_to_file(session_type, duration_seconds):
    formatted_time = format_time(duration_seconds)
    log_line = f"{strftime('%Y-%m-%d %H:%M:%S', localtime())} - {session_type} Session Time: {formatted_time}\n"
    with open("stopwatch_log.txt", "a") as file:
        file.write(log_line)

# def stopCountdown():
#     global countdown_job, paused_time, timerStart
#     if countdown_job is not None:
#         root.after_cancel(countdown_job)
#         countdown_job = None
#         paused_time = countdown_time
#     screen.itemconfig(timer_label, text="SESSION ENDED")
#     rewardsScreen()

# def stopCountdown():
#     global countdown_job, paused_time, timerStart, study_time
#     if countdown_job is not None:
#         root.after_cancel(countdown_job)
#         countdown_job = None
#         paused_time = countdown_time

#     # Calculate total study duration (time studied = total time - remaining)
#     duration_seconds = (study_time * 60) - countdown_time
#     log_session_to_file("Timer", duration_seconds)

#     screen.itemconfig(timer_label, text="SESSION ENDED")
#     rewardsScreen()

# def stopCountdown():
#     global countdown_job, paused_time, timerStart, study_time, countdown_time

#     if countdown_job is not None:
#         root.after_cancel(countdown_job)
#         countdown_job = None

#     timerStart = "OFF"

#     # Make sure values are valid
#     try:
#         total_seconds = study_time * 60
#         remaining_seconds = countdown_time if countdown_time is not None else 0
#         duration_seconds = max(0, total_seconds - remaining_seconds)

#         # Safety cap: no 300-hour sessions by accident
#         if duration_seconds > 60 * 60 * 12:  # more than 12 hours
#             duration_seconds = 0

#         log_session_to_file("Timer", duration_seconds)

#     except Exception as e:
#         print("Error logging session:", e)
#         log_session_to_file("Timer", 0)

#     screen.itemconfig(timer_label, text="SESSION ENDED")
#     rewardsScreen()

def stopCountdown():
    global countdown_job, paused_time, timerStart, study_time, countdown_time, timer_start_time

    if countdown_job is not None:
        root.after_cancel(countdown_job)
        countdown_job = None

    timerStart = "OFF"

    try:
        if timer_start_time is not None:
            # Accurate elapsed time using clock
            duration_seconds = int(time() - timer_start_time)
        else:
            # Fallback: estimate using difference
            total_seconds = study_time #* 60
            remaining_seconds = countdown_time if countdown_time is not None else 0
            duration_seconds = max(0, total_seconds - remaining_seconds)

        if duration_seconds > 60 * 60 * 12:  # cap max session to 12 hours
            duration_seconds = 0

        log_session_to_file("Timer", duration_seconds)

    except Exception as e:
        print("Error logging session:", e)
        log_session_to_file("Timer", 0)

    screen.itemconfig(timer_label, text="SESSION ENDED")
    rewardsScreen()



def resumeCountdown():
    global countdown_time, paused_time, countdown_job, timerStart
    if paused_time is not None:
        countdown_time = paused_time
        paused_time = None
        timerStart = "ON"
        updateCountdown()

def breakCountdown():
    global countdown_job, paused_time, timerStart
    if countdown_job is not None:
        root.after_cancel(countdown_job)
        countdown_job = None
        paused_time = countdown_time
        timerStart = "PAUSED"
        screen.itemconfig(timer_label, text="PAUSED")
        screen.create_rectangle(350, 370, 550, 420, fill = "white")
        screen.create_text(450, 395, text = "RESUME", font = ("Arial", 15, "bold"), fill = "hot pink")

        root.bind("<Button-1>", breakClick)

def breakClick(event):
    xMouse = event.x
    yMouse = event.y

    if 350 <= xMouse <= 550 and 370 <= yMouse <= 420:
        resumeCountdown()
    
    elif 350 <= xMouse <= 550 and 300 <= yMouse <= 350:
        #print("wow")
        stopCountdown()
        
    
def updateCountdown():
    global countdown_time, countdown_job, timerStart, timesup, motivationaldino, timerType
    
    if countdown_time > 0:
        global timertype
        mins = countdown_time // 60
        secs = countdown_time % 60
        screen.itemconfig(timer_label, text=f"{mins:02}:{secs:02}")
        countdown_time -= 1
        countdown_job = root.after(1000, updateCountdown)

        # Update buttons
        if timerStart == "OFF":
            screen.create_rectangle(350, 300, 550, 350, fill="white")
            screen.create_text(450, 325, text="START", font=("Arial", 15, "bold"), fill="hot pink")
        else:
            screen.create_rectangle(350, 300, 550, 350, fill="white")
            screen.create_text(450, 325, text="END SESSION", font=("Arial", 15, "bold"), fill="pink")
            screen.create_rectangle(350, 370, 550, 420, fill="white")
            screen.create_text(450, 395, text="PAUSE", font=("Arial", 15, "bold"), fill="pink")

        # how motivation *after* drawing UI so it appears on top
        if randint(1, 5) == 5:
            if timerType == "Pomodoro Timer":
                show_random_message()
            
        
        else:
            screen.create_rectangle(350, 300, 550, 350, fill = "white")
            screen.create_text(450, 325, text = "END SESSION", font = ("Arial", 15, "bold"), fill = "pink")
            screen.create_rectangle(350, 370, 550, 420, fill = "white")
            screen.create_text(450, 395, text = "PAUSE", font = ("Arial", 15, "bold"), fill = "pink")
    # else:
    #     screen.itemconfig(timer_label, text="Time's up!")
    #     importImages()
    #     timesup_id = screen.create_image(450, 400, image=timesup)
    
    #     def remove_timesup():
    #         screen.delete(timesup_id)
    #         rewardsScreen()
    
    #     root.after(2000, remove_timesup)
    
    # root.bind("<Button-1>", updateCountdownClick)
    
    else:
        screen.itemconfig(timer_label, text="Time's up!")
    
        # Log the session automatically on completion
        duration_seconds = study_time * 60  # full duration completed
        log_session_to_file("Timer", duration_seconds)
    
        importImages()
        timesup_id = screen.create_image(450, 400, image=timesup)
    
        def remove_timesup():
            screen.delete(timesup_id)
            rewardsScreen()
    
        root.after(2000, remove_timesup)
    root.bind("<Button-1>", updateCountdownClick)


def updateCountdownClick(event):
    xMouse = event.x
    yMouse = event.y
    if 350 <= xMouse <= 550 and 300 <= yMouse <= 350:
        if timerStart == "OFF":
            startCountdown()
        else:
            stopCountdown()
    elif 350 <= xMouse <= 550 and 370 <= yMouse <= 420:
        breakCountdown()



########################################################
#Rewards
########################################################
def rewardsScreen():
    global study_time, countdown_time, total_time, timertype, coins
    importImages()
    if timertype == "Timer":
        if countdown_time >= 0:
            timeStudying = study_time - (countdown_time)
            coinsEarned = timeStudying * 0.1
        else:
            coinsEarned = start_time * 0.1
            
    elif timertype == "Pomodoro Timer":
        coinsEarned = 2
        
    else:
        coinsEarned = total_time/60 *6
    coinsEarned = round(coinsEarned)
    screen.create_image(450, 400, image = rewardsScreenI)
    screen.create_text(500, 450, text = coinsEarned, font = ("Arial", 30, "bold"))
    with open("coins.txt", 'r+') as file:
        file.seek(0)
        coins = int(file.read() or 0)
        coins += coinsEarned
        file.seek(0)
        file.write(str(coins))
        file.truncate()
    
    root.bind("<Button-1>", rewardsScreenClick)

def rewardsScreenClick(event):
    xMouse = event.x
    yMouse = event.y
    #screen.create_rectangle(60, 60, 180, 180, fill = "yellow")
    if 60 <= xMouse <= 180 and 60 <= yMouse <= 180:
        screen.delete(rewardsScreenI)
        startScreen()
    
########################################################
#Code for pomodoro timer
########################################################
        

# Pomodoro global variables
pomodoro_subject = ""
pomodoro_study = 0
pomodoro_break = 0
pomodoro_loops = 0
current_loop = 0
pomodoro_long_break = 0
pomodori_completed = 0
study_count = 0
pomodoro_state = "study"  # "study" or "pause"
pomodoro_paused = False
pomodoro_job = None


def pomodoroSettings():
    global subject_entry, study_entry, break_entry, long_break_entry, loop_entry, pomodorosettings

    screen.delete("all")
    screen.create_image(450, 400, image=pomodorosettings)  # your background
    #screen.create_rectangle(100, 100, 800, 700, fill='yellow')
    #screen.create_text(450, 140, text="Pomodoro Setup", font=("Arial", 24, "bold"))

    screen.create_text(300, 225, text="Subject:")
    screen.create_text(300, 275, text="Study Time (min):")
    screen.create_text(300, 325, text="Short Break Time (min):")
    screen.create_text(300, 375, text="Long Break Time (min):")
    screen.create_text(300, 425, text="Loops:")
    

    subject_entry = Entry(root)
    study_entry = Entry(root)
    break_entry = Entry(root)
    long_break_entry = Entry(root)
    loop_entry = Entry(root)

    screen.create_window(500, 225, window=subject_entry, width=150)
    screen.create_window(500, 275, window=study_entry, width=150)
    screen.create_window(500, 325, window=break_entry, width=150)
    screen.create_window(500, 375, window=long_break_entry, width=150)
    screen.create_window(500, 425, window=loop_entry, width=150)

    #screen.create_rectangle(400, 500, 500, 600, fill="hot pink")
    #screen.create_text(450, 550, text="Start")

    #screen.create_rectangle(80, 80, 130, 110, fill="yellow")
    #screen.create_text(105, 95, text="Back")

    root.bind("<Button-1>", pomodoroSettingsClick)

def pomodoroSettingsClick(event):
    global pomodoro_subject, pomodoro_study, pomodoro_break, pomodoro_loops, pomodorosettings
    global current_loop, pomodoro_long_break, study_count

    xMouse, yMouse = event.x, event.y

    if 400 <= xMouse <= 500 and 500 <= yMouse <= 600:
        try:
            # Check if any field is empty
            if (not subject_entry.get() or not study_entry.get() or
                not break_entry.get() or not loop_entry.get() or
                not long_break_entry.get()):
                screen.create_text(450, 460, text="Please fill in all fields", fill="red")
                return

            pomodoro_subject = subject_entry.get()
            pomodoro_study = int(study_entry.get())
            pomodoro_break = int(break_entry.get())
            pomodoro_loops = int(loop_entry.get())
            pomodoro_long_break = int(long_break_entry.get())

            current_loop = 0
            study_count = 0
            
            
            # Append Pomodoro settings to stopwatch.txt
            with open("stopwatch_log.txt", "a") as file:
                file.write(f"\n--- Pomodoro Session ---\n")
                file.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                file.write(f"Subject: {pomodoro_subject}\n")
                file.write(f"Study Time: {pomodoro_study} min\n")
                file.write(f"Short Break: {pomodoro_break} min\n")
                file.write(f"Long Break: {pomodoro_long_break} min\n")
                file.write(f"Loops: {pomodoro_loops}\n")
                file.write("------------------------\n")

            
            pomodoroTimerScreen()

        except ValueError:
            screen.create_text(450, 460, text="Please enter valid numbers", fill="red")

    elif 60 <= xMouse <= 150 and 70 <= yMouse <= 150:
        screen.delete("all")
        timerScreen()
        

def pomodoroTimerScreen():
    global timer_label, pause_button_text, pomodoroupdatebg, phase_label, loop_label

    screen.delete("all")
    
    screen.create_image(450, 400, image=pomodoroupdatebg, tags="pomodoro_bg")
    screen.lower("pomodoro_bg")

    screen.create_text(450, 180, text=f"Pomodoro - {pomodoro_subject}", font=("Helvetica", 24, "bold"))

    timer_label = screen.create_text(450, 250, text="00:00", font=("Helvetica", 36), fill="black")

    phase_label = screen.create_text(450, 350, text="Starting...", font=("Helvetica", 20), fill="black")
    loop_label = screen.create_text(450, 380, text=f"Pomodoro 0/4  |  Set 1/{pomodoro_loops}", font=("Helvetica", 16), fill="black")

    screen.create_rectangle(400, 400, 500, 450, fill="wheat1", outline="DarkGoldenrod4", width=3, tags="pause_button")
    pause_button_text = screen.create_text(450, 425, text="Pause", font=("Helvetica", 14), tags="pause_text")

    screen.tag_bind("pause_button", "<Button-1>", togglePomodoroPause)
    screen.tag_bind("pause_text", "<Button-1>", togglePomodoroPause)

    startPomodoroCycle()
    
def pomodoroButtonClick(event):
    xMouse = event.x
    yMouse = event.y

    if 80 <= xMouse <= 130 and 80 <= yMouse <= 110:
        screen.delete("all")
        timerScreen()
    elif 500 <= xMouse <= 675 and 300 <= yMouse <= 400:
        screen.delete("all")
        pomodoroSettings()
        


def startPomodoroCycle():
    global pomodoro_countdown_time
    screen.itemconfig(phase_label, text="")
    screen.itemconfig(loop_label, text="")

    #stopDancingDino()  

    if pomodoro_state == "study":
        #stopDancingDino()
        pomodoro_countdown_time = pomodoro_study
    elif pomodoro_state == "break":
        pomodoro_countdown_time = pomodoro_break
    elif pomodoro_state == "long_break":
        pomodoro_countdown_time = pomodoro_long_break

    updatePomodoroTimer()

def updatePomodoroTimer():
    global pomodoro_countdown_time, pomodoro_job, study_count, current_loop, pomodoro_state, pomodoroupdatebg, dancing_animation_job, dancing_dino_id 
    # Ensure the background is always present
    screen.create_image(450, 400, image=pomodoroupdatebg, tags="pomodoro_bg")
    screen.lower("pomodoro_bg")

    # Continue with the rest of your logic

    if pomodoro_paused:
        if pomodoro_job is not None:
            root.after_cancel(pomodoro_job)
            pomodoro_job = None
        return
    # Only draw background once and keep it behind

    # Update phase labels
    if pomodoro_state == "study":
    # # Ensure all dancing animation is stopped and removed
    #     stopDancingDino()
    #     dancing_animation_job = None
    #     dancing_dino_id = None
    
        screen.itemconfig(phase_label, text="Time to focus!")
        screen.itemconfig(loop_label, text=f"Pomodoro {study_count + 1}/4  |  Set {current_loop + 1}/{pomodoro_loops}")
        
    elif pomodoro_state == "break":
        screen.itemconfig(phase_label, text="Short break!")
        #animateDancingDino()
    elif pomodoro_state == "long_break":
        screen.itemconfig(phase_label, text="Long break!")
        #animateDancingDino()

    if pomodoro_countdown_time > 0:
        mins, secs = pomodoro_countdown_time // 60, pomodoro_countdown_time % 60
        screen.itemconfig(timer_label, text=f"{mins:02}:{secs:02}")
        pomodoro_countdown_time -= 1
        pomodoro_job = root.after(1000, updatePomodoroTimer)
    
        # Only show motivational message during study phase
        if pomodoro_state == "study" and randint(1, 5) == 5:
            show_random_message()
    else:
        if pomodoro_state == "study":
            study_count += 1
            if study_count % 4 == 0:
                pomodoro_state = "long_break"
            else:
                pomodoro_state = "break"

        elif pomodoro_state == "break":
            pomodoro_state = "study"

        elif pomodoro_state == "long_break":
            current_loop += 1
            study_count = 0

            if current_loop >= pomodoro_loops:
                screen.itemconfig(timer_label, text="All Done!")
                
                if current_loop == pomodoro_loops:
                    rewardsScreen()
            else:
                pomodoro_state = "study"
                

        startPomodoroCycle()

def togglePomodoroPause(event):
    global pomodoro_paused, pomodoro_job
    if pomodoro_paused:
        pomodoro_paused = False
        screen.itemconfig(pause_button_text, text="Pause")
        #stopDancingDino()  # in case user paused during break
        updatePomodoroTimer()
    else:
        pomodoro_paused = True
        screen.itemconfig(pause_button_text, text="Resume")
        screen.itemconfig(timer_label, text="PAUSED")
        if pomodoro_job is not None:
            root.after_cancel(pomodoro_job)

def restartPomodoro(event):
    global current_loop, study_count, pomodoro_state
    current_loop = 0
    study_count = 0
    pomodoro_state = "study"
    startPomodoroCycle()
    


########################################################
#Calendar CODE
########################################################################
# Make calendar_entries global so it persists
calendar_entries = []

def calendarScreen():
    global backB
    screen.delete("all")  # Clear canvas drawings, but entries are preserved
    
    screen.create_text(262.5, 75, text="Calendar", font=("Helvetica", 28, "bold"), fill="black")
    screen.create_rectangle(50, 100, 475, 725, fill="white", outline="")
    screen.create_rectangle(50+450, 100, 875, 725, fill="white", outline="")
    screen.create_image(110, 70, image=backB)

    # Lines for calendar
    y = 100
    increment = 625 / 24
    for l in range(25):
        screen.create_line(50, y, 475, y, fill="red")
        y += increment

    # Labels for time
    hour = 0
    y = 100
    for l in range(25):
        screen.create_text(50, y, text=f"{hour}:00", font=("Helvetica", 8), fill="black")
        hour += 1
        y += increment

    draw_calendar_entries()  # Redraw existing entries

    from tkinter import simpledialog, colorchooser

    def get_calendar_entry():
        subject = simpledialog.askstring("Subject", "Enter the subject:")
        color = colorchooser.askcolor(title="Choose color")[1]  # Hex color
        start_time = simpledialog.askfloat("Start Time", "Enter start time (e.g., 14.0 for 2 PM):")
        end_time = simpledialog.askfloat("End Time", "Enter end time (e.g., 15.5 for 3:30 PM):")
        
        if subject and color and start_time is not None and end_time is not None:
            calendar_entries.append({
                "subject": subject,
                "color": color,
                "start_time": start_time,
                "end_time": end_time
            })
            calendarScreen()  # Redraw screen with new entry

    from tkinter import Button
    add_entry_button = Button(root, text="Add Study Session", command=get_calendar_entry)
    add_entry_button.place(x=600, y=60)

    root.bind("<Button-1>", calendarBack)


def draw_calendar_entries():
    increment = 625 / 24  # Each hour slot height
    for entry in calendar_entries:
        y1 = 100 + (entry["start_time"] * increment)
        y2 = 100 + (entry["end_time"] * increment)
        screen.create_rectangle(50, y1, 475, y2, fill=entry["color"], outline="black")
        screen.create_text(262.5, (y1 + y2) / 2, text=entry["subject"], fill="black", font=("Helvetica", 12, "bold"))


def calendarBack(event):
    xMouse = event.x
    yMouse = event.y
    if 80 <= xMouse <= 140 and 40 <= yMouse <= 100:
        screen.delete("all")
        timeLobby()
########################################################
#Schedule CODE
########################################################################

#edit so that the bars correlate with the study sessions: 
#take from txt file and convert into bars
#do not need need to 


def statsScreen():
    screen.delete("all")  # Clear canvas

    # Title
    screen.create_text(250, 30, text="May 2025", font=("Helvetica", 20, "bold"), fill="black")
    screen.create_text(250, 60, text="Daily Study Hours", font=("Helvetica", 14), fill="black")

    # Time Grid (Horizontal lines for 0 to 8 hours)
    for i in range(9):
        x = 100 + i * 50
        screen.create_line(x, 100, x, 600, fill="gray", dash=(2, 2))
        screen.create_text(x, 90, text=str(i), font=("Helvetica", 10))

    # Day Grid (Vertical lines and labels for each day)
    for i, day in enumerate(range(18, 25)):
        y = 120 + i * 60
        screen.create_text(60, y + 10, text=str(day), font=("Helvetica", 10, "bold"))
        screen.create_line(90, y + 10, 550, y + 10, fill="gray")

    # Subject Colors
    colors = {
        "default": "#d7e3c2",
        "math": "#ff006e",
        "cs": "#b6ccff",
        "english": "#f8f4b2",
        "physics": "#0000aa"
    }

    # Study bars (example data for days 21–27)
    study_data = {
        18: [("default", 0, 7.9)],
        19: [("default", 0, 2.1)],
        20: [("default", 0, 2), ("cs", 2, 4.5), ("english", 4.5, 8.8)],
        21: [("english", 0, 1.6)],
        22: [("physics", 0, 5.2)],
        23: [("physics", 0, 1)],
        24: [("physics", 0, 5.8)],
    }

    for i, day in enumerate(range(21, 28)):
        y = 120 + i * 60
        if day in study_data:
            for subject, start, end in study_data[day]:
                x1 = 100 + start * 50
                x2 = 100 + end * 50
                screen.create_rectangle(x1, y, x2, y + 20, fill=colors[subject], outline="black")

                # Optional duration label
                duration = end - start
                hours = int(duration)
                minutes = int((duration - hours) * 60)
                screen.create_text(x2 + 35, y + 10, text=f"{hours} h {minutes} m", font=("Helvetica", 8), anchor="w")

    # Legend
    legend_y = 150
    for subject, color in colors.items():
        screen.create_rectangle(580, legend_y, 600, legend_y + 20, fill=color)
        screen.create_text(620, legend_y + 10, text=subject, anchor="w", font=("Helvetica", 10))
        legend_y += 30

    # Week/Month buttons
    screen.create_rectangle(650, 30, 730, 60, fill="#274c77", outline="")
    screen.create_text(690, 45, text="Month", font=("Helvetica", 12), fill="white")
    screen.create_rectangle(580, 30, 650, 60, fill="#a3bcd3", outline="")
    screen.create_text(615, 45, text="Week", font=("Helvetica", 12), fill="black")

########################################################################           
    
#SHOPPING SCREEN AND ITEMS-----------------------------
def marketScreen1():
    #stopDancingDino()
    importImages()
    
    screen.create_rectangle(0,0,900,800, fill = "#062912")
    screen.create_image(450, 400, image = marketBg1)
    root.bind("<Button-1>", marketScreen1Click)
    #screen.create_rectangle(40, 40, 160, 160, fill = "yellow")
    # screen.create_rectangle(150, 560, 250, 650, fill = "yellow")
    # screen.create_rectangle(630,560,750,650, fill = "yellow")
def marketScreen1Click(event):
    global i
    xMouse = event.x
    yMouse = event.y
    
    if 250 <= xMouse <= 430 and 230 <= yMouse <= 390:
        i = 0
        unlockItem()
    elif 480 <= xMouse <= 670 and 230 <= yMouse <= 390:
        i = 1
        unlockItem()
    elif 260 <= xMouse <= 445 and 415 <= yMouse <= 600:
        i = 2
        unlockItem()
    elif 490 <= xMouse <= 670 and 415 <= yMouse <= 600:
        i = 3
        unlockItem()
    elif 30 <= xMouse <= 150 and 50 <= yMouse <= 155:
        startScreen()
    elif 630 <= xMouse <= 750 and 560 <= yMouse <= 650:
        marketScreen2()
    elif 40 <= xMouse <= 160 and 40 <= yMouse <= 160:
        startScreen()
        
def marketScreen2():
    importImages()
    screen.create_image(450, 400, image = marketBg2)
    root.bind("<Button-1>", marketScreen2Click)

def marketScreen2Click(event):
    global i
    xMouse = event.x
    yMouse = event.y
    

    
    if 250 <= xMouse <= 430 and 230 <= yMouse <= 350:
        i = 4
        unlockItem()
    elif 480 <= xMouse <= 670 and 230 <= yMouse <= 390:
        i = 5
        unlockItem()
    elif 260 <= xMouse <= 445 and 415 <= yMouse <= 600:
        i = 6
        unlockItem()
    elif 490 <= xMouse <= 670 and 415 <= yMouse <= 600:
        i = 7
        unlockItem()
    elif 80 <= xMouse <= 130 and 80 <= yMouse <= 120:
        startScreen()
    elif 160 <= xMouse <= 260 and 560 <= yMouse <= 650:
        marketScreen1()
    elif 630 <= xMouse <= 750 and 560 <= yMouse <= 650:
        marketScreen3()
    elif 40 <= xMouse <= 160 and 40 <= yMouse <= 160:
        startScreen()

def marketScreen3():
    importImages()
    screen.create_image(450, 400, image = marketBg3)
    root.bind("<Button-1>", marketScreen3Click)


def marketScreen3Click(event):
    global i
    xMouse = event.x
    yMouse = event.y
    
    if 250 <= xMouse <= 430 and 230 <= yMouse <= 350:
        i = 8
        unlockItem()
    elif 480 <= xMouse <= 670 and 230 <= yMouse <= 390:
        i = 9
        unlockItem()
    elif 260 <= xMouse <= 445 and 415 <= yMouse <= 600:
        i = 10
        unlockItem()
    elif 490 <= xMouse <= 670 and 415 <= yMouse <= 600:
        i = 11
        unlockItem()
    elif 80 <= xMouse <= 130 and 80 <= yMouse <= 120:
        startScreen()
    elif 160 <= xMouse <= 260 and 560 <= yMouse <= 650:
        marketScreen2()
    elif 630 <= xMouse <= 750 and 560 <= yMouse <= 650:
        marketScreen4()
    elif 40 <= xMouse <= 160 and 40 <= yMouse <= 160:
        startScreen()
        
def marketScreen4():
    importImages()
    screen.create_image(450, 400, image = marketBg4)
    root.bind("<Button-1>", marketScreen4Click)
    #screen.create_rectangle(80, 80, 130, 110, fill = "yellow")

def marketScreen4Click(event):
    global i
    xMouse = event.x
    yMouse = event.y
    
    if 250 <= xMouse <= 430 and 230 <= yMouse <= 350:
        i = 12
        unlockItem()
    elif 480 <= xMouse <= 670 and 230 <= yMouse <= 390:
        i = 13
        unlockItem()
    elif 260 <= xMouse <= 445 and 415 <= yMouse <= 600:
        i = 14
        unlockItem()
    elif 490 <= xMouse <= 670 and 415 <= yMouse <= 600:
        i = 15
        unlockItem()
    elif 80 <= xMouse <= 130 and 80 <= yMouse <= 120:
        timeLobby()
    elif 160 <= xMouse <= 260 and 560 <= yMouse <= 650:
        marketScreen3()
    elif 40 <= xMouse <= 160 and 40 <= yMouse <= 160:
        startScreen()


def unlockItem():
    global i, coins, marketItems, ownedItems, itemsPrice, buy
    importMarketImages()

    
    wantItem = marketItems[i]
    
    screen.create_image(450,400, image = buyScreen)
    screen.create_image(450,400, image = marketImages[i])
    
    if marketItems[i] in ownedItems:
        screen.create_image(450, 400, image = equip) #equip
        buy = False
        
    else:
        screen.create_image(450, 400, image = buyI) #buy
        if coins >= itemsPrice[i]:
                buy = True
        else:
            buy = False
    root.bind("<Button-1>", unlockItemClick)

def unlockItemClick(event):
    global dinoImages, marketItems, i, ownedItems, coins, itemsPrice, buy, Accessories, accessories
    importDinoImages()
    xMouse = event.x
    yMouse = event.y
    
    if 300 <= xMouse <= 700 and 400 <= yMouse <= 600:
        if buy == True:
                ownedItems.append(marketItems[i])
                coins = coins - itemsPrice[i]
                Accessories = True
                accessories = dinoImages[i]
                startScreen()
                
        else:
            if coins < itemsPrice[i]:
                screen.create_image(450, 400, image = broke)
                screen.update()
                sleep(3)
                marketScreen1()
                
            else:
                screen.create_image(450,400, image = equipped)
                screen.update()
                Accessories = True
                accessories = dinoImages[i]
                startScreen()
    elif 745 <= xMouse <= 865 and 75 <= yMouse <= 180:
        screen.delete("all")
        marketScreen1()

#CALLED WHEN THE MOUSE IS CLICKED
def mouseClickHandler(event):
    global xMouse, yMouse
    
#CALLED WHEN THE MOUSE STOPS GETTING CLICKED
def mouseReleaseHandler(event):
	global xMouse, yMouse
	
def runApp():
    startScreen()
    #if timer is done:
        
    #code for game running
    
    #starts with startScreen then timer
    #as long as study session starts, the program runs (timer =! done)
    #once it ends, run rewards and stuff
    
root.after( 500, setInitialValues()) 
screen.bind("<Button-1>", mouseClickHandler) 
screen.bind("<ButtonRelease-1>", mouseReleaseHandler) 
# screen.bind("<Key>", keyDownHandler)
# screen.bind("<KeyRelease>", keyUpHandler)
screen.pack() 
screen.focus_set() 


screen.mainloop()