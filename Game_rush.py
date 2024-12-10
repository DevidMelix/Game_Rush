import random

def input_player_data_start():
    name_player = input('Введите ваше имя: ')
    species_player = int(input('Введите вашу расу [1-10]: '))
    class_player = int(input('Введите ваш класс [1-10]: '))
    return name_player, species_player, class_player

 
def all_characteristic_player():
    charact = {
        'name': '',
        'health': 0,
        'power': 0,
        'stamina': 0,
        'defens': 0,
        'agility': 0,
    }
    return charact


def species_characteristic():
    array_parametr_species = [
                 # name     hth    pw     stm   df     agl
                 ['Человек',6.5,   5.43,  6.2,  4.5,   4.3 ],
                 ['Огр',    6.21,  6.34,  3.7,  5.6,   3.2 ],
                 ['Каджит', 5.45,  4.21,  6.23, 4.11,  5.98 ],
                 ['Дварф',  6.52,  4.7,   5.22, 6.78,  4.55 ],
                 ['Грунг',  4.2,   4.52,  6.15, 5.78,  7.05 ],
     ['Драконарожденный',   4.89,  7.13,  6.47, 4.8,   3.7 ],
                 ['Голиаф', 8.5,   3.9,   5.87, 4.72,  3.7 ],
                 ['Демон',  5.5,   7.4,   6.21, 4.1,   3.9 ],
                 ['Фурри',  4,     3.72,  3.71, 3.75,  3.80 ],
           ['Белый Ходак',  4.025, 5.77,  6.66, 7.52,  4.2 ],
         ]
    species = []
    for parametrs in array_parametr_species:
             species.append( 
                 { 'name':parametrs[0], 
                   'health':parametrs[1], 
                   'power':parametrs[2], 
                   'stamina':parametrs[3],
                   'defens':parametrs[4],
                   'agility':parametrs[5]
                 })
             
    return species 


def class_characteristic():
    array_parametr_class = [
                 # name     hth    pw     stm   df     agl
                 ['Рыцарь', 4.2,   5.6,  -3.1,  4.5,   -1 ],
                 ['Огр',    6.21,  6.34,  3.7,  5.6,   3.2 ],
                 ['Каджит', 5.45,  4.21,  6.23, 4.11,  5.98 ],
                 ['Дварф',  6.52,  4.7,   5.22, 6.78,  4.55 ],
                 ['Грунг',  4.2,   4.52,  6.15, 5.78,  7.05 ],
     ['Драконарожденный',   4.89,  7.13,  6.47, 4.8,   3.7 ],
                 ['Голиаф', 8.5,   3.9,   5.87, 4.72,  3.7 ],
                 ['Демон',  5.5,   7.4,   6.21, 4.1,   3.9 ],
                 ['Фурри',  4,     3.72,  3.71, 3.75,  3.80 ],
           ['Белый Ходак',  4.025, 5.77,  6.66, 7.52,  4.2 ],
         ]
    

    game_class = [

        {
            'name': 'Бандит',
            'health': -2.5,
            'power': -1.32,
            'stamina': 3.4,
            'defens': -2.5,
            'agility': 3.2,
            

        },

        {
            'name': 'Самурай',
            'health': 2.68,
            'power': 3.44,
            'stamina': 1.2,
            'defens': -3.5,
            'agility': 2.78,
            
        },

        {
            'name': 'Бард',
            'health': 1.76,
            'power': 1.21,
            'stamina': 2.52,
            'defens': -3.55,
            'agility': -2.21
        },

        {
            'name': 'Ведьмак',
            'health': -2.42,
            'power': 3.52,
            'stamina': 3.12,
            'defens': -2.23,
            'agility': 1.675
        },

        {
            'name': 'Маг',
            'health': -3.6,
            'power': 6.76,
            'stamina': -1.73,
            'defens': -1.24,
            'agility': 5.2
        },

        {
            'name': 'Лучник',
            'health': 2.7,
            'power': 5.76,
            'stamina': 3.7,
            'defens': -3.7,
            'agility': 3.9
        },

        {
            'name': 'Выживальщик',
            'health': 3,
            'power': 3.65,
            'stamina': 4.21,
            'defens': 3.42,
            'agility': 3.63
        },

        {
            'name': 'Нищий',
            'health': -2,
            'power': 2,
            'stamina': 2,
            'defens': -2,
            'agility': 2
        },

        {
            'name': 'Убийца',
            'health': 3.4,
            'power': 5.7,
            'stamina': -3,
            'defens': -2.86,
            'agility': 6.2
        }
        
    ]
    return game_class


