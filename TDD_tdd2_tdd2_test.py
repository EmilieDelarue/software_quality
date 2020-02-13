import unittest


def find_in_list(inputlist, tofind, start=0):
    i = 0
    result = -1
    for element in inputlist:
        if element == tofind:
            if i >= start:
                result = i
                break
        i += 1
    return result


class TestTDD2Methods(unittest.TestCase):
    def test_return_two_param(self):
        self.assertEqual(find_in_list([1,2], 2), 1)

    def test_return_three_param(self):
        self.assertEqual(find_in_list(['hihi', 2,3,4,'hihi'], 'hihi', 2), 4)


if __name__ == '__main__':
    unittest.main()
