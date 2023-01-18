import datetime
from http.client import SWITCHING_PROTOCOLS
from time import time

NUMBER_OF_MENU_POINTS = 3

def printFile(fileName):
    with open(fileName, 'r') as file:
        for line in file:
            print(line.rstrip())
    pass

#можно спрашивать и хранить в настройках формат времени для ввода
#сделать чтобы хранило часы
def get_time_in_loop():
    ok = False

    while not ok:
        str = input("Введите время в формате 0000: ")
        if len(str) > 4 or len(str) < 3:
            continue
        if len(str) == 3:
            str = "0"+str
        ok = True
    hours = int(str[:2])
    mins = int(str[2:])

    timeNow = datetime.datetime.now()
    timeobj = datetime.datetime(timeNow.year, timeNow.month, timeNow.day,hours,mins)
    return timeobj

def intro_banner():
    printFile('intro')

def menu_banner():
    printFile('menu')

def menu_switch():
    num = 0
    num_str = input("Введите номер пункта меню: ")

    is_ok = True
    try:
        num = int(num_str)
    except:
        is_ok = False
        print("Ошибка: Значение не является числом, либо содержит недопустимые символы")
    
    if (num < 1 and num > NUMBER_OF_MENU_POINTS): is_ok = False

    if (is_ok):
        if (num == 1):
            menu_from_to()
        elif (num == 2):
            pass
        elif (num == 3):
            pass

def menu_from_to():
    timeNow = datetime.datetime.now()
    timeobj = get_time_in_loop()
    timeEnd = get_time_in_loop()

    timeDiff = timeEnd - timeobj
    diffHours = timeDiff.seconds//3600
    diffMins = (timeDiff.seconds - diffHours*3600)//60
    if diffHours > 4:
        if (diffMins < 45):
            diffHours-=1
        diffMins = 45
        tT = timeobj + datetime.timedelta(minutes=diffMins, hours=diffHours)

        delta = tT - timeNow
        deltaHours = delta.seconds//3600
        deltaMins = (delta.seconds - deltaHours*3600)//60

        print(f"Работаем {str(diffHours).zfill(2)}:{str(diffMins).zfill(2)}. Это до {str(tT.hour).zfill(2)}:{str(tT.minute).zfill(2)}. Осталось {str(deltaHours).zfill(2)}:{str(deltaMins).zfill(2)}")
    else:
        print("Работаем ", diffHours, "час(а/ов)")

#____________main___________

intro_banner()
menu_banner()

while True:
    menu_switch()