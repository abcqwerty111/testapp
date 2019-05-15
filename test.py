# -*- coding: utf-8 -*-
import telebot
import urllib
import datetime
from io import BytesIO
from PIL import Image
from colorama import init
from colorama import Fore, Back, Style
from termcolor import colored

init()

bot = telebot.TeleBot('877583206:AAHco4-zSu1wbVIBX5mlk7f8EgoIVDlAHMc')

rasp = 'https://psv4.userapi.com/c848132/u232799244/docs/d4/a4c3211a3906/rasp.jpg?extra=mxbU5lfyBmwXqA8XnSkprSSTRPylfN0AhEaVtTUFI3GtF6IhYGLftwzEHZpqbsBfCSWvts1out3U4lXS0Ub8AvXjnsZlcWOioLp-HJhKlKuIZOK3kwk3HcDgZaZlae4Y2FrlUJXrhbn8qvu1jdAbjzTp'
ekz = 'https://pp.userapi.com/c852132/v852132369/11038f/5YnxKwNg2Fw.jpg'
assault = 'https://psv4.userapi.com/c848236/u232799244/docs/d3/484930f9b523/assault.png?extra=nHsMT3J9CFA5-uSjno_BMGPRm84SNAYBNQUjvSoFGDVX652oAJOAQq6Zbv2bjX6x9DPqwe9oLGM2-XlTa-pv08aFakY1DPj_DPPWyteAwJjL9Yki55zZWkOmoFrg6tOVM_yiBCfe2I61Lq37DZnpXc_hisc'
polyl = 'https://psv4.userapi.com/c848236/u232799244/docs/d14/d60e6ff6764e/polyl.png?extra=5zSTzBx7azOzW6o0geU2yIkk1tD88VNQYB3cJ-g7UR2gzls9NKw177SYj13PImIju1jJjEaW3fxKoR7pS_TMFyKb9NNQPNFFFIm3_TlpBQbJau2KqU4z_UpWjqoBM3U2yO2-Nb99dj7Pbf8nOFBz-ZrExHo'
sticker_id = 'CAADAgADPwkAAnlc4gkgcZ3NjaydaAI'

@bot.message_handler(commands = ['start', 'help'])
def command_handler(message):

    bot.send_message(message.chat.id, 'hi')

