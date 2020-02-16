from collections import Counter

if __name__ == '__main__':
    """
    Counter is a subclass of dictionary object. The Counter() function in collections module takes an iterable or a 
    mapping as the argument and returns a Dictionary. In this dictionary, a key is an element in the iterable or the 
    mapping and value is the number of times that element exists in the iterable or the mapping.
    """
    lst = [1, 6, 2, 6, 3, 3, 4, 4, 5, 5, 6]
    """
    this procedure return the total count of a number in the list
    """
    item_to_be_count = 3
    cnt = Counter(lst)
    print(cnt)

    print(lst[item_to_be_count])

    """
    The element() Function:
    You can get the items of a Counter object with elements() function. It returns a list containing all 
    the elements in the Counter object.
    """
    print(list(cnt.elements()))

    """
    The most_common() Function:
    The Counter() function returns a dictionary which is unordered. You can sort it according to the number of counts 
    in each element using most_common() function of the Counter object.
    """
    cnt = Counter(lst)
    print(cnt.most_common())

    """
    The subtract() Function
    The subtract() takes iterable (list) or a mapping (dictionary) as an argument and deducts elements count using
    that argument.
    """
    deduct = {1: 1, 2: 1}
    cnt.subtract(deduct)
    print(cnt)
