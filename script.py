import requests
import csv

from apikeys import *
from person_ids import *


total_count = len(person_ids)
current_count = 0
corrected_count = 0

log_file = open("log.csv", "w")
log_file.write("Person ID, Status code, Note")
log_file.write("\n")

for each in person_ids:
  response = requests.delete("https://api.affinity.co/persons/" + str(each), auth=('', api_key))
  current_count = current_count + 1

  if response.status_code == 200:
    corrected_count = corrected_count + 1
    print(str(current_count) + "/"+ str(total_count) + " Working on " + str(each) + " - "+ str(response.json()))
    log_file.write(str(each) + ", " + str(response.status_code) + ", " + str(response.json()))
    log_file.write("\n")
  elif response.status_code == 422:
    print(str(current_count) + "/"+ str(total_count) + " Working on " + str(each) + " - "+ str(response.json()))
    log_file.write(str(each) + ", " + str(response.status_code) + ", " + str(response.json()))
    log_file.write("\n")
  elif response.status_code == 429:
    print("Working on " + str(each) + " - 429 error - "+ str(response.json()))
    print(str(current_count) + "/"+ str(total_count) + " Working on " + str(each) + " - API Limit Reached")
    log_file.write(str(each) + ", " + str(response.status_code) + ", " + "API Limit Reached")
    log_file.write("\n")
    break
  elif response.status_code == 500:
    print("Working on " + str(each) + " - 500 error - Internal Server Error")
    print(str(current_count) + "/"+ str(total_count) + " Working on " + str(each) + " - Internal Server Error")
    log_file.write(str(each) + ", " + str(response.status_code) + ", " + "Internal Server Error")
    log_file.write("\n")
  elif response.status_code == 503:
    print(str(current_count) + "/"+ str(total_count) + " Working on " + str(each) + " - Internal Server Error")
    log_file.write(str(each) + ", " + str(response.status_code) + ", " + "Internal Server Error")
    log_file.write("\n")
  else:
  	print(str(current_count) + "/"+ str(total_count) + " Working on " + str(each) + " - "+ str(response.json()))
  	log_file.write(str(each) + ", " + str(response.status_code) + ", " + response.json()[0])
  	log_file.write("\n")

log_file.write("\n")
log_file.write("Number of successful person removed: " + str(corrected_count)+"\n")
log_file.write("Number of entries proccessed: " + str(current_count))
log_file.close()