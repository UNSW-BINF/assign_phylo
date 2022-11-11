import unittest
from numbers import Number

import numpy as np
import pickle


def is_isomorhipic(tree1: "Node", tree2: "Node") -> bool:
    """Check if two trees are isomorphic, checking their structure and distances."""
    if tree1 is None and tree2 is None:
        return True
    if (tree1 is None and tree2 is not None) or (tree1 is not None and tree2 is None):
        return False

    isomorphic_orig_order = (
        is_isomorhipic(tree1.left, tree2.left)
        and is_isomorhipic(tree1.right, tree2.right)
        and np.isclose(tree1.left_distance, tree2.left_distance)
        and np.isclose(tree1.right_distance, tree2.right_distance)
    )
    isomorphic_flip_order = (
        is_isomorhipic(tree1.left, tree2.right)
        and is_isomorhipic(tree1.right, tree2.left)
        and np.isclose(tree1.left_distance, tree2.right_distance)
        and np.isclose(tree1.right_distance, tree2.left_distance)
    )

    if isomorphic_orig_order or isomorphic_flip_order:
        return True

    return False


class TestNeighbourJoining(unittest.TestCase):
    def test_neighbour_joining_node_api(self):
        from helper_functions import neighbour_joining, Node

        distances = np.array(
            [
                [0, 14, 14, 12],
                [0, 0, 16, 14],
                [0, 0, 0, 6],
                [0, 0, 0, 0],
            ]
        )
        distances = distances + distances.T

        original_distances = distances.copy()

        tree: Node = neighbour_joining(distances)

        # Check that the distance matrix remained in-tact
        np.testing.assert_almost_equal(
            distances,
            original_distances,
            err_msg="`neighbour_joining` changed original distance matrix!",
        )

        # Check that NJ returns a Node object
        self.assertIsInstance(tree, Node)
        # Check if the Node object has a valid public API
        self.assertTrue(hasattr(tree, "id"))

        self.assertIsInstance(tree.left, Node)
        self.assertIsInstance(tree.right, Node)

        self.assertIsInstance(tree.left_distance, Number)
        self.assertIsInstance(tree.right_distance, Number)

    def test_textbook_example(self):
        from helper_functions import Node, neighbour_joining

        distances = np.array(
            [
                [0, 5, 4, 9, 8],
                [0, 0, 5, 10, 9],
                [0, 0, 0, 7, 6],
                [0, 0, 0, 0, 7],
                [0, 0, 0, 0, 0],
            ]
        )
        distances = distances + distances.T

        result = neighbour_joining(distances)
        expected = Node(
            "ROOT",
            left=Node(
                "X",
                left=Node(
                    "W",
                    left=Node("D", None, 0, None, 0),
                    left_distance=4,
                    right=Node("E", None, 0, None, 0),
                    right_distance=3,
                ),
                left_distance=2,
                right=Node("C", None, 0, None, 0),
                right_distance=1,
            ),
            left_distance=0.5,
            right=Node(
                "Y",
                left=Node("A", None, 0, None, 0),
                left_distance=2,
                right=Node("B", None, 0, None, 0),
                right_distance=3,
            ),
            right_distance=0.5,
        )

        self.assertTrue(is_isomorhipic(result, expected))


class TestPlottingDendrogram(unittest.TestCase):
    def setUp(self) -> None:

        with open("tests/example_tree_1.pickle", "rb") as f:
            self.tree_1 = pickle.load(f)

        with open("tests/example_tree_2.pickle", "rb") as f:
            self.tree_2 = pickle.load(f)

        with open("tests/test_plotting_dendrogram.pickle", "rb") as f:
            self.figure = pickle.load(f)

    def test_plotting_dendrogram(self):

        from helper_functions import plot_nj_tree

        ax = self.figure.axes

        plot_nj_tree(self.tree_1, ax=ax[2])
        plot_nj_tree(self.tree_2, ax=ax[3])

        ax[0].set_title("Test Case 1", fontsize=12)
        ax[1].set_title("Test Case 2", fontsize=12)

        ax[0].set_ylabel("Ground truth", fontsize=12)
        ax[2].set_ylabel("Your implementation", fontsize=12)

        self.figure.savefig(
            "tests/test_plotting_dendrogram", dpi=400, bbox_inches="tight"
        )


if __name__ == "__main__":
    unittest.main()
