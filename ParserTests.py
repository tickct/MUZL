import unittest
import parser as par

class TestAddMath(unittest.TestCase):
    def test_ADD_INTS(self):
        parser=par.getParser()
        self.assertEqual(parser.parse('1+2'),3.0)
        self.assertEqual(parser.parse('100+123'),223.0)
        self.assertEqual(parser.parse('1+2+3'),6)
    def test_ADD_FLOATS(self):
        parser=par.getParser()
        self.assertAlmostEqual(parser.parse('1.34+2.43'),3.77)
        self.assertAlmostEqual(parser.parse('100.2+12.3'),112.5)
        self.assertAlmostEqual(parser.parse('1.0+2.2+3.1'),6.3)
    def test_ADD_CHARS(self):
        parser=par.getParser()
        self.assertEqual(parser.parse('\'a\'+\'a\''),194)
        self.assertEqual(parser.parse('\'F\'+\'a\''),167)
        self.assertEqual(parser.parse('\'F\'+\'a\'+\'a\''),264)
        
    def test_ADD_FLOATS_AND_INT(self):
        parser=par.getParser()
        self.assertAlmostEqual(parser.parse('1.34+2'),3.34)
        self.assertAlmostEqual(parser.parse('100.2+12'),112.2)
        self.assertAlmostEqual(parser.parse('1.0+2.2+3'),6.2)
    def test_ADD_INT_AND_CHAR(self):
        parser=par.getParser()
        self.assertEqual(parser.parse('\'a\'+1'),98)
        self.assertEqual(parser.parse('2+\'F\''),72)
        self.assertEqual(parser.parse('\'F\'+ 2 +\'a\''),169)
    def test_ADD_FLOAT_AND_CHAR(self):
        parser=par.getParser()
        self.assertEqual(parser.parse('\'a\'+1.1'),98.1)
        self.assertEqual(parser.parse('2.2+\'F\''),72.2)
        self.assertEqual(parser.parse('\'F\'+ 2.5 +\'a\''),169.5)
        
    def test_ADD_FLOAT_AND_INT_AND_CHAR(self):
        parser=par.getParser()
        self.assertEqual(parser.parse('\'F\'+ 2 +97.2'),169.2)

class TestSubMath(unittest.TestCase):
    def test_SUBTRACT_INTS(self):
        parser=par.getParser()
        self.assertEqual(parser.parse('1-2'),-1.0)
        self.assertEqual(parser.parse('123-100'),23.0)
        self.assertEqual(parser.parse('1+2-3'),0)
    def test_SUBTRACT_FLOATS(self):
        parser=par.getParser()
        self.assertAlmostEqual(parser.parse('2.34-1.43'),0.91)
        self.assertAlmostEqual(parser.parse('100.2-12.3'),87.9)
        self.assertAlmostEqual(parser.parse('1.0-2.2-3.1'),-4.3)
    def test_SUBTRACT_CHARS(self):
        parser=par.getParser()
        self.assertEqual(parser.parse('\'a\'- \'a\''),0)
        self.assertEqual(parser.parse('\'a\'-\'F\''),27)
        self.assertEqual(parser.parse('\'F\'-\'a\'-\'a\''),-124)
        
    def test_SUBTRACT_FLOATS_AND_INT(self):
        parser=par.getParser()
        self.assertAlmostEqual(parser.parse('2-1.23'),0.77)
        self.assertAlmostEqual(parser.parse('100.2-12'),88.2)
        self.assertAlmostEqual(parser.parse('1.0-2.2-3'),-4.2)

    def test_SUBTRACT_INT_AND_CHAR(self):
        parser=par.getParser()
        self.assertEqual(parser.parse('\'a\'-1'),96)
        self.assertEqual(parser.parse('2-\'F\''),-68)
        self.assertEqual(parser.parse('\'F\'- 2 -\'a\''),-29)
    def test_SUBTRACT_FLOAT_AND_CHAR(self):
        parser=par.getParser()
        self.assertAlmostEqual(parser.parse('\'a\'-1.1'),95.9)
        self.assertAlmostEqual(parser.parse('2.2-\'F\''),-67.8)
        self.assertAlmostEqual(parser.parse('\'F\'- 2.5 -\'a\''),-29.5)
        
    def test_SUBTRACT_FLOAT_AND_INT_AND_CHAR(self):
        parser=par.getParser()
        self.assertAlmostEqual(parser.parse('\'F\'- 2 -97.2'),-29.2)
        
class testMultMath(unittest.TestCase):
    def test_MULT_INTS(self):
        parser=par.getParser()
        self.assertEqual(parser.parse('1*2'),2.0)
        self.assertEqual(parser.parse('123*100'),12300.0)
        self.assertEqual(parser.parse('1*2*3'),6.0)
    def test_MULT_FLOATS(self):
        parser=par.getParser()
        self.assertAlmostEqual(parser.parse('2.34*1.43'),3.3462)
        self.assertAlmostEqual(parser.parse('100.2*12.3'),1232.46)
        self.assertAlmostEqual(parser.parse('1.0*2.2*3.1'),6.82)
    def test_MULT_CHAR(self):
        parser=par.getParser()
        self.assertAlmostEqual(parser.parse('\'a\'*\'a\''),9409)
        self.assertAlmostEqual(parser.parse('\'a\'*\'F\''),6790)
        self.assertAlmostEqual(parser.parse('\'A\'*\'B\'*\'C\''),287430)
        
    def test_MULT_FLOAT_AND_INT(self):
        parser=par.getParser()
        self.assertAlmostEqual(parser.parse('2*1.23'),2.46)
        self.assertAlmostEqual(parser.parse('100.2*12'),1202.4)
        self.assertAlmostEqual(parser.parse('1.0*2.2*3'),6.6)
    def test_MULT_INT_AND_CHAR(self):
        parser=par.getParser()
        self.assertAlmostEqual(parser.parse('2*\'a\''),194)
        self.assertAlmostEqual(parser.parse('\'A\'*12'),780)
        self.assertAlmostEqual(parser.parse('1.0*2*\'a\''),194)
    def test_MULT_FLOAT_AND_CHAR(self):
        parser=par.getParser()
        self.assertAlmostEqual(parser.parse('\'a\'*1.23'),119.31)
        self.assertAlmostEqual(parser.parse('100.2*\'a\''),9719.4)
        self.assertAlmostEqual(parser.parse('\'a\'*2.2*3.0'),640.2)
        
    def test_MULT_INT_AND_FLOAT_AND_CHAR(self):
        parser=par.getParser()
        self.assertAlmostEqual(parser.parse('\'a\'*2.2*3'),640.2)

