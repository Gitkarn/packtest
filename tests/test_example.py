# from packtest.adder import add
import packtest.adder
print(packtest.__version__)

def test_adder():
    assert packtest.adder.add(1, 2) == 3