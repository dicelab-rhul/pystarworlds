from pystarworlds.Identifiable import Identifiable

class TestI(Identifiable):
    pass

def test1():
    print(Identifiable())
    print(Identifiable())

def test2():
    print(TestI())

if __name__ == "__main__":
    test1()
    test2()
