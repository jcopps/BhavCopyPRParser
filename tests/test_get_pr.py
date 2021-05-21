from datetime import datetime

from test_instance_creation import test_instance_creation

def test_get_pr():
   instance = test_instance_creation()
   results = instance.get_pr('01-01-2021', datetime.now())
   print(results)

#test_get_pr()
def test_get_pr_company():
   instance = test_instance_creation()
   instance.set_company('Tata Consultancy Services Limited')
   results = instance.get_pr('31-03-2021', datetime.now())
   print(results)

test_get_pr_company()
