# A random dataset of nested arrays is given with n levels
# Method count_edges should return number of all arrays with no more nested elements
#
# Example dataset:
#
# dataset = [
#     [
#         [
#             [
#                 []
#             ],
#             [
#                 [
#                     []
#                 ]
#             ]
#         ]
#     ],
#     [],
#     [
#         [
#             [],
#             []
#         ]
#     ]
# ]

from helpers import create_dataset

dataset, edges = create_dataset(2)


def count_edges(data):
    # @TODO implement!
    pass


assert edges == count_edges(dataset)
