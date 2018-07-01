import os
import atexit
import discord
from discord.ext import commands
import config as c
import random
import asyncio
import math

STARTUP_EXTENSIONS = [
					  'cogs.nonsense'
                      ]

bot = commands.Bot(command_prefix=c.prefix, description=c.description, pm_help=True)

@bot.event
async def on_ready():
    """ Returns true if bot is ready.
    """
    clear = lambda: os.system('cls')
    clear()
    print('-' * len(bot.user.id))
    print('Logged in as:')
    print(bot.user.name)
    print(bot.user.id)
    print(' ')
    print('Bot currently running on {} servers:'.format(len(bot.servers)))
    for s in bot.servers:
        print(' - ' + s.name + ' :: ' + s.id)
    print('-' * len(bot.user.id))
    print(' ')

    await bot.change_presence(game=discord.Game(name=c.game))

    file = open('config.py', 'r')
    cont = file.read()
    if 'token' not in cont:
        file = open('config.py', 'w')
        file.write('# merlin.py config \ntoken = \'\'')
    else:
        file.close()

@bot.command()
async def initiate(extension_name: str):
    """ Loads an extension.
        >load <extension_name>
    """
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as exopt:
        await bot.say('```py\n{}: {}\n```'.format(type(exopt).__name__, str(exopt)))
        return
    await bot.say('I have rerouted the EME to include {}.'.format(extension_name))


@bot.command()
async def drain(extension_name: str):
    """ Unloads an extension.
        >unload <extension_name>
    """
    bot.unload_extension(extension_name)
    await bot.say('I have rerouted the EME away from {}.'.format(extension_name))


@bot.command()
async def reload(extension_name: str):
    """ Loads an extension.
        >reload <extension_name>
    """
    try:
        bot.unload_extension(extension_name)
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as exopt:
        await bot.say('```py\n{}: {}\n```'.format(type(exopt).__name__, str(exopt)))
        return
    await bot.say('I have rerouted the EME to send an extra surge to {}.'.format(extension_name))

@bot.event
async def on_message(message):
    """ It is always morning in Cuba.
    """
    if any(word in message.content for word in c.cuba):
        chance = random.randint(1, 1000)
        if chance <= 533:
            await bot.send_message(message.channel, 'Except it is always morning in Cuba.')
            c.cuba_count += 1

if __name__ == '__main__':
    for extension in STARTUP_EXTENSIONS:
        try:
            bot.load_extension(extension)
        except Exception as exopt:
            exc = '{}: {}'.format(type(exopt).__name__, exopt)
            print('The EME is not responding to {}\n{}'.format(extension, exc))

    bot.run(c.token)


def exit_handler():
    """ What to do on exit.
    """
    print(' ')
    print('exiting...')


atexit.register(exit_handler)    
