import unittest
from LinesOverlap import checkLinesOverlap

class Test(unittest.TestCase):
    
    def test_valid_testCases(self):
        
        valid_testCases = [
            [(1,3), (2,8), True],
            [(2,8), (1,3), True],
            [(1,3), (4,8), False],
            [(4,8), (1,3), False],
            [(1,5), (3,6), True],
            [(3,6), (1,5), True],
            [(1,5), (6,11), False],
            [(6,11), (1,5), False],
            [(-1,-5), (-3,-6), True],
            [(-3,-6), (-1,-5), True],
            [(-1,-5), (-6,-11), False],
            [(-6,-11), (-1,-5), False],
            [(-1,2), (0,-2), True],
            [(0,-2), (-1,2), True],
            [(0,0), (0,0), True],
            [(-1,-3), (1,3), False],
            [(1,3), (-1,-3), False],
            [(1,5), (2,3), True],
            [(2,3), (1,5), True]
    ]
        
        for test_cases in valid_testCases:            
            self.assertEqual(checkLinesOverlap(test_cases[0], test_cases[1]), test_cases[2])
    
    def test_invalid_testCases(self):
        invalid_testCases = [
            [],
            [""],
            [1],
            ["1"],
            [(0,0)],
            [(1,4),[2,6]],
            [(2,3),],
            [("1","4"),("2",6)]
        ]
        for test_cases in invalid_testCases:
           
            with self.assertRaises(ValueError):                
                if len(test_cases) < 2:
                    checkLinesOverlap(test_cases,None)
                else:
                    checkLinesOverlap(test_cases[0], test_cases[1])

if __name__ == '__main__':
    unittest.main()