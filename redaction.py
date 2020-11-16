def redact_dict(input, path):
    levels=path.split(".") #get levels in a list
    endpoint=input
    for i in range(0,len(levels)):
            try:
                if type(endpoint[levels[i]]) is list:
                    if levels[i+1] == "*": # check the next level -> if all elements are to be changes
                        endpoint[levels[i]]=[perform_redaction(element) for element in endpoint[levels[i]]]
                        break
                    elif levels[i+1].isdigit(): #redact only a particular element
                        endpoint[levels[i]][int(levels[i+1])]=perform_redaction(endpoint[levels[i]][int(levels[i+1])])
                        break
                
                endpoint[levels[i]]=perform_redaction(endpoint[levels[i]])
                endpoint=endpoint[levels[i]] # update reference to next level
            except KeyError:
                break
            except IndexError:
                break

def perform_redaction(endpoint):
    if type(endpoint) is dict:
        return endpoint
    if type(endpoint) is list:
        return endpoint
    redacted_list=["*" for char in str(endpoint)]
    return "".join(redacted_list)



if __name__ == '__main__':
    input = {
        'm1': {
            'm2': {
                'm3': 55
            }
        },
        'ml': [False, 'bb', 'ccc'],
        'ml2': ['a', 'b', 'c']
    }

    paths = [
        'm1.m2.m3',
        'm2.m5',
        'ml.*',
        'ml.*.k9',
        'ml2.2',
        'ml2.2000',
    ]
    k = input
    for path in paths:
        redact_dict(input, path)
    
    assert k == {
        'm1': {
            'm2': {
                'm3': "**"
            }
        },
        'ml': ['*****', '**', '***'],
        'ml2': ['a', 'b', '*']
    }