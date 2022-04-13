from app import change


def test_quarters():
    assert({5: "quarters"} in change(1.25))

def test_change():
    assert [{5: "quarters"}, {1: "nickels"}, {4: "pennies"}] == change(1.34)