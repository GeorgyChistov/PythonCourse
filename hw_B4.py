import random

answer = random.randint(1,100)
big_phrases = ["Чего-то ты переборщил", "Эй, остуди свой максимализм!", "Большое число - большая ответственность А к этому пока не готов"]
little_phrases = ["Маловато-то будет!", "Ну зачем тебе такие маленькие числа,а?", "Я, конечно, не эксперт, но мне кажется, что это слишком мало"] 
number = int(input())
while True:
	number = int(input())
	if number > answer:
		print(random.choice(big_phrases))
	if number < answer:
		print(random.choice(little_phrases))
	if number == answer:
		print ("Вы выиграли!")
		break
