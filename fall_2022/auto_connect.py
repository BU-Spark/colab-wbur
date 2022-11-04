import pandas as pd
import pymysql
from sqlalchemy import create_engine

with open("./config/sql_login.txt", newline="") as f:
  sql_login = f.readline()

engine = create_engine(sql_login)

sql_command = '''
SELECT ccmi.post_id, cpi.party_name , case_number, case_type, case_status, file_date, status_date
FROM wp_courtdocs.cdocs_case_meta_index ccmi
INNER JOIN wp_courtdocs.cdocs_party_assignment_index cpai ON ccmi.post_id = cpai.case_id 
INNER JOIN wp_courtdocs.cdocs_party_index cpi ON cpi.post_id = cpai.party_id
WHERE cpai.party_type LIKE '%Plaintiff%'
	AND cpi.party_name LIKE '%wells%fargo%'
'''

df = pd.read_sql(sql_command, engine) #read the entire table



print(df)

#conn = engine.connect()