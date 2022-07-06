import random
import subprocess
import os


QuestBoiler = ["Idol has been stolen.","Find my son.","Kll a bad businees partner.","Fight in a ritual.","Deal with band of ruffians.","Kill our elected official.","Show of strength from the party.","Straight hunt/murder quest.","Attack/extort tax avoiders.","Facilitae a shady deal.","Murder business partner/inheritance."]
QuestEnemy = ["Bandits.","Direwolves.","Goblins.","Necromancer with zombies or followers.","Town guards.","Giant spiders.","Orcs.","Vampires with or without thralls.","Professionals.","Tainted experiments.","Wildlife."]

def roller(NUM):
    return random.randint(0,NUM)

def questgen():
    print(QuestBoiler[roller(len(QuestBoiler) - 1)])
    print(QuestEnemy[roller(len(QuestEnemy) - 1)])

for x in range(5):
    print(x+1)
    questgen()
    vid = random.choice(os.listdir("/home/toll/Videos/Videos"))
    os.system("/bin/vlc /home/toll/Videos/Videos/"+vid)
    