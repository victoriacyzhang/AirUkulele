import simpleaudio as sa
from pydub import AudioSegment

singles = ['audios/singles/c_single.wav','audios/singles/csharp_single.wav','audios/singles/d_single.wav','audios/singles/dsharp_single.wav','audios/singles/e_single.wav','audios/singles/f_single.wav','audios/singles/fsharp_single.wav','audios/singles/g_single.wav','audios/singles/gsharp_single.wav','audios/singles/a_single.wav','audios/singles/asharp_single.wav','audios/singles/b_single.wav','audios/singles/c5_single.wav']
singles_40 = ['audios/singles/c_single_40.wav','audios/singles/csharp_single_40.wav','audios/singles/d_single_40.wav','audios/singles/dsharp_single_40.wav','audios/singles/e_single_40.wav','audios/singles/f_single_40.wav','audios/singles/fsharp_single_40.wav','audios/singles/g_single_40.wav','audios/singles/gsharp_single_40.wav','audios/singles/a_single_40.wav','audios/singles/asharp_single_40.wav','audios/singles/b_single_40.wav','audios/singles/c5_single_40.wav']
for i in range(len(singles)):
    m = AudioSegment.from_wav(singles[i])
    m = m + 20
    m.export(singles_40[i], 'wav')
