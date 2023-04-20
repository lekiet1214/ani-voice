import requests
import json

def audio_query(text, output_file):
    # send a POST request to the Voicevox API endpoint with the text to convert
    response = requests.post(
        'http://localhost:50021/audio_query', params={'text': text, 'speaker': 1})

    # check if the response was successful
    if response.status_code != 200:
        print(f"Error: Voicevox Desktop app returned status code {response.status_code}",
              f"with the following message: {response.text}")
        return

    # save the data to global json variable
    global json_data
    json_data = json.loads(response.text)

    # save json to file
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)