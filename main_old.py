import pydub
import os
from pydub.playback import play
import simpleaudio as sa

CDIR = os.getcwd()

# Load the audio file
wave_obj = sa.WaveObject.from_wave_file(f"{CDIR}/sound/run.wav")

# Play the audio file
play_obj = wave_obj.play()
play_obj.wait_done()



# # Load the audio file
# sound = pydub.AudioSegment.from_file(f"{CDIR}/sound/greet3.wav", format="wav")

# # Play the audio file
# play(sound)