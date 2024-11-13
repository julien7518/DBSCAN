# DBSCAN for 2-dimensional points

This is an implementation of the DBSCAN clustering algorithm.

## The DBSCAN algorithm

DBSCAN (Density-Based Spatial Clustering of Applications with Noise) is a clustering algorithm that identifies groups of densely packed points and treats sparse regions as noise. It begins by selecting a random point and checking its neighboring points within a specified distance (`epsilon`, $\varepsilon$). If this neighborhood has enough points (`nb_points`), the point is considered a "core point," forming the start of a cluster. The algorithm then expands this cluster by adding all density-reachable points. DBSCAN repeats this process until all points are processed, marking any isolated points as noise.  
This method effectively finds clusters of arbitrary shapes and sizes.

## How it works here

This DBSCAN implementation in Python generates a random dataset, applies the clustering process, and visualizes results.
Each point is represented by a `Point` class, with `x` and `y` coordinates, plus attributes to track if it’s been visited and if it belongs to a cluster. The algorithm finds neighborhoods using Euclidean distance and expands clusters from core points that meet density requirements, marking unclustered points as noise.  
Results can be displayed graphically with `matplotlib` or printed in the console for cluster details.

### Requirements

- `matplotlib` : needed to create the point cloud
- `math` : needed to calculate the Euclidean distance
- `random` : needed to create a random dataset of point
- `typing` : needed for the type hints

If you're using Python 3.11.* or lower, replace the line 3 with

```python
from typing import Tuple, TypeAlias
```

and line 23 with

```python
cluster: TypeAlias = list[Point]
```
