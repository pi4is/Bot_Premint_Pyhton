import pyautogui
import time
import csv
from random import randint
import requests
from bs4 import BeautifulSoup
from colorama import init, Fore
from colorama import Back
import os
import glob
from threading import Thread
from datetime import datetime
from playsound import playsound
import keyboard

init(autoreset=True)

print(Fore.BLUE+Back.WHITE+"\n\n\n|-------------------------------------|")
print(Fore.BLUE+Back.WHITE+"|---------- Version bot 0.8 ----------|")
print(Fore.BLUE+Back.WHITE+"|----------- bot by @Pi4iS -----------|")
print(Fore.BLUE+Back.WHITE+"|-------------------------------------|\n\n\n")

try:
    playsound('1-BOT-IFIR-img//song.mp3', False)
except:
    print("Звук не может быть проигран")

##-Заметки: дописать паузу во время работы бота


tweets = [] ##база твитов
start_buttons_cords_x = []##координаты кнопки по x
start_buttons_cords_y = []##координаты кнопки по y
premint = ["https://www.premint.xyz/pepeapes/"] ##ссылка на преминт
email = ["sosi.clen.tolko.gorlom@mail.ru"]
account_true = 0##счет успешных аккаунтов
account_false = 0##счет ошибочных аккаунтов
error_logs = []##массив для логов ошибок
pause = False



def await_p_pause(e):
    global pause
    if e.name == '[' and e.event_type == "up":
        if pause == False:
            print("PAUSE")
            pause = True
            try:
                playsound('1-BOT-IFIR-img//pause_pause.wav', False)
            except:
                print("Звук не может быть проигран")
        else:
            print("\n\nSTART!\n\n")
            pause = False
            try:
                playsound('1-BOT-IFIR-img//start_pause.wav', False)
            except:
                print("Звук не может быть проигран")

def keyboard_pressed():
    print("scripc pause - start")
    keyboard.hook(await_p_pause)
    keyboard.wait()

thread_keyboard = Thread(target = keyboard_pressed)
thread_keyboard.start()

def kalibrity_buttons_dolphin(coords):##калибровка клавиш
    global start_buttons_cords_x, start_buttons_cords_y
    start_buttons_cords_x = []
    start_buttons_cords_y = []
    print(f"Запущена калибровка клавиш start относительно вашего дисплея, начало через 5 секунд")
    time.sleep(5)
    startButton = pyautogui.locateOnScreen('1-BOT-IFIR-img//start_btn.jpg', confidence = 0.7)
    ##print(startButton)
    ##1 число - вправо
    if startButton != None:
        for i in range(0,10):
            pyautogui.moveTo(startButton[0]+startButton[2]/2, startButton[1]+startButton[3]/2+2+coords*i)
            start_buttons_cords_x.append(startButton[0]+startButton[2]/2)
            start_buttons_cords_y.append(startButton[1]+startButton[3]/2+2+coords*i)
            time.sleep(0.5)
        user = input(f"{coords} - прошлое значение между кнопок; Если все прошло удачно, введите y, если нет - n: ")
        if user == "y":
            pass
        else:
            kalibrity_buttons_dolphin(int(input("Введите примерное расположение пикселей между кнопок")))
    else:
        print(Fore.RED+"кнопка START НЕ найдена")
    print("\n")
    
def sleep(browser):##ожидание открытия окна браузера
    awaiting = 0
    
    while awaiting <=  120:
        Button = pyautogui.locateOnScreen('1-BOT-IFIR-img//sleep.PNG', confidence = 0.7)
        if awaiting%45 == 0:
            move_and_click(start_buttons_cords_x[browser], start_buttons_cords_y[browser])
        if Button != None:
            break
        else:
            awaiting += 1
            time.sleep(1)

    if awaiting >= 115:
        return False


