import os
import random
import re
import sys


# def reverseArray(a):
#     reverse = []
#     reverse = a[::-1]
#     return reverse


# def hourglassSum(arr):
#     num_rows = len(arr)
#     num_cols = len(arr[0])
#     hg_max_sum = float('-inf')  # initialize with negative infinity

#     for i in range(num_rows - 2):
#         for j in range(num_cols - 2):
#             # Extract the hourglass cells
#             top_row = arr[i][j:j+3]
#             middle_cell = arr[i+1][j+1]
#             bottom_row = arr[i+2][j:j+3]
#             # Calculate the current hourglass sum
#             hg_current_sum = sum(top_row) + middle_cell + sum(bottom_row)
#             # Update the maximum sum if needed
#             hg_max_sum = max(hg_max_sum, hg_current_sum)

#     return hg_max_sum


def dynamicArray(n, queries):
    # Initialize dynamic array
    seqList = [[] for _ in range(n)]
    lastAnswer = 0
    answers = []

    for query in queries:
        # Parse the query
        query_type, x, y = map(int, query.split())

        if query_type == 1:
            # Query type 1: Append y to sequence (x ^ lastAnswer) % n
            idx = (x ^ lastAnswer) % n
            seqList[idx].append(y)
        elif query_type == 2:
            # Query type 2: Assign y to lastAnswer and print it
            idx = (x ^ lastAnswer) % n
            lastAnswer = seqList[idx][y % len(seqList[idx])]
            answers.append(lastAnswer)

    return answers


def main():
    # a = [1, 2, 3, 4, 5]
    # print(reverseArray(a))
    # '''start = [[1, 1, 1, 0, 0, 0],
    #          [0, 1, 0, 0, 0, 0],
    #          [1, 1, 1, 0, 0, 0],
    #          [0, 0, 2, 4, 4, 0],
    #          [0, 0, 0, 2, 0, 0],
    #          [0, 0, 1, 2, 4, 0]]'''
    # test = [[-9, -9, -9, 1, 1, 1],
    #         [0, -9, 0, 4, 3, 2],
    #         [-9, -9, -9, 1, 2, 3],
    #         [0, 0, 8, 6, 6, 0],
    #         [0, 0, 0, -2, 0, 0],
    #         [0, 0, 1, 2, 4, 0]]
    # test1 = [[-1, -1, 0, -9, -2, -2],
    #          [-2, -1, -6, -8, -2, -5],
    #          [-1, -1, -1, -2, -3, -4],
    #          [-1, -9, -2, -4, -4, -5],
    #          [-7, -3, -3, -2, -9, -9],
    #          [-1, -3, -1, -2, -4, -5]]
    # print(hourglassSum(test1))
    n, q = 2, 5
    queries = [
        "1 0 5",
        "1 1 7",
        "1 0 3",
        "2 1 0",
        "2 1 1"
    ]

# Function call
    result = dynamicArray(n, queries)
    print(result)  # Output: [7, 3]

    print("End of main")


if __name__ == "__main__":
    main()
