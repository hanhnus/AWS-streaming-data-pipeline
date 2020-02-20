sample_atomic_event = '''
{
"userId":         "019mr8mf4r",
"event":          "Card Created",
"timestamp":      "2012-12-02T00:30:12.984Z",
"properties":     {},
"hostContext":    {},
"eventContext":   {
    "ip":            "24.5.68.47",
    "eventOrigin":   "platform|sdk",
    "eventActor":    "api|platform|endUser|businessUser",
    "deviceContext": "[TBC user agent string or equiv]"
},
"sdkContext":     {
   "platform":    "web|ios|android", 
   "sdkVersion":  "1.22",
   "containerId": 4,
   "isDnDActive": false 
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
   "cardInstanceStatus":   "active|dismissed etc"
   "cardReferrer":         "stream|single|custom",
   "cardTemplateId":       32,
   "cardTemplateName":     "Overdue Fees",
   "cardTemplateType":     "basic", 
   "cardTemplateVersion":  2,
   "cardPresentation":     "bundle|individual"
},    
"triggerContext": {
   "triggerID":            2344,
   "triggerVersion":       2,
   "triggerStreamId":      3,
   "triggerStreamName":    "My Stream",
   "triggerEventId":       3,
   "triggerEventName":     "LateFees",
   "triggerEventVersion":  1
}
}
'''

list_sample_atomic_event = [sample_atomic_event]