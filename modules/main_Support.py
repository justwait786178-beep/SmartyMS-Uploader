from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)

TOKEN = "8110308118:AAF1U-U21lwirApefibAD2ZfWJWxFxvwsiU"

# ---------------------- VIP COMMAND -------------------------
async def vip(update: Update, context: ContextTypes.DEFAULT_TYPE):

    button = [[
        InlineKeyboardButton("Let's Create Bot Command🚀", url="https://lnk.ink/Txt.Downloader.Command")
    ]]

    text = (
        " *Hello Cutie Pie🌚😘* \n"
        "You Want to Use this Bot and Download Txt to Video Download Fastly?\n\n"
        "Yaar Dekho Truly Batau to ye Possible to nahi hai ki Bot Owner ki Command Change Karke "
        "New Command banaake Mera Use kar pao.\n\n"
        "*But You Can Create a New Command Header [Temporary] and use to me As Your Own Bot.*\n\n"
        "So Uske liye Niche wala Url par Visit karna then Create karna New Command "
        "*(No Need to Bot Token Or authentication)*\n\n"
        "So Tap On Below Button then Create a Costume Command. *(Using Only My Username)*\n\n"
        "For More Details Just Send to me /Help Command and explore More."
    )

    await update.message.reply_text(
        text,
        reply_markup=InlineKeyboardMarkup(button),
        parse_mode="Markdown"
    )


# When button clicked → show this message in chat (no callback needed)
async def vip_action_msg(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Go Ahead Baby😘\n"
        "Let's Create a New Costume Command.\n\n"
        "Powered By: @SmartBoy_ApnaMS\n\n"
        "*With Regards💥*\n"
        "Your Cute MS🙃",
        parse_mode="Markdown"
    )


# ---------------------- HELP COMMAND -------------------------
async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):

    button = [[
        InlineKeyboardButton("Let's Create Bot Command🚀", url="https://lnk.ink/Txt.Downloader.Command")
    ]]

    text = (
        "*Hello Baby🌚😘*\n"
        "How i can Help You.🤔\n\n"
        "Achha Txt se Video Download karne ke liye aik Costume Command Create Karna Chahte ho?\n\n"
        'So Uske liye Jo Below Button Hai *"Let\'s Create Bot Command🚀"*\n\n'
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
        "   For Ex: Suppose my Username is '@Vipuploader_bot'\n"
        "   Then You must paste only 'Vipuploader_bot' NOT '@Vipuploader_bot'\n\n"
        "9. Please try to do it in Chrome Browser Only.\n"
        "10. Remember Bot Policy: If you are owner of This Bot, Don't use the real Bot Token anywhere.\n"
        "11. If you Face Any Problem, Contact My Bot Owner—Just Send '/Owner'.\n"
        "12. Thanks For Using Me❤😘"
    )

    await update.message.reply_text(
        text,
        reply_markup=InlineKeyboardMarkup(button),
        parse_mode="Markdown"
    )


# ---------------------- OWNER COMMAND -------------------------
async def owner(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = (
        "⧣₊˚﹒✦₊  ⧣₊˚  𓂃★    ⸝⸝ ⧣₊˚﹒✦₊  ⧣₊˚\n"
        "      /)    /)\n"
        "    (｡•ㅅ•｡)〝₎₎ *Owner Intro!* ✦₊ ˊ˗   \n"
        ". .╭∪─∪────────── ✦ ⁺.\n"
        ". .┊ ◟﹫ *Name* : SmartyMS\n"
        ". .┊﹒𐐪 *Age* : 18 Coming...\n"
        ". .┊ꜝꜝ﹒*Pronouns* : MS\n"
        ". .┊ ⨳゛*Sexuality* : Male\n"
        ". .┊ ◟ヾ *Likes* : BMW Cars\n"
        ". .┊﹒𐐪 *Dislikes* : People Attitude\n"
        ". .┊ ◟£ *Tg Name*: ᴠ‌ɪ‌ᴘ‌𝗖𝘂𝗧𝗲♡𝗡𝗮𝘄𝗮𝗮𝗯𝗭𝗮𝗱𝗮𓆩♛𓆪\n"
        ". .┊ ◟﹫ *username* : @SmartBoy_ApnaMS\n"
        ". .┊﹒𐐪 *Status* : Unmarried\n"
        ". .┊ꜝꜝ﹒*Crush* : 1\n"
        ". .┊ ⨳゛*Ex* : Unlimited\n"
        ". .┊ ◟ヾ *Hobby* : Helping & Service to People.\n"
        ". .┊﹒𐐪 *Condition* : Neet Dropper\n"
        "   ╰─────────────  ✦ ⁺.\n"
        "⧣₊˚﹒✦₊  ⧣₊˚  𓂃★    ⸝⸝ ⧣₊˚﹒✦₊  ⧣₊˚"
    )

    await update.message.reply_text(text, parse_mode="Markdown")


# ---------------------- MAIN APP -------------------------
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("vip", vip))
    app.add_handler(CommandHandler("actionmsg", vip_action_msg))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("owner", owner))

    app.run_polling()


if __name__ == "__main__":
    main()