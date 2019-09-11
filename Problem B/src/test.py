import unittest
from compareVersions import checkCompareVersions

class Test(unittest.TestCase):
    def test_valid_testCases(self):
        equal_valid_testCases = [
            ['1.1', '1.1'],
            [' 1.2.3  ', '1.2.3'],
            [' 1.2.3  .0.0.0.0.0.0', '1.2.3'],
            [' 1.2.3.0.0.1.0', '1.2.3.0.0.1.0.0.0']
        ]
        for test_cases in equal_valid_testCases:
            self.assertEqual(checkCompareVersions(test_cases[0], test_cases[1]),test_cases[0]+" is equal to "+test_cases[1])

        lessThan_valid_testCases = [
            ['1.1', '1.3'],
            [' 1 .2.0  ', ' 1.2 .1'],
            ['1.4.0.6  ', '  1.4.1.0'],
            ['1', '  5'],
            [' 1 .2.0.2.2.3.5.7.1  ', ' 1.2 .1.0.0.1'],
            ['1.4.0.6.0.0  ', '  1.4.1.0.0.9.0.5'],
            ['1.0', '  5.9.8.5.2']

        ]
        for test_cases in lessThan_valid_testCases:
            self.assertEqual(checkCompareVersions(test_cases[0], test_cases[1]), test_cases[0]+" is less than "+test_cases[1])

        greaterThan_valid_testCases = [
            ['1.2.1', '1.2.0'],
            ['1.1', '0'],
            ['1.2.1', '1.2.0'],
            ['1.4.  1.0', ' 1.4.0.6'],
            [' 5', '1  '],
            ['1.2.1.0.0.0.1', '1.2.0.2.9.0.1.2.1.2.3.5'],
            ['1.4.  1.0.0.0.0.0.0', ' 1.4.0.6'],
            [' 5', '1  .0.0.0. 0']
        ]
        for test_cases in greaterThan_valid_testCases:
            self.assertEqual(checkCompareVersions(test_cases[0], test_cases[1]), test_cases[0]+" is greater than "+test_cases[1])

    def test_invalid_testCases(self):
        invalid_testCases = [
            [],
            ['1.2'],
            ['1.2',3.4]         

        ]
        for test_cases in invalid_testCases:
            with self.assertRaises(ValueError):
                if len(test_cases) < 2:
                    checkCompareVersions(test_cases, None)
                else:
                    checkCompareVersions(test_cases[0], test_cases[1])

if __name__ == '__main__':
    unittest.main()