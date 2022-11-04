"""
Author: Zikun Wang
Date: 2022-10-30
"""

import pandas as pd
import pymysql
from sqlalchemy import create_engine

from pathlib import Path
from tqdm import tqdm

with open("./config/sql_login.txt", newline="") as f:
  sql_login = f.readline()
  
print(sql_login)

engine = create_engine(sql_login)

def query_company_name(name):
  print(f"{name}: start querying")

  query_name = "%" + name.replace(" ", "%") + "%"
  print(f"{name}: query name ({query_name})")

  sql_command = f'''
  SELECT ccmi.post_id, cpi.party_name , case_number, case_type, case_status, file_date, status_date
  FROM wp_courtdocs.cdocs_case_meta_index ccmi
  INNER JOIN wp_courtdocs.cdocs_party_assignment_index cpai ON ccmi.post_id = cpai.case_id 
  INNER JOIN wp_courtdocs.cdocs_party_index cpi ON cpi.post_id = cpai.party_id
  WHERE cpai.party_type LIKE '%Plaintiff%'
  	AND cpi.party_name LIKE '{query_name}'
  '''

  df = pd.DataFrame()
  for chunk in pd.read_sql(sql_command, engine, chunksize=50):
    df=pd.concat([df, chunk])

  print(f"{name}: finished querying, saving result.")
  file_name = name.replace(" ", "_")

  filepath = Path(f"./data/debt_collector_query_result/{file_name}.csv")
  filepath.parent.mkdir(parents=True, exist_ok=True)  
  df.to_csv(filepath)

  print(f"{name}: save complete.")

#with open("./data/debt_collector_query_result/wells_fargo.csv", "w") as f:

with open("./data/debt_collector_list/debt_collector_list_cleaned.csv") as f:
  n = 516
  counter = 1
  for company_name in f:
    name = company_name.strip("\n")
    query_company_name(name)
    print(f"Finished querying ({counter}/{n}): {name}")
    counter += 1

#conn = engine.connect()