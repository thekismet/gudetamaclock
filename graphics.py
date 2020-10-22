import time
from weather import *

year = int(time.strftime('%Y'))
weekday = int(time.strftime('%w'))
day = str(time.strftime('%m%d'))
hour = int(time.strftime('%H'))
weatherid = wid()

def graphics_path():

	if hour == 1:
		graphicspath = "/home/pi/clock/gudetamaclock/graphics/sleepingbaby_white_back.png"
	elif hour == 2:
		graphicspath = "/home/pi/clock/gudetamaclock/graphics/sleepingbaby_white_back.png"
	elif hour == 3:
		graphicspath = "/home/pi/clock/gudetamaclock/graphics/sleepingbaby_white_back.png"
	elif hour >= 4 and hour <= 6:
		graphicspath = "/home/pi/clock/gudetamaclock/graphics/sleepingbaby_white_back.png"
	elif hour == 7:
		graphicspath = "/home/pi/clock/gudetamaclock/graphics/sleepingbaby_white_back.png"
	elif hour == 8:
		graphicspath = "/home/pi/clock/gudetamaclock/graphics/goodmorning_white_back.png"
	elif hour == 9:
		graphicspath = "/home/pi/clock/gudetamaclock/graphics/mohana_white_back.png"
	elif hour == 10:
		graphicspath = "/home/pi/clock/gudetamaclock/graphics/elsa2_white_back.png"
	elif hour == 11:
		graphicspath = "/home/pi/clock/gudetamaclock/graphics/rapunzel7_white_back.png"
	elif hour == 12:
		graphicspath = "/home/pi/clock/gudetamaclock/graphics/mary_white_back.png"
	elif hour == 13:
		graphicspath = "/home/pi/clock/gudetamaclock/graphics/rapunzel_white_back.png"
	elif hour == 14:
		graphicspath = "/home/pi/clock/gudetamaclock/graphics/rapunzel5_white_back.png"
	elif hour == 15:
		graphicspath = "/home/pi/clock/gudetamaclock/graphics/elsa5_white_back.png"
	elif hour == 16:
		graphicspath = "/home/pi/clock/gudetamaclock/graphics/mulan_white_back.png"
	elif hour == 17:
		graphicspath = "/home/pi/clock/gudetamaclock/graphics/bell3_white_back.png"
	elif hour == 18:
		graphicspath = "/home/pi/clock/gudetamaclock/graphics/ana2_white_back.png"
	elif hour == 19:
		graphicspath = "/home/pi/clock/gudetamaclock/graphics/rapunzel4_white_back.png"
	elif hour == 20:
		graphicspath = "/home/pi/clock/gudetamaclock/graphics/beauty_beast_red_back.png"
	elif hour == 21:
		graphicspath = "/home/pi/clock/gudetamaclock/graphics/bed_white_back.png"
	elif hour == 22:
		graphicspath = "/home/pi/clock/gudetamaclock/graphics/sleeping_princess_white_back.png"
	elif hour == 23:
		graphicspath = "/home/pi/clock/gudetamaclock/graphics/sleeping_princess_white_back.png"	

	else:
		graphicspath = "/home/pi/clock/gudetamaclock/graphics/whitesnow_white_back.png"

# Weekday

	if weekday == 5 and hour > 14 and hour <= 17:
		graphicspath = "/home/pi/clock/gudetamaclock/graphics/super_white_back.png"
	else:
		graphicspath = graphicspath
	
# Weathers	
	# snow
	if weatherid >= 600 and weatherid <= 622:
		graphicspath = "/home/pi/clock/gudetamaclock/graphics/snow_white_back.png"
	# rain
	elif weatherid == 504 or weatherid == 522:
		graphicspath = "/home/pi/clock/gudetamaclock/graphics/rainy_white_back.png"
	else:
		graphicspath = graphicspath
	
# Special days

	if day == '0101':
		graphicspath = "/home/pi/clock/gudetamaclock/graphics/rapunzel6_white_back.png"
	elif day == '0214':
		graphicspath = "/home/pi/clock/gudetamaclock/graphics/heart3_white_back.png"
	elif day == '0301':
		graphicspath = "/home/pi/clock/gudetamaclockgraphics/flag_white_back.png"
	elif day == '0815':
		graphicspath = "/home/pi/clock/gudetamaclock/graphics/flag_white_back.png"
	elif day == '1225':
		graphicspath = "/home/pi/clock/gudetamaclock/graphics/xmas_white_back.png"
	elif day == '0103':
		graphicspath = "/home/pi/clock/gudetamaclock/graphics/happybirthday5_white_back.png"
	elif day == '0814':
		graphicspath = "/home/pi/clock/gudetamaclock/graphics/happybirthday_white_back.png"
	elif day == '0912':
		graphicspath = "/home/pi/clock/gudetamaclock/graphics/happybirthday3_white_back.png"
	elif day == '0622':
		graphicspath = "/home/pi/clock/gudetamaclock/graphics/happyanniversary2_white_back.png"
	else:
		graphicspath = graphicspath
	
	return graphicspath
