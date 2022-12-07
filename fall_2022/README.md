# xc410-dara-process

Auther: Zikun Wang

This is a repository to record the method of how to clean and process the data.
And other miscellaneous stuff.

## File structure
There are three secondary folders under this main folder:
1. config: the configration files for access the data base.
2. data: the queryed data (deleted) and the analyzed data after query.
3. process: images output.

## Import data

Currently we are interested in the `cases_masscourts_org` table inside `civica_courtdocs` database.
The current operation is on a subset of the original data (20,000 rows out of 3,000,000 rows).

SQL to get the sample data: `SELECT * FROM civica_courtdocs.cases_masscourts_org LIMIT 20000`. And the sample data is stored in CSV format locally.

## Collecting debt collector informations

### Step 1: Get the name list of all MA debt collectors.

First we want to gather all the names of legal Mass debt collectors. We found two lists on mass.org from different years (2018 and 2022):
1. `fall_2022/data/debt_collector_list/debt-collector-licensee-download-07012018.xlsx`
2. `fall_2022/data/debt_collector_list/Debt%20Collector%209.30.2022.xlsx`

Then we merged the list of debt collectors into a single csv file: `fall_2022/data/debt_collector_list/debt_collector_list_uncleaned.csv`

To make the name easier to be correlated with the database, and to avoid duplication, we uses the script `clean_debt_collector_name.py` under the main entry to get a cleaned version of names: `fall_2022/data/debt_collector_list/debt_collector_list_cleaned.csv`.

### Step 2: query the relavent entries from the database

In this step we uses the file `auto_connect.py` to access the database and store the result locally for further investigation. This file accesses the database using the key stored under `config` folder and query down all the debt collector cases using the name list from the previous step.

The result will be stored under `data/debt_collector_query_result` folder in csv form. Each file will represent a registered debt collector.

### Step 3: analyzing the query result.

In `debt-collector-info_analysis.ipynb`, it reads the data from previous steps and generates basic information such as case counting, case types, case status for each debt collectors.

In `debt-collector-case-by-day-in-2020.ipynb`, we focuses on the case entries that happens in 2020. It generates bar graphs such as the case count by day. We want to find out did the debt collectors followed the government regulation during COVID.

## Investigating Bank as plantiff

TODO