from pynput.keyboard import Key, Listener
from pynput import keyboard

# quas: 1
# wex: 10
# exort: 100
STARTING_CD = 7

current_cd = STARTING_CD
last_three = [100, 100, 100]
current_spells = [None, None]

LEVEL_QUAS = {keyboard.Key.ctrl, ('q')}
LEVEL_WEX = {keyboard.Key.ctrl, ('w')}
LEVEL_EXORT = {keyboard.Key.ctrl, ('e')}


cooldowns = {"cold_snap": 20, "ghost_walk": 35, "ice_wall": 25, "emp": 30, "tornado" : 30}
spells_enum = {3 : "cold_snap", 12: "ghost_walk", 102: "ice_wall", 30: "emp", 21: "tornado",120: "alacrity", 300: "sun_strike", 210: "meatball", 201: "forge_spirits", 111: "deafening_blast"}

def invoke(): 
    invoke_score = sum(last_three)
    target = spells_enum[invoke_score]
    # print(target, invoke_score)
    if current_spells[0] != target:
        current_spells[1] = current_spells[0]
        current_spells[0] = target

def orb(orb):
    last_three[2] = last_three[1]
    last_three[1] = last_three[0]
    last_three[0] = orb

current = set()
def on_press(key):

    try:
        if key.char in LEVEL_QUAS:
            current.add(key)
            if all(k in current for k in LEVEL_EXORT):
                current_cd = current_cd - 0.3
                return
        if key.char in LEVEL_WEX:
            current.add(key)
            if all(k in current for k in LEVEL_EXORT):
                current_cd = current_cd - 0.3  
                return
        if key.char in LEVEL_EXORT:
            current.add(key)
            if all(k in current for k in LEVEL_EXORT):
                current_cd = current_cd - 0.3  
                return     

        if key.char == ('r'):
            invoke()
        elif key.char == ('q'):
            orb(1)
        elif key.char == ('w'):
            orb(10)
        elif key.char == ('e'):
            orb(100)
        
    except Exception as e:
        if key in LEVEL_QUAS:
            current.add(key)
            if all(k in current for k in LEVEL_EXORT):
                current_cd = current_cd - 0.3
                return
        if key in LEVEL_WEX:
            current.add(key)
            if all(k in current for k in LEVEL_EXORT):
                current_cd = current_cd - 0.3  
                return
        if key in LEVEL_EXORT:
            current.add(key)
            if all(k in current for k in LEVEL_EXORT):
                current_cd = current_cd - 0.3  
                return
        if key == Key.esc:
            return False
    print(last_three, current_spells, current_cd)

current = set()
def on_release(key):
    pass
    
# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()