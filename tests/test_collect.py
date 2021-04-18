from datetime import datetime

from test_instance_creation import test_instance_creation

def test_collect():
   instance = test_instance_creation()
   results = instance.collect('01-01-2020', datetime.now())
   print(results)

test_collect()

