import time
from oauth2client.service_account import ServiceAccountCredentials
import gspread

#구글 스프레드 시트 권한 취득
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'uipath_key1.json', scope)
gc = gspread.authorize(credentials)


# ss_id = '1N8aoWfR47zBa_p6w6JrsH7qYegcbkrZITGShYVaQ8jo'

# wks = gc.open(sheet_name).sheet1
# wks.update_cell()

wks = gc.open('test').worksheet('4')
list_of_lists = wks.get_all_values()
# wks.update_acell('B2', "it's down there somewhere, let me take another look.")

# a = wks.acell('B2').value
print(list_of_lists)
