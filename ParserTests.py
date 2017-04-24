import unittest
import parser as par


class TestAddMath(unittest.TestCase):
    def test_ADD_INTS(self):
        parser = par.get_parser()
        self.assertEqual(parser.parse('1+2'), 3.0)
        self.assertEqual(parser.parse('100+123'), 223.0)
        self.assertEqual(parser.parse('1+2+3'), 6)

    def test_ADD_FLOATS(self):
        parser = par.get_parser()
        self.assertAlmostEqual(parser.parse('1.34+2.43'), 3.77)
        self.assertAlmostEqual(parser.parse('100.2+12.3'), 112.5)
        self.assertAlmostEqual(parser.parse('1.0+2.2+3.1'), 6.3)

    def test_ADD_CHARS(self):
        parser = par.get_parser()
        self.assertEqual(parser.parse('\'a\'+\'a\''), 194)
        self.assertEqual(parser.parse('\'F\'+\'a\''), 167)
        self.assertEqual(parser.parse('\'F\'+\'a\'+\'a\''), 264)

    def test_ADD_HEX(self):
        parser = par.get_parser()
        self.assertEqual(parser.parse('0x1+0x1'), 2.0)
        self.assertEqual(parser.parse('0x6e+0xf'), 125.0)

    def test_ADD_FLOATS_AND_INT(self):
        parser = par.get_parser()
        self.assertAlmostEqual(parser.parse('1.34+2'), 3.34)
        self.assertAlmostEqual(parser.parse('100.2+12'), 112.2)
        self.assertAlmostEqual(parser.parse('1.0+2.2+3'), 6.2)

    def test_ADD_INT_AND_CHAR(self):
        parser = par.get_parser()
        self.assertEqual(parser.parse('\'a\'+1'), 98)
        self.assertEqual(parser.parse('2+\'F\''), 72)
        self.assertEqual(parser.parse('\'F\'+ 2 +\'a\''), 169)

    def test_ADD_FLOAT_AND_CHAR(self):
        parser = par.get_parser()
        self.assertEqual(parser.parse('\'a\'+1.1'), 98.1)
        self.assertEqual(parser.parse('2.2+\'F\''), 72.2)
        self.assertEqual(parser.parse('\'F\'+ 2.5 +\'a\''), 169.5)

    def test_ADD_HEX_AND_INT(self):
        parser = par.get_parser()
        self.assertEqual(parser.parse('0x6e+1'), 111)

    def test_add_HEX_AND_FLOAT(self):
        parser = par.get_parser()
        self.assertEqual(parser.parse('0x6e+1.0'), 111.0)

    def test_add_HEX_AND_CHAR(self):
        parser = par.get_parser()
        self.assertEqual(parser.parse('0x6e+\'A\''), 175)

    def test_ADD_ALL(self):
        parser = par.get_parser()
        self.assertEqual(parser.parse('\'F\'+ 2 +97.2+0x1'), 170.2)


