from collections import namedtuple

if __name__ == '__main__':
    """
    The namedtuple() returns a tuple with names for each position in the tuple. One of the biggest problems with 
    ordinary tuples is that you have to remember the index of each field of a tuple object. This is obviously difficult.
    The namedtuple was introduced to solve this problem.
    """
    Student = namedtuple('Student', 'fname, lname, age')
    s1 = Student('John', 'Clarke', '13')
    print(s1)

    """
    Creating a namedtuple Using List
    The namedtuple() function requires each value to be passed to it separately. Instead, you can use _make() to create
    a namedtuple instance with a list. Check the following code:
    """
    s2 = Student._make(['Adam', 'joe', '18'])
    print(s2)
