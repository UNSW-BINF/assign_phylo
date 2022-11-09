"""Helper functions for HW3"""
import numpy as np
import matplotlib.pyplot as plt


class Node:
    def __init__(
        self,
        id: str,
        children: list["Node"] = [],
        distances: list[float] = [],
        samples: list["Node"] = None,
        confidence: float = None,
    ):
        """A node in a tree use by neighbour joining algorithm.

        Parameters
        ----------
        id: str
            Name of the node
        children: list["Node"]
            List of child nodes in a tree
        distances: list[float]
            List of distances to each child respectively
        samples: list["Node"]
            List of all terminal nodes in a subtree of a node
        confidence: float
            Confidence level of a split determined by the bootstrap method
        """
        self.id = id
        self.children = children
        self.distances = distances
        self.samples = samples
        self.confidence = confidence


def neighbour_joining(distances: np.array, labels: list[str] = []) -> Node:
    """Neighbour joining algorithm

    Parameters
    ----------
    distances: np.ndarray
        A two dimensional, square, symmetric matrix containing distances between data
        points. The diagonal is zeros.
    labels: list[str]
        A list of labels for samples in distance matrix. Add labels to Node objects
        and use them when plotting a dendrogram

    Returns
    -------
    Node
        A root node of a neighbour joining tree
    """
    raise NotImplementedError()


def plot_dendrogram_NJ(tree: Node, ax: plt.axes = None, **kwargs) -> None:
    """A function for plotting neighbour joining phylogeny dendrogram.

    Parameters
    ----------
    tree: Node
        A phylogeny tree in a form of a Node object from neighbour_joining function
    ax: plt.axes
        An axes from matplotlib to which you should plot a dendrogram
    kwargs: Any
        Keyword arguments as optional parameters for more informative vizualizations

    Example
    -------
    >>> tree = neighbour_joining(distances, labels)
    >>> f, ax = plt.subplots(1,1, figsize=(8,8))
    >>> plot_dendrogram_NJ(tree=tree, ax=ax)
    >>> f.savefig("example.png")
    """
    raise NotImplementedError()


def reroot_tree(tree: Node, new_root: Node) -> Node:
    """A function to invert a tree and set a new root node.

    Parameters
    ----------
    tree: Node
        A root node of a tree
    new_root: Node
        A Node to set as a new root

    Returns
    -------
    Node
        Inverted tree with a new root node.
    """
    raise NotImplementedError()


def ladderize_tree(tree: Node) -> None:
    """Ladderize a tree.
    Sort clades with more leaf nodes such that they apear first in array of children.
    Sort a tree in place.

    Paramteres
    ----------
    tree: Node
        A root node of a tree to be ladderized
    """
    raise NotImplementedError()
