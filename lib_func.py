 #!/usr/local/bin/python3
# _*_ coding:utf8 _*_

import telepot
import time
from telepot.namedtuple import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup, InlineKeyboardButton
from data_func import html,extract,ma_A,ma_B
bot = telepot.Bot('194233496:AAFTNsUhxGYgb1ij84x0bys3Zhv3CNnE81w')
def lib_keyboard():

	tmp=ReplyKeyboardMarkup(keyboard=
	[
	[KeyboardButton(text='Nearest Lib',request_location=True)],

	[KeyboardButton(text='LWN Lib')],[KeyboardButton(text='BIZ Lib')],[KeyboardButton(text='HSS Lib')],[KeyboardButton(text='CHN Lib')],

	[KeyboardButton(text='ADM Lib')]
	],
	one_time_keyboard=True
	)
	return tmp

def lib_p_keyboard():

	tmp=ReplyKeyboardMarkup(keyboard=
	[
	[KeyboardButton(text='LWN lib')],[KeyboardButton(text='BIZ lib')],[KeyboardButton(text='HSS lib')],[KeyboardButton(text='CHN lib')],

	[KeyboardButton(text='ADM lib')]
	],
	one_time_keyboard=True
	)
	return tmp

def lib_keyboard_select(n):
	
	lwn_lib_keyboard=InlineKeyboardMarkup(inline_keyboard=
		[
		[InlineKeyboardButton(text='5F Quiet Zone',callback_data='lwn')],[InlineKeyboardButton(text='4F',callback_data='lwn')],
		[InlineKeyboardButton(text='3F',callback_data='lwn')],[InlineKeyboardButton(text='2F',callback_data='lwn')],
		]
		)
	hss_lib_keyboard=InlineKeyboardMarkup(inline_keyboard=
		[
		[InlineKeyboardButton(text='Inside',callback_data='hss')],[InlineKeyboardButton(text='Outside',callback_data='hss')],
		]
		)
	biz_lib_keyboard=InlineKeyboardMarkup(inline_keyboard=
		[
		[InlineKeyboardButton(text='B4 Quiet Zone',callback_data='biz')],[InlineKeyboardButton(text='B3',callback_data='biz')],
		[InlineKeyboardButton(text='B2 & B1',callback_data='biz')],
		]
		)
	adm_lib_keyboard=InlineKeyboardMarkup(inline_keyboard=
		[
		[InlineKeyboardButton(text='Section A',callback_data='adm')],[InlineKeyboardButton(text='Section B',callback_data='adm')],
		]
		)
	chn_lib_keyboard=InlineKeyboardMarkup(inline_keyboard=
		[
		[InlineKeyboardButton(text='Section A',callback_data='chn')],[InlineKeyboardButton(text='Section B',callback_data='chn')],
		[InlineKeyboardButton(text='Section C',callback_data='chn')],
		]
		)
	tmp=[lwn_lib_keyboard,hss_lib_keyboard,biz_lib_keyboard,adm_lib_keyboard,chn_lib_keyboard]
	return tmp[n]

def lib_p_keyboard_select(n):
	
	lwn_lib_keyboard=InlineKeyboardMarkup(inline_keyboard=
		[
		[InlineKeyboardButton(text='5F Quite Zone',callback_data='lwnp')],[InlineKeyboardButton(text='4F',callback_data='lwnp')],
		[InlineKeyboardButton(text='3F',callback_data='lwnp')],[InlineKeyboardButton(text='2F',callback_data='lwnp')],
		]
		)
	hss_lib_keyboard=InlineKeyboardMarkup(inline_keyboard=
		[
		[InlineKeyboardButton(text='Inside',callback_data='hssp')],[InlineKeyboardButton(text='Outside',callback_data='hssp')],
		]
		)
	biz_lib_keyboard=InlineKeyboardMarkup(inline_keyboard=
		[
		[InlineKeyboardButton(text='B4 Quiet Zone',callback_data='bizp')],[InlineKeyboardButton(text='B3',callback_data='bizp')],
		[InlineKeyboardButton(text='B2 & B1',callback_data='bizp')],
		]
		)
	adm_lib_keyboard=InlineKeyboardMarkup(inline_keyboard=
		[
		[InlineKeyboardButton(text='Section A',callback_data='admp')],[InlineKeyboardButton(text='Section B',callback_data='admp')],
		]
		)
	chn_lib_keyboard=InlineKeyboardMarkup(inline_keyboard=
		[
		[InlineKeyboardButton(text='Section A',callback_data='chnp')],[InlineKeyboardButton(text='Section B',callback_data='chnp')],
		[InlineKeyboardButton(text='Section C',callback_data='chnp')],
		]
		)
	tmp=[lwn_lib_keyboard,hss_lib_keyboard,biz_lib_keyboard,adm_lib_keyboard,chn_lib_keyboard]
	return tmp[n]	

def welcome_keyboard():
	tmp=ReplyKeyboardMarkup(keyboard=
	[
	[KeyboardButton(text='Library Current Status Inquiry')],

	[KeyboardButton(text='Library Status Prediction')]
	],
	one_time_keyboard=True
	)
	return tmp

def nearest_lib(x,y): 
	dis=0
	n=0
	if (pow(x-1.347757,2)+pow(y-103.680900,2) < dis):
		dis = pow(x-1.347757,2)+pow(y-103.680900,2)
		n=0
	if (pow(x-1.344308,2)+pow(y-103.682256,2) < dis):
		dis = pow(x-1.344308,2)+pow(y-103.682256,2)
		n=1
	if (pow(x-1.346526,2)+pow(y-103.680051,2) < dis):
		dis = pow(x-1.346526,2)+pow(y-103.680051,2)
		n=2
	if (pow(x-1.349541,2)+pow(y-103.683809,2) < dis):
		dis = pow(x-1.349541,2)+pow(y-103.683809,2)
		n=3
	if (pow(x-1.343871,2)+pow(y-103.682369,2) < dis):
		dis = pow(x-1.343871,2)+pow(y-103.682369,2)
		n=4
	return n

def lib_close(chat_id):
	t=time.localtime()
	# t=time.strptime('Sun Sep 28 18:31:30 2016','%a %b %d %H:%M:%S %Y')
	if t.tm_wday==6:
		bot.sendMessage(chat_id,"It's Sunday dude, all libraries are closed.\nGo relax and have fun!\nヽ(✿ﾟ▽ﾟ)ノ")
		return 1
	elif 0<=t.tm_hour<=8:
		bot.sendMessage(chat_id,"So hard-working dude! Libraries are not opened yet.\n╮(′～‵〞)╭")
		return 1
	elif t.tm_wday==5: 
		if t.tm_hour >= 17 :
			bot.sendMessage(chat_id,"Oops, all libraries have closed.\n( ˘･з･)")
			return 1
	elif t.tm_hour >= 21:
			bot.sendMessage(chat_id,"Oops, all libraries have closed.\n( ˘･з･)")
			return 1
	return 0	
	

def lib_status(lib_name):
	seats = [50,50]
	num = html()[lib_name]
	empty = seats[lib_name]-num
	if empty < 10:
		return 'There are only '+str(empty)+' seats available, quite crowded...'
	else:
		return 'There are '+str(empty)+" seats available, lots of space!"

if __name__ == '__main__':
	lib_close(123123123123123)


