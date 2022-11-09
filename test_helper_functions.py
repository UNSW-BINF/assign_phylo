import unittest
import numpy as np
import pickle


class TestNeighbourJoining(unittest.TestCase):
    def alignment_case_1(self):

        distances = np.array(
            [
                [0, 14, 14, 12],
                [0, 0, 16, 14],
                [0, 0, 0, 6],
                [0, 0, 0, 0],
            ]
        )
        distances = distances + distances.T
        return distances

    def alignment_case_2(self):

        distances = np.array(
            [
                [0, 32, 48, 96, 80],
                [32, 0, 64, 88, 72],
                [48, 64, 0, 96, 80],
                [96, 88, 96, 0, 48],
                [80, 72, 80, 48, 0],
            ]
        )
        return distances

    def test_neighbour_joining_tree_format_shallow(self):

        from helper_functions import neighbour_joining, Node

        distances = self.alignment_case_1()
        labels = [str(i + 1) for i in range(len(distances))]

        tree = neighbour_joining(distances, labels)

        # tests for object types
        self.assertIsInstance(tree, Node)

        self.assertIsInstance(tree.children, list)
        self.assertIsInstance(tree.children[0], Node)

        self.assertIsInstance(tree.distances, list)
        self.assertIsInstance(tree.distances[0], float)

        self.assertEqual(len(tree.children), len(tree.distances))

    def test_neighbour_joining_tree_format_deep(self):

        from helper_functions import neighbour_joining, Node

        distances = self.alignment_case_1()
        labels = [str(i + 1) for i in range(len(distances))]

        tree = neighbour_joining(distances, labels)

        # tests for object deep in a tree
        stack = [tree]
        while len(stack) > 0:
            node = stack.pop()

            self.assertIsInstance(node, Node)
            self.assertIsInstance(node.children, list)
            self.assertEqual(len(node.children), len(node.distances))

            stack += node.children

    def test_neighbour_joining_1(self):

        from helper_functions import neighbour_joining

        distances = self.alignment_case_1()
        labels = [str(i + 1) for i in range(len(distances))]

        tree = neighbour_joining(distances, labels)

        self.assertEqual(set(tree.distances), set([2.0, 2.0]))

        child_dist = [set([2.0, 4.0]), set([6.0, 8.0])]

        self.assertIn(set(tree.children[0].distances), child_dist)
        self.assertIn(set(tree.children[1].distances), child_dist)

    def test_neighbour_joining_2(self):

        from helper_functions import neighbour_joining

        distances = self.alignment_case_2()
        labels = [str(i + 1) for i in range(len(distances))]

        solutions = [
            set([5.0, 5.0]),
            set([30.0, 34.0]),
            set([32.0, 16.0]),
            set([14.0, 18.0]),
            set([]),
        ]

        tree = neighbour_joining(distances, labels)

        stack = [tree]
        while len(stack) > 0:
            node = stack.pop()
            self.assertIn(set(node.distances), solutions)
            stack += node.children


class TestPlottingDendrogram(unittest.TestCase):
    def setUp(self) -> None:

        with open("tests/example_tree_1.pickle", "rb") as f:
            self.tree_1 = pickle.load(f)

        with open("tests/example_tree_2.pickle", "rb") as f:
            self.tree_2 = pickle.load(f)

        with open("tests/test_plotting_dendrogram.pickle", "rb") as f:
            self.figure = pickle.load(f)

    def test_plotting_dendrogram(self):

        from helper_functions import plot_dendrogram_NJ

        ax = self.figure.axes

        plot_dendrogram_NJ(self.tree_1, ax=ax[2])
        plot_dendrogram_NJ(self.tree_2, ax=ax[3])

        ax[0].set_title("Test Case 1", fontsize=12)
        ax[0].set_title("Test Case 2", fontsize=12)

        ax[0].set_ylabel("Ground truth", fontsize=12)
        ax[2].set_ylabel("Your implementation", fontsize=12)

        self.figure.savefig(
            "tests/test_plotting_dendrogram", dpi=400, bbox_inches="tight"
        )


if __name__ == "__main__":
    unittest.main()