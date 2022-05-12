# Lib of possible user inputs

def yes(text):
    a = ['yes', 'sure', 'sure thing', 'ok', 'okay', 'roger that', 'yes please',
         'good', 'perfect', 'fact', 'yeah', 'yup', 'yas', 'uh huh']  # can add as many as you want

    text = text.lower()  # convert to all lower case

    # Check is the users command include a wake phrase
    for phrase in a:
        if phrase in text:
            return True

    return False  

def no(text):
    a = ['no', 'nope', 'nah', 'it is fine', 'its fine']  # can add as many as you want

    text = text.lower()  # convert to all lower case

    # Check is the users command include a wake phrase
    for phrase in a:
        if phrase in text:
            return True

    return False 

def thank(text):
    a = ['thank you', 'thanks', 'great', 'appreciate it',
        'much appreciated']

    for phrase in a:
        if phrase in text:
            return True

    return False

def good(text):
    a = ['good to go', 'good', 'it looks good', 'its fine', 'great', 'looks great', 'it is']
    
    for phrase in a:
        if phrase in text:
            return True

    return False

def open(text):
    a = ['open', 'lets see', 'see', 'pop it up', 'get it up', 'get it', 'bring it up', 'op', 'en']  # can add as many as you want

    text = text.lower()  # convert to all lower case

    # Check is the users command include a wake phrase
    for phrase in a:
        if phrase in text:
            return True

    return False 

def wake_word(text):
    WAKE_WORDS = ['iris', 'harris', 'virus', 'hey', 'irish', 'you there?', 'youre there']  # can add as many as you want

    text = text.lower()  # convert to all lower case

    # Check is the users command include a wake phrase
    for phrase in WAKE_WORDS:
        if phrase in text:
            return True

    return False  

def power_off(text):
    Off_WORDS = ['shutdown', 'power off']  # can add as many as you want

    text = text.lower()  # convert to all lower case

    # Check is the users command include a wake phrase
    for phrase in Off_WORDS:
        if phrase in text:
            return True

    return False  


def music(text):
    Off_WORDS = ['music', 'get me some music']  # can add as many as you want

    text = text.lower()  # convert to all lower case

    # Check is the users command include a wake phrase
    for phrase in Off_WORDS:
        if phrase in text:
            return True

    return False   


def music_genre(text):
    morning = [ 'morning',  'quiet morning',  'morning one', 'quiet']
    jazz = ['jazz', 'jazzy']

    text = text.lower()

    # 1 for morning
    for phrase in morning:
        if phrase in text:
            return 1
    
    # 2 for jazz
    for phrase in jazz:
        if phrase in text:
            return 2

    return False

def music_artist(text):
    tom = ['tom misch', 'tom', 'tom mesh']

    text = text.lower()

    # 1 for Tom Misch
    for phrase in tom:
        if phrase in text:
            return 1

    return False

def light_switch(text):
    on = ['lights on', 'im home', 'lights', 'hey buddy', 'on', 'turn on']
    off = ['lights off', 'im going out', 'lights out', 'off', 'turn off']

    text = text.lower()

    # 1 for ON
    for phrase in on:
        if phrase in text:
            return 1
    
    # 2 for OFF
    for phrase in off:
        if phrase in text:
            return 2

    return False

def light_level(text):
    bright = ['turn it up', 'up', 'brighter', 'higher', 'too dark', 'dark', 'it is too dark', 'cant see anything', 'cant see', 'cannot see']
    dim = ['turn it down', 'dim it', 'dim', 'down', 'lower', 'low', 'too', 'too bright', 'it is too bright', 'its too bright'
            'so bright', "it's too bright"]
    
    text = text.lower()

    # 1 for brighter
    for phrase in bright:
            if phrase in text:
                return 1
        
    # 2 for dimming
    for phrase in dim:
        if phrase in text:
            return 2

    return False


def light_types(text):
    house = ['house lights', 'house', 'home', 'home lights']
    reading = ['reading', 'reading lights', 'study']
    mellow = ['jazz', 'mellow', 'purple', 'dark']
    excit = ['party', 'red', 'exiting']

    text = text.lower()

    # 1 for house light
    for phrase in house:
            if phrase in text:
                return 1
    
    # 2 for reading light
    for phrase in reading:
            if phrase in text:
                return 2
    
    # 3 for mellow light
    for phrase in mellow:
            if phrase in text:
                return 3

    # 4 for excit light
    for phrase in excit:
            if phrase in text:
                return 4
    #...add more

    return False

def check_events(text):
    events = ['what do i have', 'do i have', 'check my calendar', 
            'calendar', 'on my calendar', 'appointment']
   
    text = text.lower()

    # 1 for house light
    for phrase in events:
            if phrase in text:
                return True
    
    return False

def proj(text):
    proj = ['open new project', 'new project', 'create a new project for me', 
            'lets write some codes', 'lets write some']
   
    text = text.lower()

    # 1 for house light
    for phrase in proj:
            if phrase in text:
                return True
    
    return False