import json
import psycopg2

hostname     ="localhost"
DB_User     ="postgres"
DB_Password ="Jaga123143@"
database   ="demo"
DB_port     ="5432"

try:
  conn = psycopg2.connect(host = hostname, dbname= database, user=DB_User, password=DB_Password, port=DB_port)
  
  cur= conn.cursor()
  
  create_script='''CREATE TABLE details(
                    Product Id  uuid,
                    Product Title varchar(300) ,
                    Price  int)'''
  cur.execute(create_script)    
  conn.commit()            
  conn.close()
  
  
  print("database connected sucessfully")
except:
   print("database not connected")
   

    
    
with open('C:/Users/tharu/OneDrive/Desktop/penv prac/task 2/products-data.json') as f1:
    
    
    details = json.load(f1)
    for i in details:
        print(i['_id'],i["price"],i["title"])
        
