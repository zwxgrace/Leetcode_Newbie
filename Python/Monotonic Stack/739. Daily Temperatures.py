# 739. Daily Temperatures
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0]*n    # 0 is the answer of not finding a larger datapoint
        stack = []    # initialize a stack, used for storing the index

        for i in range(n):
            # always compare with the latest added one in stack(stack top)
            while stack and temperatures[i] > temperatures[stack[-1]]:
                # when the task is satisified, do 2 things: 
                # pop up the finished index(to keep the stack monotonically increasing); 
                # calculate the result since the task is done for this index
                prev_index = stack.pop()
                result[prev_index]=i-prev_index
            # when not satisified, just keep the new one in the stack, waiting for being solved
            stack.append(i)
        return result

T = [24, 26, 28, 18, 17, 22]
result_t= dailyTemperatures(T)
print(result_t)

if __name__ == '__main__':
    solver = Solution()
    
    T = [24, 26, 28, 18, 17, 22]
    result_t = solver.dailyTemperatures(T)
    
    print(result_t)
