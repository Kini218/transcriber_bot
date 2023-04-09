import os
import speech_recognition as sr
from pydub import AudioSegment


def prepare_voice_file(audio_file_path: str) -> str:
    """
    Converts the input audio file to WAV format if necessary and returns the path to the WAV file.
    """
    ext = os.path.splitext(audio_file_path)[1]
    if ext == '.wav':
        return audio_file_path
    elif ext in ('.mp3', '.m4a', '.ogg', '.flac'):
        audio_file = AudioSegment.from_file(audio_file_path, format=ext[1:])
        wav_file = os.path.splitext(audio_file_path)[0] + '.wav'
        audio_file.export(wav_file, format='wav')
        return wav_file
    else:
        raise ValueError(f'Unsupported audio format: {ext}')


def transcribe_audio(audio_data, language: str) -> str:
    """
    Transcribes audio data to text using Google's speech recognition API.
    """
    recognizer = sr.Recognizer()
    text = recognizer.recognize_google(audio_data, language=language)
    return text


def transcribe_audio_file(audio_file_path: str, language: str) -> str:
    """
    Transcribes an audio file at the given path to text and returns the transcribed text.
    """
    wav_file = prepare_voice_file(audio_file_path)
    with sr.AudioFile(wav_file) as source:
        audio_data = sr.Recognizer().record(source)
        try:
            text = transcribe_audio(audio_data, language)
            return text
        except Exception as e:
            raise Exception(f'Error transcribing audio: {str(e)}')


if __name__ == '__main__':
    print('Please enter the path to an audio file (WAV, MP3, M4A, OGG, or FLAC):')
    audio_file_path = input().strip()
    if not os.path.isfile(audio_file_path):
        print('Error: File not found.')
    else:
        print('Please enter the language code (e.g. en-US):')
        language = input().strip()
        try:
            print('Transcription:')
            print(transcribe_audio_file(audio_file_path, language))
        except Exception as e:
            print('Error:', e)
