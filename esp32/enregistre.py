import machine,os,time

def enre_tag(tag_id,rang):
  id=tag_id
  # Enregistre chaque evenement dans le Fichier MAC-adresseMAC
  
  print("Ecriture ...")

  chaine=str(id[0])+str(' ')+str(id[1])+str(' ')+str(id[2])+str(' ')+str(id[3])+str(' ')+str(id[4])
  
  fr = open('id-salarie.txt', 'r')
 
  lines = fr.readlines()
  NumberOfLine = len(lines)
  #print(lines)
  fr.close()


  if(NumberOfLine==0): #fichier vide
    with open('id-salarie.txt', 'a') as fw:
      for i in range(rang+1):
        if(i==rang):
          fw.write(chaine+'\n')
        else:
          fw.write("0 0 0 0 0 \n") # default value
  else:
    if(rang > NumberOfLine - 1  ):
      #print("test2")
      with open('id-salarie.txt', 'a') as fw:
        fw.write(chaine+'\n')
    else:
      #print("test3")
      #print(lines)
      lines[rang]=chaine+'\n'
      #print(lines)
      with open('id-salarie.txt', 'w') as fw:
        for l in lines:
          fw.write('%s' % l)

  fw.close()