import unittest


def le_truc_a_developper(*args):
    if len(args) == 1:
        start = 0
        end = args[0]
        step = 1
    elif len(args) == 1:
        start = args[0]
        end = args[1]
        step = 1
    elif len(args) == 3:
        start = args[0]
        end = args[1]
        step = args[3]
    resultlist = [start]
    temp = start + step
    while temp < end:
        resultlist.append(temp)
        temp += step
    return resultlist


class TestTDD1Methods(unittest.TestCase):
    def test_return_type_for_one_param(self):
        self.assertEqual(type(le_truc_a_developper(10)), type([]))

    def test_return_type_for_two_param(self):
        self.assertEqual(type(le_truc_a_developper(1, 10)), type([]))

    def test_return_type_for_three_param(self):
        self.assertEqual(type(le_truc_a_developper(1, 10, 2)), type([]))

    def test_return_for_one_param(self):
        number = 10
        self.assertEqual(len(le_truc_a_developper(number)), number)
        self.assertEqual(le_truc_a_developper(number)[0], 0)

        precedentNumber = 0
        for i in le_truc_a_developper(number):
            self.assertEqual(i, precedentNumber + 1)
            precedentNumber = i



    def test_return_for_two_params(self):
        start = 5
        end = 10
        self.assertEqual(len(le_truc_a_developper(start, end)), end - start)
        self.assertEqual(le_truc_a_developper(start, end)[0], start)
        self.assertEqual(le_truc_a_developper(start, end)[-1], end - 1)

        precedentNumber = start
        for i in le_truc_a_developper(start, end):
            self.assertEqual(i, precedentNumber + 1)
            precedentNumber = i

    def test_return_for_three_params(self):
        start = 1
        end = 11
        step = 2
        self.assertEqual(len(le_truc_a_developper(start, end, step)), round((end - start) / step))
        self.assertEqual(le_truc_a_developper(start, end, step)[0], start)

        precedentNumber = start
        for i in le_truc_a_developper(start, end, step):
            self.assertEqual(i, precedentNumber + step)
            precedentNumber = i


if __name__ == '__main__':
    unittest.main()
