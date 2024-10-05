import matplotlib.pyplot as plt
import numpy as np

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_primes(limit):
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def archimedean_spiral(t):
    a = 0.1
    b = 0.1
    r = a + b * t
    x = r * np.cos(t)
    y = r * np.sin(t)
    return x, y

# Generate prime numbers up to a certain limit
limit = 150000
primes = generate_primes(limit)

# Calculate spiral coordinates for prime numbers
theta = np.array(primes)
x, y = archimedean_spiral(theta)

# Plot the spiral
plt.figure(figsize=(40, 40), dpi=600)
plt.plot(x, y, 'o', color='cyan', markersize=1)
plt.axis('off')

# Set black background
plt.gca().set_facecolor('black')
plt.gcf().set_facecolor('black')

# Remove axes
plt.axis('off')

# Save the plot as a high-resolution PNG file
plt.savefig('archimedean_spiral_primes.png', bbox_inches='tight', facecolor='black')
