import discord
from discord.ext import commands


class moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot  # This is the bot instance, it lets us interact with most things

    @commands.command(help='Kicks the specified member for the specified reason')
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        embed = discord.Embed(color=discord.Color.red())
        embed.set_author(name=str(member), icon_url=member.avatar_url)
        embed.add_field(name=f'**YOU GOT KICKED FROM**', value=f'```{ctx.guild.name}```', inline=False)
        embed.add_field(name=f'**BY**', value=ctx.author.mention, inline=False)
        if reason:
            embed.add_field(name=f'**FOR THE REASON**', value=f'`{reason}`', inline=False)
        try:
            await member.send(embed=embed)
        except discord.Forbidden:
            await ctx.send('Could not send DM to user')
        await member.kick(reason=reason)
        embed.remove_field(0)
        embed.remove_field(0)
        embed.insert_field_at(0, name=f'**GOT KICKED BY**', value=ctx.author.mention, inline=False)
        await ctx.send(embed=embed)
        ctx.message.delete()
        channel = self.bot.fetch_channel(425632491622105088)
        await channel.send(embed=embed)

    @commands.command(help='Bans the specified member for the specified reason')
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        embed = discord.Embed(color=discord.Color.red())
        embed.set_author(name=str(member), icon_url=member.avatar_url)
        embed.add_field(name=f'**YOU GOT BANNED FROM', value=f'```{ctx.guild.name}```', inline=False)
        embed.add_field(name=f'**BY**', value=ctx.author.mention, inline=False)
        if reason:
            embed.add_field(name=f'**FOR THE REASON**', value=f'`{reason}`', inline=False)
        try:
            await member.send(embed=embed)
        except discord.Forbidden:
            await ctx.send('Could not send DM to user')
        await member.ban(reason=reason)
        embed.remove_field(0)
        embed.remove_field(0)
        embed.insert_field_at(0, name=f'**GOT BANNED BY**', value=ctx.author.mention, inline=False)
        await ctx.send(embed=embed)
        await ctx.message.delete()
        channel = self.bot.fetch_channel(425632491622105088)
        await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(moderation(bot))
