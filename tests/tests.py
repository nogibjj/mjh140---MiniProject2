from src.main import printfunc as pf

def testprint():
    assert pf("String of text") == "String of text"

if __name__ == "__main__":
    testprint()