def all_enemy():
    enemies = [
        {
            'name': 'Драугр',
            'health': 3.52,
            'power': 3.12
        },
        {
            'name': 'Злобная крыса',
            'health': 2.42,
            'power': 1.5
        },
        {
            'name': 'Кикимора',
            'health': 5.12,
            'power': 7.21
        },
        {
            'name': 'Гигантский паук',
            'health': 7.56,
            'power': 5.12
        },
        {
            'name': 'Дракон',
            'health': 6.21,
            'power': 4.56
        },
        {
            'name': 'Бристелбек',
            'health': 4.75,
            'power': 4.41,
        },
        {
            'name': 'Алхун',
            'health': 3.45,
            'power': 5.8
        },
        {
            'name': 'Аспект Бахамута',
            'health': 5.12,
            'power': 4.7,
        },
        {
            'name': 'Буцефал',
            'health': 5.12,
            'power': 4.12,
        },
        {
            'name': 'Брахиозавр зомби',
            'health': 1.87,
            'power': 2.5
        },
        {
            'name': 'Воин призраков меча',
            'health': 6.35,
            'power': 6.87
        },
        {
            'name': 'Веломахус Лорхолд',
            'health': 5.967,
            'power': 5.13
        },
        {
            'name': 'Гигантский скорпион',
            'health': 4.74,
            'power': 2.14
        },
        {
            'name': 'Гнилой тролль',
            'health': 1.78,
            'power': 5.72
        },
        {
            'name': 'Двуглавый цербер',
            'health': 7.4,
            'power': 5.24
        },
        {
            'name': 'Дух дриады',
            'health': 7,
            'power': 4.957
        },
        {
            'name': 'Жрец Вечного Пламени',
            'health': 6.36,
            'power': 4.8,
        },
        {
            'name': 'Жрец Чёрной Земли',
            'health': 4.17,
            'power': 3.86
        },
        {
            'name': 'Зрелый облекс',
            'health': 6.15,
            'power': 3.98
        },
        {
            'name': 'Избранный драконом',
            'health': 7.1,
            'power': 6.11
        },
        {
            'name': 'Ифрит',
            'health': 5.7,
            'power': 4.163
        },
        {
            'name': 'Зираж-охотник',
            'health': 5.82,
            'power': 4.8
        },
        {
            'name': 'Имикс',
            'health': 2.72,
            'power': 4.21,
        },
        {
            'name': 'Когтелап',
            'health': 6.152,
            'power': 5.123
        },
        {
            'name': 'Калейн',
            'health': 4.92,
            'power': 3.78
        },
        {
            'name': 'Косатка',
            'health': 7.145,
            'power': 5.82
        },
        {
            'name': 'Кентавр',
            'health': 4.825,
            'power': 5.78
        }
        
    ]

    return enemies


def boss_enemy():
    bosses = {
        'name': 'Бармен',
        'health': 10,
        'power': 9
    }

    return bosses


def show_txt_start(species, game_class):
    print('Выбор рассы')
    for i, specie in enumerate(species):
        print(i + 1, specie['name'])
    
    print()

    print('Выбор класса')
    for i, categoty in enumerate(game_class):
        print(i + 1, categoty['name'])
    

def show_txt_player_choise(args, species, game_class):
    print()
    name_player, species_player, class_player = args
 
    new_species_player = species[species_player-1]
    new_class_player = game_class[class_player-1]

    vid = new_species_player['name']
    klass = new_class_player['name']

    print(f'{name_player}, вы {vid} - {klass}')
    return new_species_player, new_class_player, name_player, vid, klass

 
def status_characteristic_player(args, charact):
    new_species_player, new_class_player,name_player, vid, klass = args
    print('Ваши характеристики:')
    for key in charact:
        charact[key] += new_species_player[key] + new_class_player[key]
    
    del charact['name']


    for key in charact:
        charact[key] = round(charact[key], 2)


    for key, value in charact.items():
     print(key, value)
    
    return charact, name_player, vid, klass, 
        

def select_random_begin_quest():
    print()
    quest_bar_1 = f"""Проснувшись в баре за барной стойкой вы не можете вспомнить прошлую ночь, бармен говорит вам что вчера вы нехило 
так развлеклись и потратили все свое золото, с грустью вы вышли из бара и начали проверять свои карманы в надежде найти хоть пару золотых. 
Вместо золото вы нашли скомканную бумажку, вы не знаете как она оказалась у вас в кармане, раскрыв ее вы понимаете что это 
карта сокровищ ведущая к некой крепости. У вас не остается выбора как рискнуть и пойти туда."""

