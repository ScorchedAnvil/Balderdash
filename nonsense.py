""" Nonsense """
import random
import asyncio
import config as c

# unused import discord
from discord.ext import commands

class Nonsense:
    """ Nonsensical Things """

    def __init__(self, bot):
        self.bot = bot

@commands.command(pass_context=True)
    async def exorcise(self, ctx):
        """ Casts out the spirits in Relics.
            >exorcise
        """
        userid = ctx.message.author.id
        if userid == c.owner_id:
            await self.bot.say('*Goodbye.*')
            await self.bot.logout()
        else:
            resp = ['*No effect*',
                    'Did you say something?']
            srandom = random.SystemRandom()
            await self.bot.say(srandom.choice(resp))

    @commands.command(pass_context=True)
    async def poke(self, ctx):
        #Poke the specified User
        """ If you truly must...
            >poke <@user> :message
        """
        mcont = ctx.message.content
        if mcont == c.prefix + 'poke':
            #If the User trys to Poke without a target.
            resp = ['*You broke the fourth wall!*',
                    '*You have broken your finger by poking a wall*',
                    '*You poke the amalgous data of cyberspace*']
            srandom = random.SystemRandom()
            await self.bot.say(srandom.choice(resp))
        elif mcont == c.prefix + 'poke <@' + self.bot.user.id + '>':
            #If the User tries to Poke the bot.
            resp = ['*dodges*',
                    '*sidesteps*',
                    '*pokes ' + ctx.message.author.name + '*',
                    'Poking. How undignified',
                    'Excuse me?']
            srandom = random.SystemRandom()
            await self.bot.say(srandom.choice(resp))
            await self.bot.delete_message(ctx.message)
        else:
            #If the User pokes another user.
            await self.bot.say('*' + ctx.message.author.name +
                               ' poked' + mcont.replace(c.prefix + 'poke', '*'))
            await self.bot.delete_message(ctx.message)

    @commands.command(pass_context=True)
    async def hug(self, ctx):
        #Hug the specified user.
        """ <3
            >hug <@user>
        """
        mcont = ctx.message.content
        userid = ctx.message.author.id
        if mcont <= c.prefix + 'hug':
            #If the user trys to hug without a target.
            await self.bot.say('*' + ctx.message.author.name + ' tries to hug the air*')
            await self.bot.say('*AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA*')
            await self.bot.delete_message(ctx.message)
        elif mcont == c.prefix + 'hug <@' + self.bot.user.id + '>':
            #If the User tries to hug the bot.
            await self.bot.say(' Euh... you are hugging *me*? ' + 'I- I am quite flattered *o.o*')
            await self.bot.delete_message(ctx.message)
        elif mcont == c.prefix + 'hug <@' + userid + '>':
            #If the User tries to hug themselves.
            await self.bot.say(' Euh... you hug yourself. You know who you are. Good job. ')
            await self.bot.delete_message(ctx.message)
        elif mcont == c.prefix + 'hug the air':
            #If the User tries to hug the air.
            await self.bot.say('Yes yes, very clever')
            await self.bot.delete_message(ctx.message)
        else:
            #If the User tries to hug another user.
            await self.bot.say(ctx.message.author.name + ' hugged' + mcont.replace(c.prefix + 'hug', '') + ' :hearts:')
            await self.bot.delete_message(ctx.message)

    @commands.command(pass_context=True)
    async def void(self, ctx):
        #The function that send messages to the void.
        """ Scream if you like. No one will hear you.
            >void <message>
        """
        mcont = ctx.message.content
        void = self.bot.get_channel('PUT CHANNEL HERE')
        if mcont <= c.prefix + 'void':
            #If the User tries to talk to the Void without a message.
            cont = '*' + ctx.message.author.name + ' silently screams into the void* \n *AAAAAAAAAAAAAAAAAAAAAAAAAA*'
            await self.bot.send_message(destination=void, content=cont)
            await self.bot.say("*Message sent to the void*")
            await self.bot.delete_message(ctx.message)
        else:
            #If the User tries to send a message to the Void.
            cont = '*' + ctx.message.author.name + ' screams, \"' + mcont.replace(c.prefix + 'void', '') + ',\" into the void*'
            await self.bot.send_message(destination=void, content=cont)
            await self.bot.say("*Message sent to the void*")
            await self.bot.delete_message(ctx.message)

def setup(bot):
    """ defines setup """
    bot.add_cog(Nonsense(bot))
