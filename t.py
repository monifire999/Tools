import requests
import os
import time
import threading

if 'Windown':
    os.system('cls')
else:
    os.system('clear')

banner = '''\033[32m
 ________   ________   _________   ________   ___  ___   _______    ________     
|\   ____\ |\   __  \ |\___   ___\|\   ____\ |\  \|\  \ |\  ___ \  |\   __  \    
\ \  \___| \ \  \|\  \\|___ \  \_|\ \  \___| \ \  \\\  \\ \   __/| \ \  \|\  \   
 \ \  \     \ \   __  \    \ \  \  \ \  \     \ \   __  \\ \  \_|/__\ \   _  _\  
  \ \  \____ \ \  \ \  \    \ \  \  \ \  \____ \ \  \ \  \\ \  \_|\ \\ \  \\  \| 
   \ \_______\\ \__\ \__\    \ \__\  \ \_______\\ \__\ \__\\ \_______\\ \__\\ _\ 
    \|_______| \|__|\|__|     \|__|   \|_______| \|__|\|__| \|_______| \|__|\|__|
'''

print(banner)
print('\033[0m________________________________________________')
print('')
print('\033[32m 1 -  \033[0mSPAM SMS')
print('\033[32m 2 -  \033[0mSPAM EMAIL')
print('\033[32m 3 -  \033[0mSPAM DISCORD')
print('\033[32m 4 -  \033[0mDDoS Layer 7')
print('\033[32m 5 -  \033[0mSMS TEXT')
print('')
print('\033[0m________________________________________________')
print('')

choice = input('\033[34m[>>] \033[32mChoose \033[0m: \033[31m')

if (choice == '1' or choice == '01'):
    print('\n')
    print('SPAM SMS')

elif (choice == '2' or choice == '02'):
    print('\n')
    print('SPAM EMAIL')

elif (choice == '3' or choice == '03'):
    print('\n')
    print('SPAM DISCORD')

elif (choice == '4' or choice == '04'):
    print('\n')
    print('DDoS Layer 7')

elif (choice == '5' or choice == '05'):
    print('\n')
    print('SMS TEXT')

else:
    print('\n')
    print('error')