class SplittingGame:
    def arraySplitting(self, arr):
        if(len(arr) < 2):
            return 0
        return self.recurse(arr, 0, len(arr) - 1)

    def recurse(self, arr, i, h):
        if (i == h):
            return 0
        elif(i < h):

            total = sum(arr[i:h + 1])

            if(total % 2 != 0):
                return 0

            cur_sum = 0
            pivot = None
            for j in range(i, h + 1):
                cur_sum += arr[j]
                if(cur_sum == total // 2):
                    pivot = j
                    break
                elif (cur_sum > total // 2):
                    break

            if pivot is None:
                return 0

            return 1 + max(self.recurse(arr, i, pivot), self.recurse(arr, pivot + 1, h))

        return 0


ex = SplittingGame()
arr = [1, 1]
print(ex.arraySplitting(arr))
