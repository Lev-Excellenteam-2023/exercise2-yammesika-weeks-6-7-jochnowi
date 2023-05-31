def group_by(func, elements):

    result = {func(element): [] for element in elements}
    
    for element in elements:
        result[func(element)].append(element)
    return result


print(group_by(len, ["hi", "bye", "yo", "try"]))