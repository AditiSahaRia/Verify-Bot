import discord

from discord.ext import commands

import gspread 

gc = gspread.service_account(filename='python.json')
sh = gc.open_by_key('1mc1xdSQ5s3GNip_dB80K4icYdjrRHkvyuxL69zDUY2M')
worksheet = sh.sheet1

client = commands.Bot(command_prefix = '$')

TOKEN = 'ODUxODI1NjA0MTkzMjg4MjQy.YL96ag.Iuaxug-PpPCZ-77MvQ3G-xpgPGc'

@client.event
async def on_ready():
    print('Hello!')

@client.command()
async def addrole(ctx, role: discord.Role, user: discord.Member):
    if ctx.author.guild_permissions.administrator:
        await user.add_roles(role)
        await ctx.send(f'Successfully given {role.mention} to {user.mention}.')

@client.command()
async def remove(ctx, role: discord.Role, user: discord.Member):
    if ctx.author.guild_permissions.administrator:
        await user.remove_roles(role)
        await ctx.send(f'Successfully removed {role.mention} from {user.mention}.')


def info(id):
    id_list = worksheet.col_values(1)[1:]
    
    if id in id_list:
        name = worksheet.col_values(2)[1:]
        dept = worksheet.col_values(3)[1:]
        idx = id_list.index(id)
        data = [name[idx], dept[idx]]

    else:
        data = 'Error'
        
    return data

@client.command()
async def id(ctx, message):
    information = info(message)
    if information == 'Error':
        await ctx.send('No data found for this user')  

    else:
        await ctx.send(f'Name: {information[0]} and Department: {information[1]}')

client.run(TOKEN)
