speed = 990
speed_limit_town = 50
speed_limit_country = 90
town = False
violation = False
if town:
    fine = 1
    point = 3
    term = 5
    over_speed = speed - speed_limit_town
else:
    fine = 2
    point = 4
    term = 6
    over_speed = speed - speed_limit_country
speed_range = (range(1, 11), range(11, 16), range(16, 21), range(21, 26), range(26, 31),
               range(31, 41), range(41, 51), range(51, 61), range(61, 71), range(71, 1000))
fine_town = (10, 20, 30, 70, 80, 120, 160, 240, 440, 600)
fine_country = (15, 25, 35, 80, 100, 160, 200, 280, 480, 680)
point_town = (0, 0, 0, 1, 1, 1, 2, 2, 2, 2)
point_contry = (0, 0, 0, 1, 1, 1, 2, 2, 2, 2)
term_town = (0, 0, 0, 0, 0, 0, 1, 1, 2, 3)
term_country = (0, 0, 0, 0, 0, 1, 1, 2, 3, 3)
all_tuple = (speed_range, fine_town, fine_country, point_town, point_contry, term_town, term_country)
c=0
for it in all_tuple[0]:
    if over_speed in it:
        print('! ! ! В Ы Я В Л Е Н О    Н А Р У Ш Е Н И Е ! ! !')
        print('Штраф: ', all_tuple[fine][c], 'Евро')
        print('Начислено балов: ', all_tuple[point][c])
        print('Лишение прав на: ', all_tuple[term][c], 'мес.')
        violation = True
    c+=1
if violation != True:
    print("Нарушение не выявлено")

