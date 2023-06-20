import datetime,gspread,random
from oauth2client.service_account import ServiceAccountCredentials
import datetime
now = datetime.datetime.now()
date=now.strftime('%H:%M:%S')
str='23:00:00'
str1='absent'
str2='present'
#import emailing as em 

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)

client = gspread.authorize(creds)

sheet = client.open("Automate robot").get_worksheet(0)



def enroll_person_to_sheet(name,email):
    if date>str:
          
          nrows = len(sheet.col_values(1))
          pin=random.randint(999,9999)
          sheet.update_cell(nrows+1,1,name)
          sheet.update_cell(nrows+1,2,email)
          sheet.update_cell(nrows+1,3,date)
          sheet.update_cell(nrows+1,4,str1)
    else:
          nrows = len(sheet.col_values(1))
          pin=random.randint(999,9999)
          sheet.update_cell(nrows+1,1,name)
          sheet.update_cell(nrows+1,2,email)
          sheet.update_cell(nrows+1,3,date)
          sheet.update_cell(nrows+1,4,str2)
          

    
        
        
def write_to_sheet(name):
	
	namecell=sheet.find(name)
	sheet.update_cell(namecell.row)


	