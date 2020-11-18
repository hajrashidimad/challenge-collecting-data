from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome(ChromeDriverManager().install())

# we will open the browser with chrome on the page that we will scrappe the data,
browser.get("https://immo.vlan.be/fr/immobilier?propertytypes=appartement,maison&transactiontypes=a-vendre,en-vente-publique&propertysubtypes=appartement,rez-de-chaussee,duplex,penthouse,studio,loft,triplex,maison,villa,immeuble-mixte,maison-de-maitre,fermette,bungalow,chalet,chateau&countries=belgique&pageOffset=2&noindex=1")

# waiting 3 second to avoid any problem cause internet connection,
browser.implicitly_wait(3)

browser.find_element_by_id("didomi-notice-agree-button").click()
browser.implicitly_wait(3)

# we accept the cookies,
browser.find_element_by_id("didomi-notice-agree-button").click()
browser.implicitly_wait(3)

# search the value of href in the page,
elements = browser.find_elements_by_xpath('//*[@href]')

# a for loop that get the URL which contains the data,without repeated link
repeat = []
for x in elements:
    number = 0
    y = x.get_attribute('href')
    if "detail" in y and y not in repeat:
        repeat.append(y)
        with open("detail.csv","a") as detail_url:
            detail_url.write(f"\n \n {y}")