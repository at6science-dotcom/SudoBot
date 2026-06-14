import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="?sudo ", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.command()
async def ping(ctx):
    await ctx.send("SudoBot online.")


@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason="No reason provided"):
    await member.ban(reason=reason)
    await ctx.send(f"🛑 Banned {member} | Reason: {reason}")


@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason="No reason provided"):
    await member.kick(reason=reason)
    await ctx.send(f"👢 Kicked {member} | Reason: {reason}")


RULES = {
    "1A": "Be respectful to all members.",
    "1B": "No spam.",
    "2A": "No harassment."
}


@bot.command()
async def ruleref(ctx, code: str):
    rule = RULES.get(code.upper())
    if rule:
        await ctx.send(f"📜 Rule {code.upper()}: {rule}")
    else:
        await ctx.send("Rule not found.")


bot.run(os.getenv("TOKEN"))
