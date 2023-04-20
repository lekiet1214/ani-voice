import pyaudio
import sounddevice as sd
import soundfile as sf

def play_audio(filename):
    # Initialize PyAudio
    p = pyaudio.PyAudio()

    # Get the ID of the virtual audio device
    device_id = 11
    # for i in range(p.get_device_count()):
    #     info = p.get_device_info_by_index(i)
    #     print(info['name'])
    #     if 'CABLE' in info['name']:
    #         device_id = info['index']
    #         break

    #     if device_id is None:
    #         print("Virtual audio device not found.")
    #         exit()

    # Open the audio file
    data, fs = sf.read(filename, dtype='float32')

    # Get device info
    device_id = None
    device_info = sd.query_devices()
    for i in range(len(device_info)):
        # print(i, device_info[i])
        if 'CABLE Input' in device_info[i]['name']:
            print('Found name')
            if device_info[i]['max_input_channels'] == 0:
                print('Found max_input_channels')
                if device_info[i]['max_output_channels'] == 2:
                    print('Found max_output_channels')
                    if device_info[i]['default_samplerate'] == 44100:
                        print('Found default_samplerate')
                        device_id = device_info[i]['index']
                        print('device_id ', device_id)
                        break

    if device_id is None:
        print("Virtual audio device not found.")
        exit()
    
    # Play the audio file
    try:
        # device_id=15
        sd.play(data, fs, device=device_id)
        status = sd.wait()
    except KeyboardInterrupt:
        sd.stop()
        raise SystemExit('Interrupted by user')
    except Exception as e:
        raise type(e)(str(e))
    
    if status:
        raise RuntimeError('Error during playback: ' + str(status))