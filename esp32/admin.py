from machine import Pin
import mfrc522
import time
import enregistre
import read_TAG
import buzzer

def admin1():
    buzzer.buzz(0.05)
    buzzer.buzz(0.05)
    buzzer.buzz(0.05)
    print("Mode ADMIN 1")
    time.sleep(0.5)
    print('Passez nouveau badge:')
    tag = read_TAG.do_read_une_fois()



    while (tag==[0,0,0,0,0]) or (tag==[103, 240, 200, 181, 234]) or (tag==[39, 246, 1, 99, 179]) or (tag==[231, 220, 193, 100, 158]) or (tag==[2, 236, 200, 131, 165]):
        tag = read_TAG.do_read_une_fois()
        time.sleep(0.2)
    print('enregistrement tag: ', tag)
    enregistre.enre_tag(tag, 0)
    ##suppligne.ligne1(tag)
    buzzer.buzz(1)

def admin2():
    buzzer.buzz(0.05)
    buzzer.buzz(0.05)
    buzzer.buzz(0.05)
    print("Mode ADMIN 2")
    time.sleep(0.5)
    print('Passez nouveau badge:')
    tag = read_TAG.do_read_une_fois()
    while (tag==[0,0,0,0,0]) or (tag==[103, 240, 200, 181, 234]) or (tag==[39, 246, 1, 99, 179]) or (tag==[231, 220, 193, 100, 158]) or (tag==[2, 236, 200, 131, 165]):
        tag = read_TAG.do_read_une_fois()
        time.sleep(0.2)
    print('enregistrement tag: ', tag)
    enregistre.enre_tag(tag, 1)
    ##suppligne.ligne2(tag)
    buzzer.buzz(1)

def admin3():
    buzzer.buzz(0.05)
    buzzer.buzz(0.05)
    buzzer.buzz(0.05)
    print("Mode ADMIN 3")
    time.sleep(0.5)
    print('Passez nouveau badge:')
    tag = read_TAG.do_read_une_fois()
    while (tag==[0,0,0,0,0]) or (tag==[103, 240, 200, 181, 234]) or (tag==[39, 246, 1, 99, 179]) or (tag==[231, 220, 193, 100, 158]) or (tag==[2, 236, 200, 131, 165]):
        tag = read_TAG.do_read_une_fois()
        time.sleep(0.2)
    print('enregistrement tag: ', tag)
    enregistre.enre_tag(tag, 2)
    ##suppligne.ligne3(tag)
    buzzer.buzz(1)

def admin4():
    buzzer.buzz(0.05)
    buzzer.buzz(0.05)
    buzzer.buzz(0.05)
    print("Mode ADMIN 4")
    time.sleep(0.5)
    print('Passez nouveau badge:')
    tag = read_TAG.do_read_une_fois()
    while (tag==[0,0,0,0,0]) or (tag==[103, 240, 200, 181, 234]) or (tag==[39, 246, 1, 99, 179]) or (tag==[231, 220, 193, 100, 158]) or (tag==[2, 236, 200, 131, 165]):
        tag = read_TAG.do_read_une_fois()
        time.sleep(0.2)
    print('enregistrement tag: ', tag)
    enregistre.enre_tag(tag, 3)
    ##suppligne.ligne4(tag)
    buzzer.buzz(1)