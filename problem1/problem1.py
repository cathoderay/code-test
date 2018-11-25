

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
        Loop-invariant: maxs always contains 
        the highest 3 numbers found till now and
        mins always contains the lowest 2 numbers
        found.

        Space: O(n) (if you consider the input) 
        Time: O(n)
    """

    if len(l) < 3:
        raise Exception

    maxs = l[:3]
    mins = l[:3]
    mins.remove(max(maxs))
    for n in l[3:]:
        if n > min(maxs):
            maxs.remove(min(maxs))
            maxs.append(n)
        if n < max(mins):
            mins.remove(max(mins))
            mins.append(n)
    return max(mins[0]*mins[1]*max(maxs), 
               maxs[0]*maxs[1]*maxs[2])
