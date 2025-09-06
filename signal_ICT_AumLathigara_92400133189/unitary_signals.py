import numpy as np
import matplotlib.pyplot as plt

# Function to generate and plot a unit step signal
def unit_step(n):
    signal = np.array([1 if i >= 0 else 0 for i in n])  # Step: 1 for n>=0, else 0
    plt.stem(n, signal, basefmt=" ")
    plt.title("UNIT STEP")
    plt.xlabel("n")
    plt.ylabel("AMPLITUDE")
    plt.grid()
    plt.show()
    return signal

# Function to generate and plot a unit impulse signal
def unit_impulse(n):
    signal = np.array([1 if i == 0 else 0 for i in n])  # Impulse: 1 at n=0, else 0
    plt.stem(n, signal, basefmt=" ")
    plt.title("UNIT IMPULSE")
    plt.xlabel("n")
    plt.ylabel("AMPLITUDE")
    plt.grid()
    plt.show()
    return signal

# Function to generate and plot a ramp signal
def ramp_signal(n):
    signal = np.array([i if i >= 0 else 0 for i in n])  # Ramp: n for n>=0, else 0
    plt.stem(n, signal, basefmt=" ")
    plt.title("RAMP SIGNAL")
    plt.xlabel("n")
    plt.ylabel("AMPLITUDE")
    plt.grid()
    plt.show()
    return signal
