import random

class Enemy():
    hp = 200; '''static variable'''
    def __init__(self, atkl, atkh):
        self.atkl = atkl; '''dynamic variable'''
        self.atkh = atkh


    def getAtk(self):
        print('atk is:', self.atkl)

    def getHp(self):
        print('Hp is:', self.hp)

enemy1 = Enemy(40, 49)
enemy1.getAtk()
enemy1.getHp()

enemy2 = Enemy(75, 90)
enemy2.getAtk()
enemy2.getHp()

'''

playerhp=260
enemyatkl=60
enemyatkh=80



while playerhp > 0:
    dmg = random.randrange(enemyatkl, enemyatkh)
    playerhp = playerhp-dmg

    if playerhp <= 30:
        playerhp = 30

    print('Enemy strike for', dmg, 'points of damage. Current hp:', playerhp)

    if playerhp > 30:
        continue

    print("you have low health. You've been teleported to the nearst inn.")
    break'''

