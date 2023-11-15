import matplotlib.pyplot as plt
import numpy as np

# Data genereren voor de voorbeelden
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

# Subplots maken
plt.figure(figsize=(10, 6))

# Eerste subplot
plt.subplot(2, 2, 1)
plt.plot(x, y1, label='sin(x)')
plt.legend()

# Tweede subplot
plt.subplot(2, 2, 2)
plt.plot(x, y2, label='cos(x)')
plt.legend()

# Derde subplot
plt.subplot(2, 2, 3)
plt.plot(x, y3, label='tan(x)')
plt.legend()

# Overlappen van de subplots
plt.subplots_adjust(wspace=0.5, hspace=0.5)  # Aanpassen van de ruimte tussen subplots

# Titel toevoegen aan het geheel
plt.suptitle('Gegroepeerde en overlappende plots')

# Weergeven van de grafieken
plt.show()