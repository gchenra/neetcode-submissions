class Solution:
    def create_combo(self, cur_num, cur_combo, combos, n, k) -> None:
        # essentially a DFS with backtrack
        # base cases to stop recursion
        if len(cur_combo) == k:
            combos.append(cur_combo.copy())
            return
        if cur_num > n:
            # exhaust all numbers you can add
            return

        # add current number then
        # go to the number to the right of current number
        for j in range(cur_num, n+1):
            cur_combo.append(j)
            self.create_combo(j+1, cur_combo, combos, n, k)
            cur_combo.pop()

    def combine(self, n: int, k: int) -> List[List[int]]:
        # n numbers, k spots to fill
        # start from 1, move to right and fill in k spots
        # always take new number on the right side to avoid
        # creating permutation
        combos = []
        self.create_combo(1, [], combos, n, k)
        return combos
