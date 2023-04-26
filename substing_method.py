#using substring where to run use pytest -k method1/2 -v

import pytest

def test_method1():
    x=5
    y=110
    assert x==y

def test_method2():
    x=10
    y=15
    assert x+5 == y       


