# 建立给定层数的杨辉三角

class Solution:
    def yang_hui_triangle(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]

        if numRows == 2:
            return [[1], [1, 1]]

        yh_list = [[1], [1, 1]]

        for i in range(2, numRows):
            row_list = [0] * (i + 1)
            row_list[0], row_list[-1] = 1, 1
            for j in range(1, i):
                row_list[j] = yh_list[i - 1][j - 1] + yh_list[i - 1][j]
            yh_list.append(row_list)

        return yh_list
