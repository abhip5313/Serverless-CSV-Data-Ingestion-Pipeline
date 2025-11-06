# Serverless-CSV-Data-Ingestion-Pipeline

Deploy Serverless csv data ingestion Pipeline 


1. Setup RDS MySQL Database:
   - Create a database mysql "csv_ingest_db"
   - Connect this database with MySQL workbench
   - Create a table with columns exists in csv file

2. Create S3 Bucket with name "csv_ingest_bucket"

2. Create Project Folder Locally:
   - `package/` will contain Python dependencies.
  
3. Install Dependencies:
   - Run `pip3 install pymysql -t package/` to install PyMySQL for Lambda.
   
5. Package Lambda Function:
   - Zip the `package/` folder
   
6. Deploy Lambda:
   - Create Function Function 
   - Runtime: Python 3.13
   - Attach IAM Role with S3 and RDS access.
   - Deploy python code
   - Add Layer and upload zip file and attach this layer to function

7. Configure VPC (if RDS is private):
   - Lambda must be in the same VPC/subnets as RDS.
   - Security group must allow outbound on port 3306.

8. Add S3 Trigger:
   - Trigger Lambda when a CSV file is uploaded in s3
   - Event type: "put".

9. Test the Pipeline:
   - Upload a sample CSV to S3:
