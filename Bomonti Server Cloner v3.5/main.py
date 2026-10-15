import discord
from discord.ext import commands
import asyncio
import fade
import os
import sys

# Discord API standartlarına uygun tam yetkilendirme (Intents)
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

LOGO = """
██████╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ ██████╗ 
██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗
██║  ██║██║███████╗██║     ██║   ██║██████╔╝██║  ██║
██║  ██║██║╚════██║██║     ██║   ██║██╔══██╗██║  ██║
██████╔╝██║███████║╚██████╗╚██████╔╝██║  ██║██████╔╝
╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ 
         🔮 DISCORD SERVER CLONER OPEN-SOURCE v3.5 🔮
         👑 Developer: Bomonti Automation 👑
"""

@bot.event
async def on_ready():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(fade.purplepink(LOGO))
    print(f"📊 [BAŞARILI] Bot '{bot.user.name}' adıyla Discord ağına bağlandı!")
    print("=====================================================================")
    print("📢 TALİMAT: Kopyalamayı başlatmak için boş sunucunuzda şu komutu yazın:")
    print("👉  !kopyala [HEDEF_SUNUCU_ID]")
    print("=====================================================================\n")

@bot.command()
@commands.has_permissions(administrator=True)
async def kopyala(ctx, target_guild_id: int):
    # Discord API kuralları çerçevesinde botun erişebildiği sunucu şablonunu çekiyoruz
    source_guild = bot.get_guild(target_guild_id)
    current_guild = ctx.guild
    
    if not source_guild:
        await ctx.send("❌ [HATA] Belirttiğiniz ID'ye sahip sunucu bulunamadı! Botun o sunucuda da ekli olması gerekir.")
        return

    await ctx.send(f"🔄 **{source_guild.name}** sunucusunun mimarisi kopyalanıyor... Lütfen bekleyin.")
    print(f"🎨 [KOPYALAMA BAŞLADI] {source_guild.name} -> {current_guild.name}")

    print("🗑️ Eski kanallar temizleniyor...")
    for channel in current_guild.channels:
        try: await channel.delete()
        except: pass

    print("👑 Rol haritası kopyalanıyor...")
    for role in reversed(source_guild.roles):
        if role.is_default(): continue
        try:
            await current_guild.create_role(
                name=role.name,
                permissions=role.permissions,
                color=role.color,
                hoist=role.hoist,
                mentionable=role.mentionable
            )
            print(f"✅ Rol Olusturuldu: {role.name}")
        except: pass

    print("📂 Kategori ve kanallar inşa ediliyor...")
    for category in source_guild.categories:
        new_category = await current_guild.create_category(name=category.name)
        
        for channel in category.channels:
            if isinstance(channel, discord.TextChannel):
                await current_guild.create_text_channel(name=channel.name, category=new_category)
            elif isinstance(channel, discord.VoiceChannel):
                await current_guild.create_voice_channel(name=channel.name, category=new_category)
            await asyncio.sleep(0.5)

    for channel in source_guild.channels:
        if channel.category is None:
            if isinstance(channel, discord.TextChannel):
                await current_guild.create_text_channel(name=channel.name)
            elif isinstance(channel, discord.VoiceChannel):
                await current_guild.create_voice_channel(name=channel.name)

    await current_guild.text_channels.send("🎉 **MUAZZAM! Sunucu tamamen ve başarıyla kopyalandı!**")
    print("🎉 [TAMAMLANDI] Sunucu kopyalama işlemi başarıyla bitti!")

# Gerçek aktif token kodun içerisine kilitlendi
TOKEN = "BURAYA_DISCORD_BOT_TOKEN_GELECEK"


if __name__ == "__main__":
    try:
        bot.run(TOKEN)
    except Exception as e:
        print(fade.purplepink(LOGO))
        print(f"🛑 [BAĞLANTI HATASI] {e}")
        input()
