import discord
import os
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
async def on_message_delete(message):
    if(message.mentions):
        rep = '**' + message.author.name + '** ghost pinged **'
        for i in message.mentions:
            rep += str(i) + '#' + i.discriminator + ' '
        rep += '**in <#' + str(message.channel.id) + '>: ' + message.content
        channel = client.get_channel(928351060609892363)
        await channel.send(rep)
    if(message.reference):
      id = message.reference.message_id
      ctx = await message.channel.fetch_message(id)
      rep = '**' + message.author.name + '** ghost pinged (replied) ' + '<@' + str(ctx.author.id) + '>' + ' in <#' + str(message.channel.id) + '>: ' + message.content
      channel = client.get_channel(928351060609892363)
      await channel.send(rep)
client.run(os.environ['DISCORD_TOKEN'])