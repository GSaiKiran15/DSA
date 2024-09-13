list1 = []
list2 = []

p1 = 0
p2 = 0

# doesn't work for linked lists as we are using len() which we can't in LinkedList

output = []
print(min(list1, list2))
while p1 < len(list1) and p2 < len(list2):
    if list1[p1] >= list2[p2]:
        output.append(list2[p2])
        p2 += 1
    elif list1[p1] < list2[p2]:
        output.append(list1[p1])
        p1 += 1
if p1 < len(list1):
    output.extend(list1[p1:])
elif p2 < len(list2):
    output.extend(list2[p2:])
print(output)

# Best Solution


dummy = list  # ListNode() as we dont have this class
tail = dummy

while list1 and list2:  # as we come to end of an list it stops
    if list1.val < list2.val:
        tail.next = list1.val
    elif list1.val > list2.val:
        tail.next = list2.val
    tail = tail.next
if list1:
    tail.next = list1
elif list2:
    tail.next = list2
print(dummy.next)

# Explanation:
# Dummy Node:

# dummy is a placeholder node with no value ( or a default value). It's used to simplify the logic of merging two lists. This allows you to avoid having to check whether you're adding the first node to the list or any subsequent nodes.
# Tail Pointer:

# tail starts by pointing to dummy, and it is used to build the merged list by appending nodes from either list1 or list2 to tail.next. The tail pointer advances as nodes are added.
# Why dummy.next:

# Since dummy is just a placeholder node with no meaningful value, the actual merged list starts from dummy.next.
# The dummy node simplifies the process by providing a reference point to build the list, but it’s not part of the final merged list.
# Example:
# Suppose you are merging two linked lists:

# list1: 1 -> 3 -> 5
# list2: 2 -> 4 -> 6
# After merging, the resulting list will look like this:

# dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> 6
# The dummy node is just a placeholder. The actual merged list starts at dummy.next, which points to 1. Therefore, you return dummy.next to skip over the dummy node and return the correct merged list.

# Final Merged List:
# By returning dummy.next, the merged list that is returned will be:


# 1 -> 2 -> 3 -> 4 -> 5 -> 6
# This approach is common when working with linked lists to handle edge cases, such as empty lists or merging multiple lists, without needing to check for special conditions at the start.

# Purpose of tail:
# tail is a pointer that always points to the last node in the merged list as it is being constructed.
# Its job is to keep track of where the next node should be added as you merge elements from list1 and list2.
# Step-by-Step Breakdown with Example:
# Suppose we are merging:

# list1: 1 -> 3 -> 5
# list2: 2 -> 4 -> 6
# Initially, we have:

# dummy: A dummy node created as dummy = ListNode().
# tail: A pointer that initially points to the dummy node (i.e., tail = dummy).
# Step 1: Compare list1.val (1) and list2.val (2)
# Since list1.val (1) is smaller, we:
# Set tail.next = list1, meaning the tail now points to 1.
# Move list1 to the next node (list1 = list1.next, now list1 points to 3).
# Move tail to the next node (tail = tail.next, now tail points to the node with value 1).
# Now the list looks like this:

# bash
# Copy code
# dummy -> 1
# tail ----^
# Step 2: Compare list1.val (3) and list2.val (2)
# Since list2.val (2) is smaller this time, we:
# Set tail.next = list2, meaning the tail now points to 2.
# Move list2 to the next node (list2 = list2.next, now list2 points to 4).
# Move tail to the next node (tail = tail.next, now tail points to the node with value 2).
# Now the list looks like this:

# rust
# Copy code
# dummy -> 1 -> 2
#               tail ----^
# Step 3: Compare list1.val (3) and list2.val (4)
# Since list1.val (3) is smaller, we:
# Set tail.next = list1, so the tail now points to 3.
# Move list1 to the next node (list1 = list1.next, now list1 points to 5).
# Move tail to the next node (tail = tail.next, now tail points to 3).
# Now the list looks like this:

# rust
# Copy code
# dummy -> 1 -> 2 -> 3
#                     tail ----^
# Step 4: Compare list1.val (5) and list2.val (4)
# Since list2.val (4) is smaller, we:
# Set tail.next = list2, so the tail now points to 4.
# Move list2 to the next node (list2 = list2.next, now list2 points to 6).
# Move tail to the next node (tail = tail.next, now tail points to 4).
# Now the list looks like this:

# rust
# Copy code
# dummy -> 1 -> 2 -> 3 -> 4
#                           tail ----^
# Step 5: Compare list1.val (5) and list2.val (6)
# Since list1.val (5) is smaller, we:
# Set tail.next = list1, so the tail now points to 5.
# Move list1 to the next node (list1 = list1.next, now list1 is None since we reached the end).
# Move tail to the next node (tail = tail.next, now tail points to 5).
# Now the list looks like this:

# rust
# Copy code
# dummy -> 1 -> 2 -> 3 -> 4 -> 5
#                                 tail ----^
# Step 6: Append Remaining Nodes
# At this point, list1 is None, but list2 still has one more element (6). The while loop ends, and in the following part of the code:

# python
# Copy code
# if list1:
#     tail.next = list1
# elif list2:
#     tail.next = list2
# Since list2 is not None, we set tail.next = list2, linking 6 to the end of the merged list.

# The final list now looks like this:

# rust
# Copy code
# dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> 6
#                                         tail ----^
# Returning the Result:
# Finally, we return dummy.next to skip over the dummy node and return the actual head of the merged list:

# rust
# Copy code
# 1 -> 2 -> 3 -> 4 -> 5 -> 6
# Key Takeaways for tail:
# The tail pointer always points to the last node of the merged list.
# It ensures that the new nodes from either list1 or list2 are appended correctly.
# After each append operation, tail is advanced to the next node, keeping track of where the next node should be inserted.
# This way, the tail efficiently builds the merged list step by step without needing any special checks for the first node or handling null pointers directly.
