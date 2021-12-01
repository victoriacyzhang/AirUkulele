import simpleaudio as sa
from pydub import AudioSegment

m = AudioSegment.from_wav('audios/csound.wav')
m = m + 40
m.export('audios/csound40.wav', 'wav')
