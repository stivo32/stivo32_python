room_list = []

descr_0 = 'Вы находитесь в первой спальне.\n'
descr_0+= 'В комнате присутствуют двери в северной и восточной стене.\n'
descr_0+= 'Какое направление выбрать?'
room_0 = [descr_0, 3, 1, None, None]

descr_1 = 'Вы находитесь в южной части холла.\n'
descr_1+= 'Вы можете открыть одну из дверей в западной и восточной стенах коридора,' \
          ' либо перейти в северную часть коридора.\n'
descr_1+= 'Какое направление выбрать?'
room_1 = [descr_1, 4, 2, 0, None]

descr_2 = 'Вы находитесь в столовой.\n'
descr_2+= 'В комнате две двери - на западе и на севере комнаты.\n' \
descr_2+= 'Какое направление выбрать?'
room_2 = [descr_2, 5, None, None, 1]

descr_3 = 'Вы находитесь в второй спальне.\n'
descr_3+= 'В комнате все одна дверь - на юге, та через которую вы пришли.\n'
descr_3+= 'Какое направление выбрать?'
room_3= [descr_3, None, None, 0, None]

descr_4 = 'Вы находитесь в северной части холла\n'
descr_4+= 'На севере видна дверь, через которую проходит солнечный свет. Позади вас находится южная часть холла.\n'
descr_4+= 'Какое направление выбрать?'
room_4= [descr_4, 6, None, 1, None]

descr_5 = 'Вы находитесь в кухне.\n'
descr_5+= 'В комнате все одна дверь - на юге, та через которую вы пришли.\n'
descr_5+= 'Какое направление выбрать?'
room_5= [descr_5, None, None, 2, None]

descr_6 = 'Вы находитесь на открытом балконе.\n'
descr_6+= 'Прыгать вниз высоко, сзади вас дверь, ведущая в дом.\n'
descr_6+= 'Какое направление выбрать?'
room_6= [descr_6, None, None, 4, None]

room_list.append(room_0)
room_list.append(room_1)
room_list.append(room_2)
room_list.append(room_3)
room_list.append(room_4)
room_list.append(room_5)
room_list.append(room_6)

current_room = room_list[0]

done = False

while not done:
    print('\n'+current_room[0])
    answer = input()
    if answer == 'n':
        if current_room[1] is not None:
            current_room = room_list[current_room[1]]
            continue
        else:
            print('С этой стороны нету двери. Выберите другое направление..')
            continue
    elif answer == 'e':
        if current_room[2] is not None:
            current_room = room_list[current_room[2]]
            continue
        else:
            print('С этой стороны нету двери. Выберите другое направление.')
            continue
    elif answer == 's':
        if current_room[3] is not None:
            current_room = room_list[current_room[3]]
            continue
        else:
            print('С этой стороны нету двери. Выберите другое направление.')
            continue
    elif answer == 'w':
        if current_room[4] is not None:
            current_room = room_list[current_room[4]]
            continue
        else:
            print('Р’С‹ РЅРµ РјРѕР¶РµС‚Рµ РїРѕР№С‚Рё РІ СЌС‚РѕРј РЅР°РїСЂР°РІР»РµРЅРёРё')
            continue
    elif answer == 'q':
        done = True
        print('Р’С‹С…РѕРґ РёР· РёРіСЂС‹')
    else:
        print('РќРµРІР°Р»РёРґРЅС‹Р№ РІРІРѕРґ. Р’С‹Р±РёСЂР°Р№С‚Рµ РЅР°РїСЂР°РІР»РµРЅРёРµ РёР· n, e, s, w')
