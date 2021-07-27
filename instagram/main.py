import os
import shutil
import json
from sys import path
from instabot import Bot
import sys

config = {}

absoulutePath = os.path.dirname(os.path.realpath(__file__))

if os.path.isdir(os.path.join(absoulutePath, 'config')):
    shutil.rmtree(os.path.join(absoulutePath, 'config'))

try:
    config = json.load(open(os.path.join(absoulutePath, 'config.json')))
except Exception as exception:
    raise Exception('Configuration file could not be found')

if len(config) == 0:
    raise Exception('Invalid configurations')


def uploadPhoto():
    pendingPhotosPath = os.path.join(
        absoulutePath, config['pendingPhotosPath'])
    postedPhotosPath = os.path.join(absoulutePath, config['postedPhotosPath'])

    pendingPhotos = os.listdir(pendingPhotosPath)
    if len(pendingPhotos) <= 0:
        exit('No pending photos were found....')

    bot = Bot()
    try:
        if bot.login(username=config['username'], password=config['password'], is_threaded=True):

            try:
                firstPhotoName = pendingPhotos[0]
                plainName = firstPhotoName.split('.')[:-1]
                caption = ''
                for character in plainName:
                    caption += character
                bot.upload_photo(os.path.join(pendingPhotosPath, firstPhotoName), options={
                                 'rename': False}, caption=caption)
                shutil.move(os.path.join(pendingPhotosPath, firstPhotoName), os.path.join(
                    postedPhotosPath, firstPhotoName))
                print(f'''{firstPhotoName} has been posted to instagram''')
            except Exception as exception:
                print(
                    f'''{firstPhotoName} was not posted reason: {exception}''')
            bot.logout()
    except Exception as e:
        print(f'''Loging Errors: {e}''')


def uploadVideo():
    pendingVideosPath = os.path.join(
        absoulutePath, config['pendingVideosPath'])
    postedVideosPath = os.path.join(absoulutePath, config['postedVideosPath'])

    pendingVideos = os.listdir(pendingVideosPath)
    if len(pendingVideos) <= 0:
        exit("No videos were found...")

    bot = Bot()
    try:
        if bot.login(username=config['username'], password=config['password'], is_threaded=True):
            try:
                firstVideoName = pendingVideos[0]
                plainName = firstVideoName.split('.')[:-1]
                caption = ''
                for character in plainName:
                    caption += character
                bot.upload_video(os.path.join(pendingVideosPath, firstVideoName), options={
                                 'rename': False}, caption=caption)
                shutil.move(os.path.join(pendingVideosPath, firstVideoName), os.path.join(
                    postedVideosPath, firstVideoName))
                print(f'''{firstVideoName} has been posted to instagram''')
            except Exception as exception:
                print(f'''{firstVideoName} was not posted reason: {exception}''')
            bot.logout()
    except Exception as e:
        print(f'''Loging Errors: {e}''')


if 'photo' in sys.argv:
    uploadPhoto()

if 'video' in sys.argv:
    uploadVideo()