def premint_await():##ожидание страницы преминта
    awaiting = 0
    
    while awaiting <=  120:
        Button = pyautogui.locateOnScreen('1-BOT-IFIR-img//premint_await.PNG', confidence = 0.7)
        if Button != None:
            pyautogui.moveTo(Button, duration=randint(1.0,2.0))
            return True
        else:
            awaiting += 1
            time.sleep(1)

        if awaiting%15 == 0 and awaiting > 14:
            print("click F5")
            click_img("F5")
                

    if awaiting >= 115:
        return False

        
def start_profile(button):##старт нового профиля
    pyautogui.moveTo(start_buttons_cords_x[button], start_buttons_cords_y[button])


def move_and_click(x, y):##клик по x y
    pyautogui.moveTo(x, y, duration=randint(1.0,2.0))
    pyautogui.click()


def adress_chrome_click_and_press(url):##открытие новой страницы в браузере
    awaiting = 0

    while awaiting <= 60:
        Button = pyautogui.locateOnScreen('1-BOT-IFIR-img//plus_adress.PNG', confidence = 0.7)
        
        if Button == None:
            awaiting += 1
            time.sleep(1)
        else:
            pyautogui.moveTo(Button, duration=randint(1.0,2.0))
            time.sleep(1)
            pyautogui.click()
            time.sleep(0.5)
            pyautogui.typewrite(url)
            time.sleep(0.5)
            pyautogui.keyDown("Enter")
            break
        

def check_email():##проверка мыла и его ввод
    awaiting = 0
    
    while awaiting <= 5:
        Button = pyautogui.locateOnScreen('1-BOT-IFIR-img//email.PNG', confidence = 0.7)
        
        if Button == None:
            awaiting += 1
            time.sleep(1)
        else:
            pyautogui.moveTo(Button, duration=randint(1.0,2.0))
            pyautogui.PAUSE = 0.5
            pyautogui.click()
            pyautogui.PAUSE = 0.5
            pyautogui.typewrite(email[0])
            break


def follow_twiter_premint():##нажатие на фоллов твитер в странице преминта
    awaiting = 0
    
    while awaiting <= 20:
        Button = pyautogui.locateOnScreen('1-BOT-IFIR-img//follow.PNG', confidence = 0.7)
        
        if Button == None:
                awaiting += 1
                time.sleep(1)
        else:
            pyautogui.moveTo(Button[0]+Button[2]+40, Button[1]+Button[3]/2, duration=randint(1.0,2.0))
            pyautogui.PAUSE = 0.5
            pyautogui.click()
            print("follow twitter click")
            break
    
    if awaiting >= 20:
        return False

    awaiting = 0
    
    while awaiting <= 120:
        Button = pyautogui.locateOnScreen('1-BOT-IFIR-img//follow_twitter.PNG', confidence = 0.5)

        if Button == None:
                awaiting += 1
                time.sleep(1)
        else:
            pyautogui.moveTo(Button, duration=randint(1.0,2.0))
            pyautogui.PAUSE = 0.5
            pyautogui.click()
            print("follow twitter")
            break

        if awaiting%15 == 0 and awaiting > 14:
            print("click F5")
            click_img("F5")
        
    if awaiting >= 115:
        return False

    if tweet == True:
        tweeting()
        
def twitter_awaiting_giv():
    awaiting = 0
    
    while awaiting <=  120:
        Button = pyautogui.locateOnScreen('1-BOT-IFIR-img//Tweet.PNG', confidence = 0.7)
        if Button != None:
            pyautogui.moveTo(Button, duration=randint(1.0,2.0))
            return True
        else:
            awaiting += 1
            time.sleep(1)

        if awaiting%15 == 0 and awaiting > 14:
            print("click F5")
            click_img("F5")

    if awaiting > 115:
        return False

def check_follow_account():
    awaiting = 0
    
    while awaiting <=  3:
        Button = pyautogui.locateOnScreen('1-BOT-IFIR-img//following_check.PNG', confidence = 0.7)
        if Button != None:
            pyautogui.moveTo(Button, duration=randint(1.0,2.0))
            return True
        else:
            awaiting += 1
            time.sleep(1)

    if awaiting > 3:
        return False

    