#    quest_les_2 = f"""Лежа в палатке вы услышали странный звук, без промедления вы выходите и осматриваете свой лагерь. Здесь ни души, вы кричите и зовете,
#но никто не откликается. В придачу ко всей этой ситуации вы нашли в центре лагеря загодочные следы ранее не виденные вами, следы эти 
#вели прямо в темный густой лес в который вы хотели отправиться с группой, видимо придется пойти туда в одиночку, выпив для храбости и подготовив снаряжение 
#вы отправляется прямо по этим следам в поисках своих друзей."""

    all_quest = [quest_bar_1]

    now_quest = random.choice(all_quest)
    return now_quest


def select_random_enemy(enemies):
    random_enemy = random.choice(enemies) 
    return random_enemy


def transform_charact_enemy(random_enemy):
    health = round((random_enemy['health'] * 150), 2)
    power = round((random_enemy['power'] * 15), 2)
    points_enemy = {
        'name': random_enemy['name'],
        'health_point': health,
        'power_point': power
    }
    return points_enemy


def transform_charact_player(charact):
    charact, name_player, vid, klass = charact 
    health = round(charact['health'] * 100, 2)
    power = round(charact['power'] * 10, 2)
    stamina = round(charact['stamina'] * 100, 2)
    defens = round(charact['defens'] * 5, 2)
    agility = round((((charact['agility'] + charact['stamina']) * 10) // 3), 2)

    points = {
        'health_point': health,
        'power_point': power,
        'stamina_point': stamina,
        'defens_point': defens,
        'agility_point': agility
    }
    
    return points


def interface_points_enemy(points_enemy):
    health_point = round(points_enemy['health_point'], 2)
    interface_enemy = {
        'Враг': points_enemy['name'],
        'Здоровье -->': health_point,
        'Сила удара -->': points_enemy['power_point']
    }

    for key, value in interface_enemy.items():
     print(key, value)

    return interface_enemy


def interface_points(points_player, static_points_player):
    health = f'{round(points_player["health_point"], 2)} // {round(static_points_player["health_point"], 2)}'
    stamina = f'{points_player["stamina_point"]} // {static_points_player["stamina_point"]}'

    interface_player = {
        'Здоровье -->': health,
        'Сила удара -->': points_player['power_point'],
        'Выносливость -->': stamina,
        'Защита -->': points_player['defens_point'],
        'Ловкость -->': points_player['agility_point']

    }

    for key, value in interface_player.items():
     print(key, value)

    return interface_player


def input_action_player():
    action = int(input('Введите желаемое действие [1-4]: '))

    return action


def simple_attack_player(points_player, points_enemy):
    points_enemy['health_point'] -= points_player['power_point']
    points_player['stamina_point'] -= 50
    return points_player['power_point']


def risk_attack_player(points_player,points_enemy, risk_now):
    points_enemy['health_point'] -= risk_now
    points_player['stamina_point'] -= 75


def add_stamina_player(points_player, stamina_now):
    points_player['stamina_point'] += stamina_now


def add_health_player(points_player, health_now):
    points_player['health_point'] += health_now


def select_stamina():
    stamina_now = random.randint(50, 500)

    return stamina_now


def select_health():
    health_now = random.randint(50, 200)

    return health_now


def select_defens(points_player):
    defens_now = random.randint(0, int(points_player['defens_point']))
    
    return defens_now


def select_risk_attack_player(points_player):
    risk_now = random.randint(int((points_player['power_point'] // 2)), int((points_player['power_point'] * 3)))
    
    return risk_now


def select_dodge(points_player):
    agility_now = points_player['agility_point']

    dodge = [True, False]   
    chance = [agility_now % 100, 100 - agility_now % 100]

    chance_dodge = random.choices(dodge, weights=chance, k=1)[0]

    return chance_dodge


def simple_attack_enemy(points_player, points_enemy):
    defens_now = select_defens(points_player)
    points_player['health_point'] -= (abs(defens_now - points_enemy['power_point']))

    return defens_now
    

def limit_add_points_health(health_now, static_points_player, points_player):
    if points_player['health_point'] + health_now > static_points_player['health_point']:
        points_player['health_point'] = static_points_player['health_point']

    else:
        points_player['health_point'] += health_now
        
       
def limit_add_points_stamina(stamina_now, static_points_player, points_player):
    if points_player['stamina_point'] + stamina_now > static_points_player['stamina_point']:
        points_player['stamina_point'] = static_points_player['stamina_point']
    else:
        points_player['stamina_point'] += stamina_now
    

def do_action(action, points_enemy):
    risk_now = select_risk_attack_player(points_player)
    stamina_now = select_stamina()
    health_now = select_health()
    
    if action == 1:
        attack = simple_attack_player(points_player, points_enemy)
        return attack

    elif action == 2:
        risk_attack_player(points_player,points_enemy, risk_now)
        return risk_now

    elif action == 3:
        limit_add_points_health(health_now, static_points_player, points_player)
        return health_now

    elif action == 4:
        limit_add_points_stamina(stamina_now, static_points_player, points_player)
        return stamina_now
    

def show_option_txt(points_player):
    attack = points_player['power_point']
    stamina = points_player['stamina_point']

    show_txt_no_stamina(stamina, attack)
    
    print('3 - Выпить лечебное зелье [50 - 200]')
    print('4 - Отдохнуть [50 - 500]')


def show_txt_no_stamina(stamina, attack):
    if stamina < 50:
        print('1 - Нет выносливости!')
        print('2 - Нет выносливости!')
    
    elif 50 <= stamina < 75:
        print('1 - Совершить обычный удар : -50 стамины')
        print('2 - Нет выносливости!')
    
    else:
        print('1 - Совершить обычный удар : -50 стамины')
        print(f'2 - Совершить РИСКОВЫЙ УДАР [{int((points_player["power_point"] // 2))} - {int((points_player["power_point"] * 3))}]: -75 стамины')


def check_enough_stamina(points_player, action):
    if action == 1 and points_player['stamina_point'] < 50:
        return False
    
    elif action == 2 and  points_player['stamina_point'] < 75:
        return False 
    return True


def check_health_enemy(points_enemy):
    if points_enemy['health_point'] < 0.000:
        return True
        

def check_health_player(points_player):
    if points_player['health_point'] < 0.000:
        return True
        

def show_who_player(args):
    charact, name_player, vid, klass = args
    print(f'{name_player} {vid} - {klass}')
  

def show_txt_result_action(action, result):
    if action == 1:
        print(f'------------------------------->Вы нанесли обычный удар: {result}')
    
    elif action == 2:
        print(f'------------------------------->Вы нанесли РИСКОВЫЙ удар: {result}')
    
    elif action == 3:
        print(f'------------------------------->Вы восстановили {result} здоровья')
    
    elif action == 4:
        print(f'------------------------------->Вы восстановили {result} стамины')



def show_txt_defense_from_enemy(defens):
    print(f'------------------------------->Вы защитились от {defens} урона врага')


def limit_line_step():
    print('*****************************************************')
    print()


def limit_line_txt():
    print('=========================================================================')
    


def select_enemy_now(enemy):
    points_enemy = enemy

    return points_enemy


show_txt_start(species_characteristic(), class_characteristic())
print()
choise = show_txt_player_choise(input_player_data_start(), species_characteristic(), class_characteristic())
charact = status_characteristic_player(choise, all_characteristic_player())
static_points_player = transform_charact_player(charact)
points_player = transform_charact_player(charact)
print()
interface_points(points_player, static_points_player)
print()
print()


def fight_process_start_player(now_enemy):
    points_enemy = now_enemy 
    while True:
        interface_points_enemy(points_enemy)
        print('*------------------*')
        show_who_player(charact)
        interface_points(points_player, static_points_player)
        print('*------------------*')
        show_option_txt(points_player)
        action = input_action_player()
        dodge = select_dodge(points_player)
        
        if check_enough_stamina(points_player, action):
            result = do_action(action, points_enemy)
            limit_line_step()
            show_txt_result_action(action, result)
            
            if check_health_enemy(points_enemy):
                return True
            

            if dodge:
                print('------------------------------->Вы уклонились от атаки')
            else:
                show_txt_defense_from_enemy(simple_attack_enemy(points_player, points_enemy))
                if check_health_player(points_player):
                    print('Победа была близка...')
                    return False

        else:
            limit_line_step()
            continue
        print()
        

def game_rush():
    kills = 0
    while True:

        limit_line_txt()
        print(f'Вы убили: {kills}')
        limit_line_txt()
        if fight_process_start_player(transform_charact_enemy(select_random_enemy(all_enemy()))):
            kills += 1
            continue
        else:
            limit_line_txt()
            print(f'Ваш рекорд: {kills}')
            limit_line_txt()
            break


game_rush()

