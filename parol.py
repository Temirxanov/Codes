from logging.handlers import TimedRotatingFileHandler
import logging
logger = logging.getLogger("logger_fayl")
logger.setLevel(logging.INFO)
loginn = 'temirxanov'
login = input("Login:")
parol = ' 12345678'
soraw = input("Parol jazin : ")
sanaw = 0
if parol != parol or login != loginn:
    ozgeriwshi = TimedRotatingFileHandler('logss',when="midnight",interval=1,backupCount=7)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    ozgeriwshi.setFormatter(formatter)

    logger.addHandler(ozgeriwshi)
    if parol!=soraw and login == loginn:
        logger.info(f"Parol qate")
    elif parol == soraw and login != loginn:
        parol!=soraw and login == loginn
    else:
        logger.info("Login ham parolde qate")
else:
    print("parol duris")
    
    
