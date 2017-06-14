# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful
import scraperwiki
import lxml.html
import urlparse
import scraperwiki
import urllib2
import lxml.etree
import mechanize

#next_link = 0

def scrape_table(root):
    #create a record to hold the data
    record = {}
    #grab all table rows <tr> in table class="tblSearchResults"
    rows = root.cssselect("table.caseStyle tr")
    #for each row, loop through this
    for row in rows:
        #create a list of all cells <td> in that row
        table_cells = row.cssselect("td")
        if table_cells: 
        #if there is a cell, record the contents in our dataset, the first cell [0] in 'recipient' and so on
            record['Case Style'] = table_cells[0].text_content()
            record['Date Filed and Judge'] = table_cells[1].text_content()
            #record['Case Number'] = table_cells[0].strong.text_content()
            #this line adds 1 to the ID no. we set at 0 earlier
            #idno=idno+1
            #record['ID'] = idno 
            print record, '------------'
    rows2 = root.cssselect("table.CountDescription tr")
    #create a record to hold the data
    #record = {}
    #for each row, loop through this
    for row2 in rows2[0:-1]:
        #create a list of all cells <td> in that row
        table_cells = row2.cssselect("td")
        if table_cells: 
        #if there is a cell, record the contents in our dataset, the first cell [0] in 'recipient' and so on
            record['Charge'] = table_cells.text_content()
            #record['Date Filed and Judge'] = table_cells[1].text_content()
            #this line adds 1 to the ID no. we set at 0 earlier
            #idno=idno+1
            #record['ID'] = idno 
            print record, '------------'
            # Save the record to the datastore - 'ID' is our unique key - 
    scraperwiki.sqlite.save(['Date Filed and Judge'], record)
           
            



'''br = mechanize.Browser()
br.set_handle_robots( False )
br.open("http://www.oscn.net/dockets/Search.aspx")
for f in br.forms():
    print f

formcount=0
for frm in br.forms():  
    if frm.attrs[class] == "search-form":
        break
        formcount=formcount+1
        br.select_form(nr=formcount)
#br.select_form('form')
        br.form[ 'db' ] = ['garfield',]

#Get the search results

        br.submit()

br.select_form(nr=0)
print br.form
br['db'] = ['garfield']
br['dcct'] = ['31']
br['FiledDateL'] = str('01/01/2011')
print br
response = br.submit()
print response
html = response.read()
print html
root = lxml.html.fromstring(html)
scrape_table(root)'''


'''case_numbers =['5237521','5244439','5237629','5237823','5234026']
55 #go through the schoolIDs list above, and for each ID...
56 for item in schoolIDs:
57 #show it in the console
58 print item
59 #create a URL called 'next_link' which adds that ID to the end of the base_url variable
60 next_link = base_url+item+'.html'
61 #pass that new concatenated URL to a function, 'scrape_page', which is scripted above
62 scrape_page(next_link)'''


'''def addNumbers(num)
    sum=0
    for i in range(0,num+1)
        sum=sum+i
    return sum'''

'''def Add_Case_No():
    for i in range(1,744):
        global next_link
        nextlink = 0
        next_link= next_link + i
    return next_link    
    print next_link'''


def scrape_and_look_for_next_link(url):
    html = scraperwiki.scrape(url)
        #print html
    root = lxml.html.fromstring(html)
    scrape_table(root)
    global i
    i = (i + 1)  
    next_url = base_url+'GetCaseInformation.aspx?db=garfield&number=CF-2011-'+str(i)
    print next_url
    scrape_and_look_for_next_link(next_url)

# ---------------------------------------------------------------------------
# START HERE: define your starting URL - then 
# call a function to scrape the first page in the series.
# ---------------------------------------------------------------------------
base_url = 'http://www.oscn.net/dockets/'
starting_url = urlparse.urljoin(base_url, 'GetCaseInformation.aspx?db=garfield&number=CF-2011-1')
print starting_url
global i
for i in range(1,10):
    #There are 743 cases but 468 appears to be the server request limit
    scrape_and_look_for_next_link(starting_url)     
    
    
# # Read in a page
# html = scraperwiki.scrape("http://foo.com")
#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
