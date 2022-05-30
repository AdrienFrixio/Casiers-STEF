import mfrc522
from os import uname


def do_read_simple():

	if uname()[0] == 'WiPy':
    #                     SCK   MOSI   MISO   RST  CS=SDA
		rdr = mfrc522.MFRC522("P5", "P11", "P6", "P7", "P8")
	elif uname()[0] == 'esp8266':
		rdr = mfrc522.MFRC522(0, 2, 4, 5, 14)
    
	elif uname()[0] == 'esp32':
		rdr = mfrc522.MFRC522(18, 23, 19, 17, 16)
	else:
		raise RuntimeError("Unsupported platform")

	#print("")
	#print("Placer la carte devant RFID : read from address 0x08")
	#print("")
	badge=0
	

	try:
    
		while (badge==0):

			(stat, tag_type) = rdr.request(rdr.REQIDL)

			if stat == rdr.OK:

				(stat, raw_uid) = rdr.anticoll()

				if stat == rdr.OK:
          
					badge=1
					return raw_uid
                    


	except KeyboardInterrupt:
		print("Bye")

 
def do_read_unique():

	if uname()[0] == 'WiPy':
    #                     SCK   MOSI   MISO   RST  CS=SDA
		rdr = mfrc522.MFRC522("P5", "P11", "P6", "P7", "P8")
	elif uname()[0] == 'esp8266':
		rdr = mfrc522.MFRC522(0, 2, 4, 5, 14)
    
	elif uname()[0] == 'esp32':
		rdr = mfrc522.MFRC522(18, 23, 19, 17, 16)
	else:
		raise RuntimeError("Unsupported platform")


	compteur=0

	try:
    
		while (compteur<8):
			compteur=compteur+1
			if (compteur==8):
		
				raw_uid=[0,0,0,0,0]

				return raw_uid
      

			(stat, tag_type) = rdr.request(rdr.REQIDL)

			if stat == rdr.OK:

				(stat, raw_uid) = rdr.anticoll()

				if stat == rdr.OK:
          
					badge=1
					return raw_uid
                    


	except KeyboardInterrupt:
		print("Bye")

def do_read_une_fois():

	if uname()[0] == 'WiPy':
    #                     SCK   MOSI   MISO   RST  CS=SDA
		rdr = mfrc522.MFRC522("P5", "P11", "P6", "P7", "P8")
	elif uname()[0] == 'esp8266':
		rdr = mfrc522.MFRC522(0, 2, 4, 5, 14)
    
	elif uname()[0] == 'esp32':
		rdr = mfrc522.MFRC522(18, 23, 19, 17, 16)
	else:
		raise RuntimeError("Unsupported platform")

	compteur=0

	try:
    
		while (compteur<3):
			compteur=compteur+1
			if (compteur==2):
		
				raw_uid=[0,0,0,0,0]
				return raw_uid
      

			(stat, tag_type) = rdr.request(rdr.REQIDL)

			if stat == rdr.OK:


				(stat, raw_uid) = rdr.anticoll()

				if stat == rdr.OK:
          
					badge=1
					return raw_uid
                    


	except KeyboardInterrupt:
		print("Bye")








