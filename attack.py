import random


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
    break

