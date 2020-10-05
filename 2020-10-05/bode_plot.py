from scipy import signal
import matplotlib.pyplot as plt

bode = signal.TransferFunction([1], [0.001, 1])

w, mag, phase = signal.bode(bode)

plt.figure()
plt.semilogx(w, mag)
plt.title('Frequency vs. Magnitude')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Magnitude [dB]')

plt.figure()
plt.semilogx(w, phase)
plt.title('Frequency vs. Phase')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Phase [deg]')

plt.show()