class TestSubMath(unittest.TestCase):
    def test_SUBTRACT_INTS(self):
        parser = par.get_parser()
        self.assertEqual(parser.parse('1-2'), -1.0)
        self.assertEqual(parser.parse('123-100'), 23.0)
        self.assertEqual(parser.parse('1+2-3'), 0)

    def test_SUBTRACT_FLOATS(self):
        parser = par.get_parser()
        self.assertAlmostEqual(parser.parse('2.34-1.43'), 0.91)
        self.assertAlmostEqual(parser.parse('100.2-12.3'), 87.9)
        self.assertAlmostEqual(parser.parse('1.0-2.2-3.1'), -4.3)

    def test_SUBTRACT_CHARS(self):
        parser = par.get_parser()
        self.assertEqual(parser.parse('\'a\'- \'a\''), 0)
        self.assertEqual(parser.parse('\'a\'-\'F\''), 27)
        self.assertEqual(parser.parse('\'F\'-\'a\'-\'a\''), -124)

    def test_SUBTRACT_HEXS(self):
        parser = par.get_parser()
        self.assertEqual(parser.parse('0x6e-0x4f'), 31)

    def test_SUBTRACT_FLOATS_AND_INT(self):
        parser = par.get_parser()
        self.assertAlmostEqual(parser.parse('2-1.23'), 0.77)
        self.assertAlmostEqual(parser.parse('100.2-12'), 88.2)
        self.assertAlmostEqual(parser.parse('1.0-2.2-3'), -4.2)

    def test_SUBTRACT_INT_AND_CHAR(self):
        parser = par.get_parser()
        self.assertEqual(parser.parse('\'a\'-1'), 96)
        self.assertEqual(parser.parse('2-\'F\''), -68)
        self.assertEqual(parser.parse('\'F\'- 2 -\'a\''), -29)

    def test_SUBTRACT_FLOAT_AND_CHAR(self):
        parser = par.get_parser()
        self.assertAlmostEqual(parser.parse('\'a\'-1.1'), 95.9)
        self.assertAlmostEqual(parser.parse('2.2-\'F\''), -67.8)
        self.assertAlmostEqual(parser.parse('\'F\'- 2.5 -\'a\''), -29.5)

    def test_SUBTRACT_HEX_AND_INT(self):
        parser = par.get_parser()
        self.assertEqual(parser.parse('0x6e-1'), 109)

    def test_SUBTRACT_HEX_AND_FLOAT(self):
        parser = par.get_parser()
        self.assertEqual(parser.parse('0x6e-1.2'), 108.8)

    def test_SUBTRACT_HEX_AND_CHAR(self):
        parser = par.get_parser()
        self.assertEqual(parser.parse('0x6e-\'A\''), 45)

    def test_SUBTRACT_ALL(self):
        parser = par.get_parser()
        self.assertAlmostEqual(parser.parse('\'F\'- 2 -97.2-0x1'), -30.2)


class testMultMath(unittest.TestCase):
    def test_MULT_INTS(self):
        parser = par.get_parser()
        self.assertEqual(parser.parse('1*2'), 2.0)
        self.assertEqual(parser.parse('123*100'), 12300.0)
        self.assertEqual(parser.parse('1*2*3'), 6.0)

    def test_MULT_FLOATS(self):
        parser = par.get_parser()
        self.assertAlmostEqual(parser.parse('2.34*1.43'), 3.3462)
        self.assertAlmostEqual(parser.parse('100.2*12.3'), 1232.46)
        self.assertAlmostEqual(parser.parse('1.0*2.2*3.1'), 6.82)

    def test_MULT_CHAR(self):
        parser = par.get_parser()
        self.assertAlmostEqual(parser.parse('\'a\'*\'a\''), 9409)
        self.assertAlmostEqual(parser.parse('\'a\'*\'F\''), 6790)
        self.assertAlmostEqual(parser.parse('\'A\'*\'B\'*\'C\''), 287430)

    def test_MULT_FLOAT_AND_INT(self):
        parser = par.get_parser()
        self.assertAlmostEqual(parser.parse('2*1.23'), 2.46)
        self.assertAlmostEqual(parser.parse('100.2*12'), 1202.4)
        self.assertAlmostEqual(parser.parse('1.0*2.2*3'), 6.6)

    def test_MULT_INT_AND_CHAR(self):
        parser = par.get_parser()
        self.assertAlmostEqual(parser.parse('2*\'a\''), 194)
        self.assertAlmostEqual(parser.parse('\'A\'*12'), 780)
        self.assertAlmostEqual(parser.parse('1.0*2*\'a\''), 194)

    def test_MULT_FLOAT_AND_CHAR(self):
        parser = par.get_parser()
        self.assertAlmostEqual(parser.parse('\'a\'*1.23'), 119.31)
        self.assertAlmostEqual(parser.parse('100.2*\'a\''), 9719.4)
        self.assertAlmostEqual(parser.parse('\'a\'*2.2*3.0'), 640.2)

    def test_MULT_HEX_AND_INT(self):
        parser = par.get_parser()
        self.assertEqual(parser.parse('0x6e*1'), 110)

    def test_MULT_HEX_AND_FLOAT(self):
        parser = par.get_parser()
        self.assertEqual(parser.parse('0x6e*2.5'), 275)

    def test_MULT_HEX_AND_CHAR(self):
        parser = par.get_parser()
        self.assertEqual(parser.parse('0x6e*\'A\''), 7150)

    def test_MULT_ALL(self):
        parser = par.get_parser()
        self.assertAlmostEqual(parser.parse('\'a\'*2.2*3*0x2'), 1280.4)


