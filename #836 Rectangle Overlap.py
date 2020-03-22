class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        return not (rec1[2] <= rec2[0] or  # left
                    rec1[3] <= rec2[1] or  # bottom
                    rec1[0] >= rec2[2] or  # right
                    rec1[1] >= rec2[3])    # top

class Solution2(object):
    def isRectangleOverlap(self, rec1, rec2):
        return (max(rec1[1], rec2[1]) < min(rec1[3], rec2[3])) and \
        (max(rec1[0], rec2[0]) < min(rec1[2], rec2[2]))