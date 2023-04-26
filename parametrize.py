import pytest 
@pytest.mark.parametrizr("x,y,z",[(10,20,300),(20,40,200)])
def test_method(x,y,z):
    assert x*y==z