from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("JOIN OUR CHANNEL", url="https://t.me/coderzHEX")],
        [InlineKeyboardButton(
            "DEVOLPER", url="https://t.me/maxxcoderz")]
    ])
    welcomed = f"Hello <b>{message.from_user.first_name}</b>\nthis is a simple youtube downloader bot for download your favourite youtube videos\n/help for More info\nyou must subscribe to my channel in order to use me"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
