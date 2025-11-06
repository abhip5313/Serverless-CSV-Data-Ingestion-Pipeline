import boto3
import pymysql
import csv
import io

rds_host = "database endpoint" 
db_user = "username"
db_password = "Password"
db_name = "db name"
db_port = 3306


def lambda_handler(event, context):
    # Initialize S3 client
    s3 = boto3.client('s3')
    
    # Get bucket & object key from S3 event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    # Fetch CSV file from S3
    csv_file = s3.get_object(Bucket=bucket, Key=key)
    csv_content = csv_file['Body'].read().decode('utf-8').splitlines()
    
    # Connect to RDS
    try:
        conn = pymysql.connect(
            host=rds_host,
            user=db_user,
            password=db_password,
            database=db_name,
            port=db_port
        )
        cursor = conn.cursor()
        print("Connected to RDS successfully!")
    except Exception as e:
        print("ERROR: Could not connect to RDS")
        print(e)
        return {"status": "Error", "message": str(e)}
    
    # Read CSV and insert into RDS
    reader = csv.DictReader(csv_content)
    for row in reader:
        try:
            sql = "INSERT INTO users (id, name, email, age, city) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (row['id'], row['name'], row['email'], row['age'], row['city']))
        except Exception as e:
            print(f"Error inserting row {row}: {e}")
    
    conn.commit()
    cursor.close()
    conn.close()
    
    return {"status": "Success", "message": f"Processed file {key}"}
