#!/usr/local/bin/python3
# _*_ coding:utf8 _*_

import telepot
import telepot.aio
import time
import math
import time
import asyncio
from lib_func import lib_keyboard,lib_keyboard_select,nearest_lib,lib_close,lib_status,welcome_keyboard,lib_p_keyboard,lib_p_keyboard_select
from data_func import html,extract,ma_A,ma_B



lib=['LWN Lib','HSS Lib','BIZ Lib','ADM Lib','CHN Lib']
lib_p=['LWN lib','HSS lib','BIZ lib','ADM lib','CHN lib']

async def on_chat_message(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)
	print(content_type, chat_type, chat_id)

	if lib_close(chat_id):
			return

	if content_type=='text':
		
		if msg['text']=='Library Current Status Inquiry':
			# await asyncio.sleep(10)
			await bot.sendMessage(chat_id, 'Please Choose Your Library', reply_markup=lib_keyboard())

		elif msg['text']=='Library Status Prediction':
		  	await bot.sendMessage(chat_id, 'Where do you want to go?', reply_markup=lib_p_keyboard())

		elif msg['text'] in lib:
			n=lib.index(msg['text'])
			await bot.sendMessage(chat_id, 'Please Choose Your Floor and Section', reply_markup=lib_keyboard_select(n))

		elif msg['text'] in lib_p:
			n=lib_p.index(msg['text'])
			await bot.sendMessage(chat_id, 'Please Choose Your Floor and Section', reply_markup=lib_p_keyboard_select(n))

		else:
			await bot.sendMessage(chat_id, 'Welcome to NTU library assistant,\nwhat can I do for you?', reply_markup=welcome_keyboard())

	if content_type=='location':
		n=nearest_lib(msg['location']['latitude'],msg['location']['longitude'])
		print(n)
		await bot.sendMessage(chat_id, 'The nearest lib is '+lib[n]+'rary.'+'\nChoose your destination', reply_markup=lib_keyboard_select(n))


async def on_callback_query(msg):
	query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
	print('Callback Query:', query_id, from_id, query_data)
	await bot.answerCallbackQuery(query_id, text='Got it, just a moment...')
	if len(query_data)==3:
		if query_data=='lwn':
			await bot.sendMessage(from_id,text=lib_status(0))
		elif query_data=='hss':
			await bot.sendMessage(from_id,text=lib_status(0))
		elif query_data=='biz':
			await bot.sendMessage(from_id,text=lib_status(0))
		elif query_data=='adm':
			await bot.sendMessage(from_id,text=lib_status(1))
		elif query_data=='chn':
			await bot.sendMessage(from_id,text=lib_status(1))
	else:
		if query_data=='lwnp':
			await bot.sendMessage(from_id,text='In the next hour, there may be around %d people in the selected area.' % ma_A(12)) 
		elif query_data=='hssp':
			await bot.sendMessage(from_id,text='In the next hour, there may be around %d people in the selected area.' % ma_A(12)) 
		elif query_data=='bizp':
			await bot.sendMessage(from_id,text='In the next hour, there may be around %d people in the selected area.' % ma_A(12)) 
		elif query_data=='admp':
			await bot.sendMessage(from_id,text='In the next hour, there may be around %d people in the selected area.' % ma_B(12)) 
		elif query_data=='chnp':
			await bot.sendMessage(from_id,text='In the next hour, there may be around %d people in the selected area.' % ma_B(12)) 
async def database_update():
	while True:
		await html()
		await asyncio.sleep(300)

bot = telepot.aio.Bot('194233496:AAFTNsUhxGYgb1ij84x0bys3Zhv3CNnE81w')
loop=asyncio.get_event_loop()
tasks=[bot.message_loop({'chat':on_chat_message,'callback_query':on_callback_query}),database_update()]
loop.create_task(asyncio.wait(tasks))

print ('Listening ...')
loop.run_forever()



# my id 121898056