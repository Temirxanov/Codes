from logging.handlers import TimedRotatingFileHandler
import logging
logger = logging.getLogger("logger_fayl")
logger.setLevel(logging.INFO)
parol = ' 12345678'
soraw = input("Parol jazin : ")
sanaw = 0
if parol != parol:
    ozgeriwshi = TimedRotatingFileHandler('logs',when="midnight",interval=1,backupCount=7)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    ozgeriwshi.setFormatter(formatter)

    logger.addHandler(ozgeriwshi)
    logger.info(f"{sanaw} ret qate kiritdin Qate parol\n{sanaw} ret urindin")
else:
    print("parol duris")
    