from local_scripts.miniCalculator import Minicalculator

def test_suma() :
    miniCalculator = Minicalculator()
    assert miniCalculator.suma(2,3) == 5

def test_suma2() :
    miniCalculator = Minicalculator()
    assert miniCalculator.suma(3,3) == 6

def test_suma3() :
    miniCalculator = Minicalculator()
    assert miniCalculator.suma(0,5) == 5