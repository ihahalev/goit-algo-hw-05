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
            return (count, arr[mid])

    if high != last_idx:
        if high < 0 or arr[high] < x:
            return (count, arr[high + 1])
        else:
            return (count, arr[high])
    # якщо елемент не знайдений
    return None

def binary_search_by_edge(arr, x, take_high = True):
    low = 0
    last_idx = len(arr) - 1
    high = last_idx
    mid = 0
    count = 0
    low_edge = arr[0]
    high_edge = arr[-1]

    while low <= high:
        count += 1

        mid = (high + low) // 2

        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low_edge = arr[mid]
            low = mid + 1

        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            high_edge = arr[mid]
            high = mid - 1

        # інакше x присутній на позиції і повертаємо його
        else:
            return (count, arr[mid])

    if take_high:
        if high != last_idx:
            return (count, high_edge)
    else:
        if low != 0:
            return (count, low_edge)
    # якщо елемент не знайдений
    return -1

if __name__ == "__main__":
    arr = [2.3, 3.9, 4.5, 10.1, 40.7]
    xs = [2,3,4,5,50]
    for x in xs:
        result = binary_search(arr, x)
        if result is not None:
            print(f"High limit for element {x} is {result[1]}, it took {result[0]} iterations")
        else:
            print("Element is not present in array")
    edge = False
    for x in xs:
        result = binary_search_by_edge(arr, x, edge)
        if result != -1:
            print(f"{"High" if edge else "Low"} limit for element {x} is {result[1]}, it took {result[0]} iterations")
        else:
            print("Element is not present in array")
    edge = True
    for x in xs:
        result = binary_search_by_edge(arr, x, edge)
        if result != -1:
            print(f"{"High" if edge else "Low"} limit for element {x} is {result[1]}, it took {result[0]} iterations")
        else:
            print("Element is not present in array")
