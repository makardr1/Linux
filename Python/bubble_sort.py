from copy import deepcopy

def bubble_sort(nums: list) -> list:
    # Копируем исходные список
    copy_nums: list = deepcopy(nums)
    
    # Длина исходного списка
    copy_nums_length: int = len(copy_nums)
    
    # Внешний цикл
    for i in range(copy_nums_length):
        # Внутренний цикл
        for j in range(copy_nums_length - i - 1):
            # Сравниваем элементы
            if copy_nums[j] > copy_nums[j + 1]:
                copy_nums[j], copy_nums[j + 1] = copy_nums[j + 1], copy_nums[j]

    return copy_nums

print('Введите строкой числа')
print(bubble_sort([int(i)for i in input().split()]))

