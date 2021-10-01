#!/usr/bin/env python

"""find_node

Search a dict, list or tuple or any nested combination for a value, given a search path.
search path is a string composed of search keys separated by a path separator (defaults
to '.', can be overridden if '.' is a valid key value).

Will raise either KeyError or IndexError on search failure, or
ValueError if attempt to turn key into index fails because it's
not a valid index (not a number).
"""

def find_node(data, path, sep='.'):
    path_elements = path.split(sep)
    key = path_elements.pop(0)
    if type(data) in (list, tuple, str):
        key = int(key)
    elif type(data) is dict and key not in data.keys():
        key = int(key)
    remaining = data[key]
    if len(path_elements):
        return find_node(remaining, sep.join(path_elements))
    return remaining

"""test code for find_node

runs a series of queries, shows the reult and expected result
"""
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
            result = find_node(data, key)
        except (KeyError, ValueError, IndexError) as err:
            if type(err) is expected:
                print('pass')
            else:
                print(f'Caught {type(err)} on search of {data} using {key}  Expected: {expected}')
                print('fail')
        except Exception as err:
            print(f'Caught UNEXPECTED {type(err)} on search of {data} using {key}  Expected: {expected}')
            raise
        else:
            if result == expected:
                print('pass')
            else:
                print(f'retrieved {result} on search of {data} using {key}  Expected: {expected}')
                print('fail')

