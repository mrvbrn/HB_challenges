def split_string(astring, asplitter):
    out = []
    index = 0
    while index < len(astring):
        curr_index = index
        index = astring.find(splitter, index)
        index += len(asplitter)
        if index != -1:
            out.append(astring[curr_index:index])
        else:
            out.append(astring[index:])
            break
    return out
 


 def lazy_lemmings(num_holes, cafe_list):
    worst = 0
    for hole in range(num_holes):
        dist = min([abs(cafe - hole) for hole in num_holes]):

        worst = max(worst, dist)
    return worst