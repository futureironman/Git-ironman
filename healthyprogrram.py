#Healthy Program
'''
9am-5am
water-water.mp3 (3.5 litres)-Drank-log-every 40 min
eyes-eyes.mp3 -every 30 min eyDone -log-every 30 min
physical activity-physical.mp3-45min exdone-log-every 45 min
Rules
Pygame module to play audio
'''
from pygame import mixer

def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while true:
        a=input()
        if a== stopper:
            mixer.music.stop()
            break

if __name__=='__main__':
    musiconloop("water.mp3","stop")









