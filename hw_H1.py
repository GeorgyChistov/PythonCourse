import time 
import random as rn

force = [i for i in range(4,16,2)]
class Player:
  def __init__(self, hp):
    self.hp = hp
class Zombie(Player):
  def heal(self,points):
    self.hp += 5
  def bite(self, target):
    jaw = rn.choice(force)
    target.hp -= jaw
    self.hp += 1
class Human(Player):
  def hit(self,target):
    force = [i for i in range(4,16,2)]
    kick = rn.choice(force)
    if kick > 12:
      print('Great hit!')
    target.hp -= kick 
rules = False
while not rules:  
  zombie = Zombie(hp = int(input('Enter zombie health')))
  human = Human(hp = int(input('Enter human health')))
  if zombie.hp < human.hp:
    break
  else:
    print('Zombie cannot have more health, than human')
fight = True

while fight:
  print('Human attacks!')
  time.sleep(0.5)
  human.hit(zombie)
  print('zombie = ' + str(zombie.hp))
  print('human = ' + str(human.hp))
  if human.hp <= 0 or zombie.hp <= 0:
    break
  time.sleep(1)
  print('Zombie bites him!')
  time.sleep(0.5)
  zombie.bite(human)
  print('zombie =' + str(zombie.hp))
  print('human =' + str(human.hp))
  if human.hp <= 0 or zombie.hp <= 0:
    break
  time.sleep(1)
