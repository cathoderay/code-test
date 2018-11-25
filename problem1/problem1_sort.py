
def solve(l):
    """Returns the maximum product from 3 
    elements of a given list.

    Example:
        input: [1, 10, 2, 6, 5, 3]
        output: 300

    Assumptions:
        The input can contain any number 
        of integers and it raises an exception
        if the input has less than 3 values.

    Algorithm analysis:
        Sorting is n*logn 

        Space: O(n) (if you consider the input) 
        Time: O(n*logn)
    """

    if len(l) < 3:
        raise Exception
    
    l.sort()
    return max(l[0]*l[1]*l[-1], 
               l[-1]*l[-2]*l[-3])
