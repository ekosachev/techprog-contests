from typing import Optional


class Solution:
    @classmethod
    def sift_down(cls, seq: list[int], i: int) -> Optional[tuple[tuple[int, int], int]]:
        if i > len(seq) // 2 - 1:
            return None

        left_child_i = 2 * i + 1
        right_child_i = min(len(seq) - 1, 2 * i + 2)

        element = seq[i]
        left_child = seq[left_child_i]
        right_child = seq[right_child_i]

        min_index = i

        min_child_index = left_child_i if left_child < right_child else right_child_i
        if element > seq[min_child_index]:
            min_index = min_child_index

        if min_index == i:
            return None

        swap = (i, min_index)

        seq[i], seq[min_index] = seq[min_index], seq[i]

        return swap, min_index

    @classmethod
    def solve(cls) -> None:
        n = int(input())
        seq: list[int] = list(map(int, input().split(" ")))
        swaps: list[tuple[int, int]] = []

        start_index = n // 2 - 1
        stack: list[int] = list(range(start_index + 1))
        while stack:
            element = stack.pop()
            result = cls.sift_down(seq, element)
            if result is not None:
                swap, next_element = result
                swaps.append(swap)
                stack.append(next_element)

        print(len(swaps))
        for a, b in swaps:
            print(a, b)


Solution.solve()
