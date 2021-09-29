def binary_search(list, item):
    # * low e hight definem as duas metades da lista
    low = 0
    high = len(list) - 1

    while low <= high:  # ! enquanto você não tenha restringido para 1 elemento
        mid = (low + high)  # * pega o elemento do meio
        guess = list[mid]
        if guess == item:  # * se o elemento central for o item buscado, ele retorna o elemento do meio
            return mid
        # * se o chute tiver sido mais alto, ele atualiza o final da lista para a metade, assim eliminando a metame mais alta.
        elif guess > item:
            high = mid - 1
        # * se o chute tiver sido mais baixo, ele delimita que a busca seja feita na maior metade da lista.
        else:
            low = mid + 1
    return None  # * Quando o item procurado não está na lista


my_list = [1, 3, 5, 7, 9, 10]

print(binary_search(my_list, 3))  # ? retorna 1
print(binary_search(my_list, -1))  # ? retorna None
