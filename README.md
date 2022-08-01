# For this WBUR project, data is pull from the MySQL database:
There are 3 databses:\
civica_courtdocs\
wp_courtdocs\
wp_courtdocs_NORMALIZED

civica_courtdocs -> cases_masscourts_org is where you find all the court location, title of cases, types, status, status_date, file_date\
<b>NOTE: court_division and court_location are the same, so you can drop one of the either</b>\
cases_masscourts_org merge with cdocs_case_action_index on case_number.\
cdocs_party_index merge with cdocs_text_search_index on post_id.

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

