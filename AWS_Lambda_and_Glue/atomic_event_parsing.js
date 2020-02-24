'use strict';
console.log('Loading function');


exports.handler = (event, context, callback) => {
    let success = 0; // Number of valid entries found
    let failure = 0; // Number of invalid entries found

    /* Process the list of records and transform them */
    const output = event.records.map((record) => {
        // Kinesis data is base64 encoded so decode here
        console.log(record.recordId);
        const payload = (Buffer.from(record.data, 'base64')).toString('ascii');
        console.log('Decoded payload:', payload);

        // split payload into a list of events
        const lllist_event = JSON.parse(payload);
        console.log('lllist_event:', lllist_event);
        console.log('lllist_event.length:', lllist_event.length);
        console.log('typeof lllist_event:', typeof lllist_event);
        
        const list_event = JSON.parse(lllist_event);
        console.log('list_event:', list_event);
        console.log('list_event.length:', list_event.length);
        console.log('typeof list_event:', typeof list_event);
        
        var list_result = [];
        
        for(var i = 0; i < list_event.length; i++) {
            
            var   event  = list_event[i];
            const result = {};
            console.log('event:', event);
        
            for(var key_l1 in event){
        
                var isNested_l1 = Object.keys(event[key_l1]).some(function(key) {
                    return event[key_l1][key] && typeof event[key_l1][key] === 'object';
                });
        
                if(!isNested_l1){
                    var key_current_level = key_l1;
                    if(typeof event[key_l1] === 'object'){
                        for(var key_lower_level in event[key_l1]){
                            var full_key_lower_level = key_current_level + '.' + key_lower_level;
                            result[full_key_lower_level] = event[key_l1][key_lower_level];
                        }
                    } else {
                        result[key_current_level] = event[key_l1];
                    }
                } else {
                    for(var key_l2 in event[key_l1]){
        
                        var isNested_l2 = Object.keys(event[key_l1][key_l2]).some(function(key) {
                            return event[key_l1][key_l2][key] && typeof event[key_l1][key_l2][key] === 'object';
                        });
        
                        if(!isNested_l2){
                            var key_current_level = key_l1 + '.' + key_l2;
                            if(typeof event[key_l1][key_l2] === 'object'){
                                for(var key_lower_level in event[key_l1][key_l2]){
                                    var full_key_lower_level = key_current_level + '.' + key_lower_level;
                                    result[full_key_lower_level] = event[key_l1][key_l2][key_lower_level];
                                }
                            } else {
                                result[key_current_level] = event[key_l1][key_l2];
                            }
        
                        } else {
                            for(var key_l3 in event[key_l1][key_l2]) {
        
                                var isNested_l3 = Object.keys(event[key_l1][key_l2][key_l3]).some(function (key) {
                                    return event[key_l1][key_l2][key_l3][key] && typeof event[key_l1][key_l2][key_l3][key] === 'object';
                                });
        
                                if (!isNested_l3) {
                                    var key_current_level = key_l1 + '.' + key_l2 + '.' + key_l3;
                                    if(typeof event[key_l1][key_l2][key_l3] === 'object'){
                                        console.log(typeof event[key_l1][key_l2][key_l3]);
                                        for(var key_lower_level in event[key_l1][key_l2][key_l3]){
                                            var full_key_lower_level = key_current_level + '.' + key_lower_level;
                                            result[full_key_lower_level] = event[key_l1][key_l2][key_l3][key_lower_level];
                                        }
                                    } else {
                                        result[key_current_level] = event[key_l1][key_l2][key_l3];
                                    }
                                }
                            }
                        }
                    }
                }
            }
            
            console.log(result['timestamp']);
            result['event_year']  = result['timestamp'].substring(0,  4);
            result['event_month'] = result['timestamp'].substring(5,  7);
            result['event_day']   = result['timestamp'].substring(8, 10);
        
            console.log(result);
            success++;
            list_result.push(result);
        }
        
        console.log('list_result: ', list_result);
        console.log('JSON.stringify(list_result): ', JSON.stringify(list_result));
        console.log('typeof JSON.stringify(list_result): ', typeof JSON.stringify(list_result));
        
        
        console.log('Buffer.from(JSON.stringify(list_result))', Buffer.from(JSON.stringify(list_result)));
        console.log('(Buffer.from(JSON.stringify(list_result))).toString(base64)', (Buffer.from(JSON.stringify(list_result))).toString('base64'))
        
        var stringitied_list_result = JSON.stringify(list_result).replace(/^\[/, '').replace(/\]$/, '');
        var stringitied_list_result = stringitied_list_result.split("},{").join("}{");
        console.log('stringitied_list_result', stringitied_list_result);
        
        return {
            recordId: record.recordId,
            result:   'Ok',
            data:     (Buffer.from(stringitied_list_result)).toString('base64'),
        };
        
        
    });
    console.log(`Processing completed.  Successful records ${success}, Failed records ${failure}.`);
    callback(null, { records: output });
};
