import pygame as pg;import sys;
import random,os;import threading;
from getTree import *;#it creates a path list of all the files and folders i intend to
State='Playing'
cwd='/home/frnr/Workstation/Python/myMusicPlayer'#this is the path of my program


if os.getcwd()!=cwd:
    os.chdir(cwd)#i did this so i could run my code from terminal using an alias i defiened in .bashrc

def getCommand():#recieves the command of the client,tells the program what to do
    global run;global State
    global rm;global lm;
    isPlaying=f' | l:{lm.split("/")[-1]} | r:{rm.split("/")[-1]}' 
    In=input(State+isPlaying+"/ :")

    if In=='q':
        run=0
        pg.quit()
        sys.exit()
    
    elif In=='r' and State!='Paused':
        ch1.stop()
        rm=random.choice(musicList)
        ch1.play(pg.mixer.Sound(rm))
        ch1.set_volume(0,1)
        
    elif In=='l' and State!='Paused':
        ch0.stop()
        lm=random.choice(musicList)
        ch0.play(pg.mixer.Sound(lm))
        ch0.set_volume(1,0)
    elif In=='p':
        State='Paused'
        ch0.pause()
        ch1.pause()
    elif In=='re':
        State='Playing'
        ch1.unpause()
        ch0.unpause()
    else:
        print('Invalid command')

def ifBusy():#it's a thread that everysecond checks if the music is still running
    #if not play another song in the same channel
    global rm;
    global lm;

    while run:
        if State!='Paused':
            if ch0.get_busy()==0:
                 ch0.stop()
                 lm=random.choice(musicList)
                 ch0.play(pg.mixer.Sound(lm))
                 ch0.set_volume(1,0)
                 print(lm)
            if ch1.get_busy()==0:
                 ch1.stop()
                 rm=random.choice(musicList)
                 ch1.play(pg.mixer.Sound(rm))
                 ch1.set_volume(0,1)
                 print(rm)


pg.init()

musicList=getAllChildFilesByFormat('/home/frnr/Music',['mp3'])#gets the path of all mp3's in ~/Music

ch0=pg.mixer.Channel(0)#left ear
ch1=pg.mixer.Channel(1)#right ear
rm=random.choice(musicList)
lm=random.choice(musicList)#it is possible that rm value will be the same as lm
ch0.play(pg.mixer.Sound(lm))
ch1.play(pg.mixer.Sound(rm))


ch0.set_volume(1,0)
ch1.set_volume(0,1)

th0 = threading.Thread(target=ifBusy);#starts the ifBusy target

print('\n\n\n\n\n\n\n')
th0.daemon=True#for poper exit of program with threads
run=1
th0.start()

while run:
    getCommand()


