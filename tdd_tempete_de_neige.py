import unittest


def tempete_de_neige(string1, string2, *args):
    return int


class TempeteDuDesert(unittest.TestCase):

    def test1(self):
        self.assertEqual(tempete_de_neige('cochonaille', 'cho'), 2)

    def test2(self):
        self.assertEqual(tempete_de_neige('cochonaille', 'ate'), -1)

    def test3(self):
        self.assertEqual(tempete_de_neige('123456789', '45'), 3)

    def test4(self):
        self.assertEqual(tempete_de_neige('toto', 'to'), 0)

    def test_3_parameters(self):
        self.assertEqual(tempete_de_neige('cochonaille', 'cho', 3), -1)

    def test_4_parameters(self):
        self.assertEqual(tempete_de_neige('cochonaille', 'cho', 0, 1), -1)


if __name__ == '__main__':
    unittest.main()