def tweeting(): #подписка на твитер + создание твита
    if len(tweets) <= 0:
        print(Fore.RED+"Твиты из базы закончились!")
        return
    
    click_img("Tweet")
    
    for i in range(30):
        pyautogui.keyDown('BackSpace')

    random_twit = randint(0,len(tweets))
    pyautogui.typewrite(tweets[random_twit])
    tweets.pop(random_twit)
    time.sleep(2)
    
    if click_img("Tweet2") != False:
        print("Создание твита - успешно")

    
def click_to_register():##клик то регистер на странице преминта
    awaiting = 0
    
    while awaiting <= 10:
        Button = pyautogui.locateOnScreen('1-BOT-IFIR-img//register.PNG', confidence = 0.7)
        
        if Button == None:
                awaiting += 1
                time.sleep(1)
                pyautogui.scroll(-50)
        else:
            pyautogui.moveTo(Button, duration=randint(1.0,2.0))
            pyautogui.PAUSE = 0.5
            pyautogui.click()
            print(Fore.YELLOW+"Click to register - Успешно")
            time.sleep(6)
            break
        
    if awaiting >= 10:
        return False


def close_browser():##закрытие браузера
    click_img("close_browser")

        
def close_adress(adress = 3):##закрытие трех вкладок на браузере
    awaiting = 0
    for i in range(adress):
        pyautogui.hotkey('ctrl', 'w')
        time.sleep(0.5)


def connect_twitter():##подключаем твитер

    if click_img("Connect") == False:
        return
    if click_img("Connect2", 10) == False:
        return False

    
def Connect_Wallet(state = 0, password = 0):##подключаем кошель
    if state != 0:
        print("recurcu")
        
    if click_img("Connect_meta", 6) == False:
        return
        
    if state == 0:
        if click_img("Connect_meta2", 12) == False:
            return False

        if click_img("Connect_meta3", 12) == False:
            return False

    if state == 0:
        time.sleep(5)
        print(meta_pass[password])
        pyautogui.typewrite(meta_pass[password])

        if click_img("Connect_meta5", 12) == False:
            return False
        else:
            print("Ввел пасс от метамаска")
            
    click_img("Connect_meta61", 7)
        
    if click_img("Connect_meta62", 7) == False:
        return


    if click_img("Connect_meta6") == False:
        return False

def like_and_retweet(url, like = "n", retweet = "n"):
    adress_chrome_click_and_press(url)
    if twitter_awaiting_giv() == False:
        return False

    if like == "y":
        if click_img("love", 15, True) == False:##клик по love
            return False
        
    if retweet == "y":           
        if click_img("retwit", True) == False:#клик по кнопке ретвит
            return False
        if click_img("retwit_2") == False:##клик по кнопке ретвит - final
            return False      
    

    
##-------------------Работа с логами-------------------##
def remove_logs_bot():
    print(Fore.RED+"Отчистка логов\n\n")
    files = glob.glob('errors_bot_log/*')
    for f in files:
        os.remove(f)

def create_log(name):
    global error_logs
    open_and_write(name+"\n")
    screen = pyautogui.screenshot('errors_bot_log//'+name+'.png')
    error_logs.append(name)

##-------------------Работа с долфином-------------------##
def click_img(image, await_max = 5, scroll = False):
    awaiting = 0
    
    while awaiting <= await_max:
        Button = pyautogui.locateOnScreen('1-BOT-IFIR-img//'+image+".PNG", confidence = 0.85)
        
        if Button == None:
            awaiting += 1
            if scroll == True:
                pyautogui.scroll(-70)
            time.sleep(1)
        else:
            pyautogui.moveTo(Button, duration=randint(1.0,2.0))
            time.sleep(0.5)
            pyautogui.click()
            break
        
    if awaiting >= await_max:
        print(f"Не найдена кнопка: '{image}'")
        return False

    
