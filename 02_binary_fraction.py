def binary_search(arr, x):
    low = 0
    last_idx = len(arr) - 1
    high = last_idx
    mid = 0
    count = 0

    while low <= high:
        count += 1

        mid = (high + low) // 2

        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1

        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            high = mid - 1

        # інакше x присутній на позиції і повертаємо його
        else:
            return mid

    if high != last_idx:
        if high < 0 or arr[high] < x:
            return (count, arr[high + 1])
        else:
            return (count, arr[high])
    # якщо елемент не знайдений
    return None

arr = [2.3, 3.9, 4.5, 10.1, 40.7]
x = 2
result = binary_search(arr, x)
if result is not None:
    print(f"High limit for element {x} is {result[1]}, it took {result[0]} iterations")
else:
    print("Element is not present in array")

def binary_search_by_edge(arr, x, take_high = True):
    low = 0
    last_idx = len(arr) - 1
    high = last_idx
    mid = 0
    count = 0

    while low <= high:
        count += 1

        mid = (high + low) // 2

        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1

        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            high = mid - 1

        # інакше x присутній на позиції і повертаємо його
        else:
            return mid

    if take_high:
        if high != last_idx:
            if high < 0 or arr[high] < x:
                return (count, arr[high + 1])
            else:
                return (count, arr[high])
    else:
        if low != 0:
            if low > last_idx or arr[low] > x:
                return (count, arr[low - 1])
            else:
                return (count, arr[low])
    # якщо елемент не знайдений
    return -1

arr = [2.3, 3.9, 4.5, 10.1, 40.7]
x = 50
edge = False
result = binary_search_by_edge(arr, x, edge)
if result != -1:
    print(f"{"High" if edge else "Low"} limit for element {x} is {result[1]}, it took {result[0]} iterations")
else:
    print("Element is not present in array")