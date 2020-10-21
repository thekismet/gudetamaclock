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
	# extream rain
	if weatherid >= 502 and weatherid <= 504:
		graphicspath = "/home/pi/clock/gudetamaclock/graphics/mary_white_back.png"
	# heavy snow
	elif weatherid == 602 or weatherid == 622:
		graphicspath = "/home/pi/clock/gudetamaclock/graphics/snow_white_back.png"
	# cloud
	elif weatherid == 804:
		graphicspath = "/home/pi/clock/gudetamaclock/graphics/aurora.png"
	else:
		graphicspath = graphicspath
	
# Special days

	if day == '0101':
		graphicspath = "/home/pi/clock/gudetamaclock/graphics/rapunzel6_white_back.png"
	elif day == '0214':
		graphicspath = "/home/pi/clock/gudetamaclock/graphics/whitesnow_white_back.png"
	elif day == '0405' and year == 2021:
		graphicspath = "/home/pi/clock/gudetamaclockgraphics/tinkerbell_white_back.png"
	elif day == '0418' and year == 2022:
		graphicspath = "/home/pi/clock/gudetamaclock/graphics/tinkerbell_white_back.png"
	elif day == '0410' and year == 2023:
		graphicspath = "/home/pi/clock/gudetamaclock/graphics/tinkerbell_white_back.png"
	elif day == '1031' and hour > 12 and hour <= 14:
		graphicspath = "/home/pi/clock/gudetamaclock/graphics/snowman_white_back.png"
	elif day == '1031' and hour > 14 and hour <= 16:
		graphicspath = "/home/pi/clock/gudetamaclock/graphics/snowman_white_back.png"
	elif day == '1031' and hour > 16 and hour <= 18:
		graphicspath = "/home/pi/clock/gudetamaclock/graphics/cinderella_full_white_back.png"
	elif day == '1031' and hour > 18 and hour <= 20:
		graphicspath = "/home/pi/clock/gudetamaclock/graphics/cinderella_full_white_back.png"
	elif day == '1031' and hour > 20:
		graphicspath = "/home/pi/clock/gudetamaclock/graphics/jcinderella_full_white_back.png"
	elif day == '1225':
		graphicspath = "/home/pi/clock/gudetamaclock/graphics/xmas_white_back.png"
	elif day == '0912':
		graphicspath = "/home/pi/clock/gudetamaclock/graphics/pumpkin_white_back.png"
	else:
		graphicspath = graphicspath
	
	return graphicspath
