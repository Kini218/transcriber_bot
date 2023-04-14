from text_to_speech import convert_text_to_mp3
from speech_to_text import transcribe_audio_file
import telebot
from langdetect import detect

bot = telebot.TeleBot('BOT-API')


def start_text():
    return 'Welcome to our Text-to-Speech and Speech-to-Text Bot! This bot can convert text to speech and speech to text. To convert text to speech, just send a message with the text you want to convert. To convert speech to text, send an audio message or a voice note. Use the command /help if you forget something.'


def help_messsage():
    return 'Just send text message to convert it in audio file or record a voice message to convert it in text.'


def create_languages_keyboard():
    languages = {
        'English': 'en',
        'Russian': 'ru',
        'German': 'de',
        'French': 'fr',
        'Spanish': 'es'
    }

    keyboard = telebot.types.InlineKeyboardMarkup()
    for language, lang_code in languages.items():
        button = telebot.types.InlineKeyboardButton(
            text=language, callback_data=lang_code)
        keyboard.add(button)

    return keyboard


def handle_text_message(message):
    language_code = detect(message.text)
    convert_text_to_mp3(message.text, language_code)

    with open('files/text_to_speech.ogg', 'rb') as f:
        bot.send_voice(message.chat.id, f)


def handle_voice_message(message):
    try:
        file_id = message.voice.file_id
        file_info = bot.get_file(file_id)
        file_path = file_info.file_path

        downloaded_file = bot.download_file(file_path)

        with open('files/speech_to_text.ogg', 'wb') as f:
            f.write(downloaded_file)

        keyboard = create_languages_keyboard()
        message = bot.send_message(
            message.chat.id, "Please choose a language:", reply_markup=keyboard)

    except Exception as e:
        bot.reply_to(message, f"An error occurred: {e}")


def handle_language_selection(callback_query):
    lang_code = callback_query.data
    text = transcribe_audio_file('files/speech_to_text.ogg', lang_code)
    bot.send_message(callback_query.message.chat.id, text)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, start_text())


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, help_messsage())


@bot.message_handler(func=lambda message: message.text)
def handle_text(message):
    handle_text_message(message)


@bot.message_handler(content_types=['voice'])
def handle_voice(message):
    handle_voice_message(message)


@bot.callback_query_handler(func=lambda call: True)
def handle_language_selection_callback(callback_query):
    handle_language_selection(callback_query)


bot.infinity_polling()
