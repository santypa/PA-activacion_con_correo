from dotenv import load_dotenv
import os 

load_dotenv()

MYSQL_HOSTMANE= os.environ.get('MYSQL_HOSTMANE')
MYSQL_USERNAME= os.environ.get('MYSQL_USERNAME')
MYSQL_PASSWORD= os.environ.get('MYSQL_PASSWORD')
MYSQL_DATABASE= os.environ.get('MYSQL_DATABASE')
MYSQL_PORT= os.environ.get('MYSQL_PORT')

SMTP_HOSTNAME=os.environ.get('SMTP_HOSTNAME')
SMTP_PASSWORD=os.environ.get('SMTP_PASSWORD')
SMTP_USERNAME=os.environ.get('SMTP_USERNAME')

