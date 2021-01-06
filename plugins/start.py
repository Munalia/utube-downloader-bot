from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Owner👦", url="https://t.me/KumarSwamiKS")],
        [InlineKeyboardButton(
            "📷Movie Channel", url="https://t.me/MovieMess")]
    ])
    welcomed = f"Hi, <b>{message.from_user.first_name}</b>.\nThis is <b>YouTube Uploader Bot.</b>"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
