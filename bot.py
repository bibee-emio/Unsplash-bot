import os
import requests
from config import (
    API_ID,
    API_HASH,
    BOT_TOKEN,
    UNSPLASH_ACCESS_KEY
)
from pyrogram import Client,filters,types


access_key = UNSPLASH_ACCESS_KEY  
api = 'https://api.unsplash.com/photos?client_id={}'
random_photos = 'https://api.unsplash.com/photos/random/?count={}&client_id={}'
search_photos = 'https://api.unsplash.com/search/photos/?query={}&client_id={}'




# Checking whether Unsplash-Access-key is valid.If not, Quitting...
if isinstance(d:=requests.get(api.format(access_key)).json(),dict) and bool(d['errors']):
    print(f"\033[0;31m{d['errors'][0]}\n\nQuitting...\033[0m")
    exit(0)

Bot = Client('unsplash-bot',API_ID,API_HASH,bot_token=BOT_TOKEN)



privateStart = '''
Hey {},

You can get any photo from Unsplash ,which is the most powerful High Resolution Free Photo search engine, as your desire.
'''


helpText = '''
--Welcome to Help Menu--

• /start
- Start the bot.

• /ping
- Returns __Pong__.

• /photo | /image | /search     `< Query >`
- Search photos on Unsplash.

• /random | /rand
- Get random photos from Unsplash.
'''
#     `(Count must be a Integer.Specifying the query is not important)`



privateButton = types.InlineKeyboardMarkup(
    [
        [
            types.InlineKeyboardButton('Repo',url='https://github.com/bibee-emio/Unsplash-bot'),
            types.InlineKeyboardButton('Help','help-cb')
        ]
    ]
)


# Ping
@Bot.on_message(filters.command(['ping'],['/','!']))
async def botPing(c,msg: types.Message):
    await msg.reply('Pong.')



# Start the bot
@Bot.on_message(filters.command(['start','help'],['/','!']))
async def botStart(c: Client,msg: types.Message):
    if msg.chat.id < 0:
        bot = await c.get_me()
        await msg.reply_photo(
            './unsplash-welcome.jpg',
            caption='Pm me for know the Usage.',
            reply_markup=types.InlineKeyboardMarkup(
                [
                    [types.InlineKeyboardButton('Private Messsage',url=f't.me/{bot.username}')]
                ]
            )
        )
    else:
        await msg.reply_photo(
            photo='./unsplash-welcome.jpg',
            caption=privateStart.format(msg.from_user.mention),
            reply_markup=privateButton
        )







# Search Photos on Unsplash
@Bot.on_message(filters.command(['photo','search','image','img'],['/','!']))
async def searchPhoto(c,msg: types.Message):
    if len(msg.command) == 1:
        await msg.reply('__Please specify the query.__')
        return

    q = '+'.join(msg.command[1:])
    #print(q)
    re = await msg.reply('__Searching...__')

    results = requests.get(search_photos.format(q,access_key)).json()['results']
    #print(results)

    if not results:
        await re.edit('__No photo for your query.Try with deferent keywords.__')
        return


    with open(n:=f"{results[0]['id']}.jpg",'wb') as img:
        img.write(requests.get(results[0]['urls']['raw']).content)
    
    cap = results[0]['alt_description']

    await msg.reply_photo(n,caption=(f'__{cap}__' if isinstance(cap,str) else ""))
    await re.delete()
    os.remove(n)
 #   ml = []
  #  fl = []



#    for _ in range(len(results)):                     
 #       with open(n:=f"{results[_]['id']}.jpg",'wb') as img:
  #          img.write(requests.get(results[_]['urls']['full']).content)                  
   #         ml.append(types.InputMediaPhoto(n))
    #        fl.append(n)
        


    #await msg.reply_media_group(ml)
    
    #await re.delete()
    #for photo in fl:
     #   os.remove(photo)
        




# Get random photos from Unsplash
@Bot.on_message(filters.command(['random','rand'],['/','!']))
async def randomPhoto(c,msg: types.Message):
    if len(msg.command) == 1:
        count = 1
    elif len(msg.command) > 2:
        await msg.reply('__Only 1 parameter or none required.But {} were given.__'.format(len(msg.command)-1))
        return
    else:
        try:
            count = int(msg.command[1])
        except ValueError:
            await msg.reply('__[ValueError]: Only integer can accept.__')
            return


    re = await msg.reply('__Getting a random photo...__')
    results = requests.get(random_photos.format(count,access_key)).json()
    
    if not results:                                     # I think this three lines are not need...
        await re.edit('__Nothing Found.__')             # But just in case :)
        return




    with open(n:=f"{results[0]['id']}.jpg",'wb') as img:
        img.write(requests.get(results[0]['urls']['raw']).content)
    
    cap = results[0]['alt_description']

    await msg.reply_photo(n,caption=(f'__{cap}__' if isinstance(cap,str) else ""))
    await re.delete()
    os.remove(n)
    #ml = []
    #fl = []


#    for _ in range(len(results)):
 #       with open(n:=f"{results[_]['id']}.jpg",'wb') as img:
  #          img.write(requests.get(results[_]['urls']['raw']).content)
   #         ml.append(types.InputMediaPhoto(n))
    #        fl.append(n)

    #await msg.reply_media_group(ml)

    #await re.delete()
    #for photo in fl:
    #    os.remove(photo)




# Help CallBack
@Bot.on_callback_query(filters.regex('help-cb'))
async def help_cb(c,query: types.CallbackQuery):
    await query.message.edit(
        helpText,
        reply_markup=types.InlineKeyboardMarkup(
            [
                [
                    types.InlineKeyboardButton('‹ Back','back-cb')
                ]
            ]
        )
    )


# Back CallBack
@Bot.on_callback_query(filters.regex('back-cb'))
async def back_cb(c,q: types.CallbackQuery):
    await q.message.edit(
        privateStart.format(q.from_user.mention),
        reply_markup=privateButton
    )







print('\033[32mBot has booted.')
Bot.run()
print('\nBot has stoped.\033[0m')
