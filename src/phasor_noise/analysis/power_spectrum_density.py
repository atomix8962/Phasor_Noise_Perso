import numpy as np

'''
PSD.py
--> The Power Spectral Density PSD is defined by :
P = |x̂(f)|² with x̂ the Fourier Transform of the Signal

PSD(signal) return the Power Spectral Density of a signal

plotPSD(X,Y,signal,ax) plot the Power Spectral Density on a 3D axis

'''


def PSD(signal: list) -> np.array:
    f = np.fft.fft2(signal)
    f_s = np.fft.fftshift(f)
    resp = np.power(np.absolute(f_s), 2)
    return -resp
