import requests
import json

from utilities.csv_reader                   import csv_reader
from utilities.atomic_event_array_generator import list_sample_atomic_event

def send_df_to_api_gateway(df, api_gateway_endpoint):

    count_sent_row = 0

    # loop over the data records received
    for _, row in df.iterrows():

        # join the values in each row by a '|'
        # an AWS Lambda function is setup to decode the string to JSON
        string_row_values = '|'.join(str(value) for value in row)
        # 2006/01/01 00:00:00|3108 OCCIDENTAL DR|3|3C|1115|10851(A)VC TAKE VEH W/O OWNER|2404|38.55042047|-121.3914158|2020/02/15 14:27:19

        # create a dict object for each row
        json_data_record = {
            "Data":         string_row_values,
            "PartitionKey": 1                   # tell Kinesis which shard to use
        }
        print(json_data_record)

        # json.dumps(): dumps dict object to string
        # send the request to API gateway URL
        response = requests.put(url  = api_gateway_endpoint,
                                data = json.dumps(json_data_record))
        print("Response: %s" % response.text)

        count_sent_row = count_sent_row + 1

    # the count of records pushed
    print('Total Records sent to Kinesis: {0}'.format(count_sent_row))


def send_atomic_event_to_api_gateway(list_json_events, api_gateway_endpoint):

    count_sent_event = 0

    # loop over the data records received
    for json_event in list_json_events:

        # create a dict object for each row
        json_data_record = {
            "Data":         json_event,
            "PartitionKey": 1                   # tell Kinesis which shard to use
        }
        print(json_data_record)

        # json.dumps(): dumps dict object to string
        # send the request to API gateway URL
        response = requests.put(url  = api_gateway_endpoint,
                                data = json.dumps(json_data_record))
        print("Response: %s" % response.text)

        count_sent_event = count_sent_event + 1

    # the count of records pushed
    print('Total Event Records sent to Kinesis: {0}'.format(count_sent_event))

# main function
def main():

    # define API gateway endpoint
    api_gateway_endpoint = "https://qfdspt15lk.execute-api.ap-southeast-2.amazonaws.com/test/streams/kinesis-data-stream-atomic/record"

    # read data
    #df = csv_reader('crime.csv')

    # send data to API gateway
    #send_df_to_api_gateway(df, api_gateway_endpoint)

    # send auto-generated Atomic events JSON string to API gateway
    send_atomic_event_to_api_gateway(list_sample_atomic_event, api_gateway_endpoint)


if __name__ == "__main__":
    main()
