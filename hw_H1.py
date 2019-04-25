import time
import random as rn

force = [i for i in range(4,16,2)]
class Player:
  def __init__(self, health):
    self.hp = health
class Zombie(Player):
  def heal(self,points):
    self.hp += 5
  def bite(self, target):
    jaw = rn.choice(force)
    target.hp -= jaw
    self.hp += 1
    print('Oh no! Zombie bites him and damage ' + str(jaw) + '! Zombie get heal at 1')
class Human(Player):
  def hit(self,target):
    force = [i for i in range(20)]
    kick = rn.choice(force)
    print('Human attacks zombie and damage is ' + str(kick) + 'hp')
    phrases = ["GREAT HIT!", "CRITICAL DAMAGE FROM HUMAN!!!", "KAWABANGA, HE ALMOST KILL IT!"]
    if kick > 12:
      phrase = rn.choice(phrases)
      print(phrase)
    target.hp -= kick 
rules = True
while rules:  
  zombie = Zombie(health = int(input('Enter zombie health: ')))
  human = Human(health = int(input('Enter human health: ')))
  if zombie.hp < human.hp:
    break
  else:
    print('Zombie cannot have more health, than human')
fight = True

while fight:
  time.sleep(0.5)
  human.hit(zombie)
  print('zombie = ' + str(zombie.hp))
  print('human = ' + str(human.hp))
  if human.hp <= 0 or zombie.hp <= 0:
    if human.hp > 0:
      print("Human is winner!")
      break
    else:
      print("Zombie if winner")
      break
  time.sleep(1)
  time.sleep(0.5)
  zombie.bite(human)
  print('zombie =' + str(zombie.hp))
  print('human =' + str(human.hp))
  if human.hp <= 0 or zombie.hp <= 0:
        if human.hp > 0:
      print("Human is winner!")
      break
    else:
      print("Zombie if winner")
      break
  time.sleep(1)
