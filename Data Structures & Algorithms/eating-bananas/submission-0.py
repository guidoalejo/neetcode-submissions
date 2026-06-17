class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left, right = 1, max(piles)     # minimum speed is 1 banana per hour
                                        # max speed is equal the largets pile of bananas
        res = right                     # start at the maximum possible speed

        while left <= right:            # execute binary search

            k = (left + right) // 2     # k = bananas-per-hour eating rate
            hours = 0                   # to track the total hours taken at speed k

            for p in piles:             # iterate through each pile of bananas
                hours += math.ceil(p/k) # calculate time to eat(hours) for the current pile and add to total (Ceil helps us round UP the number)

            if hours <= h:          # if all bananas are eaten within the time limit 'h'
                res = k             # update the result 
                right = k - 1       # keep searching for a smaller valid speed in the left half
                
            else:                   # if the speed 'k' is too slow (hours > h)
                left = k + 1        # Search for a faster speed in the right half

        return res                      # return the minimum valid speed