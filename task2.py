# Функція для злиття двох відсортованих списків в один відсортований список
def merge_two_lists(list1, list2):
    merged = []
    i, j = 0, 0

    # Поки обидва індекси не вийшли за межі списків
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1

    # Додаємо залишок з першого списку, якщо є
    while i < len(list1):
        merged.append(list1[i])
        i += 1

    # Додаємо залишок з другого списку, якщо є
    while j < len(list2):
        merged.append(list2[j])
        j += 1

    return merged

# Функція для злиття k відсортованих списків у один відсортований список
def merge_k_lists(lists):
    if not lists:
        return []

    # Зливаємо списки парами поки не залишиться один
    while len(lists) > 1:
        merged_lists = []

        # Ітеруємося по списках двома за раз
        for i in range(0, len(lists), 2):
            list1 = lists[i]
            list2 = lists[i+1] if i + 1 < len(lists) else []
            merged_lists.append(merge_two_lists(list1, list2))

        lists = merged_lists

    return lists[0]

# Приклад використання функції
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
