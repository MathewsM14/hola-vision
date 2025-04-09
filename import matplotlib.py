import matplotlib.pyplot as plt
import numpy as np

#I = np.array([[255, 255, 255],[0, 255, 0],[0, 255, 0]])
#plt.imshow(I, vmin=0, vmax=255)
#plt.show()

I = np.array([[[0, 255, 0], [0, 128, 128]], 
                [[128, 0, 0], [128, 0, 128] ]], dtype=np.uint8)

plt.imshow(I, vmin=0, vmax=255)
plt.show()
