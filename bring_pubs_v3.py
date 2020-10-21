from scholarly import scholarly
import re
import csv
import time

#Retrieve the author's data, fill-in, and print
search_query = scholarly.search_author('OnChip-UIS')
author = next(search_query).fill()
print(author)

#Extracting number of publications to retrieve
nopubs=len(author.publications)

#Variable to fill publications' information
pub=''

#Loop to progressively fill a csv file with the information related to the publications retrieved
with open('pubs_database.csv', 'w', newline='', encoding='utf-16') as csvfile:
    write = csv.writer(csvfile, delimiter=',')
    
    for i in range(0, nopubs-1):

        #Query from GScholar to fill information related to the i-th publication
        pub = author.publications[i].fill()
        print('Publication retrieved')

        #Processing the string retrieved from Google Scholar for an appropriate format
        lis=str(pub).splitlines()
        separator=''
        pre=re.sub('\s+',' ',separator.join(lis))
        pub_soup=re.sub("'\s'",'',pre)

        #Extracting title from publication soup
        m=re.search("'title': '(.*?)',",pub_soup)
        title=m.group(1)

        #Extracting authors from publication soup
        m=re.search("'author': '(.*?)',",pub_soup)
        auth=m.group(1)

        #Extracting conference/journal/book from publication soup
        if re.search("'conference': '(.*?)',",pub_soup):
            m=re.search("'conference': '(.*?)',",pub_soup)
            conference=m.group(1)

        elif re.search("""'conference': "(.*?)",""",pub_soup):
            m=re.search("""'conference': "(.*?)",""",pub_soup)
            conference=m.group(1)
            
        elif re.search("'journal': '(.*?)',",pub_soup):
            m=re.search("'journal': '(.*?)',",pub_soup)
            conference=m.group(1)

        elif re.search("""'journal': "(.*?)",""",pub_soup):
            m=re.search("""'journal': "(.*?)",""",pub_soup)
            conference=m.group(1)

        elif re.search("'book': '(.*?)',",pub_soup):
            m=re.search("'book': '(.*?)',",pub_soup)
            conference=m.group(1)

        elif re.search("""'book': "(.*?)",""",pub_soup):
            m=re.search("""'book': "(.*?)",""",pub_soup)
            conference=m.group(1)

        else:
            conference=''

        #Extracting cites from publication soup
        m=re.search("'cites': '(.*?)'",pub_soup)
        cites=m.group(1)

        #Extracting url from publication soup
        m=re.search("'url': '(.*?)'",pub_soup)
        url=m.group(1)

        #Extracting year from publication soup
        if re.search("'year': '(.*?)'",pub_soup):
            m=re.search("'year': '(.*?)'",pub_soup)
            year=m.group(1)
        else:
            year=''
        
        write.writerow([title, auth, conference, year, cites, url])
            
        time.sleep(60)
