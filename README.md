
# For this WBUR project, data is pull from the MySQL database:
There are 3 databses:\
civica_courtdocs\
wp_courtdocs\
wp_courtdocs_NORMALIZED

civica_courtdocs -> cases_masscourts_org is where you find all the court location, title of cases, types, status, status_date, file_date\
<b>NOTE: court_division and court_location are the same, so you can drop one of the either</b>\

You'll be using wp_courtdocs the most:\
cdocs_case_action_index\
cdocs_case_meta_index\
cdocs_party_assignment_index\
cdocs_party_index

wp_courtdocs -> cdocs_case_meta_index is where you find all the post_id, case_number, case_type, case_status\
wp_courtdocs -> cdocs_case_action_index is where you find action of each cases.

cases_masscourts_org <b>merge</b> with cdocs_case_action_index on case_number and <b>map</b> judge_id with _tmp_judges. 
cdocs_party_index <b>merge</b> with cdocs_text_search_index on post_id.

Some of the codes are written by python and basic SQL. Since theres no jupyter notebooks for SQL, Below are the SQL codes that I used.

For SQL command:\
Main used:\
<b>SELECT</b> col, <b>COUNT(col)</b>\
<b> FROM </b> name_of_table\
<b>GROUP BY</b> col

<b> SELECT </b> *\
<b>FROM name_of_table </b>

Filtering:

<b> SELECT </b> col\
<b>WHERE col = (something) </b>\
<b> FROM </b> name_of_table


# Content

One notebook is preliminary analysis on Mass Court Data, done at week1.

The second notebook Bank_Plaintiff_Proportion.ipynb investigates proportion of banks as plaintiff from 2005-2022. 

The third notebook Judges_Devision.ipynb classfies judges with different categories. 
