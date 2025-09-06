
import numpy as np
import matplotlib.pyplot as plt

from signal_ICT_Mit_chodvadiya_92400133088 import Trigonometric_signal as ts
from signal_ICT_Mit_chodvadiya_92400133088 import unitary_signal as us
from signal_ICT_Mit_chodvadiya_92400133088 import operations as op

# 1. Unit Step Signal
n = np.arange(0, 20)
step_signal = us.unit_step(n)
plt.figure()
plt.stem(n, step_signal)
plt.title("Unit Step Signal")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid(True)

# 2. Unit Impulse Signal
impulse_signal = us.unit_impulse(n)
plt.figure()
plt.stem(n, impulse_signal)
plt.title("Unit Impulse Signal")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid(True)

# 3. Sine Wave
t = np.linspace(0, 1, 1000)
sine_signal = ts.sine_wave(A=2, f=5, phi=0, t=t)
plt.figure()
plt.plot(t, sine_signal)
plt.title("Sine Wave: A=2, f=5Hz")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)

# 4. Time-shifted Sine Wave (+5 units)
shifted_sine = op.time_shift(sine_signal, k=5)  # shift implemented as index shift
plt.figure()
plt.plot(t, sine_signal, label="Original")
plt.plot(t, shifted_sine, label="Shifted (+5 units)")
plt.title("Time Shift of Sine Wave")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)

# 5. Addition of Unit Step and Ramp
ramp_signal = us.ramp_signal(n)
added_signal = op.signal_addition(step_signal, ramp_signal)
plt.figure()
plt.stem(n, added_signal)
plt.title("Addition of Unit Step and Ramp Signal")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid(True)

# 6. Multiplication of Sine and Cosine
cosine_signal = ts.cosine_wave(A=2, f=5, phi=0, t=t)
multiplied_signal = op.signal_multiplication(sine_signal, cosine_signal)
plt.figure()
plt.plot(t, multiplied_signal)
plt.title("Multiplication of Sine and Cosine Waves")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
