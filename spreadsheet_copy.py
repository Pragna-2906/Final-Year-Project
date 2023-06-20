import datetime,gspread,random
from oauth2client.service_account import ServiceAccountCredentials
import datetime
now = datetime.datetime.now()
date=now.strftime('%H:%M:%S')
str='23:00:00'
str2='absent'
str1='present'
#import emailing as em 
id_1='Pragna'
id_2='Parnab'
id_3='Suman'
id_4='Swapnamoy'
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)

client = gspread.authorize(creds)

sheet = client.open("Data").get_worksheet(0)
#print(len(sheet.col_values(1)))


def enroll_person_to_sheet(name,email):
    if date<str:
          sheet.update_cell(1,2,'Name')
          #sheet.update_cell(1,2,'Email')
          sheet.update_cell(1,7,'LastPresentTime')
          #sheet.update_cell(1,4,'Status')

          if name==id_1:
                nrows = len(sheet.col_values(1))
                #pin=random.randint(999,9999)
                #sheet.update_cell(nrows+1,1,name)
                #sheet.update_cell(2,2,email)
                sheet.update_cell(2,7,date)
                #sheet.update_cell(12,4,str1)
          elif name==id_2:
                nrows = len(sheet.col_values(1))
                #pin=random.randint(999,9999)
                #sheet.update_cell(nrows+1,1,name)2
                #sheet.update_cell(34,2,email)
                sheet.update_cell(3,7,date)
                #sheet.update_cell(2,4,str1)      
      
          elif name==id_3:
                nrows = len(sheet.col_values(1))
                #pin=random.randint(999,9999)
                #sheet.update_cell(nrows+1,1,name)
                #sheet.update_cell(4,2,email)
                sheet.update_cell(4,7,date)
                #sheet.update_cell(3,4,str1)
          elif name==id_4:
                nrows = len(sheet.col_values(1))
                #pin=random.randint(999,9999)
                #sheet.update_cell(nrows+1,1,name)
                #sheet.update_cell(6,2,email)
                sheet.update_cell(5,7,date)
                #sheet.update_cell(1,4,str1)
          else:
                nrows = len(sheet.col_values(1))
                #pin=random.randint(999,9999)
                #sheet.update_cell(nrows+1,1,name)
                #sheet.update_cell(6,2,email)
                sheet.update_cell(6,7,date)
                #sheet.update_cell(1,4,str1)
  #  else:
          #nrows = len(sheet.col_values(1))
          #pin=random.randint(999,9999)
          #sheet.update_cell(nrows+1,1,name)
          #sheet.update_cell(nrows+1,2,email)
          #sheet.update_cell(nrows+1,3,date)
          #sheet.update_cell(nrows+1,4,str2)
          

    
        
        
def write_to_sheet(name):
	
	namecell=sheet.find(name)
	sheet.update_cell(namecell.row)


	