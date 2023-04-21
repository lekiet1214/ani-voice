from helpers import audio_query, synthesis
import sys

def text_to_voice(text_translated, filename, data):

    try:
        # read text
        with open(text_translated, 'r', encoding='utf-8') as f:
            text = f.read()

        # send a POST request to the Voicevox API endpoint with the text to convert
        audio_query(text, data)

        # send a POST request to the Voicevox API endpoint with the parameters
        synthesis(filename, data)
    except Exception as e:
        raise type(e)(str(e))
    
sys.modules[__name__] = text_to_voice