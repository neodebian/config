import suds
from suds.client import Client
#import logging
import requests
#from bs4 import BeautifulSoup
from openpyxl import Workbook

#Excel 
workbook = Workbook()
sheet = workbook.active
filename = "dictionnaire.xlsx"


#logging.basicConfig(level=logging.INFO)
#logging.getLogger('suds.client').setLevel(logging.DEBUG)
#logging.getLogger('suds.transport').setLevel(logging.DEBUG)
#logging.getLogger('suds.xsd.schema').setLevel(logging.DEBUG)
#logging.getLogger('suds.wsdl').setLevel(logging.DEBUG)
page = requests.get('https://www.google.fr/search?sxsrf=ALeKk002BSi8kvmKCj8j3RX6vHy-EdMXNw%3A1587240083564&source=hp&ei=k1ybXqSkIJyBjLsPr86J-Aw&q=dragon&oq=dragon&gs_lcp=CgZwc3ktYWIQAzIECAAQQzIECAAQQzIECAAQQzIECAAQQzIECAAQQzIECAAQQzIECAAQQzIECAAQQzIECAAQQzIECAAQQzoHCCMQ6gIQJzoECCMQJzoGCCMQJxATOgIIADoFCAAQgwFQ74QfWKSZH2Cenh9oAHAAeACAAeQBiAHSBZIBBTUuMS4xmAEAoAEBqgEHZ3dzLXdperABCg&sclient=psy-ab&ved=0ahUKEwjkueiK4vLoAhWcAGMBHS9nAs8Q4dUDCAY&uact=5')
#soup = BeautifulSoup(page.content,'html.parser')

#title = soup.find(id="rcnt")

#print(soup.get_text())

user='jga'
password='ccmpw5$$'
url = 'https://p4p-sogeclair-recette.cloud-horoquartz.fr:443/P4p/services/ExternalWebServiceV2'
wsdl = 'file:///home/neodebian/projetPython/tuto/externalSquirelWebServicesV2.wsdl'
client = Client(wsdl, location=url,)

def request_data():
    data = client.service.getAvailablesData(user,password)
    last_param = 0
    for parametre in data.data:
        if last_param != parametre.id:
         print(str(parametre.id) + " " + parametre.label)
        last_param = parametre.id

def request_resource():
    dataRessource = client.service.getAvailablesResourcesTypes(user,password)
    last_paramRessource = 0
    for parametreRessource in dataRessource.resourcesTypes:
        if last_paramRessource != parametreRessource.id:
            print(str(parametreRessource.id) + " " + parametreRessource.label)
        last_param = paccmpw5$$rametreRessource.id

def request_data_resource(resourcesTypes):
    idx=1
    data = client.service.getAvailablesDataForResourceType(user,password,resourcesTypes)
    last_param = 0
    print ('données de ressource')
    for parametre in data.data:
        if last_param != parametre.id:
         print(str(parametre.id) + " " + parametre.label + " " + str(parametre.type))
         last_param = parametre.id
         idx += 1



request_resource()
request_data_resource(99)


workbook.save(filename)
