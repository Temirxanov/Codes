# --------as shutil pathlib--------
import os
'''print(os.getcwd())''' #get correct working dictonary
                    # Fayldin qay jerde ekenin tabiw ushin cwd

# papka jaratiw
'''os.mkdir("Jana_papka")''' # 1 papka jaratadi 
'''os.makedirs("Tiykargi_papka/ishki papka")''' #Papkanin ishinen papka jaratadi

'''
os.remove("sfbsb.py")''' #Fayldi oshiriw
'os.rmdir("Jana_papka")' #Papkani oshiriw

# Shutil moduli - Fayllardi koriw ham nusxalaw

import shutil
'''shutil.copy("text.txt","Nusxa.txt")''' # Bar fayldi nusxalaydi

'''os.mkdir("Papka")'''
# shutil.move("Nusxa.txt","Jana_papka")
# Bar fayldi korsetilgen papkanin ishine koshiredi

'''shutil.rmtree("Papka") '''
# Fayldin ishindegi hamme narsesi menen oshiredi


# Pathlib jana usilda fayllar menen islew

# from pathlib import Path
# import shutil
# Path("taza").mkdir(exist_ok=True) # Taza papka jaratadi
# for fayl in Path(".").glob('*txt'): # txt fayl di izleydi 
#     shutil.copy(fayl,'taza') # Harbirin koshiredi

'''
from pathlib import Path
a=input('Kodti amelge asrasizba(Awa/yaq):').lower()
if a=='awa':
    print("Kod isledi")
    Path("Python").mkdir(exist_ok=True) 
    for fayl in Path(".").glob('*py'): 
        shutil.copy(fayl,'Python')
        break
else:
    print("Kod istemedi")
'''


# # Keyingi tema: Log fayllar ham qatelerdi jazip bariwy
# import logging
# try:
#     a={"Pyton"}
#     c=a["y"]
# except TypeError as e:
#     logging.error("Dictte formatinda element alinbaydi")

# a=14
# print(f"Jasin {a} te")

import os
from pathlib import Path
a=input('Kodti amelge asrasizba(Awa/yaq):').lower()
if a=='awa':
    print("Kod isledi")
    Path("Python").mkdir(exist_ok=True) 
    for fayl in Path(".").glob('*py'): 
        shutil.copy(fayl,'Python')
        break
else:
    print("Kod istemedi")
os.remove("3-Sabaq_dev.py")