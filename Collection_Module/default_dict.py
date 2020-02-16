from collections import defaultdict

if __name__ == "__main__":
    """
    The defaultdict works exactly like a python dictionary, except for it does not throw KeyError when you try 
    to access a non-existent key.

    Instead, it initializes the key with the element of the data type that you pass as an argument at the creation 
    of defaultdict. The data type is called default_factory.
    """

    nums = defaultdict(int)
    nums['one'] = 1
    nums['two'] = 2
    print(nums['one'])
    """
    In this example, int is passed as the default_factory. Notice that you only pass int, not int(). 
    Next, the values are defined for the two keys, namely, 'one' and 'two', but in the next line we try to access a 
    key that has not been defined yet.
    """

    """
    For example, let's say you want the count of each name in a list of names given as "Mike, John, Mike, Anna, Mike, 
    John, John, Mike, Mike, Britney, Smith, Anna, Smith".
    """
    count = defaultdict(int)
    names_list = "Mike John Mike Anna Mike John John Mike Mike Britney Smith Anna Smith".split()
    for names in names_list:
        count[names] += 1
    print(count)
