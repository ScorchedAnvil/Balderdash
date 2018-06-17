import os
import atexit
import discord
from discord.ext import commands
import config as c
import random
import asyncio
import math

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
    print('427295582399234048')

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
    print('427295582399234048')
    print('exiting...')


atexit.register(exit_handler)    
