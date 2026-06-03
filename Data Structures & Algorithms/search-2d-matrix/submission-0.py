class Solution:
        def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
                
                m = len(matrix)
                n = len(matrix[0])  # total length of the list

                left = 0
                right = m * n - 1   #last element

                while left <= right:
                    mid = (left + right) // 2  #get the middle point

                    row = mid // n  #to know which row we're in
                    col = mid % n   #to know which collumn we're in
                    mid_val = matrix[row][col]

                    if mid_val == target:
                        return True
                    elif mid_val < target:
                        left = mid + 1
                    else:
                        right = mid - 1
                
                # if loop ends and has not found the value
                return False







# flat = []
#        for row in matrix:
#            flat.extend(row)
#        return target in flat