'''
You have a set of non-overlapping intervals. You are given a new interval [start, end], insert this new interval into the set of intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.



Problem Constraints
0 <= |intervals| <= 105



Input Format
First argument is the vector of intervals

second argument is the new interval to be merged



Output Format
Return the vector of intervals after merging



Example Input
Input 1:

Given intervals [1, 3], [6, 9] insert and merge [2, 5] .
Input 2:

Given intervals [1, 3], [6, 9] insert and merge [2, 6] .


Example Output
Output 1:

 [ [1, 5], [6, 9] ]
Output 2:

 [ [1, 9] ]

'''


def insert(intervals, newInterval):

    res=[]
    if not intervals:
        res.append(newInterval)
        return res

    x=newInterval.start
    y=newInterval.end
    merge=False
    start=x
    end=y


    if start<intervals[0].start and end< intervals[0].end:
        res.append(Interval(start,end))

    for i in range(len(intervals)):
        if x<=intervals[i].end and y>=intervals[i].start:
            start=min(start,intervals[i].start)
            end=max(end,intervals[i].end)
            merge=True
        elif i>0 and start>intervals[i-1].end and end < intervals[i].start:
            res.append(Interval(x,y))
            res.append(intervals[i])
        else:
            if merge:
                res.append(Interval(start,end))
                merge=False
            res.append(intervals[i])

    l=len(intervals)
    if x>intervals[l-1].start and y>intervals[l-1].end:
        res.append(Interval(x,y))

    if merge:
        res.append(Interval(start,end))


    return res
