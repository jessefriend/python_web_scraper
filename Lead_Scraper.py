'''
Created on Apr 17, 2018

@author: Jesse
'''
import urllib.request
from bs4 import BeautifulSoup as soup
import csv

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

def main():  
    #create url opener 
    opener = AppURLopener()
    
    #create csv to write out information, write out headers for file
    fp = open("Potential_Leads.csv", "a", newline='')
    headers = "Lead, Organization, Conference, URL\n"
    fp.write(headers)
    
    #change link to website you want to scrape
    link= 'awesome-website-for-leads.cooommm'
    
    #open it up
    open_url = opener.open(link)
    
    #opening connection, grabbing the page
    get_html = open_url.read()
    
    #html parsing
    soup_stuff = soup(get_html, "html.parser")
    
    #grab each parent element, change this according to how html elements are organized in desired page
    containers = soup_stuff.find_all("tr")
    
    #loop through and grab what we need, change lead_info to reflect child elements you wish to extract
    try: 
        
        for container in containers:
            lead_info = container.find_all("td")
            
            
            #some authors include non ascii characters 
            author = ''.join([i if ord(i) < 128 else ' ' for i in lead_info[0].text])
            if len(lead_info) > 1:
                company = lead_info[1].text
            
            if len(author) == 1:
                exit
            else:
                #write out info you want to csv
                csv_row = [author, company, "AWESOME WEBSITE", link]
                wr = csv.writer(fp, dialect='excel')
                wr.writerow(csv_row)
         
             
    except UnicodeEncodeError:
        pass    
         
    fp.close()
    
if __name__ == '__main__':   
    main()


