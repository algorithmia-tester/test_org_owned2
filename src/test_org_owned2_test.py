from . import test_org_owned2

def test_test_org_owned2():
    assert test_org_owned2.apply("Jane") == "hello Jane"
