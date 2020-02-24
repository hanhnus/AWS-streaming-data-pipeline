import string
import random

def string_generator(size = 6, chars = string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def generate_json_event_string():
    json_event = '{'
    json_event = json_event + '"userId":"' + string_generator(10) + '",'
    json_event = json_event + '"event":"' + random.choice(['Card Created', 'Card Dismiss', 'Card Accepted', 'Card Rejected']) + '",'
    json_event = json_event + '"timestamp":"2012-' + random.choice(['01', '02', '03'])  # year & month
    json_event = json_event + '-' + random.choice(['10',   '20',  '25'])                   # day
    json_event = json_event + 'T' + random.choice(['08',   '12',  '16'])                   # hour
    json_event = json_event + ':' + random.choice(['15',   '30',  '45'])                   # minute
    json_event = json_event + ':' + random.choice(['15',   '30',  '45'])                   # second
    json_event = json_event + '.' + random.choice(['123', '456', '789']) + 'Z",'           # millisecond
    json_event = json_event + '"properties":{'   + random.choice(['"property_1":"p1"', '"property_2":"p2"', '"property_1":"p1","property_2":"p2"']) + '},'
    json_event = json_event + '"hostContext":{'  + random.choice(['"hostContext_1":"hc1"', '"hostContext_2":"hc2"', '"hostContext_1":"hc1","hostContext_2":"hc2"']) + '},'
    json_event = json_event + '"eventContext":{' + random.choice(['"ip":"12.34.56.78"', '"ip":"87.65.43.21"']) + ','
    json_event = json_event + '"eventOrigin":'   + random.choice(['"platform"', '"sdk"']) + ','
    json_event = json_event + '"eventActor":'    + random.choice(['"api"', '"platform"', '"endUser"', '"businessUser"']) + ','
    json_event = json_event + '"deviceContext":' + random.choice(['"iOS"', '"Android"']) + ','
    json_event = json_event + '"userLocalTimestamp":"2012-' + random.choice(['01', '02', '03'])  # year & month
    json_event = json_event + '-' + random.choice(['10',   '20',  '25'])                   # day
    json_event = json_event + 'T' + random.choice(['08',   '12',  '16'])                   # hour
    json_event = json_event + ':' + random.choice(['15',   '30',  '45'])                   # minute
    json_event = json_event + ':' + random.choice(['15',   '30',  '45'])                   # second
    json_event = json_event + '.' + random.choice(['123', '456', '789']) + 'Z"},'           # millisecond

    json_event = json_event + '"sdkContext":{"platform":' + random.choice(['"web"', '"ios"', '"android"']) + ','
    json_event = json_event + '"sdkVersion":'   + random.choice(['"1.20"', '"1.22"', '"2.01"']) + ','
    json_event = json_event + '"containerId":'   + random.choice(['3', '5', '7']) + ','
    json_event = json_event + '"isDnDActive":'   + random.choice(['true', 'false']) + '},'

    json_event = json_event + '"streamContext":{"streamId":' + random.choice(['2', '4', '6']) + ','
    json_event = json_event + '"streamName":'           + random.choice(['"My Stream"', '"His Stream"', '"Her Stream"']) + ','
    json_event = json_event + '"streamSize":'           + random.choice(['12', '24', '48']) + ','
    json_event = json_event + '"streamSizeVisible":'    + random.choice(['3', '6', '12']) + ','
    json_event = json_event + '"cardPositionInStream":' + random.choice(['1', '2', '3']) + '},'

    json_event = json_event + '"cardContext":{"cardInstanceId":"' + string_generator(7, string.ascii_uppercase + string.digits) + '",'
    json_event = json_event + '"cardInstanceStatus":'           + random.choice(['"active"', '"dismissed"', '"accepted"']) + ','
    json_event = json_event + '"cardReferrer":'           + random.choice(['"stream"', '"single"', '"custom"']) + ','
    json_event = json_event + '"cardTemplateId":'    + random.choice(['8', '16', '32']) + ','
    json_event = json_event + '"cardTmplateName":'           + random.choice(['"Overdue Fees"', '"Taxes"', '"Utility Bills"']) + ','
    json_event = json_event + '"cardTemplateType":'           + random.choice(['"basic"', '"others"']) + ','
    json_event = json_event + '"cardTemplateVersion":'    + random.choice(['1', '2', '3']) + ','
    json_event = json_event + '"cardPresentation":' + random.choice(['"bundle"', '"individual"']) + '},'


    json_event = json_event + '"triggerContext":{"triggerId":"' + string_generator(4, string.digits) + '",'
    json_event = json_event + '"triggerVersion":'           + random.choice(['1', '2', '3']) + ','
    json_event = json_event + '"triggerStreamId":'           + random.choice(['5', '6', '7']) + ','
    json_event = json_event + '"triggerStreamName":'    + random.choice(['"My Stream"', '"His Stream"', '"Her Stream"']) + ','
    json_event = json_event + '"triggerEventId":'           + random.choice(['2', '3', '4']) + ','
    json_event = json_event + '"triggerEventName":'           + random.choice(['"LateFees"', '"OtherFees"']) + ','
    json_event = json_event + '"triggerEventVersion":'    + random.choice(['1', '2', '3']) + ','
    json_event = json_event + '"triggerEventMetadata":{"A":"string","B":123},'
    json_event = json_event + '"triggerCardId":'           + random.choice(['8', '16', '32']) + ','
    json_event = json_event + '"triggerCardName":'    + random.choice(['"Overdue Fees"', '"Taxes"', '"Utility Bills"']) + ','
    json_event = json_event + '"triggerCardVersion":'           + random.choice(['1', '2', '3']) + ','
    json_event = json_event + '"triggerCardMetadata":{"C":666.53,"D":"meta"}}}'

    return json_event





sample_atomic_event = '['

for i in range(100):
    sample_atomic_event = sample_atomic_event + generate_json_event_string()
    if i < 99:
        sample_atomic_event = sample_atomic_event + ','

sample_atomic_event = sample_atomic_event + ']'

print(sample_atomic_event)

list_sample_atomic_event = [sample_atomic_event]






'''
sample_atomic_event = 
[{
    "userId":         "019mr8mf4r",
    "event":          "Card Created",
    "timestamp":      "2012-12-02T00:30:12.984Z",
    "properties":     {
                          "property_1":           "p1"
                      },
    "hostContext":    {
                          "hostContext_1":        "hc1"
                      },
    "eventContext":   {
                          "ip":                   "24.5.68.47",
                          "eventOrigin":          "platform",
                          "eventActor":           "api",
                          "deviceContext":        "[TBC user agent string or equiv]",
                          "userLocalTimestamp":   "2012-12-02T00:30:12.984Z"
                      },
    "sdkContext":     {
                          "platform":             "web", 
                          "sdkVersion":           "1.22",
                          "containerId":          4,
                          "isDnDActive":          false 
                      },
    "streamContext":  {
                          "streamId":             1,
                          "streamName":           "My Stream",
                          "streamSize":           12, 
                          "streamSizeVisible":    12, 
                          "cardPositionInStream": 3
                      },
    "cardContext":    {
                          "cardInstanceId":       "J87HJ21",
                          "cardInstanceStatus":   "active",
                          "cardReferrer":         "stream",
                          "cardTemplateId":       32,
                          "cardTemplateName":     "Overdue Fees",
                          "cardTemplateType":     "basic", 
                          "cardTemplateVersion":  2,
                          "cardPresentation":     "bundle"
                      },   
    "triggerContext": {
                          "triggerID":            2344,
                          "triggerVersion":       2,
                          "triggerStreamId":      3,
                          "triggerStreamName":    "My Stream",
                          "triggerEventId":       3,
                          "triggerEventName":     "LateFees",
                          "triggerEventVersion":  1,
                          "triggerEventMetadata": {
                                                      "A": "string",
                                                      "B": 123
                                                  },
                          "triggerCardId":        32,
                          "triggerCardName":      "Overdue Fees",
                          "triggerCardVersion":   2,
                          "triggerCardMetadata":  {
                                                       "C": 666.53,
                                                       "D": "meta"
                                                   }

                      }
}, 

{
    "userId":         "01wreth8mf4r",
    "event":          "Card Modified",
    "timestamp":      "2012-12-22T22:22:22.222Z",
    "properties":     {
                          "property_1":           "p1",
                          "property_2":           "p2"
                      },
    "hostContext":    {
                          "hostContext_1":        "hc1",
                          "hostContext_2":        "hc2"
                      },
    "eventContext":   {
                          "ip":                   "24.5.68.47",
                          "eventOrigin":          "sdk",
                          "eventActor":           "platform",
                          "deviceContext":        "[TBC user agent string or equiv]",
                          "userLocalTimestamp":   "2012-12-02T00:30:12.984Z"
                      },
    "sdkContext":     {
                          "platform":             "ios", 
                          "sdkVersion":           "1.22",
                          "containerId":          4,
                          "isDnDActive":          false 
                      },
    "streamContext":  {
                          "streamId":             1,
                          "streamName":           "My Stream",
                          "streamSize":           12, 
                          "streamSizeVisible":    12, 
                          "cardPositionInStream": 3
                      },
    "cardContext":    {
                          "cardInstanceId":       "J87HJ21",
                          "cardInstanceStatus":   "dismissed",
                          "cardReferrer":         "single",
                          "cardTemplateId":       32,
                          "cardTemplateName":     "Overdue Fees",
                          "cardTemplateType":     "basic", 
                          "cardTemplateVersion":  2,
                          "cardPresentation":     "individual"
                      },   
    "triggerContext": {
                          "triggerID":            2344,
                          "triggerVersion":       2,
                          "triggerStreamId":      3,
                          "triggerStreamName":    "My Stream",
                          "triggerEventId":       3,
                          "triggerEventName":     "LateFees",
                          "triggerEventVersion":  1,
                          "triggerEventMetadata": {
                                                      "A": "string",
                                                      "B": 123
                                                  },
                          "triggerCardId":        32,
                          "triggerCardName":      "Overdue Fees",
                          "triggerCardVersion":   2,
                          "triggerCardMetadata":  {
                                                       "C": 666.53,
                                                       "D": "meta"
                                                   }

                      }
}, 

{
    "userId":         "019333mf4r",
    "event":          "Card Created",
    "timestamp":      "2012-12-03T00:33:33.984Z",
    "properties":     {
                          "property_1":           "p1",
                          "property_2":           "p2",
                          "property_3":           "p3"
                      },
    "hostContext":    {
                          "hostContext_1":        "hc1",
                          "hostContext_2":        "hc2",
                          "hostContext_3":        "hc3"
                      },
    "eventContext":   {
                          "ip":                   "24.5.68.47",
                          "eventOrigin":          "platform",
                          "eventActor":           "endUser",
                          "deviceContext":        "[TBC user agent string or equiv]",
                          "userLocalTimestamp":   "2012-12-02T00:30:12.984Z"
                      },
    "sdkContext":     {
                          "platform":             "android", 
                          "sdkVersion":           "1.22",
                          "containerId":          4,
                          "isDnDActive":          false 
                      },
    "streamContext":  {
                          "streamId":             1,
                          "streamName":           "My Stream",
                          "streamSize":           12, 
                          "streamSizeVisible":    12, 
                          "cardPositionInStream": 3
                      },
    "cardContext":    {
                          "cardInstanceId":       "J87HJ21",
                          "cardInstanceStatus":   "active",
                          "cardReferrer":         "custom",
                          "cardTemplateId":       32,
                          "cardTemplateName":     "Overdue Fees",
                          "cardTemplateType":     "basic", 
                          "cardTemplateVersion":  2,
                          "cardPresentation":     "bundle"
                      },   
    "triggerContext": {
                          "triggerID":            2344,
                          "triggerVersion":       2,
                          "triggerStreamId":      3,
                          "triggerStreamName":    "My Stream",
                          "triggerEventId":       3,
                          "triggerEventName":     "LateFees",
                          "triggerEventVersion":  1,
                          "triggerEventMetadata": {
                                                      "A": "string",
                                                      "B": 123
                                                  },
                          "triggerCardId":        32,
                          "triggerCardName":      "Overdue Fees",
                          "triggerCardVersion":   2,
                          "triggerCardMetadata":  {
                                                       "C": 666.53,
                                                       "D": "meta"
                                                   }

                      }
}, 

{
    "userId":         "019444mf4r",
    "event":          "Card Created",
    "timestamp":      "2012-12-03T00:44:44.444Z",
    "properties":     {
                          "property_1":           "p1",
                          "property_2":           "p2",
                          "property_3":           "p3",
                          "property_4":           "p4"
                      },
    "hostContext":    {
                          "hostContext_1":        "hc1",
                          "hostContext_2":        "hc2",
                          "hostContext_3":        "hc3",
                          "hostContext_4":        "hc4"
                      },
    "eventContext":   {
                          "ip":                   "24.5.68.47",
                          "eventOrigin":          "sdk",
                          "eventActor":           "businessUser",
                          "deviceContext":        "[TBC user agent string or equiv]",
                          "userLocalTimestamp":   "2012-12-02T00:30:12.984Z"
                      },
    "sdkContext":     {
                          "platform":             "web", 
                          "sdkVersion":           "1.22",
                          "containerId":          4,
                          "isDnDActive":          false 
                      },
    "streamContext":  {
                          "streamId":             1,
                          "streamName":           "My Stream",
                          "streamSize":           12, 
                          "streamSizeVisible":    12, 
                          "cardPositionInStream": 3
                      },
    "cardContext":    {
                          "cardInstanceId":       "J87HJ21",
                          "cardInstanceStatus":   "dismissed",
                          "cardReferrer":         "stream",
                          "cardTemplateId":       32,
                          "cardTemplateName":     "Overdue Fees",
                          "cardTemplateType":     "basic", 
                          "cardTemplateVersion":  2,
                          "cardPresentation":     "individual"
                      },   
    "triggerContext": {
                          "triggerID":            2344,
                          "triggerVersion":       2,
                          "triggerStreamId":      3,
                          "triggerStreamName":    "My Stream",
                          "triggerEventId":       3,
                          "triggerEventName":     "LateFees",
                          "triggerEventVersion":  1,
                          "triggerEventMetadata": {
                                                      "A": "string",
                                                      "B": 123
                                                  },
                          "triggerCardId":        32,
                          "triggerCardName":      "Overdue Fees",
                          "triggerCardVersion":   2,
                          "triggerCardMetadata":  {
                                                       "C": 666.53,
                                                       "D": "meta"
                                                   }

                      }
}, 

{
    "userId":         "019mr8mf4r",
    "event":          "Card Created",
    "timestamp":      "2012-12-04T00:55:55.555Z",
    "properties":     {
                          "property_1":           "p1",
                          "property_2":           "p2",
                          "property_3":           "p3",
                          "property_4":           "p4",
                          "property_5":           "p5"
                      },
    "hostContext":    {
                          "hostContext_1":        "hc1",
                          "hostContext_2":        "hc2",
                          "hostContext_3":        "hc3",
                          "hostContext_4":        "hc4",
                          "hostContext_5":        "hc5"
                      },
    "eventContext":   {
                          "ip":                   "24.5.68.47",
                          "eventOrigin":          "platform",
                          "eventActor":           "api",
                          "deviceContext":        "[TBC user agent string or equiv]",
                          "userLocalTimestamp":   "2012-12-02T00:30:12.984Z"
                      },
    "sdkContext":     {
                          "platform":             "ios", 
                          "sdkVersion":           "1.22",
                          "containerId":          4,
                          "isDnDActive":          false 
                      },
    "streamContext":  {
                          "streamId":             1,
                          "streamName":           "My Stream",
                          "streamSize":           12, 
                          "streamSizeVisible":    12, 
                          "cardPositionInStream": 3
                      },
    "cardContext":    {
                          "cardInstanceId":       "J87HJ21",
                          "cardInstanceStatus":   "active",
                          "cardReferrer":         "single",
                          "cardTemplateId":       32,
                          "cardTemplateName":     "Overdue Fees",
                          "cardTemplateType":     "basic", 
                          "cardTemplateVersion":  2,
                          "cardPresentation":     "bundle"
                      },   
    "triggerContext": {
                          "triggerID":            2344,
                          "triggerVersion":       2,
                          "triggerStreamId":      3,
                          "triggerStreamName":    "My Stream",
                          "triggerEventId":       3,
                          "triggerEventName":     "LateFees",
                          "triggerEventVersion":  1,
                          "triggerEventMetadata": {
                                                      "A": "string",
                                                      "B": 123
                                                  },
                          "triggerCardId":        32,
                          "triggerCardName":      "Overdue Fees",
                          "triggerCardVersion":   2,
                          "triggerCardMetadata":  {
                                                       "C": 666.53,
                                                       "D": "meta"
                                                   }

                      }
}



]
'''