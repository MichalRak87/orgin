

def get_triange_field(height: int,base: int) -> float:
    print(0.5 * base * height,end='')

def test_triange_area(capsys):
    base = 10
    height =10

    get_triange_field(base,height)
    out,err = capsys.readouterr()
    out = float(out)

    assert out == 50.0


