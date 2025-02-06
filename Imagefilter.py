import math
import sys

from PIL import Image, ImageFilter

# Ensure correct usage
if len(sys.argv) !=2:
    sys.exit("Usage: Python filter.py filename")

# Open image
image = Image.open(sys.arvg[1]).covert("RGB")

# Filter mage according to edge detection kernel
filtered = image.filter(ImageFilter.Kernel(
    size =(3, 3),
    kernel=[-1, -1, -1, -1, 8, -1, -1, -1, -1],
    scale=1
))
# show resulting image
filtered.show()