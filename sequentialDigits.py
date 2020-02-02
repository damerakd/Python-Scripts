class Solution:
    def sequentialDigits(self, low, high):
        sample = "123456789"
        n = 10
        nums = []

        for length in range(len(str(low)), len(str(high)) + 1):
            #print("length", length)
            for start in range(n - length):
                #print("start", start)
                num = int(sample[start: start + length])
                #print("num", num)
                if num >= low and num <= high:
                    nums.append(num)
                #print("nums", nums)       
        return nums

s = Solution()
print(s.sequentialDigits(100, 400))