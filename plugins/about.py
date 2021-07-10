from pyrogram import Client, Filters


@Client.on_message(Filters.command(["about"]))
async def start(client, message):
    aboutxt = f"A simple youtube downloder bot for downloading your favourite youtube vedios ; if u found any bugs/issues report it to @coderzsupport"
    await message.reply_text(aboutxt)
