import math, random
from matplotlib import pyplot as plt
from typing import Tuple


class Point(object):
    """
    Represents a point in the plane.
    """
    def __init__(self, x: float, y:float) -> None:
        self.x: float = x
        self.y: float = y
        self.isVisited: bool = False
        self.isInCluster: bool = False

    def __repr__(self) -> str:
        return f'({self.x}, {self.y})'

    def __str__(self) -> str:
        return self.__repr__()


type cluster = list[Point]


def random_dataset(nb_points: int, minimum: float, maximum: float, nb_decimals: int = 2) -> list[Point]:
    """
    Generates a random dataset of points.

    :param nb_points: Number of points to generate
    :param minimum: Minimum coordinates of the points
    :param maximum: Maximum coordinates of the points
    :param nb_decimals: Number of decimal in points' coordinates
    :return: A random dataset of points
    """
    datas: list[Point] = []
    for i in range(nb_points):

        datas.append(Point(round(random.uniform(minimum, maximum), nb_decimals), round(random.uniform(minimum, maximum), nb_decimals)))
    return datas


def euclidean_distance(p1: Point, p2: Point) -> float:
    """
    Return the Euclidean distance between two points.

    :param p1: First point
    :param p2: Second point
    :return: Euclidean distance in the plane
    """
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)


def neighborhood(data: list[Point], p: Point, epsilon: float) -> list[Point]:
    """
    Return the neighborhood of a point.

    :param data: List of all points in the plane
    :param p: Point in the center
    :param epsilon: Distance threshold
    :return: List of all points in the neighborhood
    """
    neighbors:list[Point] = []
    for other in data:
        if euclidean_distance(p, other) < epsilon:
            neighbors.append(other)
    return neighbors


def extend_cluster(data: list[Point], p:Point, epsilon: float, neighbors: list[Point], nb_points: int, c: cluster) -> None:
    """
    Extend a cluster of points.

    :param data: List of all points in the plane
    :param p: First point to add
    :param epsilon: Distance threshold
    :param neighbors: List of all points in the neighborhood
    :param nb_points: Minimum number of points in the neighborhood
    :param c: Cluster to extend
    """
    c.append(p)
    p.isInCluster = True
    for other in neighbors:
        if not other.isVisited:
            other.isVisited = True
            new_neighbors = neighborhood(data, other, epsilon)
            if len(new_neighbors) >= nb_points:
                neighbors.extend(new_neighbors)
            if not other.isInCluster:
                c.append(other)



def dbscan(data: list[Point], epsilon: float, nb_points: int) -> Tuple[list[cluster], list[Point]]:
    """
    Apply a DBSCAN algorithm to the points in data.

    :param data: List of all points in the plane
    :param epsilon: Distance threshold
    :param nb_points: Minimum number of points in the neighborhood
    :return: A list of all clusters and a list of points considered noise
    """
    clusters: list[cluster] = []
    noises: list[Point] = []
    for other in data:
        if not other.isVisited:
            other.isVisited = True
            neighbors: list[Point] = neighborhood(data, other, epsilon)
            if len(neighbors) < nb_points:
                noises.append(other)
            else:
                clusters.append([])
                extend_cluster(data, other, epsilon, neighbors, nb_points, clusters[-1])

    return clusters, noises


def show_dbscan(clusters: list[cluster], noises: list[Point] | None = None) -> None:
    """
    Show a graph of clusters and noises from a DBSCAN algorithm.

    :param clusters: List of all clusters
    :param noises: List of all noises points
    """
    plt.title("DBSCAN Algorithm")

    colors: list[str] = ['b', 'g', 'r', 'c', 'm', 'y']
    for i in range(len(clusters)):
        for element in clusters[i]:
            plt.scatter(element.x, element.y, s=8, c=colors[i%len(colors)])
    for noise in noises:
        plt.scatter(noise.x, noise.y, s=1, c='k')

    plt.show()


def print_dbscan(clusters: list[cluster], noises: list[Point] | None = None) -> None:
    """
    Print a DBSCAN clustering result.

    :param clusters: List of all clusters
    :param noises: List of all noises points
    """
    for i in range(len(clusters)):
        print(f'Cluster {i + 1}\n---------')
        for element in clusters[i]:
            print(str(element), end=", ")
        print()

    if noises is not None: print("Noises\n------")
    for element in noises:
        print(str(element), end=", ")


if __name__ == "__main__":
    dataset: list[Point] = random_dataset(1000, -100, 100)
    (clusters_list, noises_points) = dbscan(dataset, 5, 5)
    # print_dbscan(clusters_list, noises_points)
    print(f'Numbers of clusters: {len(clusters_list)}')
    show_dbscan(clusters_list, noises_points)