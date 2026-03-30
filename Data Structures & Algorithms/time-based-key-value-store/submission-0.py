class TimeMap:

    def __init__(self):
        self.keyList = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyList:
            self.keyList[key] = []
        self.keyList[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res, val = "", self.keyList.get(key, [])

        l, r = 0, len(val) - 1
        while l <= r:
            m = (l + r) // 2
            if val[m][1] <= timestamp:
                res = val[m][0]
                l = m + 1
            else:
                r = m - 1
        
        return res
