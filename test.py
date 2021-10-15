import requests
import csv

from apikeys import *
from person_ids import *

# from __future__ import division

# total_count = len(person_id)
# current_count = 0
# corrected_count = 0

# print("{0:.0f}%".format(current_count/total_count * 100))

response = requests.delete("https://api.affinity.co/persons/64192646", auth=('', api_key))
print("Working on " + " - " + str(response.json()))