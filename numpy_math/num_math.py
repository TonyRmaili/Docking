import numpy as np
import matplotlib.pyplot as plt

# Generate an array of x values from 0 to 2π (0 to 360 degrees)
x = np.linspace(0, 2 * np.pi, 1000)

# Compute the sine of each x value
y = np.sin(x)

# Create a plot
plt.plot(x, y, label='Sine Wave')

# Add labels and title
plt.xlabel('x values (radians)')
plt.ylabel('sin(x)')
plt.title('Plot of the Sine Wave')

# Add a grid
plt.grid(True)

# Show the legend
plt.legend()

# Save the plot as a PNG file
plt.savefig('/app/output/sine_wave_plot.png')
