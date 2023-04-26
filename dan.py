import json
import urllib.request
import webbrowser
import os


R = '\033[91m'
Y = '\033[93m'
G = '\033[92m'
CY = '\033[96m'
W = '\033[97m'
path = os.path.isfile('/data/data/com.termux/files/usr/bin/bash')








def vic():
    os.system('clear')
    print( Y + '''
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░██████░░███░░░░███░░████████░░░░
░░░██░░░██░████░░████░░░░░██░░░░░░░
░░░██░░░██░██░████░██░░░░░██░░░░░░░
░░░██████░░██░░██░░██░░░░░██░░░░░░░
░░░██░░░░░░██░░░░░░██░░░░░██░░░░░░░
░░░██░░░░░░██░░░░░░██░░░░░██░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                               v0.1 ''' + R )

vic()


def menu():
    print("""
[1]  Информация по ip
[2]  Генерация ссылки iploger
[00] Выйти    
    """)
menu()

def main2():
    print('''
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░███░░░█████░░░█████░░███░░░░░██░░░░░
░░░░░░█░░░█░██░░░██░██░░░██░████░░░░██░░░░░
░░░░░░█░░░░░█░░░░░█░█░░░░░█░██░██░░░██░░░░░
░░░░░░░███░░█░░░░░█░█░░░░░█░██░░██░░██░░░░░
░░░░░░░░░░█░█░░░░░█░█░░░░░█░██░░░██░██░░░░░
░░░░░░█░░░█░██░░░██░██░░░██░██░░░░████░░░░░
░░░░░░░███░░░█████░░░█████░░██░░░░░███░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

[1] выйти

''')


def menu3():
    ch2 = int(input("выберете катерегорию: "))
    if ch2 == 1:
        vic()
        menu()
        menu2()
def menu2():

    ch = int(input("выберете катерегорию: "))

    if ch == 1:
        main1()
    elif ch == 2:
        main2()
    elif ch == 00:
        os.system('exit')
        os.system('exit')

    else:
        print('Неизвестная команда попробуйте еше раз')
        vic()
        menu()
        menu2()









def main1():
    import json
    import urllib.request
    import webbrowser
    import os
    try:
        R = '\033[91m'
        Y = '\033[93m'
        G = '\033[92m'
        CY = '\033[96m'
        W = '\033[97m'
        path = os.path.isfile('/data/data/com.termux/files/usr/bin/bash')

        def start():
            os.system('clear')
            print(CY + """
     _ ______ _       _                 
    | (_____ (_)     | |                
    | |_____) )  ____| |  _ _____  ____ 
    | |  ____/ |/ ___) |_/ ) ___ |/ ___)
    | | |    | ( (___|  _ (| ____| |    
    |_|_|    |_|\____)_| \_)_____)_|   """ + Y + """v1.0""" + G + """


    """)

        def m3():
            try:
                print(R + """\n
    #""" + Y + """ выберете раздел""" + G + """ >>""" + Y + """

    1)""" + G + """информация об вашем IP""" + Y + """
    2)""" + G + """узнать информацию о чужом IP""" + Y + """
    3)""" + G + """ вернутся в меню
    """)
                ch = int(input(CY + "Ващ выбор: " + W))
                if ch == 1:
                    main2()
                    m3()
                elif ch == 2:
                    main()
                    m3()
                elif ch == 3:
                    print("Выход................")
                    vic()
                    menu()
                    menu2()

                else:
                    print(R + "\nНеизвестная команда\n")
                    vic()
                    menu()
            except ValueError:
                print(R + "\nНеизвестная команда поробуйде еще раз \n")
                vic()
                menu()
                menu2()
        def finder(u):
            try:
                try:
                    response = urllib.request.urlopen(u)
                    data = json.load(response)

                    print(R + "\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                    print(Y + '\n>>>' + CY + ' детали IP\n ')
                    print(G + "1) IP адрес : " + Y, data['query'], '\n')
                    print(G + "2) Провайдер : " + Y, data['org'], '\n')
                    print(G + "3) Город : " + Y, data['city'], '\n')
                    print(G + "4) Регион : " + Y, data['regionName'], '\n')
                    print(G + "5) Страна : " + Y, data['country'], '\n')
                    print(G + "6) Локация\n")
                    print(G + "\tДолгота : " + Y, data['lat'], '\n')
                    print(G + "\tШирина : " + Y, data['lon'], '\n')
                    l = 'https://www.google.com/maps/place/' + str(data['lat']) + '+' + str(data['lon'])
                    print(R + "\n#" + Y + "ссылка на Google : " + CY, l)
                    path = os.path.isfile('/data/data/com.termux/files/usr/bin/bash')
                    if path:
                        link = 'am start -a android.intent.action.VIEW -d ' + str(l)
                        pr = input(R + "\n>>" + Y + " Открыть ссылку в вашем браузере?" + G + " (y|n): " + W)
                        if pr == "y":
                            lnk = str(link) + " > /dev/null"
                            os.system(str(lnk))
                            start()
                            m3()
                        elif pr == "n":
                            print("\nCheck another IP or exit using Ctrl + C\n\n")
                            start()
                            m3()
                        else:
                            print("\nInvalid choice! Please try again\n")
                            m3()
                    else:
                        pr = input(R + "\n>>" + Y + " Открыть ссылку в вашем браузере?" + G + " (y|n): " + W)
                        if pr == "y":
                            webbrowser.open(l, new=0)
                            start()
                            m3()
                        elif pr == "n":
                            print(R + "\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                            print(Y + "\nCheck another IP or exit using " + R + "Ctrl + C\n\n")
                            start()
                            m3()
                        else:
                            print(R + "\nInvalid choice! Please try again\n")
                            m3()
                    return
                except KeyError:
                    print(R + "\nError! Неверный IP/вебсайт Адрес!\n" + W)
                    m3()
            except urllib.error.URLError:
                print(R + "\nError!" + Y + " Пожалуйста проверте свое интернет сединение!\n" + W)
                exit()

        def main():
            u = input(G + "\n>>> " + Y + "Введите IP Адрес/вебсайт Адрес:" + W + " ")
            if u == "":
                print(R + "\nEnter valid IP Address/website address!")
                main()
            else:
                url = 'http://ip-api.com/json/' + u
                finder(url)

        def main2():
            url = 'http://ip-api.com/json/'
            finder(url)

        start()
        m3()
    except KeyboardInterrupt:
        print(Y + "\Хорошего дня :)" + W)

menu2()

def main2():
    print('''
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░███░░░█████░░░█████░░███░░░░░██░░░░░
░░░░░░█░░░█░██░░░██░██░░░██░████░░░░██░░░░░
░░░░░░█░░░░░█░░░░░█░█░░░░░█░██░██░░░██░░░░░
░░░░░░░███░░█░░░░░█░█░░░░░█░██░░██░░██░░░░░
░░░░░░░░░░█░█░░░░░█░█░░░░░█░██░░░██░██░░░░░
░░░░░░█░░░█░██░░░██░██░░░██░██░░░░████░░░░░
░░░░░░░███░░░█████░░░█████░░██░░░░░███░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
''')



menu3()