def await_dolph():##ожидание открытия нового долфина
    awaiting = 0
    
    while awaiting !=  240:
        Button = pyautogui.locateOnScreen('1-BOT-IFIR-img//await_D.PNG', confidence = 0.7)

        if Button != None:
            break
        else:
            time.sleep(0.5)

    if awaiting >= 240:
        return False
    
    
def dolphin_open(number):##открытие нового долфина
    print(Fore.GREEN+f"|- Dolphin {dolphin_email[number]} - СТАРТ -|\n")
    open_and_write(f"|---------- Dolphin {dolphin_email[number]} - СТАРТ ----------|\n")
    
    if click_img("Exit_D") == False:
        return False
    
    if click_img("YES") == False:
        return False
    
    if click_img("email_D") == False:
        return False
    
    time.sleep(1)
    pyautogui.typewrite(dolphin_email[number])
    
    if click_img("Pass_D") == False:
        return False
    
    time.sleep(1)
    pyautogui.typewrite(dolphin_pass[number])
    if click_img("auto_D") == False:
        return False
    
    if await_dolph() == False:
        return False
    
    time.sleep(2)
    return True


##-------------------Работа с таблицей-------------------##
    
dolphin_email = []
dolphin_pass = []
meta_pass = []
twitter_tag = []

def tabel():
    twit_tag = 0
    global dolphin_email, dolphin_pass, meta_pass, twitter_tag
    
    print(Back.CYAN+"-------------------------------------------------------------------")
    print(Back.CYAN+"№ |    EMAIL DOLPHIN      | PASS DOLPHIN  |       PASS META       |")
    with open("premint.csv", encoding='utf-8', newline = '') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")
        i = 0
        for row in reader:
            if row["почта долфин / №долфин"] == "":
                pass
            elif row["почта долфин / №долфин"] == "почта долфин / №долфин":
                pass
            else:
                print(i, "|", row["почта долфин / №долфин"], "|", row["пасс долфин"], "|", row["метамаск пасс"], "|")
                dolphin_email.append(row["почта долфин / №долфин"])
                dolphin_pass.append(row["пасс долфин"])
                meta_pass.append(row["метамаск пасс"])
                i += 1
            if row["твиттер данные"] == "":
                pass
            elif row["твиттер данные"] == "Дискорд логин/пароль":
                twit_tag += 1
            elif twit_tag == 0:
                if row["твиттер данные"].split(":")[0] == "https":
                    pass
                else:
                    twitter_tag.append(row["твиттер данные"].split(":")[0])
                
    print(Back.CYAN+"№ |    EMAIL DOLPHIN      | PASS DOLPHIN  |       PASS META       |")
    print(Back.CYAN+"-------------------------------------------------------------------")
    print("Теги твитеров:",twitter_tag)
    print("\n")
    
    user_min = int(input("С какого аккаунта начать: "))
    user_max = int(input("Каким аккаунтом закончить: "))+1

    print("\n\n")
    return user_min, user_max


##-------------------Работа с логами и тхт-------------------##

def open_and_write(text):
    f = open('logs_bot.txt', "a")
    f.write(text)
    f.close()


##-------------------Работа с базой твитов-------------------##
def upload_base_twits():
    global tweets
    numbers = 0
    print("Начало проверки подключения к базе новостей")
    try: 
        url = 'https://cryptonews.net/'
        page = requests.get(url)
        if page.status_code == 200:
            print(Fore.GREEN+f"База новостей доступна - {url}\n")
    except:
        print(Fore.RED+f"Ошибка с подключением к базе новостей: {url}\n\n")
        return
    
    user = input("Вы хотите получить базу новостей, для использования их в твитах?\nВведите 'y' - если да: ")
    if user == "y":
        minimal = int(input("С какой страницы новостей начать? (от 1): "))
        maximal = int(input("Какой страницей новостей закончить? (до 7882): "))
        print(Fore.GREEN+"Начало парсинга")
        
        threads = []
        for i in range(minimal, maximal):
            url = 'https://cryptonews.net/?page='+str(i)

            process = Thread(target=requests_url, args=[url])
            process.start()
            threads.append(process)
            
        for process in threads:
            process.join()    

        print(Fore.GREEN+"База успешно обновлена\n")
    
        user = input("Вы хотите увидить базу твитов? 'y' - да: ")
        if user == "y":
            for i in range(0, len(tweets)):
                print(tweets[i])
        print("\n\n")
        
