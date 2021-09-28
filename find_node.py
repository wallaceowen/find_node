#!/usr/bin/env python

"""find_node

Search a dict, list or tuple or any nested combination for a value, given a search path.
search path is a string composed of search keys separated by a path separator (defaults
to '.', can be overridden if '.' is a valid key value).

For example: find_node(data, "dbtables.flow_table.temperatures.7") returns 101.5

with data:
    {
        'dbtables': {
            'film_table': {
            },
            'flow_table': {
                'chemistry': 4,
                'temperatures': [68.2, 71.4, 88.3, 89.5, 93.3, 98.1, 100.2, 101.5, 106.1],
                'stock': {'chem1': 5, 'chem2': 4, 'chem3': 11 },
            }
            'cart_table': {
                'allergens': 4,
                'stipple_intervals': {'brown': 0, 'blue': 4.4, 'red': 9.1 },
                'fish': ['mars', 'spud', 'neo'],
            }
        }
    }


Will raise either KeyError or IndexError on search failure, or
ValueError if attempt to turn key into index fails because it's
not a valid index (not a number).
"""

def find_node(data, path, sep='.'):
    if not len(path):
        return data
    path_elements = path.split(sep)
    key = path_elements[0]
    if type(data) in (list, tuple, str):
        key = int(key)
    elif type(data) is dict and key not in data.keys():
        key = int(key)
    if len(path_elements) > 1:
        return find_node(data[key], sep.join(path_elements[1:]))
    else:
        return data[key]


if __name__ == '__main__':

    tests = (
        # data, key, expected result
        ( {'a': {'b': {'c': 'd'}, 'e': 1} }, 'a.b.c', 'd'),
        ( ['a', ['b', 'c', ['d', 'e', 'f', 'g']]], "1.2.3", 'g'),
        ( ['a', ['b', 'c', ['d', 'e', 'f', 'g']]], "1.b.3", ValueError),
        ( ['a', ['b', 'c', 'defg']], "1.2.3", 'g'),
        ( ['a', {'2': {3: '4'}}], "1.2.3", '4'),
        ( ['a', {'2': {3: '4'}}], "1.2.4", KeyError),
        ( {'a': ['first', {'c': 'd'}]}, "a.1.c", 'd'),
        ( {'a': ['first', {'c': 'd'}]}, "a.2.c", IndexError),
    )

    for test in tests:
        try:
            data, key, expected = test
            foo = find_node(data, key)
        except (KeyError, ValueError, IndexError) as err:
            print(f'Caught {type(err)} on search of {data} using {key}.  Expected: {expected}')
        except Exception as err:
            print(f'Caught UNEXPECTED {type(err)} on search of {data} using {key}.  Expected: {expected}')
        else:
            print(f'retrieved {foo} on search of {data} using {key}.  Expected: {expected}')

