class WelcomeMessage(commands.Cog):
    """Welcome Message"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(member: discord.Member):
        if member.guild.id != 777720307334512670:
            return
        embed = discord.Embed(
            title="Welcome",
            description="Welcome description",
            timestamp=datetime.utcnow(),
            color=discord.Colour.random(),
    )
        await bot.get_channel(777720307540295718).send(embed=embed)

def setup(bot):
    bot.add_cog(WelcomeMessage(bot))
