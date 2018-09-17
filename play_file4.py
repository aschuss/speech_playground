# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 12:12:30 2018

@author: paschu
"""

WAVE_OUTPUT_FILENAME = "file.wav"

def int_or_str(text):
    """Helper function for argument parsing."""
    try:
        return int(text)
    except ValueError:
        return text

#parser = argparse.ArgumentParser(description=__doc__)
#parser.add_argument('filename', help='audio file to be played back')
#parser.add_argument('-d', '--device', type=int_or_str,
 #                   help='output device (numeric ID or substring)')
#args = parser.parse_args()
try:
    import sounddevice as sd
    import soundfile as sf
    import librosa
    data, fs = sf.read(WAVE_OUTPUT_FILENAME, dtype='float32')
    sd.play(data, fs)
    status = sd.wait()
    print("shifting up a major 3rd")
    y_shift = librosa.effects.pitch_shift(data, fs, 7)
    sd.play(y_shift, fs)
    status = sd.wait()
    y_slow = librosa.effects.time_stretch(data, 0.5)
    print("playing stretch")
    sd.play(y_slow, fs)
    status = sd.wait()

except:
    print("Unexpected error:")
    
    
    
    