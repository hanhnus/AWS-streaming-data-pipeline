# Streaming Data Pipeline - AWS Deployment

[![standard-readme compliant](https://img.shields.io/badge/AWS-Kinesis-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)
[![standard-readme compliant](https://img.shields.io/badge/AWS-Lambda-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)
[![standard-readme compliant](https://img.shields.io/badge/AWS-S3-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)
[![standard-readme compliant](https://img.shields.io/badge/AWS-Glue-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)
[![standard-readme compliant](https://img.shields.io/badge/AWS-Athena-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

## Architecture
<img src="https://github.com/hanhnus/streaming_data_pipeline_AWS_deployment/blob/master/image/AWS_Architecture.png"/>

## Table of Contents

- [Background](#Background)
- [Pipeline](#Pipeline)
	- [Send data to AWS Kinesis Data Stream](#Send-data-to-AWS-Kinesis-using-Python)
	- [AWS Kinesis Delivery Stream](#Delivery-data-from-Data-Stream-to-S3-bucket-through-Delivery-Stream-with-Lambda-data-transformation)
	- [Lambda function](#Lambda-function-decoding)
	- [AWS Glue](#AWS-Glue)
	- [AWS Athena](#AWS-Athena)
- [Maintainers](#maintainers)
- [Contributing](#contributing)

## Background

The streaming data pipeline in this repo is to simulate Atomic app sending cards/events data to Kinesis Data Stream by making API call and the following data processing and query in AWS. A sample data set ([Crime Records in Sacramento](http://samplecsvs.s3.amazonaws.com/SacramentocrimeJanuary2006.csv)) in CSV format is selected in this demo due to its variety of data types in different columns, including datetime, string, int, double and struct. In a later stage, the cards/events real-time streaming data can be send to Kinesis Data Stream, which will replace the "local PC" part in above diagram.

## Pipeline

### Send data to AWS Kinesis using Python
<img src="https://github.com/hanhnus/streaming_data_pipeline_AWS_deployment/blob/master/image/AWS_Kinesis_Data_Stream.png"  width="300"/>

A [Python script](https://github.com/hanhnus/streaming_data_pipeline_AWS_deployment/blob/master/stream_data_to_Kinesis.py) is built to 
1. Read raw data from CSV file into DataFrame
2. Encode the data items from String to bytes
3. Encapsulate the encoded bytes together with the corresponding partition keys in a JSON list (after reading certain amount of data items, eg. every 50 rows)
4. Send the JSON lists to Kinesis Data Stream by making API call periodically

### Delivery data from Data Stream to S3 bucket through Delivery Stream (with Lambda data transformation)
<img src="https://github.com/hanhnus/streaming_data_pipeline_AWS_deployment/blob/master/image/AWS_Kinesis_Data_Firehose_Deliverty_Stream.png"  width="600"/>

A Kinesis Data Firehose Delivery Stream is set up to delivery the streaming data:
* **Source:**              Kinesis Data Stream
* **Data Transformation:** defined [Lambda function](https://github.com/hanhnus/streaming_data_pipeline_AWS_deployment/blob/master/payload_decoding.js)
* **Destination:**         S3 bucket
* **Source Backup:**       backup S3 bucket

### Lambda function (decoding)
Since the data items are encoded from String to bytes in Python script, the payload received in AWS Kinesis need to be decoded to JSON format. The process is done in AWS Lambda through Javascript Lambda Function code:
https://github.com/hanhnus/streaming_data_pipeline_AWS_deployment/blob/master/payload_decoding.js

### AWS Glue
<img src="https://github.com/hanhnus/streaming_data_pipeline_AWS_deployment/blob/master/image/AWS_S3_Glue_Athena.png" width="280"/>

An AWS Glue ETL job is set up to keep the schema of the source data and create a new dataset in Parquet format:
* **Data Source:**  JSON format data in S3 bucket
* **Data Target:**  Parquet format data in S3 bucket
* **Schema:**       Keep unchanged

<img src="https://github.com/hanhnus/streaming_data_pipeline_AWS_deployment/blob/master/image/AWS_Glue.png" width="400"/>

AWS Glue ETL script: https://github.com/hanhnus/streaming_data_pipeline_AWS_deployment/blob/master/AWS_Glue_ETL_script.py

### AWS Athena

Query the top 10 records in the Parquet table generated in the previous step:

<img src="https://github.com/hanhnus/streaming_data_pipeline_AWS_deployment/blob/master/image/AWS_Athena_query_result.png"/>

## Maintainers

[@HanHan](https://github.com/hanhnus).

## Contributing

Feel free to dive in! [Open an issue](https://github.com/atomic-app/sentiment-docker/issues/new) or submit PRs.
 
