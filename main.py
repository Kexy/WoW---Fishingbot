#                               Yeet-Bot (v0.1)
#                               /$/$/$/$/$/$/$/
#    Please don't use this bot on the official servers since it is detected!


import logging

# Variables & Settings
APP_NAME = 'World of Warcraft-64'
yeetIMG = "yeet.png"
findYeet = 0.5
findSplash = 0.7
Settings.MoveMouseDelay = 0

# Constants
CAST_YEET = 'cast_yeet'
FIND_YEET = 'find_yeet'
WAIT_SPLASH = 'wait_splash'
GET_LOOT = 'get_loot'

# Logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(message)s')
def log(msg):
    logging.debug(msg)

# Area
App.focus(APP_NAME)
searchingArea = selectRegion('Select the fishing area')

# WoW focus
App.Focus(APP_NAME)

#init
status = CAST_YEET
startTime = time.time()
foundYEET = None
yeetIMG = Pattern(yeetIMG)

while True:
    elapsedTime = time.time() - startTime

    if elapsed>20:
        status = CAST_YEET

    if status==FIND_YEET and elapsedTime>8:
        status = CAST_YEET

    if status=CAST_YEET:
        type('1')
        mouseMove(searchingArea.getTopLeft())
        startTime = time.time()
        status = FIND_YEET
        sleep(1)

    if status==FIND_YEET
        foundYEET = searchingArea.exists(yeetImg.similar(findYeetSimilarity))

        if foundYeet:
            status = WAIT_SPLASH
            mouseMove(foundYEET)

    if status==WAIT_SPLASH:
        expand = foundYEET.nearby(10)

        if not expand.exists(yeetIMG.similar(findSplashSimilarity), 1):
            log('Magikarp used splash!')
            status = GET_LOOT

    if status==GET_LOOT:
        rightClick(foundYEET, KeyModifier.SHIFT)
        status = CAST_YEET
        sleep(3)
