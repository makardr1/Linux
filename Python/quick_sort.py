def quick_sort(nums: list) -> list:
    # Условие выхода из рекурсии
    if len(nums) <= 1:
        return nums

    # Опорный элемент
    support_num: int | float = nums[0]

    # Элементы по значению меньше опорного
    left: list[int | float] = [i for i in nums if i < support_num]

    # Элементы по значению равны опорному
    center: list[int | float] = [i for i in nums if i == support_num]

    # Элементы по значению больше опорного
    right: list[int | float] = [i for i in nums if i > support_num]

    return quick_sort(left) + center + quick_sort(right)

print('Введите строкой числа')
print(quick_sort([int(i) for i in input().split()]))
