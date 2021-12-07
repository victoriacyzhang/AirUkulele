import simpleaudio as sa
from pydub import AudioSegment

singles = ['audios/singles/c_single.wav','audios/singles/csharp_single.wav','audios/singles/d_single.wav','audios/singles/dsharp_single.wav','audios/singles/e_single.wav','audios/singles/f_single.wav','audios/singles/fsharp_single.wav','audios/singles/g_single.wav','audios/singles/gsharp_single.wav','audios/singles/a_single.wav','audios/singles/asharp_single.wav','audios/singles/b_single.wav','audios/singles/c5_single.wav']
singles_40 = ['audios/singles/c_single_40.wav','audios/singles/csharp_single_40.wav','audios/singles/d_single_40.wav','audios/singles/dsharp_single_40.wav','audios/singles/e_single_40.wav','audios/singles/f_single_40.wav','audios/singles/fsharp_single_40.wav','audios/singles/g_single_40.wav','audios/singles/gsharp_single_40.wav','audios/singles/a_single_40.wav','audios/singles/asharp_single_40.wav','audios/singles/b_single_40.wav','audios/singles/c5_single_40.wav']
majors = ['audios/majorchords/cmajor.wav', 'audios/majorchords/csharpmajor.wav', 'audios/majorchords/dmajor.wav', 'audios/majorchords/dsharpmajor.wav', 'audios/majorchords/emajor.wav', 'audios/majorchords/fmajor.wav', 'audios/majorchords/fsharpmajor.wav', 'audios/majorchords/gmajor.wav', 'audios/majorchords/gsharpmajor.wav', 'audios/majorchords/amajor.wav', 'audios/majorchords/asharpmajor.wav', 'audios/majorchords/bmajor.wav', 'audios/majorchords/c5major.wav']
majors_40 = ['audios/majorchords/cmajor_40.wav', 'audios/majorchords/csharpmajor_40.wav', 'audios/majorchords/dmajor_40.wav', 'audios/majorchords/dsharpmajor_40.wav', 'audios/majorchords/emajor_40.wav', 'audios/majorchords/fmajor_40.wav', 'audios/majorchords/fsharpmajor_40.wav', 'audios/majorchords/gmajor_40.wav', 'audios/majorchords/gsharpmajor_40.wav', 'audios/majorchords/amajor_40.wav', 'audios/majorchords/asharpmajor_40.wav', 'audios/majorchords/bmajor_40.wav', 'audios/majorchords/c5major_40.wav']
for i in range(len(singles)):
    m = AudioSegment.from_wav(singles[i])
    m = m + 20
    m.export(singles_40[i], 'wav')

    l = AudioSegment.from_wav(majors[i])
    l = l + 20
    l.export(majors_40[i], 'wav')
