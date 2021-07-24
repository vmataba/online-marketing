import os
import shutil
import json
from sys import path
from instabot import Bot


config = {}

absoulutePath = os.path.dirname(os.path.realpath(__file__))

if os.path.isdir(os.path.join(absoulutePath,'config')):
    shutil.rmtree(os.path.join(absoulutePath,'config'))

try:
    config = json.load(open(os.path.join(absoulutePath, 'config.json')))
except Exception as exception:
    raise Exception('Configuration file could not be found')

if len(config) == 0:
    raise Exception('Invalid configurations')


pendingPhotosPath = os.path.join(absoulutePath, config['pendingPhotosPath'])
postedPhotosPath = os.path.join(absoulutePath, config['postedPhotosPath'])


bot = Bot()

try:
    if bot.login(username=config['username'], password=config['password'],is_threaded=True):
        pendingPhotos = os.listdir(pendingPhotosPath)
        if len(pendingPhotos) <= 0:
            print('No pending photos were found....')
        else:
            firstPhotoName = pendingPhotos[0]
            try:
                bot.upload_photo(os.path.join(pendingPhotosPath, firstPhotoName),options={'rename':False})
                shutil.move(os.path.join(pendingPhotosPath,firstPhotoName),os.path.join(postedPhotosPath,firstPhotoName))
                print(f'''{firstPhotoName} has been posted to instagram''')
            except Exception as exception:
                print(f'''{firstPhotoName} was not posted reason: {exception}''')

        bot.logout()
except Exception as e:
    print(f'''Loging Errors: {e}''')

