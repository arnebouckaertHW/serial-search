def search (a, first: int, size: int, target: int):
    """Search for a desired element in a list of elements
    starting at a a[first]

    Args:
        a (int): the list to search
        first (int): the list index to start searching
        size (int): the number of elements to search
        target (int): the element to search for

    Returns:
        int: If target appears in the list, the index of the element
        that contains the target, else -1
    """    
    # set an int variable i to 0
    i = 0

    # set a boolean variable found to False
    found = False

    # while there are more elements to search
    # and the target has not been found
    while i < size and not found:
        # if the current element is the target
        if a[first + i] == target:
            # set found to True
            found = True
        # otherwise
        else:
            # increment i
            i += 1

    # check if the target was found
    if found:
        # return the index of the target
        return first + i
    else:
        # return negative one
        return -1
    