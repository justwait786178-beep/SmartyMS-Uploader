from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)

TOKEN = "8121301262:AAFnv0pxa37IaazAh4gCKNSb6-JjSzafANI"


# ---------------------- VIP COMMAND -------------------------

async def vip(update: Update, context: ContextTypes.DEFAULT_TYPE):

    button = [[
        InlineKeyboardButton("Let's Create Bot Command🚀", url="https://lnk.ink/Txt.Downloader.Command")
    ]]

    text = (
        "*Hello Cutie Pie🌚😘*\n"
        "You Want to Use this Bot and Download Txt to Video Download Fastly?\n\n"
        "Yaar Dekho Truly Batau to ye Possible to nahi hai ki Bot Owner ki Command Change Karke "
        "New Command banaake Mera Use kar pao.\n\n"
        "*But You Can Create a New Command Header [Temporary] and use to me As Your Own Bot.*\n\n"
        "So Uske liye Niche wala Url par Visit karna then Create karna New Command "
        "*(No Need to Bot Token Or authentication)*\n\n"
        "So Tap On Below Button then Create a Costume Command. *(Using Only My Username)*\n\n"
        "For More Details Just Send to me /help Command and explore More."
    )

    await update.message.reply_text(
        text,
        reply_markup=InlineKeyboardMarkup(button),
        parse_mode="HTML"
    )


# ---------------------- VIP ACTION MESSAGE -------------------------

async def actionmsg(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "Go Ahead Baby😘\n"
        "Let's Create a New Costume Command.\n\n"
        "Powered By: @SmartBoy_ApnaMS\n\n"
        "*With Regards💥*\n"
        "Your Cute MS🙃",
        parse_mode="HTML"
    )


# ---------------------- HELP COMMAND (FIXED NAME) -------------------------

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):

    button = [[
        InlineKeyboardButton("Let's Create Bot Command🚀", url="https://lnk.ink/Txt.Downloader.Command")
    ]]

    text = (
        "*Hello Baby🌚😘*\n"
        "How i can Help You.🤔\n\n"
        "Achha Txt se Video Download karne ke liye aik Costume Command Create Karna Chahte ho?\n\n"
        "So Uske liye Jo Below Button Hai *\"Let's Create Bot Command🚀\"*\n\n"
        "Point wise niche dekh lo 👇\n\n"

        "1. Copy My Username. *[Bot Username]*\n"
        '2. Send to me Command "vip".\n'
        "3. Tap Below Button.\n"
        "4. Redirect to Our Website.\n"
        "5. Now Create a Costume Command header.\n"
        "6. For Creating just Type 'Command'\n"
        "   Then Next Line Type 'My Username' *(Replace with My Actual Username)*\n"
        "   Then Next Line Type 'Token'\n"
        '   Then Next Line Type "Value:" And Type "{false}"\n'
        "   Then Type 'ID'\n"
        "   Then Next Line 'Value:' Then Type 'Your User ID' *(Replace it with Your Actual User Id)*\n"
        "   Then Type 'Owner Username'\n"
        "   Then Next Line Type 'Value:' then Type 'False'\n"
        "   Then Type 'Costume Command'\n"
        "   Then Next Line Type 'Command' *(Write Your Actual Bot Command)*\n"
        "   Then Next Line Type 'Command header'\n"
        "   Then Next Line Type 'False'\n"
        "   Then Next Line Type 'logo'\n"
        "   Then Next Line Type 'private'\n"
        "   Then Next Line Type 'Bot Run'\n"
        "   Then Next Line Type 'Main.py'\n"
        "   Then Type 'Run' *(Your Bot Will Be Started With new Costume Commands)*\n\n"

        "7. After all Doing Just Back to Bot.\n"
        "8. Remember username type without '@'\n\n"
        "9. Please try to do it in Chrome Browser Only.\n"
        "10. Don't use the real bot token anywhere.\n"
        "11. For help send /owner\n"
        "12. Thanks For Using Me❤😘"
    )

    await update.message.reply_text(
        text,
        reply_markup=InlineKeyboardMarkup(button),
        parse_mode="Markdown"
    )


# ---------------------- OWNER COMMAND -------------------------

async def owner(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
⧣₊˚﹒✦₊  ⧣₊˚  𓂃★    ⸝⸝ ⧣₊˚﹒✦₊  ⧣₊˚
      /)    /)
    (｡•ㅅ•｡)〝₎₎  <b>Owner Intro!</b> ✦₊ ˊ˗
╭∪─∪────────── ✦ ⁺.
┊ ◟﹫ <b>Name</b> : SmartyMS
┊ 𐐪 <b>Age</b> : 18 Coming...
┊ <b>Pronouns</b> : MS
┊ <b>Sexuality</b> : Male
┊ ◟ヾ <b>Likes</b> : BMW Cars
┊ <b>Dislikes</b> : People Attitude
┊ <b>Tg Name</b> : ᴠ‌ɪ‌ᴘ‌𝗖𝘂𝗧𝗲♡𝗡𝗮𝘄𝗮𝗮𝗯𝗭𝗮𝗱𝗮𓆩♛𓆪
┊ <b>Username</b> : <code>@SmartBoy_ApnaMS</code>
┊ <b>Status</b> : Unmarried
┊ <b>Crush</b> : 1
┊ <b>Ex</b> : Unlimited
┊ <b>Hobby</b> : Helping & Service to People
┊ <b>Condition</b> : Neet Dropper
╰─────────────  ✦ ⁺.
⧣₊˚﹒✦₊  ⧣₊˚  𓂃★    ⸝⸝ ⧣₊˚﹒✦₊  ⧣₊˚
"""

    await update.message.reply_text(text, parse_mode="HTML")


# ---------------------- MAIN APP -------------------------

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("vip", vip))         # FIXED
    app.add_handler(CommandHandler("help", help_cmd))  # FIXED
    app.add_handler(CommandHandler("owner", owner))   # FIXED
    app.add_handler(CommandHandler("actionmsg", actionmsg))  # FIXED

    app.run_polling()


if __name__ == "__main__":
    main()