import discord
import keep_alive
import os
from discord.ext import commands

print('Merci de patienter...')
print('Merci de patienter...')
print('Merci de patienter...')
print('Merci de patienter...')
print('Merci de patienter...')
print('Merci de patienter...')
print('Merci de patienter...')
print('Merci de patienter...')
print('Merci de patienter...')
print('Merci de patienter...')
print('Merci de patienter...')
print('Merci de patienter...')
print('Merci de patienter...')
print('Merci de patienter...')
print('Merci de patienter...')
print('Merci de patienter...')
print('Merci de patienter...')
print('Merci de patienter...')
print('Merci de patienter...')
print('Merci de patienter...')
print('Merci de patienter...')
print('Merci de patienter...')
print('Merci de patienter...')
print('Merci de patienter...')
print('Merci de patienter...')
print('Merci de patienter...')
print('Merci de patienter...')
print('Merci de patienter...')
print('Merci de patienter...')
print('Merci de patienter...')
print('Merci de patienter...')
print('Merci de patienter...')
print('Merci de patienter...')
print('Merci de patienter...')
print('Merci de patienter...')
print('Merci de patienter...')
print('Merci de patienter...')
print('Merci de patienter...')
print('Merci de patienter...')
print('Merci de patienter...')
print('Merci de patienter...')
print('Merci de patienter...')
print('Merci de patienter...')
print('Merci de patienter...')
print('Merci de patienter...')
print('Merci de patienter...')
print('Merci de patienter...')
print('Merci de patienter...')
class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx, *, channel: discord.VoiceChannel):
        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)
        await channel.connect()

    @commands.command()
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()

bot = commands.Bot(command_prefix=("#"))
@bot.event
async def on_ready():
    print('                                ·▄▄▄▄•▄▄▄ .·▄▄▄▄   ▄▄· ▄▄▄         ▄· ▄▌')
    print('                                ▪▀·.█▌▀▄.▀·██· ██ ▐█ ▌▪▀▄ █· ▄█▀▄ ▐█▪██▌')
    print('                                ▄█▀▀▀•▐▀▀▪▄▐█▪ ▐█▌██ ▄▄▐▀▀▄ ▐█▌.▐▌▐█▌▐█▪')
    print('                                █▌▪▄█▀▐█▄▄▌██. ██ ▐███▌▐█•█▌▐█▌.▐▌ ▐█▀·.')
    print('                               ·▀▀▀ • ▀▀▀ ▀▀▀▀▀• ·▀▀▀ .▀  ▀ ▀█▄▀▪  ▀ • ')
    print('════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════')
    print('Connecté en tant que {0} ton id est ({0.id}) va faire tes heures de voc bg'.format(bot.user))
    print('                               Auto voc | Par ZedCroy <3 | Auteur : ZedCroy#5908')
    print('Pour utiliser ce programme utilise un double compte et fait #join et l id du channel') 
    print('Exemple : #join 000000000000')
    print('════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════')
    
keep_alive.keep_alive()
bot.add_cog(Music(bot))
bot.run(os.getenv("TOKEN"))