def requests_url(url):
    global tweets
    
    try:
        page = requests.get(url)
                
        soup = BeautifulSoup(page.text, "html.parser")
        allNews = soup.findAll('a', class_='title')

        for data in allNews:
            tweets.append(data.text)
        
        print(Fore.GREEN+f"Прасинг - {url} - УСПЕШНО")
    except:
        print(Fore.RED+f"Прасинг - {url} - ОШИБКА")
    
    
##-------------------Работа с функциями - сам бот-------------------##


##like_and_retweet("https://www.premint.xyz/rage/", "y", "n")

time_start = datetime.now().time()

open_and_write(f"\n| ---------- log - {time_start} - Start ---------- |\n\n")

    
 
remove_logs_bot()##Отчистка логов
upload_base_twits()##обновление базы твитов
user_min, user_max = tabel() ##Загрузка с таблицы и получам откуда начать, где закончить
kalibrity_buttons_dolphin(47) ##Калибровка кнопок        

tweet = input("Введите 'y' - если нужны рандомные твиты из базы: ")

bot_stabel = int(input("Введите принцип работы: \n1.Преминт\n2.Гивы\nВаш выбор: "))

if bot_stabel == 1:
    minimal = int(input("Введите каким профелем начинать: "))-1
    maximal = int(input("Введите каким профелем заканчивать: "))
    premint = input("Введите ссылку/ссылки на преминт: ").split(" ")
    email[0] = input("Введите мыло на преминт, там где, оно нужно будет, если не надо введите 'n': ")
    twitter_follow_url = input("Введите ссылку/сылки на аккаунты (подписка на них), если он один - 'n', будет авто поиск: ").split(" ")
    twitter_url = input("Введите ссылку на  пост, который нужно лайкнуть/ретвитнуть, если не надо введите 'n': ")
    if twitter_url != 'n':
        love_button = input("Вам нужен лайк на этот пост, если да - 'y': ")
        retw_button = input("Вам нужен ретвит на этот пост, если да - 'y': ")

    if tweet == "y":
        tweet = True
    print("\n\n")

    try:
        for dolphins in range(user_min, user_max):##бегаем по аккаунтам долфина
            if dolphin_open(dolphins) == False:##Открытие страницы долфина
                print(Fore.RED+"|---------- Ошибка со в ходом в DOLPHIN, ПЕРЕЗАПУСТИТЕ СКРИПТ ----------|")
                break
                
            for browser in range(minimal, maximal):
                while pause == True:
                    pass
                print(Fore.GREEN+f"|---------- Аккаунт {browser+1} - СТАРТ ----------|")
                open_and_write(f"Аккаунт {browser+1} - СТАРТ\n")
                
                move_and_click(start_buttons_cords_x[browser], start_buttons_cords_y[browser]) ##открытие страницы долфина нового
                
                if sleep(browser) == False:##ожидание открытия окна
                    print(Fore.RED+f"Аккаунт {browser+1} - ПРЕВЫШЕНО время ожидания на ОТКРЫТИЕ браузера (2 минуты)!\n")
                    account_false += 1
                    break

                
                for urls in range(0, len(premint)):
                    print(Fore.YELLOW+f"PREMINT: {premint[urls]}")
                    
                    adress_chrome_click_and_press(premint[urls])##открытие вкладки
                    
                    if premint_await() == False:##ожидание открытия страницы преминта
                        print(Fore.RED+f"Аккаунт {browser+1} выдал ошибку - превышено время ожидания преминта!\n")
                        account_false += 1
                        create_log(str(dolphin_email[dolphins])+"-"+str(browser+1)+"_premint")
                        close_adress(1)
                        continue
                        
                    if Connect_Wallet(0, dolphins) == False:##коннект метамаска на преминт
                        print(Fore.RED+f"Аккаунт {browser+1} выдал ошибку по метамаску!\n")
                        account_false += 1
                        create_log(str(dolphin_email[dolphins])+"-"+str(browser+1)+"_metamask")
                        close_adress(1)
                        continue
                    
                    if connect_twitter() == False:##привязка твитера на преминт
                        print(Fore.RED+f"Аккаунт {browser+1} выдал ошибку по привязке твиттера!\n")
                        account_false += 1
                        create_log(str(dolphin_email[dolphins])+"-"+str(browser+1)+"_twitter_connect")
                        close_adress(1)
                        continue

                    
                    if twitter_follow_url[0] == "n":
                        if follow_twiter_premint() == False:##твитера - подписка на странице преминта
                            print(Fore.RED+f"Аккаунт {browser+1} выдал ошибку по подписке на твитер!\n")
                            account_false += 1
                            create_log(str(dolphin_email[dolphins])+"-"+str(browser+1)+"_twitter_follow")
                            close_adress(1)
                            continue
                    else:
                        true_follow = 0
                        false_follow = 0
                        for i in range(len(twitter_follow_url)):
                            print("follow on account twitter")
                            adress_chrome_click_and_press(twitter_follow_url[i]+"  ")
                            
                            if twitter_awaiting_giv() == False:##ждем когда откроется твиттер
                                false_follow += 1
                                create_log(str(dolphin_email[dolphins])+"-"+str(browser+1)+"_follow")
                                print(Fore.RED+f"Аккаунт {browser+1} выдал ошибку - по подписке на аккаунты!\n")
                                time.sleep(1)
                                continue
                            
                            if check_follow_account() == False:
                                if click_img("follow_twitter") == False:
                                    false_follow += 1
                                    create_log(str(dolphin_email[dolphins])+"-"+str(browser+1)+"_follow")
                                    print(Fore.RED+f"Аккаунт {browser+1} выдал ошибку - по подписке на аккаунты!\n")
                                    time.sleep(1)
                                    continue
                                else:
                                    true_follow += 1
                            else:
                                true_follow += 1
                        
                        if false_follow > 0:
                            print(Fore.RED+f"Аккаунт {browser+1} выдал ошибку по подпискам на аккаунты\n")
                            account_false += 1
                            create_log(str(dolphin_email[dolphins])+"-"+str(browser+1)+"_twitter_like_or_retw")
                            close_adress(false_follow)
                            continue
                        else:
                            time.sleep(3)
                            close_adress(len(twitter_follow_url))##закрытие открытых вкладок
                        

                    if twitter_url != "n":
                        if like_and_retweet(twitter_url, love_button, retw_button) == False:
                            print(Fore.RED+f"Аккаунт {browser+1} выдал ошибку по лайку/ретвиту!\n")
                            account_false += 1
                            create_log(str(dolphin_email[dolphins])+"-"+str(browser+1)+"_twitter_like_or_retw")
                            close_adress(1)
                            continue
                        else:
                            time.sleep(2)
                            close_adress(1)
   
                    adress_chrome_click_and_press(premint[urls])##открытие вкладки

                    if premint_await() == False:##ожидание открытия страницы преминта
                        print(Fore.RED+f"Аккаунт {browser+1} выдал ошибку - превышено время ожидания преминта!\n")
                        account_false += 1
                        create_log(str(dolphin_email[dolphins])+"-"+str(browser+1)+"_premint")
                        continue
                    
                    if email[0] != "n":
                        check_email()##проверка мыла
                    
                    if click_to_register() == False:##клик по кнопке регистрации - конец
                        print(Fore.RED+f"Аккаунт {browser+1} выдал ошибку - не смог найти кнопку регистора на преминт!\n")
                        account_false += 1
                        create_log(str(dolphin_email[dolphins])+"-"+str(browser+1)+"_register")
                        continue

                    open_and_write(f"PREMINT: {premint[urls]} - УСПЕШНО\n")
                    account_true += 1
                    close_adress(2)##закрытие открытых вкладок
                    
                close_browser()##закрытие браузера
                
                open_and_write(f"Аккаунт {browser+1} - ЗАВЕРШЕНО\n")
                print(Fore.GREEN+f"|---------- Аккаунт {browser+1} - ЗАВЕРШЕНО ----------|\n")

            open_and_write(f"|- Dolphin {dolphin_email[dolphins]} - КОНЕЦ -|\n\n")    
            print(Fore.GREEN+f"\n|---------- Dolphin {dolphin_email[dolphins]} - КОНЕЦ ----------|\n\n")   
    except Exception as err:
        try:
            playsound('1-BOT-IFIR-img//dead.mp3')
        except:
            pass
        print(Back.CYAN+Fore.RED+"Ошибка: "+err)


