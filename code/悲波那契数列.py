
import traceback

# class Solution:
#     def fib(self, n: int) -> int:
#         if(n == 0):
#             return 0
#         if(n == 1):
#             return 1
#         return self.fib(n-1) + self.fib(n-2)


def fib(n: int) -> int:
    if(n==3):
        g()
    if(n < 2):
        return 0
    return fib(n-1) + fib(n-2)


def g():
    for line in traceback.format_stack():
        print(line.strip())


