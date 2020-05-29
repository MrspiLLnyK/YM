import os
from pytube import YouTube
import telebot
import ffmpeg

bot = telebot.TeleBot('1081392460:AAERkn4dxDytKngDcC1M_wGdxa_D_Rgte_E')

@bot.message_handler(commands=['start'])
def download(message):
    try:
        bot.send_message(message.chat.id, text="Погнали")
        global new_name
        print(message.text[7:])
        yt = YouTube(message.text[7:])
        yt.streams.first().download()

        old_name = yt.streams.first().default_filename
        new_name = old_name[:-4] + '.mp3'

        stream = ffmpeg.input(old_name)
        stream = ffmpeg.output(stream, new_name)
        ffmpeg.run(stream)
        os.remove(old_name)
        bot.send_message(message.chat.id, "Готово")
    except Exception as e:
        bot.send_message(message.chat.id, text=e)

@bot.message_handler(commands=['2'])
def send(message):
    try:
        bot.send_message(message.chat.id, text="Погнали")
        file = open(new_name, 'rb')
        bot.send_audio(message.chat.id, file)
        file.close()
        os.remove(new_name)
    except Exception as e:
        bot.send_message(message.chat.id, text=e)


if __name__ == "__main__":
    bot.polling(none_stop=True)