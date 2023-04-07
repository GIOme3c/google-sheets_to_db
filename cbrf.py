from requests import request
# from lxml import etree
from pprint import pprint
import xmltodict


def get_usd_course():
    xml_response = request("GET","https://cbr.ru/scripts/XML_daily.asp")
    courses = xmltodict.parse(xml_response.text)['ValCurs']['Valute']
    # pprint(courses)
    for item in courses:
        if item['@ID'] == 'R01235':
            return float(item['Value'])

    

get_usd_course()