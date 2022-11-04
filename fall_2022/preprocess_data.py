"""
This file is use to preprocess the exported CSV data.
Since there exists data blobs in the CSV data, OpenRefine cannot correctly recognize it.

Field availiable:
[
'"id"', '"scrape_hash"', '"court_department"', 
'"court_division"', '"court_location"', '"case_title"', 
'"case_number"', '"case_type"', '"case_status"', 
'"case_judge"', '"dcm_track"', '"property_address"', 
'"parties"', '"judgments"', '"events"', 
'"docket_information"', '"case_disposition"', 
'"financial_summary"', '"receipts"', '"ticklers"', 
'"subsequent_action_subject"', '"linked_cases"', 
'"next_event"', '"status_date"', '"file_date"', 
'"scrape_script_parameters"', '"last_scraped_at"', '"last_migrated_at"']

Author: Zikun Wang
Date: 2022-10-6
"""

import csv
import json

data_path = "./data/cases_masscourts_org_sample_20000.json"
batch_size = 100

def pretty_json(s):
  return json.dumps(case_list[0], indent=4)

def addToDictCount(dict, e):
  if e in dict:
    dict[e] += 1
  else:
    dict[e] = 1

if __name__ == "__main__":
  
  # Open the input data
  header = []
  data = []

  with open(data_path, newline='') as f:
    raw_data = "".join([row for row in f])

  json_data = json.loads(raw_data)
  case_list = json_data["SELECT * FROM civica_courtdocs.cases_masscourts_org LIMIT 20000"]
  
  #print(case_list[0])
  #print(json.dumps(case_list[0], indent=4))

  # Parse the data

  # Get the data for number of cases with judgements
  case_with_judgement = [case for case in case_list if case['judgments'] != {}]
  #print(len(case_with_judgement))
  print(pretty_json(case_with_judgement[0]))
  print(case_with_judgement[0]['judgments'])
  




  pass
