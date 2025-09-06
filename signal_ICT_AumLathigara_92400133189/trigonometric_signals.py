import numpy as np
import matplotlib.pyplot as plt

# Function to generate and plot a sine wave
def sine_wave(A, f, phi, t):
    signal = A * np.sin(2 * np.pi * f * t + phi)  # Sine wave formula
    # Plot sine wave
    plt.plot(t, signal)
    plt.title("SINE WAVE")
    plt.xlabel(" -TIME- ")
    plt.ylabel("AMPLITUDE")
    plt.grid()
    plt.show()
    return signal

# Function to generate and plot a cosine wave
def cosine_wave(A, f, phi, t):
    signal = A * np.cos(2 * np.pi * f * t + phi)  # Cosine wave formula
    # Plot cosine wave
    plt.plot(t, signal)
    plt.title("COSINE WAVE")
    plt.xlabel("--TIME")
    plt.ylabel("AMPLITUDE")
    plt.grid()
    plt.show()
    return signal

# Function to generate and plot an exponential signal
def exponential_signal(A, a, t):
    signal = A * np.exp(a * t)  # Exponential signal formula
    # Plot exponential signal
    plt.plot(t, signal)
    plt.title("EXPONENTIAL SIGNAL")
    plt.xlabel("Time")
    plt.ylabel("amplitude")
    plt.grid()
    plt.show()
    return signal
