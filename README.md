# g_scholar

This project is composed of: 

1) Two modified-library directories, which have to be placed in Lib/site-packages, and only work with Python 3. 

2) One python script "bring_pubs_v3.py" to retrieve all the publicacions information of a given Google Scholar username, and to put the information in a csv database file. 

3) One python script "pubs_org.py", which takes the information inside the csv database file, organizes it, and puts it inside a previously tested HTML template, with an 
appropriate format. Also, this script saves the HTML file with the publications info in a given website server, using the credentials given by the user.
