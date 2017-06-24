class FarmAnimals:
    max_weight = 1000 #kg
    status = 'live'
    time_for_wake_up = 5
    time_for_sleep = 21

    def voice(self, voice_type):
        return voice_type.upper()

    def feed_value(self, cost, count):
        food_cost = cost * count
        return food_cost

    def day_deals(self, day_plan):
        for deal in day_plan:
            print(deal)


class Livestock(FarmAnimals):
    time_for_wake_up = 6
    count_animals = 15
    product = 'Meat'


class Birds(FarmAnimals):
    count_animals = 30
    product = ['Eggs', 'Meat']
    day_plan = ['Проснуться', 'Нести яйца', 'Есть', 'Заснуть']
    food = 'Крупа'
    cost = 10


class Cows(Livestock):
    voice_type = 'Muuuu!'
    food = 'Овес'
    cost = 100 #RUB
    count_animals = 5
    day_plan = ['Проснуться','Подоиться','Пастись на лугу','Вернуться','Заснуть']


class Goats(Livestock):
    voice_type = 'Beeee!'
    food = 'Овес'
    max_weight = 200  # kg
    cost = 100  # RUB
    count_animals = 2
    day_plan = ['Проснуться', 'Пободаться', 'Пастись на лугу', 'Вернуться', 'Заснуть']


class Pigs(Livestock):
    voice_type = 'Hru-Hru!'
    food = 'Требуха'
    max_weight = 500  # kg
    cost = 10  # RUB
    count_animals = 8
    day_plan = ['Проснуться', 'Есть', 'Лежать в луже', 'Есть', 'Лежать в луже', 'Есть', 'Заснуть']


class Ducks(Birds):
    voice_type = 'Crya!'
    count_animals = 5
    max_weight = 10  # kg


class Chickens(Birds):
    voice_type = 'Kudah!'
    count_animals = 17
    max_weight = 4  # kg
    day_plan = ['Проснуться', 'Разбудить всех', 'Нести яйца', 'Есть', 'Заснуть']


class Geese(Birds):
    voice_type = 'GAAGAA! I will kill you!' #гуси страшные! :)
    count_animals = 3
    max_weight = 10  # kg
    cost = 100


def animal_data(animal_class=Pigs()):
    print('Популяция: {} ед.'.format(animal_class.count_animals))
    print('Крик: {}'.format(animal_class.voice(animal_class.voice_type)))
    print('Подьем в {0}, отбой в {1}'.format(animal_class.time_for_wake_up, animal_class.time_for_sleep))
    print('Ест: {}'.format(animal_class.food))
    print('Затраты на еду в день: {} долларов'.format(animal_class.feed_value(animal_class.cost, animal_class.count_animals)))
    print('\nРаспорядок дня:')
    shedule = animal_class.day_deals(animal_class.day_plan)


def animal_research():
    while True:
        input_animal = input('Введите животное (cows, goats, pigs, ducks, chickens, geese) (q для выхода): ').lower()
        if input_animal == 'cows':
            animal_data(Cows())
        elif input_animal == 'goats':
            animal_data(Goats())
        elif input_animal == 'pigs':
            animal_data(Pigs())
        elif input_animal == 'geese':
            animal_data(Geese())
        elif input_animal == 'chickens':
            animal_data(Chickens())
        elif input_animal == 'ducks':
            animal_data(Ducks())
        elif input_animal == 'q':
            break


animal_research()
