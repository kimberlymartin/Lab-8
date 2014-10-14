import random

print "A monster approaches! Prepare to fight!"

damageByMonster = random.randint(1,35)
playerHealth = 100
monsterHealth = 100
punchDmg = 5
swordDmg = 10
fireballDmg = 30
mana = 5

print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
print "You have " + str(playerHealth) + " health."
print "The monster has " + str(monsterHealth) + " health."
print "You have " + str(mana) + " mana."

while playerHealth > 0 and monsterHealth > 0:
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "What attack would you like to use?"
    print "1 - punch, 2 - sword, 3 - fireball."
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    attack = int(raw_input())
    if attack == 1:
        print "You have selected the command punch."
        monsterHealth = monsterHealth - punchDmg
    elif attack == 2:
        if mana >= 2:
            print "You have selected the command sword."
            monsterHealth = monsterHealth - swordDmg
            mana = mana - 2
        else:
            print "You don't have enough mana for that attack."
            print "You use punch instead."
            monsterHealth = monsterHealth - punchDmg
    else:
        if mana >= 4:
            print "You have selected the command fireball."
            monsterHealth = monsterHealth - fireballDmg
            mana = mana - 4
        else:
            print "You don't have enough mana for that attack."
            print "You use punch instead."
            monsterHealth = monsterHealth - punchDmg
    playerHealth = playerHealth - damageByMonster
    mana = mana + 1
    print "The monster has " + str(monsterHealth) + " health."
    print "You have " + str(playerHealth) + " health."
    print "You have " + str(mana) + " mana."
    
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

if playerHealth <= 0:
    print "You have " + str(playerHealth) + " health."
    print "You have been defeated by the monster."
elif playerHealth <= 0 and monsterHealth <= 0:
    print "The monster has " + str(monsterHealth) + " health."
    print "You have " + str(playerHealth) + " health."
    print "You defeated the monster, but you died as well."
else:
    print "The monster has " + str(monsterHealth) + " health."
    print "You defeated the monster."
