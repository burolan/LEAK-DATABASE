import requests
from os import system
from time import sleep
from colorama import Fore, Style
from bs4 import BeautifulSoup


while 1:
    try :   
        system("cls||clear")  
        print(Fore.LIGHTRED_EX+"██╗░░░░░███████╗░█████╗░██╗░░██╗  ██████╗░░█████╗░████████╗░█████╗░██████╗░░█████╗░░██████╗███████╗\n██║░░░░░██╔════╝██╔══██╗██║░██╔╝  ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝\n██║░░░░░█████╗░░███████║█████═╝░  ██║░░██║███████║░░░██║░░░███████║██████╦╝███████║╚█████╗░█████╗░░\n██║░░░░░██╔══╝░░██╔══██║██╔═██╗░  ██║░░██║██╔══██║░░░██║░░░██╔══██║██╔══██╗██╔══██║░╚═══██╗██╔══╝░░\n███████╗███████╗██║░░██║██║░╚██╗  ██████╔╝██║░░██║░░░██║░░░██║░░██║██████╦╝██║░░██║██████╔╝███████╗\n╚══════╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝  ╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═════╝░╚═════"+Fore.LIGHTRED_EX)
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
        print("\t")

        secim = int((input(Fore.RESET + " 1- Mail İle Sızıntı Arama\n 2- Boş\n 3- Boş\n 4- Çıkış\n\n" + Fore.RESET + " Seçim: ")))
        if secim==1:
                system("cls||clear")  
                print(Fore.LIGHTRED_EX+"██╗░░░░░███████╗░█████╗░██╗░░██╗  ██████╗░░█████╗░████████╗░█████╗░██████╗░░█████╗░░██████╗███████╗\n██║░░░░░██╔════╝██╔══██╗██║░██╔╝  ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝\n██║░░░░░█████╗░░███████║█████═╝░  ██║░░██║███████║░░░██║░░░███████║██████╦╝███████║╚█████╗░█████╗░░\n██║░░░░░██╔══╝░░██╔══██║██╔═██╗░  ██║░░██║██╔══██║░░░██║░░░██╔══██║██╔══██╗██╔══██║░╚═══██╗██╔══╝░░\n███████╗███████╗██║░░██║██║░╚██╗  ██████╔╝██║░░██║░░░██║░░░██║░░██║██████╦╝██║░░██║██████╔╝███████╗\n╚══════╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝  ╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═════╝░╚═════"+Fore.LIGHTRED_EX)
                print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
                print("\t")
                mail = str(input(Fore.RESET + "Mail'inizi giriniz :  "+ Fore.RESET))
                files = {
                'act': (None, mail),
                'accounthide': (None, 'test'),
                'submit': (None, ' go '),
                }
                if ("@" not in mail or ".com" not in mail) and mail != "":
                     system("cls||clear")
                     print("HATALI EMAİL")
                     sleep(2)
                     print("\t")
                     print("ANA MENUYE DONULUYOR...")
                     sleep(3)
                     continue
                else :
                    response = requests.post('https://www.hotsheet.com/inoitsu/', files=files)
                    sonuc = response.text
                    icerik = BeautifulSoup(response.content , "html.parser")
                    f = icerik.find(id="summary").get_text()
                    system("cls||clear")
                    print(Fore.LIGHTRED_EX+"██╗░░░░░███████╗░█████╗░██╗░░██╗  ██████╗░░█████╗░████████╗░█████╗░██████╗░░█████╗░░██████╗███████╗\n██║░░░░░██╔════╝██╔══██╗██║░██╔╝  ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝\n██║░░░░░█████╗░░███████║█████═╝░  ██║░░██║███████║░░░██║░░░███████║██████╦╝███████║╚█████╗░█████╗░░\n██║░░░░░██╔══╝░░██╔══██║██╔═██╗░  ██║░░██║██╔══██║░░░██║░░░██╔══██║██╔══██╗██╔══██║░╚═══██╗██╔══╝░░\n███████╗███████╗██║░░██║██║░╚██╗  ██████╔╝██║░░██║░░░██║░░░██║░░██║██████╦╝██║░░██║██████╔╝███████╗\n╚══════╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝  ╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═════╝░╚═════"+Fore.LIGHTRED_EX)
                    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
                    print("\t")
                    sleep(1)
                    print(mail+" "+"Sorgulanıyor.")
                    sleep(0.75)
                    print(mail+" "+"Sorgulanıyor..")
                    sleep(0.75)
                    print(mail+" "+"Sorgulanıyor...")
                    sleep(0.75)
                    print(mail+" "+"Sorgulanıyor....")
                    sleep(1.2)

                    system("cls||clear")
                    print(Fore.LIGHTRED_EX+"██╗░░░░░███████╗░█████╗░██╗░░██╗  ██████╗░░█████╗░████████╗░█████╗░██████╗░░█████╗░░██████╗███████╗\n██║░░░░░██╔════╝██╔══██╗██║░██╔╝  ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝\n██║░░░░░█████╗░░███████║█████═╝░  ██║░░██║███████║░░░██║░░░███████║██████╦╝███████║╚█████╗░█████╗░░\n██║░░░░░██╔══╝░░██╔══██║██╔═██╗░  ██║░░██║██╔══██║░░░██║░░░██╔══██║██╔══██╗██╔══██║░╚═══██╗██╔══╝░░\n███████╗███████╗██║░░██║██║░╚██╗  ██████╔╝██║░░██║░░░██║░░░██║░░██║██████╦╝██║░░██║██████╔╝███████╗\n╚══════╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝  ╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═════╝░╚═════"+Fore.LIGHTRED_EX)
                    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
                    print("\t")  
                    print(mail+" "+"için sonuçlar...")
                    print("\t")
                    if "Email addresses" in f:
                        print(Fore.RESET+"Kullanıcı adınız :  "+Fore.RED+"Paylaşılmış"+Fore.RED)
                        
                    else : print(Fore.GREEN+"Email adresiniz :  sızdırılmamış"+Fore.GREEN)
                    
                    if "Geographic locations" in f:
                           print(Fore.RESET+"Konum bilgileriniz  :  "+Fore.RED+"Paylaşılmış"+Fore.RED)
                        
                    else : print(Fore.GREEN+"konumunuz :  Paylaşılmamış"+Fore.GREEN)
                    
                    if "Passwords" in f:
                        print(Fore.RESET+"Şifreniz :  "+Fore.RED+"Sızdırılmış"+Fore.RED)
                    else : print(Fore.GREEN+"Şifreniz :  sızdırılmamış"+Fore.GREEN)
                    if "Usernames" in f:
                        print(Fore.RESET+"Kullanıcı adınız :  "+Fore.RED+"Sızdırılmış"+Fore.RED)
                    else : print(Fore.GREEN+"Kullanıcı adınız :  "+Fore.GREEN)
                    print("\t") 
        
                    print("\t")
                    if "Email addresses" in f:
                        g = (input(Fore.WHITE+"SIZINTIYLA ALAKALI DAHA FAZLA BİLGİ ALMAK İSTİYOR MUSUNUZ? Y/H :  "+Fore.WHITE))
                        if g == "Y" or g == "y":
                             system("cls||clear")
                             print(Fore.LIGHTRED_EX+"██╗░░░░░███████╗░█████╗░██╗░░██╗  ██████╗░░█████╗░████████╗░█████╗░██████╗░░█████╗░░██████╗███████╗\n██║░░░░░██╔════╝██╔══██╗██║░██╔╝  ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝\n██║░░░░░█████╗░░███████║█████═╝░  ██║░░██║███████║░░░██║░░░███████║██████╦╝███████║╚█████╗░█████╗░░\n██║░░░░░██╔══╝░░██╔══██║██╔═██╗░  ██║░░██║██╔══██║░░░██║░░░██╔══██║██╔══██╗██╔══██║░╚═══██╗██╔══╝░░\n███████╗███████╗██║░░██║██║░╚██╗  ██████╔╝██║░░██║░░░██║░░░██║░░██║██████╦╝██║░░██║██████╔╝███████╗\n╚══════╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝  ╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═════╝░╚═════"+Fore.LIGHTRED_EX)
                             print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
                             print("\t")
                             h = icerik.find(id="BreachDtl").get_text()
                             print(Fore.WHITE+h+Fore.WHITE)
                             print("\t")
                    else:pass         
                    cıkıs = input(Fore.WHITE+"ANA MENÜYE DÖNMEK İSTİYOR MUSUNUZ? Y/H :  "+Fore.WHITE)
                    if cıkıs=="Y" or cıkıs=="y":
                        continue
                    else : sleep(9999)
        elif secim==4:
             break            
                 
            
    except:
         system("cls||clear")
         print(Fore.LIGHTRED_EX+"██╗░░░░░███████╗░█████╗░██╗░░██╗  ██████╗░░█████╗░████████╗░█████╗░██████╗░░█████╗░░██████╗███████╗\n██║░░░░░██╔════╝██╔══██╗██║░██╔╝  ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝\n██║░░░░░█████╗░░███████║█████═╝░  ██║░░██║███████║░░░██║░░░███████║██████╦╝███████║╚█████╗░█████╗░░\n██║░░░░░██╔══╝░░██╔══██║██╔═██╗░  ██║░░██║██╔══██║░░░██║░░░██╔══██║██╔══██╗██╔══██║░╚═══██╗██╔══╝░░\n███████╗███████╗██║░░██║██║░╚██╗  ██████╔╝██║░░██║░░░██║░░░██║░░██║██████╦╝██║░░██║██████╔╝███████╗\n╚══════╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝  ╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═════╝░╚═════"+Fore.LIGHTRED_EX)
         print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
         print("\t")
         print(mail+" "+"Sorgulanıyor.")
         sleep(0.50)
         print(mail+" "+"Sorgulanıyor..")
         sleep(0.50)
         print(mail+" "+"Sorgulanıyor...")
         sleep(0.50)
         print(mail+" "+"Sorgulanıyor....")
         sleep(0.50)
         print(mail+" "+"Sorgulanıyor.....")
         sleep(0.50)
         system("cls||clear")
         print(Fore.LIGHTRED_EX+"██╗░░░░░███████╗░█████╗░██╗░░██╗  ██████╗░░█████╗░████████╗░█████╗░██████╗░░█████╗░░██████╗███████╗\n██║░░░░░██╔════╝██╔══██╗██║░██╔╝  ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝\n██║░░░░░█████╗░░███████║█████═╝░  ██║░░██║███████║░░░██║░░░███████║██████╦╝███████║╚█████╗░█████╗░░\n██║░░░░░██╔══╝░░██╔══██║██╔═██╗░  ██║░░██║██╔══██║░░░██║░░░██╔══██║██╔══██╗██╔══██║░╚═══██╗██╔══╝░░\n███████╗███████╗██║░░██║██║░╚██╗  ██████╔╝██║░░██║░░░██║░░░██║░░██║██████╦╝██║░░██║██████╔╝███████╗\n╚══════╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝  ╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═════╝░╚═════"+Fore.LIGHTRED_EX)
         print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
         print("\t")
         print(Fore.LIGHTGREEN_EX+"Email Adresiniz Sorgulandı Fakat Yeni Sızıntı Bulunamadı."+Fore.LIGHTGREEN_EX)
         sleep(3)
         print(Fore.WHITE+"ANA MENÜYE DÖNÜLÜYOR..."+Fore.WHITE)
         sleep(3)
         continue