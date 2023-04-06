from pprint import pprint

import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

from config import CREDENTIALS_FILE, SPREADSHEET_ID


############################################################### connextion to spreadsheet
credentials = ServiceAccountCredentials.from_json_keyfile_name(
        CREDENTIALS_FILE, 
        [
            'https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive'
        ])

httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)
###############################################################


def get_data():
    
    values = service.spreadsheets().values().get(
        spreadsheetId=SPREADSHEET_ID,
        range='A1:E10',
        majorDimension='COLUMNS'
    ).execute()
    pprint(values)