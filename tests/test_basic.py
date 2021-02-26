from bhavpr import BhavPR


def test_instance_creation():
    instance = BhavPR()
    return instance


instance = test_instance_creation()

# Lookup for a company
def test_lookup():
    results = instance.get_symbol("itc")
    print(results)


test_lookup()
