import boto3            # AWS SDK for Python
import pandas   as pd
import datetime as dt


# function to create a client with aws for a specific service and region
def create_client(service, region):
    return boto3.client(service, region_name = region)


# function to correctly display numbers in 2 value format (i.e. 06 instead of 6)
def lengthen(value):
    if len(value) == 1:
        value = "0" + value
    return value


# function for generating new runtime to be used for time field in ES
def get_now():
    now   = str(dt.datetime.now())
    year    = now[:4]
    month   = now[5:7]
    day     = now[8:10]
    hour    = now[11:13]
    minutes = now[14:16]
    seconds = now[17:19]
    # return a date string in the correct format for ES
    return "%s/%s/%s %s:%s:%s" % (year, month, day, hour, minutes, seconds)


# to modify the format of datetime
def transform_datetime(df):

    dates = df['cdatetime']  # get the datetime field
    new_dates  = []

    # loop over all records
    for date in dates:
        date    = date.replace('/', '-')     # replace the slash with dash
        date    = date + ":00"               # add seconds to the datetime
        split   = date.split(" ")            # split the datetime
        date    = split[0]                   # get just date
        months  = date.split('-')[0]         # get months
        days    = date.split('-')[1]         # days
        years   = "20" + date.split('-')[2]  # years
        time    = split[1]                   # get time
        hours   = time.split(':')[0]         # get hours
        minutes = time.split(':')[1]         # get minutes
        seconds = time.split(':')[2]         # get seconds

        # build up a string in the right format
        new_datetime = years + "/" + lengthen(months)  \
                             + "/" + lengthen(days)    \
                             + " " + lengthen(hours)   \
                             + ":" + lengthen(minutes) \
                             + ":" + seconds

        # add it the list
        new_dates.append(new_datetime)

    # update the datetime with the transformed version
    df['cdatetime'] = new_dates

    return df


# to send data to Kinesis
def send_kinesis(kinesis_client, kinesis_stream_name, kinesis_shard_count, data):

    list_json_kinesis_data_stream_record  = []   # empty list to store data
    (rows, columns)                = data.shape  # get rows and columns off provided data
    total_num_bytes_string_rows    = 0           # counter for bytes
    rowCount                       = 0           # as we start with the first
    totalRowCount                  = rows        # using our rows variable we got earlier
    fSendKinesis                   = False       # flag to update when it's time to send data
    shardCount                     = 1           # shard counter

    # loop over each of the data rows received
    for _, row in data.iterrows():

        # join the row_values together by a '|'
        string_row_values = '|'.join(str(value) for value in row)
        # 2006/01/01 00:00:00|3108 OCCIDENTAL DR|3|3C|1115|10851(A)VC TAKE VEH W/O OWNER|2404|38.55042047|-121.3914158|2020/02/15 14:27:19

        # encode the string to bytes
        encoded_row_values = bytes(string_row_values, 'utf-8')
        # b'2006/01/01 00:00:00|3108 OCCIDENTAL DR|3|3C|1115|10851(A)VC TAKE VEH W/O OWNER|2404|38.55042047|-121.3914158|2020/02/15 14:25:51'


        # create a dict object for each row
        json_kinesis_data_stream_record = {
            "Data":         encoded_row_values,  # data byte-encoded
            "PartitionKey": str(shardCount)      # some key used to tell Kinesis which shard to use
        }

        list_json_kinesis_data_stream_record.append(json_kinesis_data_stream_record)             # add the object to the list

        num_bytes_string_row_values = len(string_row_values.encode('utf-8'))                     # get the number of bytes from the string
        # 136

        total_num_bytes_string_rows = total_num_bytes_string_rows + num_bytes_string_row_values  # count the total bytes

        # check conditional whether ready to send
        if len(list_json_kinesis_data_stream_record) == 50:   # if 50 records are packed up, then proceed
            fSendKinesis = True  # set the flag

        if total_num_bytes_string_rows > 50000:               # if the byte size is over 50000, proceed
            fSendKinesis = True  # set the flag

        if rowCount == totalRowCount - 1:                     # if the last record in the results is reached
            fSendKinesis = True  # set the flag

        # if the flag is set
        if fSendKinesis == True:

            # put the records to kinesis
            response = kinesis_client.put_records(
                Records    = list_json_kinesis_data_stream_record,
                StreamName = kinesis_stream_name
            )
            print(response)

            # resetting row_values ready for next loop
            list_json_kinesis_data_stream_record = []     # empty array
            fSendKinesis                         = False  # reset flag
            total_num_bytes_string_rows          = 0      # reset bytecount

            # increment shard count after each put
            shardCount = shardCount + 1

            # if it's hit the max, reset
            if shardCount > kinesis_shard_count:
                shardCount = 1

        # regardless, make sure to incrememnt the counter for rows.
        rowCount = rowCount + 1

    # log out how many records were pushed
    print('Total Records sent to Kinesis: {0}'.format(totalRowCount))


# main function
def main():

    print("Start Time: " + str(dt.datetime.now()))

    # create a client representing Amazon Kinesis in region ap-southeast-2
    kinesis = boto3.client('kinesis',
                           region_name = 'ap-southeast-2')

    # load in data from the csv
    df = pd.read_csv('crime.csv')
    # columns: cdatetime | address | district | beat | grid | crimedescr | ucr_ncic_code | latitude | longitude

    # modify the date and add loadtime field
    df = transform_datetime(df)

    # send the data to Kinesis Data Stream
    stream_name        = "kinesis-data-stream3-python"
    stream_shard_count = 1

    send_kinesis(kinesis, stream_name, stream_shard_count, df)  # send

    # log time
    print("Finished Time: " + str(dt.datetime.now()))


if __name__ == "__main__":
    main()