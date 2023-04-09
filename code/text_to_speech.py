from gtts import gTTS
import gtts.lang


def fix_pdfplumber_issue(text_with_unicode: str) -> str:
    """
    Replace unicode character 312 with the letter 'к' in the input text.
    Also remove any newline characters from the text.
    """
    text = text_with_unicode.replace(chr(312), 'к')
    text = text.replace('\n', '')
    return text


def is_valid_language(lang: str) -> bool:
    """
    Check if the given language code is a valid language code
    for the gTTS library.
    """
    return lang in gtts.lang.tts_langs()


def convert_text_to_mp3(input_text: str, lang='en') -> None:
    """
    Convert the given input text to an MP3 file using the gTTS library.
    The language can be specified using a two-letter language code (e.g. 'en').
    """
    if not is_valid_language(lang):
        return

    # Convert text to desired format
    converted_text = fix_pdfplumber_issue(input_text)

    # Get voice and save it in file with the same filename
    tts = gTTS(converted_text, lang=lang)
    tts.save('files/text_to_speech.ogg')


if __name__ == '__main__':
    print('[*]Input text')
    input_text = input()
    print('[*]Input language')
    lang = input()
    convert_text_to_mp3(input_text, lang)
    print(f"[*]File was saved successfully as 'files/text_to_speech.ogg'")
