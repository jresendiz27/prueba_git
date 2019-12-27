import time

def value_to_seconds(end, start):
    return (end - start) * 1000

def binary_search(list, item):
    start = time.time()
    low = 0
    high = len(list) - 1
    found = None
    while low <= high:
        mid = int((low + high)/2)
        guess = list[mid]

        if guess == item and found is None:
            found = mid
        if guess > item:
            high = mid-1
        else:
            low = mid+1
    end = time.time()
    print(f"BS) Elapsed Time (s): {value_to_seconds(end, start)}")
    return found

def recursive_binary_search(list, item):
    pass

def linear_search(list, item):
    start = time.time()
    found = None
    for it in list:
        if it is item:
            found = item
            break
    end = time.time()
    print(f"LS) Elapsed Time (s): {value_to_seconds(end, start)}")
    return found

def aux_recursive_linear_search(list, index, valor_a_buscar):
    if len(list) < index:
        return None #No lo encontré
    elif list[index] is valor_a_buscar:
        return valor_a_buscar
    else:
        index+=1
        return aux_recursive_linear_search(list, index, valor_a_buscar)


def recursive_linear_search(list, item):
    start = time.time()
    found = aux_recursive_linear_search(list, 0, item)
    end = time.time()
    print(f"RLS) Elapsed Time (s): {value_to_seconds(end, start)}")
    return found

def python_easy_find(list, item):
    start = time.time()
    found = item in list
    end = time.time()
    print(f"PEF) Elapsed Time (s): {value_to_seconds(end, start)}")
    return found


my_list = []
for i in range(2, 100):
    my_list.append(i)

print (f"BS) found at Pos: {binary_search(my_list, 600)}")
print(f"LS) found at Pos: {linear_search(my_list, 600)}")
print(f"PEF) found at Pos: {python_easy_find(my_list, 600)}")
print(f"RLS) found at Pos: {recursive_linear_search(my_list, 4)}")
print("-"*60)
print(f"BS) Found at Pos: {binary_search(my_list, -1)}")
print(f"LS) Found at Pos: {linear_search(my_list, -1)}")
print(f"PEF) found at Pos: {python_easy_find(my_list, -1)}")
print(f"RLS) found at Pos: {recursive_linear_search(my_list, -1)}")
print("-" * 60)
