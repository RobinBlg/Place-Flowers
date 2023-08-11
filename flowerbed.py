def can_place_flowers(flowerbed, n):
    count = 0
    i = 0
    while i < len(flowerbed):
        if flowerbed[i] == 0:
            if i == 0 or flowerbed[i - 1] == 0:
                if i == len(flowerbed) - 1 or flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    count += 1
        i += 1

    return count >= n

# Example 1
flowerbed1 = [1, 0, 0, 0, 1]
n1 = 1
print(can_place_flowers(flowerbed1, n1))  # Output: True

# Example 2
flowerbed2 = [1, 0, 0, 0, 1]
n2 = 2
print(can_place_flowers(flowerbed2, n2))  # Output: False
