from keep_alive import keep_alive
import discord
import os

client = client = discord.Client()


@client.event
async def on_ready():
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name="New answers every day!"))
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('!ela'):
    embed=discord.Embed(title='Answers', description = "Here are the answers for  Dragonwings quiz 3 and 4: https://cdn.discordapp.com/attachments/826462226511560734/830928266713890886/Dragonwings_quiz_3_and_4.txt", color=0xff6961)
    await message.channel.send(embed=embed)
  
  
  if msg.startswith('!about'):
    embed=discord.Embed(title='About this bot.', description='Hi, I am a bot that will give you answers for your homework! I have many commands! To see them say !commands.', color=0xaec6cf)
    await message.channel.send(embed=embed)
    
  if msg.startswith('!science'):
    embed=discord.Embed(title='Science', description="Here is the answers for Science: https://cdn.discordapp.com/attachments/826462226511560734/827193723484897310/science_answerse.txt (posted by Imprinxa)", color=0xff808b)
    await message.channel.send(embed=embed)
    
  if msg.startswith('!missinghomework'):
    embed=discord.Embed(title='Thank you!', description='Thank you for reporting this to us. <@494607399618084864> , <@504243679377227797> , please update the assignments!', color=0xf7e948)
    await message.channel.send(embed=embed)

  if msg.startswith('!math'):
    embed=discord.Embed(title='Math', description='Here are the answers for the math homework: https://cdn.discordapp.com/attachments/826462226511560734/831216097482637352/Jason_Ampomah_-_Block_1_Solving_more_ratio_problems_Day_2.pdf' , color=0x89CFF0)
    await message.channel.send(embed=embed)
  
  if msg.startswith('!ss'):
    embed=discord.Embed(title='Error.', description="Answers for social studies cannot be posted due to it needing a unique answer. Sorry :P! If this is untrue, use !missinghomework", color=0x9932CC)
    await message.channel.send(embed=embed)

  if msg.startswith('!help'):
    embed=discord.Embed(title="Help", description="Hi! I am AnswerBot, a bot that gives answers! Here are all of the commands: !(subject) - Gives the answers of a subject (It changes daily!) !about - Gives more overview to what this bot does! !missinghomework - If there is an assignment that is not listed, use this command! It will ping the bot owners and kindly ask them to update the assignments! And that is all! We want to keep this bot simple!", color=0x9932CC)
    await message.channel.send(embed=embed)
 
  if msg.startswith('!credits'):
    embed=discord.Embed(title="Credits", description="This bot was made by Jason Ampomah and Jason Aguilar on Repl.it using <:python:823900279313006653> ", color=0xFFFF00)
    await message.channel.send(embed=embed)

  

  if msg.startswith('!support'):
    embed=discord.Embed(title='Support', description="You can support the devs by subscribing to <@494607399618084864> s <:youtube:823900279631118337> YouTube channel at https://youtube.com/c/Splode1", color=	0x0000FF)
    await message.channel.send(embed=embed)

  if msg.startswith('!commands'):
    embed=discord.Embed(title='Commands', description="Here are all of my commands:\n!ela - Gives the answer to the current ELA assignment\n!math - Gives the answer to the current Math assignment\n!ss - Gives the current Social Studies assignment answers\n!science - Gives the answer to the current science assignment\n!about - Gives a brief overview on what this bot does\n!help - Similar to !about\n!report - Reports a user\n!support - Support the creators of this bot.\n !apply - apply for a work poster position. ", color=0xFF5733)
    await message.channel.send(embed=embed)

  if msg.startswith("!usercount"):
    embed=discord.Embed(title='User Count', description='Here is the User Count for this server:\n19 people total\n5 bots\n14 Students\n4 Admins\n1 AnswerBot (that is me! :D)', color=0xFDFD96)
    await message.channel.send(embed=embed)
  
  if msg.startswith('like bruh we got lives we arent robots'):
    embed=discord.Embed(title='uh', description='**cough** **cough**', color=0xFDFD96)
    await message.channel.send(embed=embed)

  if msg.startswith('dog water'):
    embed=discord.Embed(title='uh', description='i am right here.', color=0xFDFD96)
    await message.channel.send(embed=embed)

  if msg.startswith('sped bot'):
    embed=discord.Embed(title='uh', description='i am right here.', color=0xFDFD96)
    await message.channel.send(embed=embed)

  if msg.startswith('dumb bot'):
    embed=discord.Embed(title='uh', description='i am right here.', color=0xFDFD96)
    await message.channel.send(embed=embed)

  if msg.startswith('stupid bot'):
    embed=discord.Embed(title='uh', description='i am right here.', color=0xFDFD96)
    await message.channel.send(embed=embed)
    
  if msg.startswith('!apply'):
    embed=discord.Embed(title="Thank you!", description="A moderator will contact you if you get the position.", color=0xFDFD96)
    await message.channel.send (embed=embed)
keep_alive()
client.run(os.getenv('TOKEN'))