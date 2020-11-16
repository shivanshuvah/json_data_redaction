# json_data_redaction
A python application to redact json data selectively along with nesting feature enabled

The  code is  used to redact certain information from a JSON.

Redacting means removing of the information without changing the structure of the information. The point is to not know what the information was, but ensure that we know that it was present.

The code allows nesting of the path to any degree.

Assumption :  The lists are always leaf nodes with primitive values i.e (string, float, int, bool).

If the path leads to a dict, no redaction should happen.

The paths variable uses a custom JSON path notation which uses:

1. the "." as a delimiter for every level of nesting

2. the "*" to indicate if all the elements in a list are subject to change

3. the "[0-9]+" i.e. positive digits to indicate a single element in the list that is subject to change

```
def redact_dict(input, path):
#main redaction function

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
    
```