class testDivMath(unittest.TestCase):
    def test_DIV_INTS(self):
        parser = par.get_parser()
        self.assertEqual(parser.parse('1/2'), 0.5)
        self.assertEqual(parser.parse('123/100'), 1.23)
        self.assertAlmostEqual(parser.parse('1/2/3'), 0.1666666666)

    def test_DIV_FLOATS(self):
        parser = par.get_parser()
        self.assertAlmostEqual(parser.parse('2.34/1.43'), 1.636363636)
        self.assertAlmostEqual(parser.parse('100.2/12.3'), 8.146341463)
        self.assertAlmostEqual(parser.parse('1.0/2.2/3.1'), 0.146627566)

    def test_DIV_CHARS(self):
        parser = par.get_parser()
        self.assertAlmostEqual(parser.parse('\'a\'/\'a\''), 1)
        self.assertAlmostEqual(parser.parse('\'a\'/\'F\''), 1.385714286)
        self.assertAlmostEqual(parser.parse('\'A\'/\'B\'/\'C\''), 0.014699231)

    def test_DIV_FLOAT_AND_INT(self):
        parser = par.get_parser()
        self.assertAlmostEqual(parser.parse('2/1.23'), 1.626016267)
        self.assertAlmostEqual(parser.parse('100.2/12'), 8.35)
        self.assertAlmostEqual(parser.parse('1.0/2.2/3'), 0.151515152)

    def test_DIV_INT_AND_CHAR(self):
        parser = par.get_parser()
        self.assertAlmostEqual(parser.parse('\'a\'/97'), 1)
        self.assertAlmostEqual(parser.parse('140/\'F\''), 2)
        self.assertAlmostEqual(parser.parse('\'A\'/66/\'C\''), 0.014699231)

    def test_DIV_FLOAT_AND_CHAR(self):
        parser = par.get_parser()
        self.assertAlmostEqual(parser.parse('\'a\'/97.2'), 0.997942387)
        self.assertAlmostEqual(parser.parse('46.5/\'F\''), 0.664285714)
        self.assertAlmostEqual(parser.parse('\'A\'/45.6/\'C\''), 0.021275203)

    def test_DIV_HEX_AND_INT(self):
        parser = par.get_parser()
        self.assertEqual(parser.parse('0x6e/2'), 55)

    def test_DIV_HEX_AND_FLOAT(self):
        parser = par.get_parser()
        self.assertEqual(parser.parse('0x6e/2.5'), 44)

    def test_DIV_HEX_AND_CHAR(self):
        parser = par.get_parser()
        self.assertAlmostEqual(parser.parse('0x6e/\'A\''), 1.692307692)

    def test_DIV_ALL(self):
        parser = par.get_parser()
        self.assertAlmostEqual(parser.parse('\'A\'/45.6/67/0x2'), 0.010637601)


class TestNegatives(unittest.TestCase):
    def test_NEG_NUMBER(self):
        parser = par.get_parser()
        self.assertEqual(parser.parse('-1'), -1.0)
        self.assertEqual(parser.parse('-2.1'), -2.1)


