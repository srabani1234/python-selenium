import pytest

# all the testcase file name either start with test (demo1_test.py/test_demo1.py)
# or End with test.if it is de_test_mo.py then not run
# all the test method name compulsory start with test
# To run : py.test /py.test classname.py / py.test packagename/classname.py
# To run perticular method (def test_login_F()/def test_login_K) : py.test -k login -v
# To tun group/set of test case use annotation @pytest.mark.login. And run group by py.test -m login [run all the test
# cases from same packeage have marker login][here login use
# in annotation it can be anything] , py.test classname.py -m login / py.test packagename/classname.py -m login
@pytest.mark.login
def test_m1():
    a=2
    b=3
    assert a+1 == b, "Test passed"
    assert a==b ,"Test fail as a not equal b"
def test_m2():
    name = "selenium"
    assert name == "selenium"
def test_m3():
    assert  True

def test_m4():
    assert  False

def test_m5():
    assert 100==100
def test_m6():
    assert "srabani" == "SRABANI"

@pytest.mark.login
def test_login_FB():
    assert "Admin" == "Admin"



