# Function Def'n
# Separate news headlines and its page from its RSS feed

# Header
import sys
sys.path.append(r"C:\Users\Peter\Desktop\IRIS\components\lib")
import header as h

# configure lightbulbs
def config():
    num_lights = None
    lifx = h.LifxLAN(num_lights)
    devices = lifx.get_lights()
    while True:
        try:
            bulb = devices[0]
            bulb_2 = devices[1]
            print("lights configured")
            break

        except IndexError:
            print("Having trouble finding your bulbs, please wait...", end="\r")
            h.time.sleep(1)

# Return indiviual bulb
def bulb():
    num_lights = None
    lifx = h.LifxLAN(num_lights)
    devices = lifx.get_lights()
    bulb_1 = devices[0]
    bulb_2 = devices[1]

    return bulb_1, bulb_2

# Check the status of the lightbulbs, and return 0 for off, 65535 for on
def status(): 
    num_lights = None
    lifx = h.LifxLAN(num_lights)
    devices = lifx.get_lights()
    while True:
        try:
            bulb_1 = devices[0]
            bulb_2 = devices[1]
            break

        except IndexError:
            print("Having trouble finding your bulbs, please wait...", end="\r")
            h.time.sleep(1)

    status1 = bulb_1.get_power()
    status2 = bulb_2.get_power()

    if (status1 == 65535 and status2 == 65535):
        return 1
    else:
        return 0

# Check the status of the bulbs, and return its color as a list of int
def color():
    num_lights = None
    lifx = h.LifxLAN(num_lights)
    devices = lifx.get_lights()
    bulb_1 = devices[0]
    bulb_2 = devices[1]

    status1 = bulb_1.get_color()
    status2 = bulb_2.get_color()

    return status1, status2