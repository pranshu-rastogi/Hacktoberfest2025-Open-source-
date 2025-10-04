class Solution(object):
    def largestGoodInteger(self, num):
        l = []
        res = num[0]
        for i in range(1, len(num)):
            if num[i] == num[i - 1] and len(res) < 3:
                res += num[i]
            else:
                l.append(res)
                res = num[i]

        l.append(res)

        best = ""
        for group in l:
            if len(group) == 3:
                best = max(best, group)

        return best
