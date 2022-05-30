'''
carte_blanche_adrien = [63, 227, 52, 41, 193]
carte_jeune_adrien = [51, 172, 74, 217, 12]
badge_bleu_adrien = [199, 103, 218, 115, 9]
carte_blanche_greg = [198, 148, 159, 37, 232]
carte_jeune_greg = [121, 245, 189, 104, 89]
carte_jeune_JP = [67, 64, 75, 217, 145]
'''
#--------------------RFID--------------------
from read_TAG import do_read_une_fois
import machine
import time
import enregistre
import admin
import buzzer


tag = [0, 0, 0, 0, 0]
id_salarie = [0, 0, 0, 0, 0]
compteurLigne = 0
compteurCouleur = 0
#--------------------LED---------------------
from machine import Pin

led_jaune = Pin(26, Pin.OUT)
led_jaune.value(0)

from neopixel import NeoPixel

neo = machine.Pin(14, machine.Pin.OUT)   # GPIO13 en sortie pour piloter WS2812b
bandeau_led = NeoPixel(neo, 10)   # Cree une instance pour piloter 5 WS2812b

vert = (0, 255, 0)
rouge = (255,0,0) 
bleu = (0, 0, 128)
blanc = (127,127,127)
jaune = (255,180,0)
off = (0,0,0)

bandeau_led[0] = (off)  # eteindre la led verte 0
bandeau_led.write()  # Affiche toutes les Led
bandeau_led[1] = (off)  # eteindre la led  1
bandeau_led.write()  # Affiche toutes les Led
bandeau_led[2] = (off)  # eteindre la led  2
bandeau_led.write()  # Affiche toutes les Led
bandeau_led[3] = (off)  # eteindre la led verte 3
bandeau_led.write()  # Affiche toutes les Led
bandeau_led[4] = (off)  # eteindre la led verte 3
bandeau_led.write()  # Affiche toutes les Led

#------------------BUZZER-------------------
buzzer = Pin(33, Pin.OUT)
buzzer.value(0)
compteur = 0

#------------------GACHE--------------------
gache = Pin(12, Pin.OUT)
gache.value(0)

#-------------------------------------------
while(1):
  compteurLigne = 0
  compteurCouleur = 0
  led_jaune.on()
  f = open('id-salarie.txt', 'r')
  print("-------------------------------------------")
  print("Attente BADGE...")
  print("-----")
  
  while(tag==[0, 0, 0, 0, 0]):
    tag = do_read_une_fois()
  print("ID Salarie: ", id_salarie)
  print("Badge lu: ", tag)
  ok=0

  print("-----")

  if tag==[103, 240, 200, 181, 234]:
    bandeau_led[0] = (bleu)
    bandeau_led.write()
    admin.admin1()
    time.sleep(1)
  
  elif tag==[39, 246, 1, 99, 179]:
    bandeau_led[1] = (bleu)
    bandeau_led.write()
    admin.admin2()
    time.sleep(1)
  
  elif tag==[231, 220, 193, 100, 158]:
    bandeau_led[2] = (bleu)
    bandeau_led.write()
    admin.admin3()
    time.sleep(1)
  

  elif tag==[2, 236, 200, 131, 165]:
    bandeau_led[3] = (bleu)
    bandeau_led.write()
    admin.admin4()
    time.sleep(1)

  
  else:
    for id_salarie in f.readlines():
      print("-----")
      id_salarie = id_salarie.split()
      print(id_salarie)
      print(tag)

      print("-----")

      if(int(id_salarie[0])== tag[0]):
        print("0 OK")
        if(int(id_salarie[1]) == tag[1]):
          print("1 OK")
          if(int(id_salarie[2]) == tag[2]):
            print("2 OK")
            if(int(id_salarie[3]) == tag[3]):
              print("3 OK")
              if(int(id_salarie[4]) == tag[4]):
                print("4 OK")
                print("-----")
                print("CARTE OK")
                ok=1
                compteurCouleur = compteurLigne
      compteurLigne = compteurLigne +1
      
              
  if(ok==1):
    if(compteurCouleur == 0):
      led_jaune.off()
      buzzer.on()
      gache.on()
      bandeau_led[0] = (vert)  # allumer la led 0 verte
      bandeau_led.write()  # Affiche toutes les Led

    if(compteurCouleur == 1):
      led_jaune.off()
      buzzer.on()
      gache.on()
      bandeau_led[1] = (vert)  # allumer la led 1 verte
      bandeau_led.write()  # Affiche toutes les Led

    if(compteurCouleur == 2):
      led_jaune.off()
      buzzer.on()
      gache.on()
      bandeau_led[2] = (vert)  # allumer la led 2 verte
      bandeau_led.write()  # Affiche toutes les Led

    if(compteurCouleur == 3):
      led_jaune.off()
      buzzer.on()
      gache.on()
      bandeau_led[3] = (vert)  # allumer la led 3 verte
      bandeau_led.write()  # Affiche toutes les Led

    time.sleep(0.75)
    buzzer.off()
    print("-------------------------------------------")

  if(ok==0):
    print("CARTE INCONNUE")
    led_jaune.off()
    gache.off()

    bandeau_led[0] = (rouge)  # allumer la led 0 rouge
    bandeau_led.write()  # Affiche toutes les Led  
    bandeau_led[1] = (rouge)  # allumer la led 1 rouge
    bandeau_led.write()  # Affiche toutes les Led  
    bandeau_led[2] = (rouge)  # allumer la led 2 rouge
    bandeau_led.write()  # Affiche toutes les Led  
    bandeau_led[3] = (rouge)  # allumer la led 3 rouge
    bandeau_led.write()  # Affiche toutes les Led  

    print("-------------------------------------------")

    for compteur in range(3):
      buzzer.on()
      time.sleep(0.1)
      buzzer.off()
      time.sleep(0.03)
  buzzer.off()
  time.sleep(1.64)
  
  #--------------------------------------------
  buzzer.off()
  gache.off()
  bandeau_led[0] = (off)  # eteindre la led verte 0
  bandeau_led.write()  # Affiche toutes les Led
  bandeau_led[1] = (off)  # eteindre la led  1
  bandeau_led.write()  # Affiche toutes les Led
  bandeau_led[2] = (off)  # eteindre la led  2
  bandeau_led.write()  # Affiche toutes les Led
  bandeau_led[3] = (off)  # eteindre la led verte 3
  bandeau_led.write()  # Affiche toutes les Led
  bandeau_led[4] = (off)  # eteindre la led verte 3
  bandeau_led.write()  # Affiche toutes les Led
  
  f.close()
  tag = [0, 0, 0, 0, 0]  
  time.sleep(0.5)