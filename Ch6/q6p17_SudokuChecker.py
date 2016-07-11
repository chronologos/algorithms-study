"""
"""
import unittest


class MyTest(unittest.TestCase):
    def setUp(self):
        # CheckSudoku should return None
        self.ill_formed = [[5,3,4,6,7,8,9,1,2],
                [6,7,2,1,9,5,3,4,8],
                [1,9,8,3,4,2,5,6,7],
                [8,5,9,7,6,1,4,2,3],
                [4,2,6,8,5,3,7,9],  # <---
                [7,1,3,9,2,4,8,5,6],
                [9,6,1,5,3,7,2,8,4],
                [2,8,7,4,1,9,6,3,5],
                [3,4,5,2,8,6,1,7,9]]

        # CheckSudoku should return True
        self.valid = [[5,3,4,6,7,8,9,1,2],
                [6,7,2,1,9,5,3,4,8],
                [1,9,8,3,4,2,5,6,7],
                [8,5,9,7,6,1,4,2,3],
                [4,2,6,8,5,3,7,9,1],
                [7,1,3,9,2,4,8,5,6],
                [9,6,1,5,3,7,2,8,4],
                [2,8,7,4,1,9,6,3,5],
                [3,4,5,2,8,6,1,7,9]]

        # CheckSudoku should return False
        self.invalid = [[5,3,4,6,7,8,9,1,2],
                [6,7,2,1,9,5,3,4,8],
                [1,9,8,3,8,2,5,6,7],
                [8,5,9,7,6,1,4,2,3],
                [4,2,6,8,5,3,7,9,1],
                [7,1,3,9,2,4,8,5,6],
                [9,6,1,5,3,7,2,8,4],
                [2,8,7,4,1,9,6,3,5],
                [3,4,5,2,8,6,1,7,9]]
        # CheckSudoku should return False
        self.invalid2 = [[5,3,4,6,7,8,9,1,2], # <----- (4)
                [6,7,2,1,9,5,3,4,8],
                [1,9,4,3,4,2,5,6,7], # <-----
                [8,5,9,7,6,1,4,2,3],
                [4,2,6,8,5,3,7,9,1],
                [7,1,3,9,2,4,8,5,6],
                [9,6,1,5,3,7,2,8,4],
                [2,8,7,4,1,9,6,3,5],
                [3,4,5,2,8,6,1,7,9]]

        # CheckSudoku should return True
        self.easy = [[2,9,0,0,0,0,0,7,0],
                [3,0,6,0,0,8,4,0,0],
                [8,0,0,0,4,0,0,0,2],
                [0,2,0,0,3,1,0,0,7],
                [0,0,0,0,8,0,0,0,0],
                [1,0,0,9,5,0,0,6,0],
                [7,0,0,0,9,0,0,0,1],
                [0,0,1,2,0,0,3,0,6],
                [0,3,0,0,0,0,0,5,9]]

        # CheckSudoku should return True
        self.hard = [[1,0,0,0,0,7,0,9,0],
                [0,3,0,0,2,0,0,0,8],
                [0,0,9,6,0,0,5,0,0],
                [0,0,5,3,0,0,9,0,0],
                [0,1,0,0,8,0,0,0,2],
                [6,0,0,0,0,4,0,0,0],
                [3,0,0,0,0,0,0,1,0],
                [0,4,0,0,0,0,0,0,7],
                [0,0,7,0,0,0,3,0,0]]

    def test(self):
        self.assertEqual(CheckSudoku(self.easy),True)
    def test1(self):
        self.assertEqual(CheckSudoku(self.hard),True)
    def test2(self):
        self.assertEqual(CheckSudoku(self.valid),True)
    def test3(self):
        self.assertEqual(CheckSudoku(self.invalid),False)
    def test3b(self):
        self.assertEqual(CheckSudoku(self.invalid2),False)
    def test4(self):
        self.assertEqual(CheckSudoku(self.ill_formed),None)


def CheckSudoku(grid: list):
    seen_in_row = [[False for i in range(10)] for j in range(9)]  
    # inner list is for digits 0-9
    # outer list is for rows/cols/box 0-9
    seen_in_col = [[False for i in range(10)] for j in range(9)]  
    seen_in_box = [[False for i in range(10)] for j in range(9)]  

    if len(grid) != 9:
        print("too many rows")
        return
    # check rows
    for row_num, row in enumerate(grid):
        # print("Row %s" %row_num)
        if len(row) != 9:
            print("too many cols r:%d c:%d"%(row_num, col))
            return
        for col,item in enumerate(row):
            # print("Col %s" %col)
            if item == 0:
                continue
            if not 0 < item < 10 and isinstance(item,int):
                print("int out of range")
                return
            if not seen_in_row[row_num][item]:
                seen_in_row[row_num][item] = True
            elif seen_in_row[row_num][item]:
                return False
            if not seen_in_col[col][item]:
                seen_in_col[col][item] = True
            elif seen_in_col[col][item]:
                return False
            if not seen_in_box[MapRowColToBox(row_num, col)][item]:
                seen_in_box[MapRowColToBox(row_num, col)][item] = True
            elif seen_in_box[MapRowColToBox(row_num, col)][item]:
                return False
    return True

def MapRowColToBox(row, col):
    # index of boxes starts from upper left at 0 to bottom right at 9
    if  row < 3 and col < 3:
        box = 0
    elif  row < 3 and 3  <=  col < 6:
        box = 1
    elif  row < 3 and 6  <=  col < 9:
        box = 2
    elif  3 <=  row < 6 and col < 3:
        box = 3
    elif  3 <=  row < 6 and 3 <= col < 6:
        box = 4
    elif  3 <=  row < 6 and 6 <= col < 9:
        box = 5
    elif  6 <=  row < 9 and col < 3:
        box = 6
    elif  6 <=  row < 9 and 3 <= col < 6:
        box = 7
    elif  6 <=  row < 9 and 6 <= col < 9:
        box = 8
    else:
        raise Error("Not supposed to be here")
    return box



    # check cols


    pass

if __name__ == '__main__':
    unittest.main()
