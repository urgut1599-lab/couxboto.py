import telebot, io
from PIL import Image, ImageDraw, ImageFont

bot = telebot.TeleBot("xxxx")

@bot.message_handler(commands=['start'])
def s(m):
    bot.send_message(m.chat.id, "👋Salom!\nMatn kiriting:")

@bot.message_handler(func=lambda m: True)
def t(m):
    i = Image.new("RGB", (1240,1754), "white")
    d = ImageDraw.Draw(i)
    f = ImageFont.truetype("arial.ttf", 40)
    y = 100
    for line in m.text.split("\n"):
        d.text((100, y), line, font=f, fill="black")
        y += 60
    b = io.BytesIO()
    i.save(b, "PNG")
    b.seek(0)
    bot.send_photo(m.chat.id, b)
    bot.send_message(m.chat.id, "✅ Tayyor.")

bot.infinity_polling()
