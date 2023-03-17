class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        
        def memo(n, cache):
            if n <= 1:
                return n
            if n in cache:
                return cache[n]

            cache[n] = memo(n-1, cache) + memo(n-2, cache)
            return cache[n]

        return memo(n +1, cache)
