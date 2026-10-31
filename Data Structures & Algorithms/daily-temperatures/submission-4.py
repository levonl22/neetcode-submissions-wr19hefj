class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        res = [0] * len(temps)
        stack = []

        for i, t in enumerate(temps):
            while stack and t > temps[stack[-1]]:
                j = stack.pop()
                res[j] = i - j
            stack.append(i)
        return res