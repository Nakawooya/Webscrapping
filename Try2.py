from bs4 import BeautifulSoup;
import requests 
import csv

html_text = requests.get('https://edition.cnn.com/sport').text
soup = BeautifulSoup(html_text,'lxml')

Headlines = soup.find_all('div',class_ = 'card container__item container__item--type-section container_lead-plus-headlines-with-images__item container_lead-plus-headlines-with-images__item--type-section')
csv_file = open('_cms_file.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Article','link','picture'])

for Headline in Headlines:
 Article = Headline.find('div',class_ ='container__headline container_lead-plus-headlines-with-images__headline').text
#link = Headline.find('a',class_='container__link container_lead-plus-headlines-with-images__link container_lead-plus-headlines-with-images__left container_lead-plus-headlines-with-images__light')[href]
 image = Headline.find('div',class_ = 'image image__hide-placeholder image--eq-extra-small')
 link = Headline.a['href']
 picture = Headline.picture.img['src']
#print(image.text)
 print(f' Information: {Article} ')
 print(f'more : {link}')
 print(f'link :{picture}')
 
 #print()
 csv_writer.writerow([Article,link,picture])

csv_file.close()
