from pprint import pprint

import httplib2
from apiclient import discovery
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
sheet_service = discovery.build('sheets', 'v4', http = httpAuth)
drive_service = discovery.build('drive', 'v3', http = httpAuth)
###############################################################

def get_page_token():
    page_token = drive_service.changes().getStartPageToken().execute().get("startPageToken")
    return page_token


def get_data():
    values = sheet_service.spreadsheets().values().get(
        spreadsheetId=SPREADSHEET_ID,
        range='A1:E10',
    ).execute()
    return values['values']


if __name__ == "__main__":
    get_data()