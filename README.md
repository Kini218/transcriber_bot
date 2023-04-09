# Transcriber Bot: Telegram Text-to-Speech and Speech-to-Text Bot

"Transcriber Bot" is a Telegram bot written in Python that can perform Text-to-Speech (TTS) and Speech-to-Text (STT) conversions. The bot uses the `text_to_speech` and `speech_to_text` modules for the conversion and `telebot` library for communication with Telegram API. The `langdetect` module is used to detect the language of the input text.

The Transcriber Bot can be used by sending a text message to perform TTS conversion or by sending an audio message to perform STT conversion. The bot will automatically detect the language of the input text and perform the appropriate conversion. The bot also provides an inline keyboard for the user to select the language for the STT conversion.

This Transcriber Bot can be useful for people who need to convert text to speech or vice versa, such as for language learners or people with speech or hearing disabilities.

## Installation

To use this Transcriber Bot, you need to have Python 3 installed on your machine. You also need to install the required packages using the following command:

```python
pip install -r requirements.txt
```


After installing the required packages, you need to create a bot on Telegram and obtain an API token. You can follow the instructions [here](https://core.telegram.org/bots#creating-a-new-bot) to create a bot and obtain an API token.

Once you have the API token, you can replace the `BOT-API` placeholder in the code with your API token.

## Usage

To use the Transcriber Bot, simply run the `bot.py` script using the following command:

```python
transcriber_bot.py
```


The bot will start listening for incoming messages from the Telegram API. You can then use the bot by sending a text message to perform TTS conversion or by sending an audio message to perform STT conversion. You can also use the `/help` command to see all available commands.

## License

This code is licensed under the [MIT License](https://github.com/username/repo/blob/master/LICENSE). Feel free to use and modify this code for your own purposes.
