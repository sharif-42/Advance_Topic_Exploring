from collections import OrderedDict, Counter

if __name__ == "__main__":
    """
    OrderedDict is a dictionary where keys maintain the order in which they are inserted, which means if you change the
    value of a key later, it will not change the position of the key.
    """
    od = OrderedDict()
    od['a'] = 1
    od['b'] = 2
    od['c'] = 3
    print(od)

    """
    Following example is an interesting use case of OrderedDict with Counter. Here, we create a Counter from a list and 
    insert element to an OrderedDict based on their count.
    Most frequently occurring letter will be inserted as the first key and the least frequently occurring letter 
    will be inserted as the last key.
    """
    lst = ["a", "c", "c", "c", "b", "a", "a", "b", "c"]
    cnt = Counter(lst)
    od = OrderedDict(cnt.most_common())
    for key, value in od.items():
        print(key, value)
