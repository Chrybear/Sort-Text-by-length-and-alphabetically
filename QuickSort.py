# Initially, I thought about sorting the list manually via quicksort
# Once for length, and again for alphabetical
# However, I found out python can do both of those things natively, and quite easily.

# !!!Currently does not work!!!
# May return and fix later, not needed for main python file.


# Quicksort method
def qSort(words, low, high, isLength):
    # words = array of words, low = starting index, high = ending index,
    # isLength is a boolean to check if we're sorting based on length or alphabetically
    if low < high:
        partition = getPartition(words, low, high, isLength)

        # recurse before the partition
        qSort(words, low, partition - 1, isLength)
        # recurse after the partition
        qSort(words, partition + 1, high, isLength)

# Partition methon
def getPartition(words, low, high, isLength):
    # words = array of words, low = starting index, high = ending index,
    # isLength is a boolean to check if we're sorting based on length or alphabetically

    # Get the pivot value
    piv = words[high]

    # Get index to the left of the pivot so far
    leftPiv = low - 1

    for x in range(low, high - 1):
        # First, check what we're testing on
        if isLength:
            # Is the value less than the pivot?
            if len(words[x]) < len(piv):
                # Increase left index
                leftPiv += 1
                # Swap the two positions since the new one is lower
                words[x], words[leftPiv] = words[leftPiv], words[x]
        else:
            # Is the value less than the pivot?
            if min(words[x].lower(), piv.lower) == piv.lower:  # need to make them lowercase for proper comparison
                # Increase left index
                leftPiv += 1
                # Swap the two positions since the new one is lower
                words[x], words[leftPiv] = words[leftPiv], words[x]

    # Swap the value to the right of leftPiv with the value at the index of high
    words[leftPiv + 1], words[high] = words[high], words[leftPiv + 1]
    # return the leftPiv + 1 index
    return leftPiv + 1

