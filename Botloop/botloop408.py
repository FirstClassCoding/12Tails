from contextlib import AbstractAsyncContextManager
import pyautogui as py
import time

print('bot start!')

count = 0
exp = 327
bonus_exp = 101

class bot:

    def walk() :
        print('walking to redpanda')
        py.keyDown('s')
        time.sleep(0.8)
        py.keyUp('s')
        time.sleep(0.5)
        py.keyDown('q')
        time.sleep(3)
        py.keyUp('q')
        time.sleep(0.5)
        print('walk end')

    def attackLoop() :
        print('attack loop start')
        bot.solokill()
        print('#1 kill earn %d exp' %exp)

        time.sleep(1)
        py.keyDown('w')
        time.sleep(3.8)
        py.keyUp('w')
        time.sleep(0.5)
        bot.attack()
        print('#2 kill earn %d exp' %exp)

        time.sleep(1)
        py.keyDown('w')
        time.sleep(5)
        py.keyUp('w')
        time.sleep(0.5)
        bot.attack()
        print('#3 kill earn %d exp' %exp)

        time.sleep(1)
        py.keyDown('q')
        time.sleep(7)
        py.keyUp('q')
        time.sleep(0.5)
        py.keyDown('w')
        time.sleep(3)
        py.keyUp('w')
        time.sleep(0.5)
        bot.attackEnemy()
        print('enemy kill')

    def solokill() :
        py.press('space')
        while True :
            if (py.locateOnScreen('cactun.png') != None) :
                py.click()
            else :
                break
    
    def attack(i = 0) :
        while (py.locateOnScreen('cactun.png') != None) :
            py.click()
            time.sleep(0.1)
            return bot.attack(i)
        
        while (py.locateOnScreen('cacton.png') != None) :
            py.click()
            time.sleep(0.1)
            return bot.attack(i)

        if (i < 10) :
            py.press('space')
            i += 1
            return bot.attack(i)

        else :
            print('monster not found')

    def attackEnemy() :
        py.press('space')
        py.press('1')
        while True :
            if (py.locateOnScreen('enemy.png') != None) :
                py.click()
            else :
                break

    def moves(locate, time) :
        py.moveTo(locate, duration = time)

    def moveAndClick(locate, time) :
        py.moveTo(locate, duration = time)
        py.click(locate)

    def advanceMoveAndClick(locate, time, posX, posY) :
        py.moveTo(locate, duration = time)
        py.moveRel(posX, posY, duration = time)
        py.click()

    def talkButton() :
        print('find talk button')

        if (py.locateOnScreen('talk_button.png') != None) :
            print('find talk button success')
            return py.locateOnScreen('talk_button.png')

        elif (py.locateOnScreen('talk_button1.png') != None) :
            print('find talk button success')
            return py.locateOnScreen('talk_button1.png')

        print('can\'t find talk button')

    def friendMenu() :
        return py.locateOnScreen('friend_menu.png')

    def selectRoom() :
        return py.locateOnScreen('408create_by_404.png')

    def selectRoomOnClick() :
        return py.locateOnScreen('408create_by_404_onclick.png')

    def refreshButton() :
        return py.locateOnScreen('refresh_button.png')

    def joinButton() :
        return py.locateOnScreen('join_button.png')

    def checkHost() :
        return py.locateOnScreen('host408check.png')

    def readyButton() :
        return py.locateOnScreen('ready_button.png')

    def cancelButton() :
        return py.locateOnScreen('cancel_button.png')

    def roomEnter() :
        return py.locateOnScreen('room_enter.png')

    def endMission() :
        return py.locateOnScreen('end_mission408.png')

    def rootItem() :
        return py.locateOnScreen('root_item.png')

    def goToGuild() :
        return py.locateOnScreen('gotoguild.png')

def talkToRedPanda() :
    while True :
        if (bot.talkButton() != None) :
            bot.moveAndClick(bot.talkButton(), 0.2)
            print('talk to red panda')
            time.sleep(1)
            break
        time.sleep(1)

def selectFriendMenu() :
    while True :
        if (bot.friendMenu() != None) :
            bot.moveAndClick(bot.friendMenu(), 0.2)
            print('select friend menu')
            break
        time.sleep(1)

def selectRoom() :
    while True :
        time.sleep(1)
        if (bot.selectRoom() != None) :
            bot.advanceMoveAndClick(bot.selectRoom(), 0.2, 0, -12)
            print('select room')
            break

        elif (bot.selectRoomOnClick() != None) :
            bot.moves(bot.selectRoomOnClick(), 0.2)
            print('room selected')
            break

        bot.moveAndClick(bot.refreshButton(), 0.2)
        print('refresh room!')
        time.sleep(1)

def joinRoom() :
    while True :
        if (bot.joinButton() != None) :
            bot.moveAndClick(bot.joinButton(), 0.2)
            print('joining room!')
            break
        time.sleep(1)

def checkHost() :
    print('checking host')
    while True :
        if (bot.checkHost() != None) :
            bot.moveAndClick(bot.readyButton(), 0.2)
            print('ready!')
            break

        # elif (bot.checkHost() == None) :
        #     bot.moveAndClick(bot.cancelButton(), 0.2)
        #     print('not this room!')
        #     selectRoom()
        #     joinRoom()
        
        time.sleep(1)

def waitForEnterRoom() :
    print('starting')
    while True :
        if (bot.roomEnter() != None) :
            print('enter room success')
            time.sleep(5)
            break
        time.sleep(1)

def waitForEndMission() :
    print('waiting for end mission')
    while True :
        if (bot.endMission() != None) :
            print('mission end!')
            break
        time.sleep(1)

def rootItem() :
    while (bot.rootItem() == None) :
        bot.moveAndClick(bot.rootItem(), 0.5)
        print('item has been root!')
        if (bot.rootItem() != None) :
            print('root item checked! get quiting!')
            break

def goToGuild() :
    while True :
        if (bot.goToGuild() != None) :
            bot.moveAndClick(bot.goToGuild(), 0.2)
            print('going to guild')
            break
        time.sleep(1)

def checkGuild() :
    print('loading back to guild')
    while True :
        if (bot.roomEnter() != None) :
            print('go to guild complete!')
            time.sleep(1)
            break
        time.sleep(1)

while True :
    bot.walk()
    talkToRedPanda()
    selectFriendMenu()
    selectRoom()
    joinRoom()
    checkHost()
    waitForEnterRoom()
    bot.attackLoop()
    waitForEndMission()
    goToGuild()
    checkGuild()
    count += 3
    print('end round %d total earn %d' %(count / 3, (count * exp) + (count * bonus_exp)))
    time.sleep(1)
    # break

# print(bot.talkButton())
