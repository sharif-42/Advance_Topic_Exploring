from collections import ChainMap

if __name__ == '__main__':
    """
    ChainMap is used to combine several dictionaries or mappings. It returns a list of dictionaries.
    """

    dict1 = {'a': 1, 'b': 2}
    dict2 = {'c': 3, 'b': 4}
    chain_map = ChainMap(dict1, dict2)
    print(chain_map.maps)

    """
    Another important point is ChainMap updates its values when its associated dictionaries are updated. 
    For example, if you change the value of 'c' in dict2 to '5', you will notice the change in ChainMap as well.
    """
    print(chain_map['b'])
    dict1['b'] = 5
    print(chain_map)
    print(chain_map['b'])

    """
    
    Getting Keys and Values from ChainMap
    You can access the keys of a ChainMap with keys() function. Similarly, you can access the values of elements with
    values() function, as shown below:
    """
    print(list(chain_map.keys()))
    print(list(chain_map.values()))

    """
    Adding a New Dictionary to ChainMap
    If you want to add a new dictionary to an existing ChainMap, use new_child() function. 
    It creates a new ChainMap with the newly added dictionary.
    """
    dict3 = {'e': 5, 'f': 6}
    new_chain_map = chain_map.new_child(dict3)
    print(new_chain_map)

