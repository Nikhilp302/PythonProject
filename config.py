import psycopg2
import psycopg2.extras

#My PHPmyAdmin String
USERNAME = 'postgres'  # Replace with your master username 
PASSWORD = '12345'  # Replace with your RDS instance password
ENDPOINT = "localhost"  # Replace with your RDS endpointENDPOINT = "127.0.0.1"  # Replace with your RDS endpoint
PORT = 5432   # Replace with the RDS instance port
# REGION = "us-east-2a"  # Replace with your AWS region
DBNAME = 'KAAS'  # Replace with the name of your SCHEMA in MySQL workbench
# SSL_CA = "mysql-ssl-ca-cert.pem"  # Replace with the folder location of your SSL bundle
# CURSORCLASS = psycopg2.cursors.DictCursor  # No need to modify this
CURSORCLASS = psycopg2.extras.DictCursor

