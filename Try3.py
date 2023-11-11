from bs4 import BeautifulSoup;
import requests 
#import time
import csv




html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

soup = BeautifulSoup(html_text,'lxml')

jobs = soup.find_all('li',class_ = 'clearfix job-bx wht-shd-bx')
csv_file = open('_cms_scrape.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['companyname','skills Required','informationn'])
for job in jobs:
    published_date = job.find('span', class_ ='sim-posted').span.text
    if 'few' in published_date:
      company_name = job.find('h3',class_ = 'joblist-comp-name').text.replace(' ','')
      skills = job.find('span',class_ = 'srp-skills').text.replace(' ','')
      more_info = job.header.h2.a['href']
      print(f"company {company_name}")
      print(f"skills {skills}")
      print(f"information {more_info}")
      print(
         
      )

    csv_writer.writerow([company_name,skills,more_info])

csv_file.close()
          
         

        
    #print(published_date)


    #print(f'''
    #company Name:{company_name}
    #Required Skills: {skills}
        #   ''')   
    
            
#if __name__ == '__main__':
 #while True:
  # find_jobs()
   #time_wait = 10
   #print(f'waiting {time_wait} minutes...')
   #time.sleep(time_wait * 60)
