#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
 Each box is numbered sequentially from 0 to n - 1 and
  each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

Prototype: def canUnlockAll(boxes)
boxes is a list of lists
A key with the same number as a box opens that box
You can assume all keys will be positive integers
There can be keys that do not have boxes
The first box boxes[0] is unlocked
Return True if all boxes can be opened, else return False
 """


def canUnlockAll(boxes):
    """ Function to implement lockboxes  """

    keys = list((boxes[0]))
    boxes = {str(x): boxes[x] for x in range(1, len(boxes))}
    opened_boxes = []
    for _ in range(len(boxes)):
        for index in boxes:
            if int(index) in keys:
                keys.extend(boxes[index])
                opened_boxes.append(index)
        opened_boxes = sorted(list(set(opened_boxes)))
        keys = sorted(list(set(keys)))
    for key in opened_boxes:
        del boxes[key]

    if not boxes:
        return True
    else:
        return False