elif bot_stabel == 2:
    minimal = int(input("Введите каким профелем начинать: "))-1
    maximal = int(input("Введите каким профелем заканчивать: "))
    tweet_url = input("Введите ссылку на сам ГИВ: ")
    acc_follow = input("Введите ссылку/ссылки на аккаунты, на которые надо подписаться, 'n' - если не надо: ").split(" ")
    fraze_tag = input("Введите фразу, которую надо вводить в теге друзей в начале, 'n' - если не надо: ")
    teg_people = int(input("Введите кол-во людей, которых надо тегнуть (0 - если не надо): "))
    notify = input("Надо ли нажимать на колокол, когда подписаллся на аккаунт, 'n' - если не надо: ")

    if notify == "y":
        notify = True
        
    if tweet == "y":
        tweet = True
    print("\n\n")

    try:
        for dolphins in range(user_min, user_max):##бегаем по аккаунтам долфина
            if dolphin_open(dolphins) == False:##Открытие страницы долфина
                print(Fore.RED+"|---------- Ошибка со в ходом в DOLPHIN, ПЕРЕЗАПУСТИТЕ СКРИПТ ----------|")
                break
                
            for browser in range(minimal, maximal):
                while pause == True:
                    pass
                print(Fore.GREEN+f"|---------- Аккаунт {browser+1} - СТАРТ ----------|")
                open_and_write(f"Аккаунт {browser+1} - СТАРТ\n")
                
                move_and_click(start_buttons_cords_x[browser], start_buttons_cords_y[browser]) ##открытие страницы долфина нового
                
                if sleep(browser) == False:##ожидание открытия окна
                    print(Fore.RED+f"Аккаунт {browser+1} - ПРЕВЫШЕНО время ожидания на ОТКРЫТИЕ браузера (2 минуты)!\n")
                    account_false += 1
                    break
                    
                
                if like_and_retweet(tweet_url, 'y', 'y') == False:##открытие вкладки гива + лайк и ретвит
                    account_false += 1
                    create_log(str(dolphin_email[dolphins])+"-"+str(browser+1)+"_love")
                    close_adress(1)##закрытие открытых вкладок
                    close_browser()##закрываем браузер 
                    print(Fore.RED+f"Аккаунт {browser+1} выдал ошибку - нажатие кнокпи Love!\n")
                    continue
                    
                

                if teg_people != 0:##тегаем друзей - 2 этап
                    click_img("replay", True)##тегаем друзей - 1 этап
                    
                    time.sleep(3)
                    if fraze_tag != "n":
                        pyautogui.typewrite(fraze_tag)
                        
                    for i in range(teg_people):
                        time.sleep(3)
                        random_twit = randint(0,len(twitter_tag)-1)
                        if twitter_tag[random_twit][0] == "@":
                            pyautogui.typewrite(twitter_tag[random_twit]+" ")
                        else:
                            pyautogui.typewrite("@"+twitter_tag[random_twit]+" ")
                            
                    if click_img("replay_giv") == False:
                        account_false += 1
                        create_log(str(dolphin_email[dolphins])+"-"+str(browser+1)+"_friends")
                        close_adress(1)##закрытие открытых вкладок
                        close_browser()##закрываем браузер 
                        print(Fore.RED+f"Аккаунт {browser+1} выдал ошибку - по тегам друзей!\n")
                        continue
                            
                        time.sleep(5)

                if tweet == True:
                    tweeting()

                if acc_follow[0] != "n":
                    true_follow = 0
                    false_follow = 0
                    for i in range(len(acc_follow)):##подписываемся на аккаунты
                        print("follow on account twitter")
                        adress_chrome_click_and_press(acc_follow[i]+"  ")
                        
                        if twitter_awaiting_giv() == False:##ждем когда откроется твиттер
                            false_follow += 1
                            create_log(str(dolphin_email[dolphins])+"-"+str(browser+1)+"_follow")
                            print(Fore.RED+f"Аккаунт {browser+1} выдал ошибку - по подписке на аккаунты!\n")
                            continue

                        if check_follow_account() == False:
                            if click_img("follow_twitter") == False:
                                false_follow += 1
                                create_log(str(dolphin_email[dolphins])+"-"+str(browser+1)+"_follow")
                                print(Fore.RED+f"Аккаунт {browser+1} выдал ошибку - по подписке на аккаунты!\n")
                                continue
                            
                            if notify == True:
                                if click_img("notify") == False:
                                    false_follow += 1
                                    create_log(str(dolphin_email[dolphins])+"-"+str(browser+1)+"_follow")
                                    print(Fore.RED+f"Аккаунт {browser+1} выдал ошибку - по подписке на аккаунты!\n")
                                    continue
                            true_follow += 1
                        else:
                            true_follow += 1
                            
                if false_follow > 0:
                    account_false += 1
                    close_adress(true_follow+1)
                    time.sleep(2)
                    close_browser()##закрытие браузера
                else:
                    account_true += 1
                    time.sleep(2)
                    close_adress(true_follow+1)##закрытие открытых вкладок
                    time.sleep(2)
                    close_browser()##закрытие браузера
                
                
                open_and_write(f"Аккаунт {browser+1} - ЗАВЕРШЕНО\n")
                print(Fore.GREEN+f"|---------- Аккаунт {browser+1} - ЗАВЕРШЕНО ----------|\n")

            open_and_write(f"|- Dolphin {dolphin_email[dolphins]} - КОНЕЦ -|\n\n")    
            print(Fore.GREEN+f"\n|---------- Dolphin {dolphin_email[dolphins]} - КОНЕЦ ----------|\n\n")
        
    except Exception as err:
        print(Back.CYAN+Fore.RED+"Ошибка"+err)

   
print(Fore.GREEN+"\n\n|---------- РАБота - ОКОНЧЕННА, УРА УРА УРА ----------|\n\n")

print(Fore.GREEN+"Дозаписываю логи в тхт\n")

time_end = datetime.now().time()
open_and_write(f"Успешно заполненно аккаунтов : {account_true}\nОшибки заполнения premint: {account_false}\n")
open_and_write(f"| ---------- log - {time_end} - END ---------- |\n\n")


print(Fore.GREEN+f"Успешно заполненно ссылок premint: {account_true}")
print(Fore.RED+f"Ошибки заполнения premint: {account_false}\n")

for i in range(0, len(error_logs)):
    print(error_logs[i])

try:
    playsound('1-BOT-IFIR-img//dead.mp3', False)
except:
    print("Звук не может быть проигран")

    
input("\nНажмите 'Enter' чтоб завершить работу ")
