import numpy as np
import matplotlib.pyplot as plt

# Function to perform time shifting of a discrete-time signal
def time_shift(signal, k):
    shifted = np.roll(signal, k)  # Shift signal by k samples
    # Plot original and shifted signals
    plt.plot(signal, label="Original")
    plt.plot(shifted, label=f"Shifted by {k}")
    plt.title("Time Shift Operation")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid(True)
    plt.show()
    return shifted

# Function to perform time scaling (downsampling by factor k)
def time_scale(signal, k):
    scaled = signal[::k] if k > 0 else signal  # Take every k-th sample
    # Plot original and scaled signals
    plt.plot(signal, label="Original")
    plt.plot(np.arange(0, len(scaled) * k, k), scaled, label=f"Scaled by {k}")
    plt.title("Time Scaling Operation")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid(True)
    plt.show()
    return scaled

# Function to add two signals element-wise
def signal_addition(signal1, signal2):
    result = signal1 + signal2
    # Plot both signals and their sum
    plt.plot(signal1, label="Signal 1")
    plt.plot(signal2, label="Signal 2")
    plt.plot(result, label="Added Signal")
    plt.title("Signal Addition")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid(True)
    plt.show()
    return result

# Function to multiply two signals element-wise
def signal_multiplication(signal1, signal2):
    result = signal1 * signal2
    # Plot both signals and their product
    plt.plot(signal1, label="Signal 1")
    plt.plot(signal2, label="Signal 2")
    plt.plot(result, label="Multiplied Signal")
    plt.title("Signal Multiplication")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid(True)
    plt.show()
    return result
