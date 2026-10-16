class TimeMap:

    def __init__(self):
        self.myDict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.myDict:
            self.myDict[key] = []
        self.myDict[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.myDict:
            return ""
        values = self.myDict[key]
        l, r = 0, len(self.myDict[key])-1
        res = ""
        while l <= r:
            mid = (l + r)//2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l = mid+1
            else:
                r = mid-1
        return res

