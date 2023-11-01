import pytest
from funciones import multiple

@pytest.mark.parametrize("a,b,resp",[
    (2,4,0),
    (4,8,0),
])
def test_multiple (a, b, resp):
    assert multiple(a,b) == resp