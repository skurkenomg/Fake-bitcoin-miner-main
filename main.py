import os,string;from pystyle import *;from time import sleep;from random import choice, randint
import time
import sys
from colorama import Fore
from colorama import Style
    
os.system("color D")    
    
sys.stdout.write('\r Loading |   ')
time.sleep(0.1)
sys.stdout.write('\r Loading /   ')
time.sleep(0.1)
sys.stdout.write('\r Loading -   ')
time.sleep(0.1)
sys.stdout.write('\r Loading \\   ')
time.sleep(0.1)
sys.stdout.write('\r Loading |   ')
time.sleep(0.1)
sys.stdout.write('\r Loading /   ')
time.sleep(0.1)
sys.stdout.write('\r Loading -   ')
time.sleep(0.1)
sys.stdout.write('\r Loading \\   ')
time.sleep(0.1)
sys.stdout.write('\r Loading -   ')
time.sleep(0.1)
sys.stdout.write('\r Loading \\   ')
time.sleep(0.1)
sys.stdout.write('\r Loading -   ')
time.sleep(0.1)
sys.stdout.write('\r Loading \\   ')
time.sleep(0.1)
os.system("cls")

os.system("color D")
print("""
███████╗ █████╗ ██╗  ██╗███████╗    ██████╗ ████████╗ ██████╗    ███╗   ███╗██╗███╗   ██╗███████╗██████╗ 
██╔════╝██╔══██╗██║ ██╔╝██╔════╝    ██╔══██╗╚══██╔══╝██╔════╝    ████╗ ████║██║████╗  ██║██╔════╝██╔══██╗
█████╗  ███████║█████╔╝ █████╗      ██████╔╝   ██║   ██║         ██╔████╔██║██║██╔██╗ ██║█████╗  ██████╔╝
██╔══╝  ██╔══██║██╔═██╗ ██╔══╝      ██╔══██╗   ██║   ██║         ██║╚██╔╝██║██║██║╚██╗██║██╔══╝  ██╔══██╗
██║     ██║  ██║██║  ██╗███████╗    ██████╔╝   ██║   ╚██████╗    ██║ ╚═╝ ██║██║██║ ╚████║███████╗██║  ██║
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝    ╚═════╝    ╚═╝    ╚═════╝    ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝                                                                                                                                                                                                                                                                                                             
""")



os.system("title " + "Fake BTC Miner")
class Code:
   def __init__(self):
      print(f"{Col.light_green}")
      print(f"\t\t\t {Col.white} {Col.light_green}")
      try:





         c = int(input(f"""
{Col.white}[{Col.dark_red}1{Col.white}]{Col.pink} BTC
{Col.white}> """))
      except:os.system('cls');self.__init__()
      if c == 1:
            self.btc()
      else:os.system('cls');self.__init__()
   def btc(self):
      while True:
         btc = input(f"\n{Col.white}[{Col.light_red}+{Col.white}]{Col.light_red} Enter Your BTC Wallet Address {Col.white}>> ")
         if btc.startswith("3") or btc.startswith("bc1") or btc.startswith("1"):print(f"\n{Col.white}[{Col.green}+{Col.white}]{Col.green} Checking Address...");sleep(2);break
         elif btc.startswith("3") or btc.startswith("bc1") or btc.startswith("1"):print(f"\n{Col.white}[{Col.green}+{Col.white}]{Col.green} Valid Address | Starting Process..");sleep(2)
         else:print(f"{Col.white}[{Col.red}+{Col.white}]{Col.red} Invalid BTC Address");sleep(2)
      print(f"{Col.white}[{Col.green}+{Col.white}]{Col.green} Valid Address | Starting Process..");sleep(1)
      print(f"{Col.white}[{Col.dark_red}+{Col.white}]{Col.dark_red} Decrypting in : {Col.white}1.5 Seconds")
      sleep(1.5)
      proxies = randint(100,170)
      seconds = randint(23142,43254)
      print(f"{Col.white}[{Col.light_red}+{Col.white}]{Col.dark_red} Scraped : {Col.white}{proxies} {Col.dark_red}proxies in{Col.white} 1.5{seconds} {Col.dark_red}seconds")
      sleep(2.5)
      print("\n")
      while True:
         print("\n")
         m = randint(200,750)
         for _ in range(m):
            chars = string.ascii_lowercase + string.ascii_uppercase
            a = ''.join(choice(chars) for _ in range(64))
            print(f"{Col.dark_red}[{Col.dark_red}-{Col.dark_red}]{Col.dark_red} bc1{Col.dark_red}{a} ---> 0.00BTC {Col.dark_red} - {Col.dark_red}0.00$")
            sleep(0.1)
         mo= randint(57,980)
         mo2 = randint(10,80)
         chars = string.ascii_lowercase + string.ascii_uppercase
         a = ''.join(choice(chars) for _ in range(64))
         print(f"{Col.green}[{Col.green}-{Col.green}]{Col.green} We got a hit - {Col.green}{a} - {Col.green}{mo}.{mo2}$")
         sleep(1)
         print(f"{Col.white}[{Col.white}-{Col.white}]{Col.white} Transfer {Col.white}{mo}.{mo2}$ BTC to", {Col.blue}, btc)
         input(f"{Col.white}[{Col.dark_red}-{Col.white}]{Col.dark_red} Press Enter to exit")
Code()