import facebook
import os
import shutil
import json


config = {}

try:
    config = json.load(open('config.json'))
except Exception as exception:
    raise Exception('Configuration file could not be found')

if len(config) == 0:
    raise Exception('Invalid configurations')

accessToken = config['accessToken']

pendingPhotosPath = config['pendingPhotosPath']
postedPhotosPath = config['postedPhotosPath']

socialGraph = facebook.GraphAPI(accessToken)

pendingPhotos = os.listdir(pendingPhotosPath)
if len(pendingPhotos) <= 0:
    print('No pending photos were found....')
else:
    try:
        firstPhotoName = pendingPhotos[0]
        plainName = firstPhotoName.split('.')[:-1]
        caption = ''
        for character in plainName:
            caption += character
        photoPostResponse = socialGraph.put_photo(open(f'''{pendingPhotosPath}/{firstPhotoName}''','rb'),message=caption)
        shutil.move(f'''{pendingPhotosPath}/{firstPhotoName}''',f'''{postedPhotosPath}/{firstPhotoName}''')
        print(f'''{firstPhotoName} has been posted to a facebook page''')
    except Exception as exception:
        print(f'''{firstPhotoName} was not posted reason: {exception}''')

