import audio_query
import synthesis

def text_to_voice(text_translated, filename, data):
    # read text
    with open(text_translated, 'r', encoding='utf-8') as f:
        text = f.read()

    # send a POST request to the Voicevox API endpoint with the text to convert
    audio_query.audio_query(text, data)

    # send a POST request to the Voicevox API endpoint with the parameters
    synthesis.synthesis(filename, data)