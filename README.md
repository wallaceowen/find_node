# find_node

find_node: a convenience function for python data access

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
