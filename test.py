import pytest 
@pytest.mark.login

def test_m1():
    a=3
    b=4
    assert a+1==b , "test failed"
    

def test_m2():
    name = 'selenium'
    assert name.upper()=="SELENIUM"

@pytest.mark.login   
def test_m3():
    assert True

def test_m4():
    assert True

@pytest.mark.login
def test_m5():
    assert 100==100

def test_m6():
    assert True

@pytest.mark.login
def test_login_FB():
    assert "admin"=="admin"


print('LL')