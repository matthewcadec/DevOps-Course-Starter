def your_function(mid):
    length = len(mid)
    
    if length % 2 == 0:
        return None
    
    return mid[length // 2]

print(your_function('abcde'))