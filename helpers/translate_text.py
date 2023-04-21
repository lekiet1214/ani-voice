from mtranslate import translate
import json
import sys

def translate_text(input, filename):
    
    try:
        # read text
        with open(input, 'r', encoding='utf-8') as f:
            text = f.read()

        # Read config file
        with open('config.json', 'r') as f:
            config = json.load(f)


        # translate text to Japanese
        translation = translate(text, config['language'])

        # write translated text to file
        with open(filename, 'w', encoding='UTF-8') as f:
            f.write(translation)

        print(f"Translated text saved to {filename}")
        print(f"Translated text: {translation}")
    except Exception as e:
        raise type(e)(str(e))
    
sys.modules[__name__] = translate_text    