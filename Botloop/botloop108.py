import pyautogui as py
import time

print('bot start!')

# py.keyDown('s')
# time.sleep(0.5)
# py.keyUp('s')
# time.sleep(0.5)
# py.keyDown('q')
# time.sleep(2)
# py.keyUp('q')
# time.sleep(2)

while True :

    talk_button = py.locateOnScreen('talk_button.png')

    if (talk_button != None) :
            py.moveTo(talk_button, duration = 0.2)
            py.click(talk_button)
            print('talk to red panda')
        
    while (talk_button == None) :
        py.keyDown('s')
        time.sleep(0.5)
        py.keyUp('s')
        time.sleep(0.5)
        py.keyDown('q')
        time.sleep(2)
        py.keyUp('q')
        time.sleep(2)

        talk_button = py.locateOnScreen('talk_button.png')

        if (talk_button != None) :
            py.moveTo(talk_button, duration = 0.2)
            py.click(talk_button)
            print('talk to red panda')
            break
 
    time.sleep(6)

    friend_menu = py.locateOnScreen('friend_menu.png')
    py.moveTo(friend_menu, duration = 0.2)
    py.click(friend_menu)
    print('select friend menu')

    select_room = py.locateOnScreen('108create_by_404.png')
    select_room_onclick = py.locateOnScreen('108create_by_404_onclick.png')
    refresh_button = py.locateOnScreen('refresh_button.png')

    while (select_room == None) :
        select_room = py.locateOnScreen('108create_by_404.png')
        if (select_room != None) :
            py.moveTo(select_room, duration = 0.2)
            py.moveRel(0 , -12 , duration = 0.2)
            py.click()
            print('select room')
            break

        elif (select_room_onclick != None) :
            py.moveTo(select_room_onclick, duration = 0.2)
            print('room selected')
            break

        py.moveTo(refresh_button, duration = 0.2)
        py.click(refresh_button)
        print('refresh room!')
        time.sleep(2)

    join_button = py.locateOnScreen('join_button.png')
    py.moveTo(join_button, duration = 0.2)
    py.click(join_button)
    print('joining room!')

    check_host = py.locateOnScreen('host108check.png')

    while (check_host == None or check_host != None) :
        check_host = py.locateOnScreen('host108check.png')
        print('checking host')

        if (check_host != None) :
            ready_button = py.locateOnScreen('ready_button.png')
            py.moveTo(ready_button, duration = 0.2)
            py.click(ready_button)
            print('ready!')
            break

        elif (check_host == None) :
            cancel_button = py.locateOnScreen('cancel_button.png')
            py.moveTo(cancel_button, duration = 0.2)
            py.click(cancel_button)
            print('not this room!')

    room_enter = py.locateOnScreen('room_enter.png')

    while (room_enter == None) :

        room_enter = py.locateOnScreen('room_enter.png')

        if (room_enter != None) :
            time.sleep(4)
            break

    py.press('space')
    py.press('5')
    time.sleep(1)
    py.press('6')

    end_mission = py.locateOnScreen('end_mission.png')
    while (end_mission == None) :
        end_mission = py.locateOnScreen('end_mission.png')
        item_root = py.locateOnScreen('item_root.png')
        print('waiting for end mission')
        if (end_mission != None) :
            print('mission end!')
            break
        elif (item_root != None) :
            print('item not root')
            break

    root_item = py.locateOnScreen('root_item.png')
    while (root_item == None) :
        root_item = py.locateOnScreen('root_item.png')
        rooting = py.locateOnScreen('rooting.png')
        py.moveTo(rooting, duration = 0.5)
        py.click(rooting)
        print('item has been root!')
        if (root_item != None) :
            print('root item checked! get quiting!')
            break

    gotoguild = py.locateOnScreen('gotoguild.png')
    py.moveTo(gotoguild, duration = 0.2)
    py.click(gotoguild)
    print('going to guild')

    room_enter = py.locateOnScreen('room_enter.png')

    while (room_enter == None) :
        room_enter = py.locateOnScreen('room_enter.png')
        print('waiting get back to guild')
        time.sleep(1)
        if (room_enter != None) :
            print('go to guild complete!')
            time.sleep(2)
            break
