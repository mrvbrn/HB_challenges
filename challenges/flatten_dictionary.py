"""Given a dictionary, write a function to flatten it. 
Consider the following input/output scenario for better understanding:"""

input = {
  'Key1': '1',
  'Key2': {
    'a' : '2',
    'b' : '3',
    'c' : {
      'd' : '3',
      'e' : '1'
      }
    }
}

""" output = {
  'Key1': '1',
  'Key2.a': '2',
  'Key2.b' : '3',
  'Key2.c.d' : '3',
  'Key2.c.e' : '1'
}"""


def flatten_dict(d):
    def items():
        for key, value in d.items():
            if isinstance(value, dict):
                for subkey, subvalue in flatten_dict(value).items():
                    yield key + "." + subkey, subvalue
            else:
                yield key, value

    return dict(items())


print(flatten_dict(input))


def flatten_dictionary(d):
    result = {}
    stack = [iter(d.items())]
    keys = []
    while stack:
        for k, v in stack[-1]:
            keys.append(k)
            if isinstance(v, dict):
                stack.append(iter(v.items()))
                break
            else:
                result[".".join(keys)] = v
                keys.pop()
        else:
            if keys:
                keys.pop()
            stack.pop()
    return result


print(flatten_dictionary(input))


