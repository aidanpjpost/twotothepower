#TWOTOTHEPOWER BOT BY AIDAN POST (WWW.AIDANPJPOST.COM)

import tweepy
import time

configFile = 'twitterbot.config'
credFile = 'credentials.config'
logOutput = 'DEBUG: '
daySec = 86400

def message(y):
    value = str(2**y)
    string = ('2 to the power of '+ str(y) + ' is ' + str(value))
    return string

def reset():
    updateConfig('startDay', 0, configFile)
    updateConfig('lastDay', 0, configFile)
    updateConfig('dayNum', 0, configFile)
    updateConfig('doneForDay', 2, configFile)

def getConfig(name, filename):
    config = open(filename)
    for line in config:
        if name in line:
            line = line.strip(name)
            line = line.strip('=')
            line = line.strip('\n')
            config.close()
            return(line)

def updateConfig(name, val, filename):
    oldVal = (str(name) + '=' + str(getConfig(name, filename)))
    newVal = (str(name) + '=' + str(val))
    s = open(filename).read()
    s = s.replace(oldVal, newVal)
    f = open(filename, 'w')
    f.write(s)
    f.close()

consumer_key = getConfig('consumer_key', credFile)
consumer_secret = getConfig('consumer_secret', credFile)
access_token = getConfig('access_token', credFile)
access_token_secret = getConfig('access_token_secret', credFile)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

startDay = long(getConfig('startDay',configFile))
lastDay = long(getConfig('lastDay',configFile))
dayNum = int(getConfig('dayNum',configFile))
doneForDay = int(getConfig('doneForDay',configFile))

if startDay == 0: 
    startDay = long(time.time())
    updateConfig('startDay', startDay, configFile)
if lastDay == 0: 
    lastDay = long(time.time())
    updateConfig('lastDay', lastDay, configFile)
if dayNum == 0: 
    dayNum = 1
    updateConfig('dayNum', dayNum, configFile)
if doneForDay == 2: 
    doneForDay = 0
    updateConfig('doneForDay', doneForDay, configFile)

while dayNum <= 365:
    
    print(logOutput+ 'Bot is active')
    if doneForDay == 0:
        
        line = message(dayNum)
        print(logOutput + line)
        api.update_status(line)
        
        doneForDay = 1
        dayNum = dayNum+1
        print(logOutput+ 'done for day')
        updateConfig('doneForDay', doneForDay, configFile)
        updateConfig('dayNum', dayNum, configFile)

    if (long(time.time()) - (lastDay + daySec)) >= 0 :
    
        lastDay = long(time.time())
        print(logOutput + 'day change')
        updateConfig('lastDay', lastDay, configFile)
        doneForDay = 0
    time.sleep(1800)