class TestIntCast(unittest.TestCase):
    def test_INT_to_INT(self):
        parser = par.get_parser()
        self.assertEqual(parser.parse('1.int'), 1)
        self.assertEqual(parser.parse('234.int'), 234)

    def test_FLOAT_to_INT(self):
        parser = par.get_parser()
        self.assertEqual(parser.parse('1.6.int'), 2)
        self.assertEqual(parser.parse('1.2.int'), 1)

    def test_CHAR_to_INT(self):
        parser = par.get_parser()
        self.assertEqual(parser.parse('\'a\'.int'), 97)
        self.assertEqual(parser.parse('\'A\'.int'), 65)

    def test_HEX_to_INT(self):
        parser = par.get_parser()
        self.assertEqual(parser.parse('0x61.float'), 97.0)
        self.assertEqual(parser.parse('0x41.float'), 65.0)


class TestFloatCast(unittest.TestCase):
    def test_INT_to_FLOAT(self):
        parser = par.get_parser()
        self.assertEqual(parser.parse('1.float'), 1.0)
        self.assertEqual(parser.parse('234.float'), 234.0)

    def test_FLOAT_to_FLOAT(self):
        parser = par.get_parser()
        self.assertAlmostEqual(parser.parse('1.6.float'), 1.6)
        self.assertAlmostEqual(parser.parse('1.2.float'), 1.2)

    def test_CHAR_to_FLOAT(self):
        parser = par.get_parser()
        self.assertEqual(parser.parse('\'a\'.float'), 97.0)
        self.assertEqual(parser.parse('\'A\'.float'), 65.0)

    def test_HEX_to_FLOAT(self):
        parser = par.get_parser()
        self.assertEqual(parser.parse('0x61.float'), 97.0)
        self.assertEqual(parser.parse('0x41.float'), 65.0)


class TestCharCast(unittest.TestCase):
    def test_INT_to_CHAR(self):
        parser = par.get_parser()
        self.assertEqual(parser.parse('97.char'), 'a')
        self.assertEqual(parser.parse('66.char'), 'B')

    def test_FLOAT_to_CHAR(self):
        parser = par.get_parser()
        self.assertEqual(parser.parse('97.6.char'), 'a')
        self.assertEqual(parser.parse('66.2.char'), 'B')

    def test_CHAR_to_CHAR(self):
        parser = par.get_parser()
        self.assertEqual(parser.parse('\'a\'.char'), 'a')
        self.assertEqual(parser.parse('\'A\'.char'), 'A')

    def test_HEX_to_CHAR(self):
        parser = par.get_parser()
        self.assertEqual(parser.parse('0x61.char'), 'a')
        self.assertEqual(parser.parse('0x41.char'), 'A')


class TestHexCast(unittest.TestCase):
    def test_INT_to_HEX(self):
        parser = par.get_parser()
        self.assertEqual(parser.parse('97.hex'), '0x61')
        self.assertEqual(parser.parse('66.hex'), '0x42')

    def test_FLOAT_to_HEX(self):
        parser = par.get_parser()
        self.assertEqual(parser.parse('97.6.hex'), '0x61')
        self.assertEqual(parser.parse('66.2.hex'), '0x42')

    def test_CHAR_to_HEX(self):
        parser = par.get_parser()
        self.assertEqual(parser.parse('\'a\'.hex'), '0x61')
        self.assertEqual(parser.parse('\'A\'.hex'), '0x41')

    def test_HEX_to_HEX(self):
        parser = par.get_parser()
        self.assertEqual(parser.parse('0x42.hex'), '0x42')
        self.assertEqual(parser.parse('0x61.hex'), '0x61')


class PresidenceTest(unittest.TestCase):
    def test_MULT_over_ADD(self):
        parser = par.get_parser()
        self.assertEqual(parser.parse('3*2+1'), 7)
        self.assertEqual(parser.parse('1+3*2'), 7)
    def test_DIV_over_ADD(self):
        parser = par.get_parser()
        self.assertAlmostEquals(parser.parse('3+4/2'), 5)
        self.assertAlmostEquals(parser.parse('4/2+3'), 5)
    def test_PARENS_over_ALL(self):
        parser = par.get_parser()
        self.assertEqual(parser.parse('(1+2)*3'), 9)
        self.assertEqual(parser.parse('6/(1+2)'), 2)


if __name__ == '__main__':
    unittest.main()
