from mtranslate import translate

def translate_text(input, filename):
    # read text
    with open(input, 'r', encoding='utf-8') as f:
        text = f.read()

    # translate text to Japanese
    translation = translate(text, 'ja')

    # write translated text to file
    with open(filename, 'w', encoding='UTF-8') as f:
        f.write(translation)

    print(f"Translated text saved to {filename}")
    print(f"Translated text: {translation}")