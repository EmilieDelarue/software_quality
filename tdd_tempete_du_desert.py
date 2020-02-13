import unittest


def tempete_du_desert(arg1, arg2):


class TempeteDuDesert(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(tempete_du_desert(53.136, 1.80), (16.4, 'Dénutrition'))
        self.assertEqual(tempete_du_desert(53.46, 1.80), (16.5, 'Maigreur'))
        self.assertEqual(tempete_du_desert(59.94, 1.80), (18.5, 'Maigreur'))
        self.assertEqual(tempete_du_desert(60.264, 1.80), (18.6, 'Corpulence Normale'))
        self.assertEqual(tempete_du_desert(81, 1.80), (25, 'Corpulence Normale'))
        self.assertEqual(tempete_du_desert(84.24, 1.80), (26, 'Surpoids'))
        self.assertEqual(tempete_du_desert(97.2, 1.80), (30, 'Surpoids'))
        self.assertEqual(tempete_du_desert(100.44, 1.80), (31, 'Obésité modérée'))
        self.assertEqual(tempete_du_desert(113.4, 1.80), (35, 'Obésité modérée'))
        self.assertEqual(tempete_du_desert(116.64, 1.80), (36, 'Obésité sévère'))
        self.assertEqual(tempete_du_desert(129.6, 1.80), (40, 'Obésité sévère'))
        self.assertEqual(tempete_du_desert(132.84, 1.80), (41, 'Obésité morbide'))

    def test_type(self):
        self.assertEqual(tempete_du_desert('arg1', 'arg2'), 'Veuillez mettre des floats en entrée')
        self.assertEqual(tempete_du_desert(['arg1'], ['arg2']), 'Veuillez mettre des floats en entrée')

if __name__ == '__main__':
    unittest.main()
