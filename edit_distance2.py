
from call_counter import countcalls

def memoize(func):
    cache = {}

    def decorator(str1, str2):
        if (str1, str2) not in cache:
            cache[(str1, str2)] = func(str1, str2)
        return cache[(str1, str2)]

    decorator.cache = cache
    return decorator


@countcalls
@memoize
def edit_distance2(str1, str2):

    if len(str1) == 0:
        return len(str2)

    if len(str2) == 0:
        return len(str1)

    if str1[-1] == str2[-1]:
        return edit_distance2(str1[:-1], str2[:-1])

    return 1 + min(edit_distance2(str1, str2[:-1]),      # Insert
                   edit_distance2(str1[:-1], str2),      # Remove
                   edit_distance2(str1[:-1], str2[:-1])  # Replace
                   )
