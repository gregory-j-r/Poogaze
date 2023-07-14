import audiofile
from scipy.io  import wavfile
import simpleaudio
import matplotlib.pyplot as plt
import numpy as np
sr, data = wavfile.read("AIW.wav")
sr = sr//2
data = data[sr*100:sr*150]

print(data.dtype)
def lowPass(data,B=0.05):
    out = np.empty_like(data)
    out[0]=data[0]
    for i,v in enumerate(data[1:]):
        B = (np.cos(120/4/60/2*4*i/sr)+1)/2*0.8+0.2
        out[i+1] = out[i]*(1-B)+data[i+1]*B

    return out


# lp = lowPass(data)
# print(lp)
# plt.plot(data)
# plt.plot(lp)
# plt.show(block=False)

# wave_obj_og = simpleaudio.WaveObject(data[0:5*sr],sample_rate=sr)
wave_obj = simpleaudio.WaveObject(lowPass(data),sample_rate=sr)
# wave_obj_og.play().wait_done()# plt.plot(lp)
wave_obj.play().wait_done()# plt.plot(lp)

# plt.plot(data)
# plt.show()
