def vote(votes):
    max = 0
    for dig in votes:
        if max < votes.count(dig):
            max = dig
    return max