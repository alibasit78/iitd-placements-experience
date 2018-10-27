class GroupTravel:
    def verify(self, arr, k):
        cap = k
        for each in arr:
            if each <= cap:
                cap -= each
            elif each > cap:
                return False
            if cap == 0:
                cap = k
        return True if cap == k else False

    def naive(self, arr):
        start = max(arr)
        last = sum(arr)
        result = []
        for i in range(start, last // 2):
            if(last % i == 0 and self.verify(arr, i)):
                result.append(i)
        result.append(last)
        return result

    def solve(self, arr):
        return self.naive(arr)


ex = GroupTravel()
arr = [1, 2, 1, 1, 1, 2, 1, 3]
print(ex.solve(arr))
