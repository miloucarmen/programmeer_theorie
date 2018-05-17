import numpy as np
from scipy.spatial import distance
dist = distance.cdist([1,2], [3,2])
print(dist)