class testDivMath(unittest.TestCase):
    def test_DIV_INTS(self):
        parser=par.getParser()
        self.assertEqual(parser.parse('1/2'),0.5)
        self.assertEqual(parser.parse('123/100'),1.23)
        self.assertAlmostEqual(parser.parse('1/2/3'),0.1666666666)
    def test_DIV_FLOATS(self):
        parser=par.getParser()
        self.assertAlmostEqual(parser.parse('2.34/1.43'),1.636363636)
        self.assertAlmostEqual(parser.parse('100.2/12.3'),8.146341463)
        self.assertAlmostEqual(parser.parse('1.0/2.2/3.1'),0.146627566)
    def test_DIV_CHARS(self):
        parser=par.getParser()
        self.assertAlmostEqual(parser.parse('\'a\'/\'a\''),1)
        self.assertAlmostEqual(parser.parse('\'a\'/\'F\''),1.385714286)
        self.assertAlmostEqual(parser.parse('\'A\'/\'B\'/\'C\''),0.014699231)
    def test_DIV_FLOAT_AND_INT(self):
        parser=par.getParser()
        self.assertAlmostEqual(parser.parse('2/1.23'),1.626016267)
        self.assertAlmostEqual(parser.parse('100.2/12'),8.35)
        self.assertAlmostEqual(parser.parse('1.0/2.2/3'),0.151515152)
    def test_DIV_INT_AND_CHAR(self):
        parser=par.getParser()
        self.assertAlmostEqual(parser.parse('\'a\'/97'),1)
        self.assertAlmostEqual(parser.parse('140/\'F\''),2)
        self.assertAlmostEqual(parser.parse('\'A\'/66/\'C\''),0.014699231)
    def test_DIV_FLOAT_AND_CHAR(self):
        parser=par.getParser()
        self.assertAlmostEqual(parser.parse('\'a\'/97.2'),0.997942387)
        self.assertAlmostEqual(parser.parse('46.5/\'F\''),0.664285714)
        self.assertAlmostEqual(parser.parse('\'A\'/45.6/\'C\''),0.021275203)
    def test_DIV_INT_AND_FLOAT_AND_CHAR(self):
        parser=par.getParser()
        self.assertAlmostEqual(parser.parse('\'A\'/45.6/67'),0.021275203)
class TestNegatives(unittest.TestCase):
    def test_NEG_NUMBER(self):
        parser=par.getParser()
        self.assertEqual(parser.parse('-1'),-1.0)
        self.assertEqual(parser.parse('-2.1'),-2.1)

class TestIntCast(unittest.TestCase):
    def test_INT_to_INT(self):
        parser=par.getParser()
        self.assertEqual(parser.parse('1.int'),1)
        self.assertEqual(parser.parse('234.int'),234)
    def test_FLOAT_to_INT(self):
        parser=par.getParser()
        self.assertEqual(parser.parse('1.6.int'),1)
        self.assertEqual(parser.parse('1.2.int'),1)
    def test_CHAR_to_INT(self):
        parser=par.getParser()
        self.assertEqual(parser.parse('\'a\'.int'),97)
        self.assertEqual(parser.parse('\'A\'.int'),65)
                        

class TestFloatCast(unittest.TestCase):
    def test_INT_to_FLOAT(self):
        parser=par.getParser()
        self.assertEqual(parser.parse('1.float'),1.0)
        self.assertEqual(parser.parse('234.float'),234.0)
    def test_FLOAT_to_FLOAT(self):
        parser=par.getParser()
        self.assertAlmostEqual(parser.parse('1.6.float'),1.6)
        self.assertAlmostEqual(parser.parse('1.2.float'),1.2)
    def test_CHAR_to_FLOAT(self):
        parser=par.getParser()
        self.assertEqual(parser.parse('\'a\'.float'),97.0)
        self.assertEqual(parser.parse('\'A\'.float'),65.0)

class TestCharCast(unittest.TestCase):
    def test_INT_to_CHAR(self):
        parser=par.getParser()
        self.assertEqual(parser.parse('97.char'),'a')
        self.assertEqual(parser.parse('66.char'),'B')
    def test_FLOAT_to_CHAR(self):
        parser=par.getParser()
        self.assertEqual(parser.parse('97.6.char'),'a')
        self.assertEqual(parser.parse('66.2.char'),'B')
    def test_CHAR_to_CHAR(self):
        parser=par.getParser()
        self.assertEqual(parser.parse('\'a\'.char'),'a')
        self.assertEqual(parser.parse('\'A\'.char'),'A')
if __name__ == '__main__':
    unittest.main()
