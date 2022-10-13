# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
text = 'прриветб аоаоарра алалашаш жщнщнекщ абв оокеок елкеоктпт рпннабв пррабв ренкцуцо лршненнааб , ммрмрагжыз , рписиабв . '
print(text)
delElem = input('Введите элемент для удаления:')
textString=text.split()
#print(textString)
newString=[]
for elem in textString:
   if delElem not in elem:
      newString.append(elem)
print(" ".join(newString))
