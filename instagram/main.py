import os
import shutil
import json
from instabot import Bot


config = {}

absoulutePath = os.path.dirname(os.path.realpath(__file__))

try:
    config = json.load(open(os.path.join(absoulutePath,'config.json')))
except Exception as exception:
    raise Exception('Configuration file could not be found')

if len(config) == 0:
    raise Exception('Invalid configurations')


pendingPhotosPath = os.path.join(absoulutePath,config['pendingPhotosPath'])
postedPhotosPath = os.path.join(absoulutePath,config['postedPhotosPath'])


bot = Bot()

try:
    bot.login(username=config['username'],password=config['password'])
except Exception as e:
    print(f'''Login Error: {e}''')

try:
    bot.upload_photo("/home/victor/Desktop/photo1.png", caption="Uploaded by Bot")
except Exception as e:
    print(f'''Photo upload Error: {e}''')
