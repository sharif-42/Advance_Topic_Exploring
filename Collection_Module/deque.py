from collections import deque

if __name__ == '__main__':
    """
    The deque is a list optimized for inserting and removing items.
    """
    lst = ["a", "b", "c"]
    deq = deque(lst)
    print(deq)

    """
    Inserting Elements to deque
    You can easily insert an element to the deq we created at either of the ends. To add an element to the right of 
    the deque, you have to use append() method.
    
    If you want to add an element to the start of the deque, you have to use appendleft() method.
    """
    deq.append("d")
    deq.appendleft("e")
    print(list(deq))

    """
    Removing Elements from the deque
    Removing elements is similar to inserting elements. You can remove an element the similar way you insert elements. 
    To remove an element from the right end, you can use pop() function and to remove an element from left, 
    you can use popleft().
    """
    deq.pop()
    print(deq)
    deq.popleft()
    print(deq)
    """
    Counting Elements in a deque
    If you want to find the count of a specific element, use count(x) function. You have to specify the element 
    for which you need to find the count, as the argument.
    """
    print(deq.count("a"))

    """
    Clearing a deque
    If you want to remove all elements from a deque, you can use clear() function.
    """
    print(deq)
    print("Deq ", deq.clear())
    print(deq)
