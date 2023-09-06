from src.main import printfunc as pf

def test_print():
    assert pf("String of text") == "String of text"

if __name__ == "__main__":
    test_print()