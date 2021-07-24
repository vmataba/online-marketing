# Welcome to Online Markeing Tool
> Online Marketing Tool helps you to periodically post images and videos (not yet  supported) to your
>Facebook page and Instagram account

This tool currently supports
1. Facebook
2. Instagram

### 1. Facebook
> You will need a facebook APP for this to work, if you have not yet created one
> you can do so from [here] (https://developers.facebook.com/apps)
> Once you have created an app, copy its *ID*, *secrete* and *page access token*
> *NOTE:* page access token is mandatory 
> Make sure page access token has permissions to these
> - pages_show_list
> - pages_messaging
> - publish_to_groups
> - page_events
> - pages_read_engagement
> - pages_manage_metadata
> - pages_read_user_content
> - pages_manage_posts
> - pages_manage_engagement
> - public_profile 
> When you are done with all the above procedures, rename the file
> facebook/config.example.py to facebook/config.py and fill required inputs

### 2. Instagram
> In this case only username and password are required
> Other steps are similar to *Facebook Part*

In either parts (Facebook and Instagram) this is folder structure
- main.py, entry spript of the program
- config.json, program configuration file (derived from config.example.py)
- photos/pending, a folder for photos to be posted
- photos/posted, a folder for all posted photos
- videos/pending, a folder for all videos to be posted
- videos/posted, a folder for all posted videos

## Requirements
1. You must have Python 3.x installed on your machine
2. For Facebook Part, you must have facebook-sdk module installed
    ```
    pip3 install facebook-sdk
    ```
    See full documentation from [here] (https://facebook-sdk.readthedocs.io/en/latest/)
3. For Instagram Part, you must have instabot extension installed
    ```
    pip3 install instabot
    ```
## How to run the program
After you have set up everything this is how you can run the program
1. Post the first image from the pending images list
```
python3 <path_to_your_program_folder>/facebook/main.py
```
2. For periodic posting you may want to use cron jobs, run the same command in cronjob.
Example posting single image afer every 30 minutes
```
*/30 * * * * python3 <path_to_your_program_folder>/facebook/main.py
```
Learn more about cronjobs [here] (https://crontab.guru/)

For PC users you may want to use *Task Schedulers*

The same steps work for Instagram