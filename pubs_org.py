import csv
import ftplib

#Variables to save information related to publications and theses, with an appropriate format for HTML
pubs=''
theses=''

#Loop to retrieve information from the csv database, and sorting publications and theses
with open('pubs_database.csv', newline='', encoding='utf-16') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    pubs_count = 0
    th_count = 0
    for row in csv_reader:
        title=row[0]
        auth=row[1]
        conference=row[2]
        year=row[3]
        cites=row[4]
        url=row[5]
        if conference=='':
            theses+='<tr>\n<td style="text-align:left; border:none;">'+'<p><a href="'+url+'">'+title+'</a><br>'+auth+'<br>'+'Universidad Industrial de Santander, Bucaramanga, Colombia'+'</p></td>\n<td style="border:none;">'+year+'</td>\n</tr>'
            th_count += 1
        else:
            pubs+='<tr>\n<td style="text-align:left; border:none;">'+'<p><a href="'+url+'">'+title+'</a><br><font size = "2.5" color = "#808080">'+auth+'</font><br><font size = "2.5" color = "#808080">'+conference+'</font></p></td>\n<td style="border:none;">'+cites+'</td>\n<td style="border:none;">'+year+'</td>\n</tr>'
            pubs_count += 1
    print(f'Processed {pubs_count} publications and {th_count} theses.')


#HTML previously-tested code and format for publications
message = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"
  "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
    
    
<head>
<!--<meta charset="gb18030">-->
<!--<meta name="generator" content="jemdoc, see http://jemdoc.jaboc.net/" />-->
<meta charset="UTF-8">
<meta http-equiv="Content-type" content="text/html; charset=UTF-8">
<link rel="stylesheet" href="jemdoc.css" type="text/css" />
<style>
table {{
  width: 100%;
}}
th.citedby, th.year {{
  width: 10%
}}
</style>
<title>Publications</title>
</head>


<body>
<table summary="Table for page layout." id="tlayout">
<tr valign="top">
<td id="layout-menu">
<div class="menu-item"><a href="index.html">Home</a></div>
<div class="menu-category">Research</div>
<div class="menu-item"><a href="pubs_test.html" class="current">Publications</a></div>
<div class="menu-item"><a href="interface.html">High-Speed&nbsp;Interface</a></div>
<div class="menu-item"><a href="security.html">Security&nbsp;Circuits</a></div>
<div class="menu-item"><a href="open.html">Open&nbsp;-&nbsp;V</a></div>
<div class="menu-category">Outreach</div>
<div class="menu-item"><a href="teaching.html">Teaching</a></div>
<div class="menu-item"><a href="people.html">People</a></div>
<div class="menu-item"><a href="news.html">News</a></div>
<div class="menu-item"><a href="gallery.html">Gallery</a></div>
<div class="menu-item"><a href="contact.html">Contact</a></div>
</td>
<td id="layout-content">
<div id="toptitle">
<h1>Publications</h1>
</div>

<iframe style="margin-left:30%" src="https://www.onchipuis.io/citationschart.php?id=MC8gR0EAAAAJ&amp;lang=en" name="myiframe" border="0" width="100%" frameborder="0" height="300" allowtransparency="true"></iframe>

<script src="https://www.kryogenix.org/code/browser/sorttable/sorttable.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>

<link href="//maxcdn.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css" rel="stylesheet">

<table class="sortable" id="myTable" style="width:90%; text-align:center; border:none;">
  <tr>
    <th>Title, authors and conference/journal</th>
    <th class="citedby">Cited by</th>
    <th class="year">Year</th>
  </tr>
{0}
</table>

<script>
window.onload = function() {{
    (document.getElementsByTagName( 'th' )[2]).click();
    (document.getElementsByTagName( 'th' )[2]).click();
}};
</script>

<div id="footer">
<div id="footer-text">
Page generated 2020-05-13 19:10:05 Hora de verano romance, by <a href="http://jemdoc.jaboc.net/">jemdoc</a>.
</div>
</div>
</td>
</tr>
</table>
</body>
</html>"""

#Saving "message" code as an HTML file
message=message.format(pubs)
f = open('pubs_test.html','w',encoding='utf-8')
f.write(message)
f.close()

#HTML previously-tested code and format for theses
message_thes = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"
  "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
<head><meta charset="gb18030">
<meta name="generator" content="jemdoc, see http://jemdoc.jaboc.net/" />

<link rel="stylesheet" href="jemdoc.css" type="text/css" />
<title>Theses and reports</title>
</head>
<body>
 
<table summary="Table for page layout." id="tlayout">
<tr valign="top">
<td id="layout-menu">
<div class="menu-item"><a href="index.html">Home</a></div>
<div class="menu-category">Research</div>
<div class="menu-item"><a href="publications.html" class="current">Publications</a></div>
<div class="menu-item"><a href="interface.html">High-Speed&nbsp;Interface</a></div>
<div class="menu-item"><a href="security.html">Security&nbsp;Circuits</a></div>
<div class="menu-item"><a href="open.html">Open&nbsp;-&nbsp;V</a></div>
<div class="menu-category">Outreach</div>
<div class="menu-item"><a href="teaching.html">Teaching</a></div>
<div class="menu-item"><a href="people.html">People</a></div>
<div class="menu-item"><a href="news.html">News</a></div>
<div class="menu-item"><a href="gallery.html">Gallery</a></div>
<div class="menu-item"><a href="contact.html">Contact</a></div>
</td>
<td id="layout-content">
<div id="toptitle">
<h1>Theses and reports</h1>
</div>

<table style="width:90%; text-align:center; border:none;">
  <tr>
    <th>Title and authors</th>
    <th>Year</th>
  </tr>
{0}
</table>

<div id="footer">
<div id="footer-text">
Page generated 2020-05-13 19:10:05 Hora de verano romance, by <a href="http://jemdoc.jaboc.net/">jemdoc</a>.
</div>
</div>
</td>
</tr>
</table>
</body>
</html>"""

#Saving "message_thes" code as an HTML file
message_thes=message_thes.format(theses)
f = open('thes_test.html','w',encoding='utf-8')
f.write(message_thes)
f.close()

#Saving the HTML files into the website database
# session = ftplib.FTP('148.**.***.***','somebranch@example.com','password')
# file = open('pubs_test.html','rb')                  # file to send
# session.storbinary('STOR pubs_test.html', file)     # send the file
# file.close()                                    # close file and FTP
# session.quit()

# session = ftplib.FTP('148.**.***.***','somebranch@example.com','password')
# file = open('thes_test.html','rb')                  # file to send
# session.storbinary('STOR thes_test.html', file)     # send the file
# file.close()                                    # close file and FTP
# session.quit()
