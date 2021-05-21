from test_instance_creation import test_instance_creation

instance = test_instance_creation()

def test_collect():
   results = instance.collect('01-01-2020', '31-12-2020')
   print(results)

#test_collect()

# Lookup for a company
def test_lookup():
    results = instance.get_symbol("itc")
    print(results)

test_lookup()

def test_set_symbol():
    results = instance.set_company("ITC Limited")
    print(results)

test_set_symbol()

def test_pr_parser():
    results = instance.get_pr('01-01-2020', '15-01-2020')
    print(results)

test_pr_parser()
