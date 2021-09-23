"""
Описать класс Warrior:

- атрибут name - имя юнита (тип str)
- атрибут health_points - показатель здоровья (тип int от 0 до 100)
- магический метод __init__, который не принимает аргументов и создает юнита со
  100 health_points


Описать класс Arena:

- атрибут warriors - все воины на арене (тип set)
- магический метод __init__, который принимает необязательный аргумент warriors
- метод add_warrior
- метод choose_warriors
- метод hit

Создать список, в который добавить 5 объектов класса Warrior.

В случайном порядке они бьют друг друга. Тот, кто бьет, здоровья не теряет.
У того, кого бьют, оно уменьшается на 20 очков от одного удара.
После каждого удара надо выводить сообщение, какой юнит атаковал,
и сколько у противника осталось здоровья.
Как только у кого-то заканчивается ресурс здоровья он удаляется из списка.
Программа завершается, когда останется один юнит, на экран выводится сообщение о том,
кто одержал победу.
"""