def merge_sort(list_):
    if len(list_) > 1:
        mid = len(list_)//2
        left = list_[:mid]
        right = list_[mid:]

        left = merge_sort(left)
        right = merge_sort(right)

        return merge(left, right)
    return list_

def merge(list_left, list_right):
    sorted_list = []
    count_left = count_right = 0
    while count_left < len(list_left) and count_right < len(list_right):
        if list_left[count_left] < list_right[count_right]:
            sorted_list.append(list_left[count_left])
            count_left += 1
        else:
            sorted_list.append(list_right[count_right])
            count_right += 1

    sorted_list.extend(list_left[count_left:])
    sorted_list.extend(list_right[count_right:])
    return sorted_list

lista = [25, 13, 77, 21, 11, 80]
print(merge_sort(lista))