@bot.message_handler(content_types = ['text'])
@bot.edited_message_handler(content_types = ['text'])
def send_echo(message):

    mt = message.text
    mid = message.chat.id
    name = message.from_user.first_name
    wd = datetime.datetime.today().weekday()
    
    if 'асписани' in mt:
        bot.send_photo(mid, rasp)
        answer = 'Вот Ваше расписание, сэр'

    elif 'ривет' in mt:
        answer = 'Приветствую Вас, ' + name

    elif 'пар' in mt:
        if wd == 0:
            answer = ('''Понедельник:
10:55-12:40    ЭК (Лекция-410)/---
13:10-14:55    ЭК (Лаб-411)
15:05-16:50    ИМ (Лекция-411)''')
        elif wd == 1:
            answer = ('''Вторник:
09:00-10:45    ПиРПБД (Лаб-300е)
10:55-12:40    КИ (Лаб-411)
13:10-14:55    АСБУ (Лекция/Семинар-411)
15:05-16:50    АСБУ (Лаб-411)''')
        elif wd == 2:
            answer = ('''Среда:
10:55-12:40    ОАК (Лекция-I-210)/---
13:10-14:55    ИМ (Лаб-411)
15:05-16:50    ЭК (Лаб-410)''')
        elif wd == 3:
            answer = ('''Четверг:
10:55-12:40    ОиТЗИ (Лекция-411)/КИ (Лекция=300в)
13:10-14:55    ОиТЗИ (Лаб-411)
15:05-16:50    ---/ИМ (Лекция-410)''')
        elif wd == 4:
            answer = ('''Пятница:
09:00-10:45    ПиРПБД (Лаб-300е)
10:55-12:40    ПиРПБД (Лекция-300б)/(Семинар-411)
13:10-14:55    ОиТЗИ (Лаб-411)
15:05-16:50    ОАК (Семинар-I-226)/---''')
        else:
            answer = 'Сегодня выходной, сэр\nНо не стоит отдыхать, проведите свободное время с пользой'

    elif 'пасиб' in mt:
        answer = 'я создан, чтобы служить Вам, сэр'

    elif 'кзамен' in mt:
        bot.send_photo(mid, ekz)
        answer = 'Расписание экзаменов'

    elif 'наний исследования' in mt:
        answer = '''
1. Общемировые условия развития инновационной экономики знаний
2. Фундаментальные аналитические исследования
3. Построение кругового массива и его редактирование в Autocad
https://vk.com/doc232799244_502140883?hash=bdb6ada638e96bece6&dl=1de4a2ac1fbdea3de9'''

    elif 'истем ansys' in mt:
        bot.send_photo(mid, 'https://pp.userapi.com/c852228/v852228540/11a1c8/bMH-hDt0W2U.jpg')
        answer = '''
1. Основные группы стейкхолдеров CAE- и PLM- систем
2. ANSYS
3. Пример сложения матриц в MathCAD
https://vk.com/doc232799244_502141301?hash=66dfb48e01f2c9413f&dl=ac304d64c59b4e2cd7'''

    elif 'истем ANSYS' in mt:
        bot.send_photo(mid, 'https://pp.userapi.com/c852228/v852228540/11a1c8/bMH-hDt0W2U.jpg')
        answer = '''
1. Основные группы стейкхолдеров CAE- и PLM- систем
2. ANSYS
3. Пример сложения матриц в MathCAD
https://vk.com/doc232799244_502141301?hash=66dfb48e01f2c9413f&dl=ac304d64c59b4e2cd7'''

    elif 'ystèmes MathWorks' in mt:
        bot.send_photo(mid, assault)
        answer = '''
1. Dassault Systèmes
2. MathWorks
3. Опишите процесс построения следующей фигуры
https://vk.com/doc232799244_502141613?hash=f811f2347fa816ff5a&dl=0a4d4f5738a7fc288d'''

    elif 'ystemes mathworks' in mt:
        bot.send_photo(mid, assault)
        answer = '''
1. Dassault Systèmes
2. MathWorks
3. Опишите процесс построения следующей фигуры
https://vk.com/doc232799244_502141613?hash=f811f2347fa816ff5a&dl=0a4d4f5738a7fc288d'''

    elif 'utodesk АСКОН' in mt:
        answer = '''
1. Опишите продукты Autodesk
2. АСКОН
3. Перемножьте вектор-строки v1 = (9 2 -5 4) и v2 = (3 7 -6 1)
https://vk.com/doc232799244_502308911?hash=fd54fa205fa3d9eab3&dl=8bd3069c9db6818eb2
'''

    elif 'utodesk аскон' in mt:
        answer = '''
1. Опишите продукты Autodesk
2. АСКОН
3. Перемножьте вектор-строки v1 = (9 2 -5 4) и v2 = (3 7 -6 1)
https://vk.com/doc232799244_502308911?hash=fd54fa205fa3d9eab3&dl=8bd3069c9db6818eb2
'''

    elif 'наний систем' in mt:
        bot.send_photo(mid, polyl)
        answer = '''
1. Общемировые условия развития инновационной экономики знаний
2. Cложность MCAE-систем
3. Опишите процесс создания двуцветной полилинии по примеру, изображённому на рисунке
https://vk.com/doc232799244_502309111?hash=5e609d2644f1d23d03&dl=b615110f015f6cf8b7
'''

    elif 'ехнологий технологий' in mt:
        answer = '''
1. Объем рынка CAE-технологий
2. Структура доходов ведущих поставщиков PLM-технологий
3. Опишите процесс создания пирамиды из отрезков. Опишите процесс окрашивания граней в различные цвета
https://vk.com/doc232799244_502308910?hash=d72d5334c4a8f9336f&dl=8f2ec849abb3c9eb14


1. Финансовый анализ рынка CAD-, CAE- и PLM-технологий
2. Объем рынка CAE-технологий 
3. Опишите процесс умножения вектора-строки v1 = (9 2 -5 4) и v2 = (3 7 -6 1) в MathCad
'''

    elif 'ехнологий систем' in mt:
        answer = '''
1. Структура рынка PLM-технологий и доля CAE-технологий
2. Тop-11 рынка CAE систем
3. Опишите процесс создания матрицы три на три, воспользовавшись функцией matrix ()
https://vk.com/doc232799244_502142049?hash=dee7f3a807d0e8c352&dl=d2cda3fe162b20ae16'''

    elif 'cs моделирования' in mt:
        answer = '''
1. ADEM, Model Studio CS
2. Создание и внедрение отечественного ПО имитационного моделирования. Создание отечественного 3D-ядра трехмерного моделирования.
3. Опишите процесс работы со слоями в Autocad
https://vk.com/doc232799244_502142439?hash=4e223f6c8dac44d0c4&dl=2f3757a1e71981279f'''

    elif 'CS моделирования' in mt:
        answer = '''
1. ADEM, Model Studio CS
2. Создание и внедрение отечественного ПО имитационного моделирования. Создание отечественного 3D-ядра трехмерного моделирования.
3. Опишите процесс работы со слоями в Autocad
https://vk.com/doc232799244_502142439?hash=4e223f6c8dac44d0c4&dl=2f3757a1e71981279f'''

    elif 'истем систем' in mt:
        answer = '''
1. Рынок MCAE-систем
2. Сложность MCAE-систем
3. Опишите процесс сложения и разности матриц с размерностью 2:3
https://vk.com/doc232799244_502142778?hash=0f193ecb321f73f194&dl=dff4be6af403694028


1. Cложность MCAE-систем
2. Основные группы стейкхолдеров CAE- и PLM- систем
3. Опишите процесс создания и пример сложения матриц в MathCAD
https://vk.com/doc232799244_502309972?hash=65838887f9199cf701&dl=b94fab3cabae2b262b
'''

    elif 'онцепция design' in mt:
        answer = '''
1. Инновационная M^3-концепция – “MultiDisciplinary & MultiScale / MultiStage& MultiTechnology (MultiCAD & MultiCAE)”-концепция*.
2. Концепция “Simulation-Based Design”
3. Опишите процесс создания своего типа линии в Autocad
https://vk.com/doc232799244_502323181?hash=c7c142bc025cd8aa03&dl=8677db68ab91fe73dc
'''

    elif 'онцепция Design' in mt:
        answer = '''
1. Инновационная M^3-концепция – “MultiDisciplinary & MultiScale / MultiStage& MultiTechnology (MultiCAD & MultiCAE)”-концепция*.
2. Концепция “Simulation-Based Design”
3. Опишите процесс создания своего типа линии в Autocad
https://vk.com/doc232799244_502323181?hash=c7c142bc025cd8aa03&dl=8677db68ab91fe73dc
'''

    elif 'esign технологии' in mt:
        answer = '''
1. Эволюция концепции “Simulation-Based Design”.
2. САD/САМ-технологии
3. Опишите процесс построения матрицы и нахождения определителя в Mathcad
https://vk.com/doc232799244_502323182?hash=1bf1ee33f151a303ec&dl=ad74d5edfb1074e3b8
'''

    elif 'ce системы' in mt:
        answer = '''
1. Concurrent Engineering (CE)
2. PDM-системы
3. Опишите процесс вычисления значения функции sin(x) и cos(x) на отрезке [0, 10] с шагом 0.5 в Mathcad
https://vk.com/doc232799244_502323183?hash=1c2ceaeebb89045a11&dl=a37ce8b1da34d5c2d0
'''

    elif 'CE системы' in mt:
        answer = '''
1. Concurrent Engineering (CE)
2. PDM-системы
3. Опишите процесс вычисления значения функции sin(x) и cos(x) на отрезке [0, 10] с шагом 0.5 в Mathcad
https://vk.com/doc232799244_502323183?hash=1c2ceaeebb89045a11&dl=a37ce8b1da34d5c2d0
'''

    elif 'anagement collaboration' in mt:
        answer = '''
1. Research Knowledge Management
2. 3D Visualization & Virtual Reality & Global Visual Collaboration
3. Опишите процесс cоздания матрицы произвольного размера и нахождения минимального и максимального элемента матрицы.
https://vk.com/doc232799244_502305346?hash=b8f7fe2b730301e717&dl=ad954dd3ea74999c89
'''

    elif 'anagement Collaboration' in mt:
        answer = '''
1. Research Knowledge Management
2. 3D Visualization & Virtual Reality & Global Visual Collaboration
3. Опишите процесс cоздания матрицы произвольного размера и нахождения минимального и максимального элемента матрицы.
https://vk.com/doc232799244_502305346?hash=b8f7fe2b730301e717&dl=ad954dd3ea74999c89
'''

    elif 'нализ технологии' in mt:
        answer = '''
1. FEA (конечно-элементный анализ; КЭ анализ)
2. PLM - технологии
3. Опишите процесс построения массива пятиугольников с размерностю 2:3 и смещение его по оси Х на 45 градусов в Mathcad
https://vk.com/doc232799244_502305339?hash=6852353e2852b5682c&dl=7b1ddd6fcc6b3ff102
'''

    elif 'наний mathworks' in mt:
        bot.send_photo(mid, assault)
        answer = '''
1. Общемировые условия развития инновационной экономики знаний
2. MathWorks
3. Опишите процесс построения следующей фигуры
https://vk.com/doc232799244_502306253?hash=1d042663cca1be33c8&dl=c266c1813599c4a18c
'''

    elif 'истемы исследования' in mt:
        answer = '''
1. САD/САМ-системы
2. Фундаментальные аналитические исследования
3. Опишите процесс создания пирамиды из отрезков. Опишите процесс окрашивания граней в различные цвета
https://vk.com/doc232799244_502309970?hash=761a55a462d359370c&dl=757ce60adc8969e212
'''

    elif 'истем corporation' in mt:
        answer = '''
1. Рынок MCAE-систем
2. Классификация MCAE-систем компании Cyon Research Corporation
3. Опишите процесс построения кругового массива и его редактирование в Autocad
https://vk.com/doc232799244_502309973?hash=4ba8cab7d973bf6d59&dl=34bb0aac207f956129
'''

    elif 'NSYS моделирования' in mt:
        bot.send_photo(mid, polyl)
        answer = '''
1. ANSYS
2. Создание и внедрение отечественного ПО имитационного моделирования
3. Опишите процесс создания двуцветной полилинии по примеру,  изображённому на рисунке
'''

    elif 'nsys моделирования' in mt:
        bot.send_photo(mid, polyl)
        answer = '''
1. ANSYS
2. Создание и внедрение отечественного ПО имитационного моделирования
3. Опишите процесс создания двуцветной полилинии по примеру,  изображённому на рисунке
'''

    elif 'cs технологии' in mt:
        answer = '''
1. ADEM, Model Studio CS
2. PDM - технологии
3. Опишите процесс вычисления значения функции sin(x) и cos(x) на отрезке [0, 10] с шагом 0.5 в Mathcad
'''

    elif 'CS технологии' in mt:
        answer = '''
1. ADEM, Model Studio CS
2. PDM - технологии
3. Опишите процесс вычисления значения функции sin(x) и cos(x) на отрезке [0, 10] с шагом 0.5 в Mathcad
'''

    elif 'истем технологии' in mt:
        answer = '''
1. Тop-11 рынка CAE систем
2. PDM - технологии
3. Опишите процесс создания матрицы три на три, воспользовавшись функцией  matrix () в MathCad
'''

    elif 'ystemes autodesk' in mt:
        answer = '''
1. Dassault Systèmes
2. Опишите продукт Autodesk
3. Опишите процесс работы со слоями в Autocad
https://vk.com/doc232799244_502281594?hash=7525b0ba712e7a59d7&dl=1e9b2af08caea7a46e
'''

    elif 'ystèmes Autodesk' in mt:
        answer = '''
1. Dassault Systèmes
2. Опишите продукт Autodesk
3. Опишите процесс работы со слоями в Autocad
https://vk.com/doc232799244_502281594?hash=7525b0ba712e7a59d7&dl=1e9b2af08caea7a46e
'''

    elif 'ystèmes autodesk' in mt:
        answer = '''
1. Dassault Systèmes
2. Опишите продукт Autodesk
3. Опишите процесс работы со слоями в Autocad
https://vk.com/doc232799244_502281594?hash=7525b0ba712e7a59d7&dl=1e9b2af08caea7a46e
'''

    elif 'athworks аскон' in mt:
        answer = '''
1. MathWorks
2. АСКОН
3. Опишите виды штриховки в AutoCAD.
https://vk.com/doc232799244_502281599?hash=8f486987461dc672a9&dl=08b5f08d5df46cddf7
'''

    elif 'athWorks АСКОН' in mt:
        answer = '''
1. MathWorks
2. АСКОН
3. Опишите виды штриховки в AutoCAD.
https://vk.com/doc232799244_502281599?hash=8f486987461dc672a9&dl=08b5f08d5df46cddf7
'''

    elif 'esign технологий' in mt:
        answer = '''
1. Концепция “Simulation-Based Design”
2. Объем рынка CAE-технологий
3. Опишите приемы выполнения объектной привязки в AutoCAD
https://vk.com/doc232799244_502281601?hash=a4c1a392aeb0ab97b7&dl=8e1cb16991b8552352
'''

    else:
        answer = 'Не понял Вас, сэр'
        bot.send_sticker(mid, sticker_id)
        bot.send_message(888833912, mt)

    bot.send_message(mid, answer)
    print(colored(mid, 'red'))
    print(colored(name, 'yellow'))
    print(colored(mt, 'white'))
    print(colored(answer, 'green'))
    print(' ')

@bot.message_handler(content_types = ['sticker'])
def sticker_handler(message):
    bot.send_sticker(message.chat.id, sticker_id)

bot.polling(none_stop = True)