from keep_alive import keep_alive
import discord
import os

client = discord.Client()



@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('!ela'):
    await message.channel.send('Here are the answers for ELA on 3/22/21: ***Dragonwings Quiz 2***: 1.box 2.true 3.They look as shells of wood 4.wind rider 5.chainamaan ')
  
  
  if msg.startswith('!about'):
    await message.channel.send('I am a bot that simply helps with homework')
    
  if msg.startswith('!science'):
    await message.channel.send('There is no homework for science today, If there is, but an assignment is not listed, please respond with !missinghomework and the name of the assignment following it.')
    
  if msg.startswith('!missinghomework'):
    await message.channel.send('Thank you for responding with !missinghomework. A moderator will be with you shortly to renew the bot.')

  if msg.startswith('!math'):
    await message.channel.send('Here is the PDF link for todays math homework! https://cdn.discordapp.com/attachments/823574191957213254/823576512220364840/Jason_Ampomah_-_Block_1_Unit_4_Lesson_11.pdf')
  
  if msg.startswith('!ss'):
    await message.channel.send('Here is the answers for Introduction to Hinduism and Buddhism Webquest: https://cdn.discordapp.com/attachments/639963928931336208/823607935186763786/Jason_Aguilar_-_Introduction_to_Hinduism_and_Buddhism_Webquest.pdf , **Remember to paraphrase!**')

  if msg.startswith('!help'):
    await message.channel.send('Hi! I am AnswerBot, a bot that gives answers! Here are all of the commands: !(subject) - Gives the answers of a subject (It changes daily!) !about - Gives more overview to what this bot does! !missinghomework - If there is an assignment that is not listed, use this command! It will ping the bot owners and kindly ask them to update the assignments! And that is all! We want to keep this bot simple!')
 
  if msg.startswith('!credits'):
    await message.channel.send('This bot was made by Jason Ampomah and Jason Aguilar on Repl.it using python code')
    
  if msg.startswith('!report'):
    await message.channel.send('We have recieved your request and will get back with you shortly, please do not report falsely or this will result in a kick. Time span = Now - 1 week, if no moderators get back with you within a week please try again.') 
  
  
keep_alive()
client.run(os.getenv('TOKEN'))