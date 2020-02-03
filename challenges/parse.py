"""return inside of "<>" and "()" string."""

""" 
>>> parse_string("welcome <nuna> (enjoy  <your> stay)")
>>> ["nuna", "enjoy <your> stay"]
>>>parse_string(welcome <nuna> <enjoy your stay>")
>>> ["nuna", "enjoy your stay"]
"""

def parse_string(input):
    result = []
    i = 0
    while i<len(input):
        if input[i] == "<":
            for j in range(i, len(input)):
                if input[j] == ">" :
                    result.append(input[i+1:j])
                    i = j
                    break
        elif input[i] == "(":
            for k in range(i, len(input)):
                if input[k] == ")":
                    result.append(input[i+1:k])
                    i = k
        i+=1
    return result


print (parse_string("welcome <nuna> (enjoy  <your> stay>)"))


