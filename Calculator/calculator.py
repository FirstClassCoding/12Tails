program = str(input("Please Select Program \n1.hpdrain Calculator\n2.Effect Calculator\n3.Cha Calculator\n4.Original Cool Down Calculator\n5.Cha Agi Optimization\n6.TT&CO Success Rate\nPlease Enter Program With Number Here >>> "))

if program == '1':
    double_effect = str(input("Have Double Effect line C ? (Yes = Y / No = N) >>> "))
    weapon = str(input("Have Water Dungeon Weapon ? (Yes = Y / No = N) >>> "))
    accessory = str(input("Have Water Dungeon Accessory ? (Yes = Y / No = N) >>> "))

    #weapon = 12% accessory = 8% double effect = 24%

    f_lck = int(input("Front Status lck >>> "))
    b_lck = int(input("Back Status lck >>> "))
    total_lck = int(f_lck) + int(b_lck)

    if accessory == 'N' and weapon == 'N' and double_effect == 'N':
        hpDrain = 0
        x = hpDrain * ((total_lck/100) + 1)
        percent_hpDrain = ((x*100) / (x - hpDrain + 100))
        print("hpDrain = %.2f"%(percent_hpDrain),"%")
    
    elif accessory == 'N' and weapon == 'N' and double_effect == 'Y':
        hpDrain = 0
        x = hpDrain * ((total_lck/100) + 1)
        percent_hpDrain = ((x*100) / (x - hpDrain + 100))
        print("hpDrain = %.2f"%(percent_hpDrain),"%")

    elif accessory == 'N' and weapon == 'Y' and double_effect == 'N':
        hpDrain = 12
        x = hpDrain * ((total_lck/100) + 1)
        percent_hpDrain = ((x*100) / (x - hpDrain + 100))
        print("hpDrain = %.2f"%(percent_hpDrain),"%")

    elif accessory == 'N' and weapon == 'Y' and double_effect == 'Y':
        hpDrain = 24
        x = hpDrain * ((total_lck/100) + 1)
        percent_hpDrain = ((x*100) / (x - hpDrain + 100))
        print("hpDrain = %.2f"%(percent_hpDrain),"%")

    elif accessory == 'Y' and weapon == 'N' and double_effect == 'N':
        hpDrain = 8
        x = hpDrain * ((total_lck/100) + 1)
        percent_hpDrain = ((x*100) / (x - hpDrain + 100))
        print("hpDrain = %.2f"%(percent_hpDrain),"%")

    elif accessory == 'Y' and weapon == 'N' and double_effect == 'Y':
        hpDrain = 8
        x = hpDrain * ((total_lck/100) + 1)
        percent_hpDrain = ((x*100) / (x - hpDrain + 100))
        print("hpDrain = %.2f"%(percent_hpDrain),"%")

    elif accessory == 'Y' and weapon == 'Y' and double_effect == 'N':
        hpDrain = 8 + 12
        x = hpDrain * ((total_lck/100) + 1)
        percent_hpDrain = ((x*100) / (x - hpDrain + 100))
        print("hpDrain = %.2f"%(percent_hpDrain),"%")

    elif accessory == 'Y' and weapon == 'Y' and double_effect == 'Y':
        hpDrain = 8 + 24
        x = hpDrain * ((total_lck/100) + 1)
        percent_hpDrain = ((x*100) / (x - hpDrain + 100))
        print("hpDrain = %.2f"%(percent_hpDrain),"%")

elif program == '2':
    effect_percent = int(input("Enter Total Percent of Effect >>> "))
    f_lck = int(input("Front Status lck >>> "))
    b_lck = int(input("Back Status lck >>> "))
    total_lck = int(f_lck) + int(b_lck)
    x = effect_percent * ((total_lck/100) + 1)
    percent_effect = ((x*100) / (x - effect_percent +100))
    print("Effect = %.2f"%(percent_effect),"%")

elif program == '3':
    f_cha = int(input("Front Status cha >>> "))
    b_cha = int(input("Back Status cha >>> "))
    buff_duration = int(input("Enter Buff Duration >>> "))
    total_cha = int(f_cha) + int(b_cha)
    buff_cha = total_cha * 1.5
    buffs = buff_duration + (buff_duration * buff_cha / 100)
    print("Total Duration With cha = %d"%(buffs),"Second")
    print("Time Extended is %d Second"%(buff_duration * buff_cha / 100))

elif program == '4':
    f_agi = int(input("Front Status agi >>> "))
    b_agi = int(input("Back Status agi >>> "))
    ncd = int(input("Cool Down in Game >>> "))
    total_agi = int(f_agi) + int(b_agi)
    decrease_cd = str(input("Have RevisedArt[Decrease Cool Down line C] ? (Yes = Y / No = N) >>> "))

    if decrease_cd == 'N':
        cd = ncd / (1 - (total_agi / (total_agi + 128)))
        print("Original Cool Down is %d Second"%(cd))

    elif decrease_cd == 'Y':
        cd = ncd / ((1 - (total_agi / (total_agi + 128))) * 0.88)
        print("Original Cool Down Without agi is %d Second"%(cd))

elif program == '5':
    f_agi = int(input("Front Status agi >>> "))
    b_agi = int(input("Back Status agi >>> "))
    f_cha = int(input("Front Status cha >>> "))
    b_cha = int(input("Back Status cha >>> "))
    
    buff_duration = int(input("Enter Buff Duration >>> "))
    ncd = int(input("Cool Down in Game >>> "))
    
    total_agi = int(f_agi) + int(b_agi)
    total_cha = int(f_cha) + int(b_cha)
    
    decrease_cd = str(input("Have RevisedArt[Decrease Cool Down line C] ? (Yes = Y / No = N) >>> "))

    if decrease_cd == 'N':
        cd = ncd / (1 - (total_agi / (total_agi + 128)))
        print("Original Cool Down is %d Second"%(cd))

    elif decrease_cd == 'Y':
        cd = ncd / ((1 - (total_agi / (total_agi + 128))) * 0.88)
        print("Original Cool Down Without agi is %d Second"%(cd))

    buff_cha = total_cha * 1.5
    buffs = buff_duration + (buff_duration * buff_cha / 100)
    
    print("Total Duration With cha = %d"%(buffs),"Second")
    print("Time Extended is %d Second"%(buff_duration * buff_cha / 100))

elif program == '6':
    lvl = str(input("Enter Level of TT&CO [1/2] >>> "))
    f_lck = int(input("Front Status lck >>> "))
    b_lck = int(input("Back Status lck >>> "))
    total_lck = int(f_lck) + int(b_lck)
    hpmon = int(input("Enter hp Monster >>> "))
    
    if lvl == '1':
        success_rate = 100 * (total_lck / hpmon)
        
    elif lvl == '2':
        success_rate = 100 * ((total_lck * 2) / hpmon)

    print("Success Rate is %.2f"%(success_rate),"%")

