from concurrent.futures import ThreadPoolExecutor
from threading import Thread
from utils import LinkThread,DetailsThread
import csv


# houseSubTypeStart = 72
# aptSubTypeStart = 10
# house_url = []
# apt_url = []
# for i in range(33):
#      house_url.append('https://www.zimmo.be/fr/biens/?status=1&type%5B0%5D=5&subType%5B0%5D='+str(houseSubTypeStart)+'&hash=eaaefff3761dbc9ada3a877ef9184200&priceIncludeUnknown=1&priceChangedOnly=0&bedroomsIncludeUnknown=1&bathroomsIncludeUnknown=1&constructionIncludeUnknown=1&livingAreaIncludeUnknown=1&landAreaIncludeUnknown=1&commercialAreaIncludeUnknown=1&yearOfConstructionIncludeUnknown=1&epcIncludeUnknown=1&queryCondition=and&includeNoPhotos=1&includeNoAddress=1&onlyRecent=0&onlyRecentlyUpdated=0&isPlus=0&region=none#gallery')
#      houseSubTypeStart += 1
# for i in range(4):
#     apt_url.append('https://www.zimmo.be/fr/biens/?status=1&type%5B0%5D=1&subType%5B0%5D='+str(aptSubTypeStart)+'&hash=aef0530b2cb50bf0b51f00277f373d22&priceIncludeUnknown=1&priceChangedOnly=0&bedroomsIncludeUnknown=1&bathroomsIncludeUnknown=1&constructionIncludeUnknown=1&livingAreaIncludeUnknown=1&landAreaIncludeUnknown=1&commercialAreaIncludeUnknown=1&yearOfConstructionIncludeUnknown=1&epcIncludeUnknown=1&queryCondition=and&includeNoPhotos=1&includeNoAddress=1&onlyRecent=0&onlyRecentlyUpdated=0&isPlus=0&region=none#gallery')
#     aptSubTypeStart += 1
# for url in apt_url:
#     thread_aptSubTypeStart = LinkThread(url)
#     thread_aptSubTypeStart.start()
    # Computer friendly uncomment it if you don't want to see your cpu burn in the flames of thread.
#     thread_aptSubTypeStart.join()
    # told u !
csv_file = open('list_of_datas.csv', 'a')

csv_writer = csv.writer(csv_file)



#creating headlines of the table
csv_writer.writerow(['Locality', 'Type of property', 'Subtype of property', 'Price (€)', 'Type of sale',
                   'Number of rooms', 'Area (m²)', 'Fully equipped kitchen', 'Furnished', 'Open fire',
                   'Terrace', 'Garden', 'bathroom','Surface area of the plot of land (m²)', 'Number of facades',
                   'Swimming pool', 'State of the building'])

with open("zimmo_details_link.csv", "r") as a_file:
     with ThreadPoolExecutor(max_workers=1) as executor:
          for num,line in enumerate(a_file):
               stripped_url = line.strip()
               thread_num = DetailsThread(stripped_url)
               executor.submit(thread_num.run)
               # Computer friendly uncomment it if you don't want to see your cpu burn in the flames of thread.
    