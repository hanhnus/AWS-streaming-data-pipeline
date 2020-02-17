# Streaming Data Pipeline - AWS Deployment

[![standard-readme compliant](https://img.shields.io/badge/AWS-Kinesis-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)
[![standard-readme compliant](https://img.shields.io/badge/AWS-Lambda-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)
[![standard-readme compliant](https://img.shields.io/badge/AWS-S3-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)
[![standard-readme compliant](https://img.shields.io/badge/AWS-Glue-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)
[![standard-readme compliant](https://img.shields.io/badge/AWS-Athena-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

## Architecture
<img src="https://github.com/hanhnus/streaming_data_pipeline_AWS_deployment/blob/master/image/AWS_Architecture.png"/>

## Table of Contents

- [Background](#background)
- [Feature](#feature)
- [Installation (Docker Deployment)](#installation)
- [Usage](#usage)
	- [UI in Browser](#Access-the-Sentiment-Analysis-UI-in-Browser)
	- [cURL Request in Terminal](#Send-cURL-Request-in-Terminal)
- [Testing](#API-testing)
	- [Unit Testing (pytest)](#Unit-Testing-pytest)
	- [API Testing (Swagger UI)](#API-Testing-Swagger-UI)
- [Running in AWS](#Running-in-AWS)
- [Maintainers](#maintainers)
- [Contributing](#contributing)

## Background

The streaming data pipeline in this repo is to simulate Atomic app sending cards/events data to Kinesis Data Stream by making API call. A sample data set ([Crime Records in Sacramento](http://samplecsvs.s3.amazonaws.com/SacramentocrimeJanuary2006.csv)) in CSV format is selected in this demo due to its variety of data types in different columns, including datetime, string, int, double and struct.

## Feature

- User Interface in Browser (Flask Framework)
- JSON Interaction through Terminal (cURL)
- Requests Error Handling
- Unit Testing (Pytest)
- API Testing (Swagger UI)
- Logging
- Docker Deployment
- Healthcheck
- AWS Deployment

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
* Source: Kinesis Data Stream
* Data Transformation: defined Lambda function
* Destination: S3 bucket
* Source Backup: backup S3 bucket

|                     |                         |
| ---                 | ---                     |
| Source              | Kinesis Data Stream     |
| Data Transformation | defined Lambda function |
| Destination         | S3 bucket               |
| Source Backup       | backup S3 bucket        |













## Usage

### Access the Sentiment Analysis UI in Browser
```
http://localhost:32768
http://127.0.0.1:32768
```
The port to access can be checked by running:
```
docker port sentiment_analysis 
```

#### Sample Response
<img src="https://github.com/atomic-app/sentiment-docker/blob/master/images/UI_browser.png" width="600"/>


### Send cURL Request in Terminal
```
curl --header "Content-Type: application/json"    \
     --request POST                               \
     --data '{"sentence":"I love dog."}'          \
     http://localhost:32768/curl
```

```
curl --header "Content-Type: application/json" --request POST --data '{"sentence":"I love dog."}' http://localhost:32768/curl
```
#### Sample Response

<img src="https://github.com/atomic-app/sentiment-docker/blob/master/images/cURL_request.png" width="500"/>


## API Testing

### Unit Testing (pytest)

Run test case in PyCharm Terminal:
```
pytest -vv --disable-warnings
```


Tests cover:  

&emsp; - empty payload  
&emsp; - more than one element in payload (variances & cases in different sequences are also tested)  
&emsp;&emsp;&emsp; -- same key, same value  
&emsp;&emsp;&emsp; -- same key, diff value  
&emsp;&emsp;&emsp; -- diff key, same value  
&emsp;&emsp;&emsp; -- diff key, diff value  
&emsp; - one element in payload, but the key is not "sentence"  
&emsp; - JSON Decode Errors  
&emsp;&emsp;&emsp; -- value is not string  
&emsp;&emsp;&emsp; -- key is not string  
&emsp; - ML model tests  

<img src="https://github.com/atomic-app/sentiment-docker/blob/master/images/unit_test_result.png"/>

### API Testing (Swagger UI)

A bad request, as an example, is tested in Swagger UI as showed below (which contains no English letter in the input sentence), the correct error code and error message are responded.

<img src="https://github.com/atomic-app/sentiment-docker/blob/master/images/swager_API_test_1.png"/>

<img src="https://github.com/atomic-app/sentiment-docker/blob/master/images/swager_API_test_2.png"/>

## Running in AWS

<img src="https://github.com/atomic-app/sentiment-docker/blob/master/images/access_service_thr__public_IP_(AWS).png"/>

### AWS Deployment

https://github.com/atomic-app/sentiment-docker/blob/master/AWS_Deployment/README.md

## Maintainers

[@HanHan](https://github.com/hanhnus).

## Contributing

Feel free to dive in! [Open an issue](https://github.com/atomic-app/sentiment-docker/issues/new) or submit PRs.
 
