import unittest
import parser as par

class TestMath(unittest.TestCase):
    def test_ADD_INTS(self):
        parser=par.getParser()
        self.assertEqual(parser.parse('1+2'),3.0)
        self.assertEqual(parser.parse('100+123'),223.0)
        self.assertEqual(parser.parse('1+2+3'),6)
    def test_ADD_DOUBLES(self):
        parser=par.getParser()
        self.assertAlmostEqual(parser.parse('1.34+2.43'),3.77)
        self.assertAlmostEqual(parser.parse('100.2+12.3'),112.5)
        self.assertAlmostEqual(parser.parse('1.0+2.2+3.1'),6.3)
    def test_ADD_DOUBLE_AND_INT(self):
        parser=par.getParser()
        self.assertAlmostEqual(parser.parse('1.34+2'),3.34)
        self.assertAlmostEqual(parser.parse('100.2+12'),112.2)
        self.assertAlmostEqual(parser.parse('1.0+2.2+3'),6.2)
        
    def test_SUBTRACT_INTS(self):
        parser=par.getParser()
        self.assertEqual(parser.parse('1-2'),-1.0)
        self.assertEqual(parser.parse('123-100'),23.0)
        self.assertEqual(parser.parse('1+2-3'),0)
    def test_SUBTRACT_DOUBLES(self):
        parser=par.getParser()
        self.assertAlmostEqual(parser.parse('2.34-1.43'),0.91)
        self.assertAlmostEqual(parser.parse('100.2-12.3'),87.9)
        self.assertAlmostEqual(parser.parse('1.0-2.2-3.1'),-4.3)
    def test_SUBTRACT_DOUBLE_AND_INT(self):
        parser=par.getParser()
        self.assertAlmostEqual(parser.parse('2-1.23'),0.77)
        self.assertAlmostEqual(parser.parse('100.2-12'),88.2)
        self.assertAlmostEqual(parser.parse('1.0-2.2-3'),-4.2)
        
    def test_MULT_INTS(self):
        parser=par.getParser()
        self.assertEqual(parser.parse('1*2'),2.0)
        self.assertEqual(parser.parse('123*100'),12300.0)
        self.assertEqual(parser.parse('1*2*3'),6.0)
    def test_MULT_DOUBLES(self):
        parser=par.getParser()
        self.assertAlmostEqual(parser.parse('2.34*1.43'),3.3462)
        self.assertAlmostEqual(parser.parse('100.2*12.3'),1232.46)
        self.assertAlmostEqual(parser.parse('1.0*2.2*3.1'),6.82)
    def test_MULT_DOUBLE_AND_INT(self):
        parser=par.getParser()
        self.assertAlmostEqual(parser.parse('2*1.23'),2.46)
        self.assertAlmostEqual(parser.parse('100.2*12'),1202.4)
        self.assertAlmostEqual(parser.parse('1.0*2.2*3'),6.6)

    def test_DIV_INTS(self):
        parser=par.getParser()
        self.assertEqual(parser.parse('1/2'),0.5)
        self.assertEqual(parser.parse('123/100'),1.23)
        self.assertAlmostEqual(parser.parse('1/2/3'),0.1666666666)
    def test_DIV_DOUBLES(self):
        parser=par.getParser()
        self.assertAlmostEqual(parser.parse('2.34/1.43'),1.636363636)
        self.assertAlmostEqual(parser.parse('100.2/12.3'),8.146341463)
        self.assertAlmostEqual(parser.parse('1.0/2.2/3.1'),0.146627566)
    def test_DIV_DOUBLE_AND_INT(self):
        parser=par.getParser()
        self.assertAlmostEqual(parser.parse('2/1.23'),1.626016267)
        self.assertAlmostEqual(parser.parse('100.2/12'),8.35)
        self.assertAlmostEqual(parser.parse('1.0/2.2/3'),0.151515152)

    def test_NEG_NUMBER(self):
        parser=par.getParser()
        self.assertEqual(parser.parse('-1'),-1.0)
        self.assertEqual(parser.parse('-2.1'),-2.1)
if __name__ == '__main__':
    unittest.main()
