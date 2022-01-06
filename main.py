import discord
import os
import sys
import re
import time
from keep_alive import keep_alive

keep_alive()
client = discord.Client()

global botDisable
botDisable = True

@client.event
async def on_ready():
  channel = client.get_channel(928351060609892363)
  print('Logged in')
  rep = 'Bot started'
  await channel.send(rep)
@client.event
async def on_message(message):
  channel = client.get_channel(928351060609892363)
  global botDisable
  #check if is a bot
  if botDisable == True:
    if message.author.bot:
      return
  #run
  if message.content == '!!!botenable':
    botDisable = False
    await channel.send('Will keep track of bot ping')
  if message.content == '!!!botdisable':
    botDisable = True
    await channel.send('Will not keep track of bot ping')
  elif message.content == '!!!restart':
    rep = 'Restarting!'
    await channel.send(rep)
    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
  #pause bot
  elif message.content == '!!!pause':
    if message.channel.id == 928351060609892363:
      rep = 'Bot paused for 5 minutes'
      await channel.send(rep)
      time.sleep(300)
      os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
  #main func
  elif '<@' in message.content:
    #avoid looping
    if message.channel.id != 928351060609892363:
      #gathering imformation
      author = await client.fetch_user(message.author.id)
      channel_id = '<#' + str(message.channel.id) + '>'
      #processing string (remove mention)
      m = message.content
      i = 0
      if '<@!' in message.content:
        a = re.findall('<@![0-9]+>', m)
        while i < len(a):
            id = a[i][3:len(a[i]) - 1]
            user = await client.fetch_user(int(id))
            u = '*' + str(user) + '*'
            m = m.replace(a[i], str(u))
            i = i + 1
      else:
        a = re.findall('<@[0-9]+>', m)
        while i < len(a):
            id = a[i][2:len(a[i]) - 1]
            user = await client.fetch_user(int(id))
            u = '*' + str(user) + '*'
            m = m.replace(a[i], str(u))
            i = i + 1
    #send message
    rep = '**' + str(author) + " pinged in " + channel_id + '**' + ': ' + m
    await channel.send(rep)
    print(rep)
client.run(os.environ['DISCORD_TOKEN'])