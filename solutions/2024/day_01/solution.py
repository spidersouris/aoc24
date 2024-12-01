# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/1

from ...base import StrSplitSolution, answer


def get_lists(input: list[str]) -> tuple[list[int], list[int]]:
    left_list = [int(x.split()[0]) for x in input]
    right_list = [int(x.split()[1]) for x in input]

    return left_list, right_list


def get_sim(right_list: list[int], first_left_number: int) -> int:
    count = right_list.count(first_left_number)
    return first_left_number * count


class Solution(StrSplitSolution):
    _year = 2024
    _day = 1

    @answer(2430334)
    def part_1(self) -> int:
        res = []
        left, right = get_lists(self.input)
        for _ in list(zip(left, right)):
            min_left, min_right = min(left), min(right)
            res.append(max(min_left, min_right) - min(min_left, min_right))
            left.remove(min_left)
            right.remove(min_right)

        return sum(res)

    @answer(28786472)
    def part_2(self) -> int:
        res = []
        left, right = get_lists(self.input)
        for first, _ in zip(left, right):
            res.append(get_sim(right, first))

        return sum(res)
