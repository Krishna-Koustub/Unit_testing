import pytest

@pytest.fixtures

def numbers():
    a=10
    b=20
    c=25
    return[a,b,c]

def test_method1(numbers):
    x=15
    assert numbers[0]==x

def test_method2(numbers):
    y=20
    assert numbers[1]==y    

def test_method3(numbers):
    z=25
    assert numbers[z]==z    


