def playing_map():
    data = range(0, 10)
    print(list(map(lambda x: x ** 2, data)))


def sum_up(offset, data) -> int:
    offset += data[0]
    if len(data) > 1:
        offset = sum_up(offset, data[1:])
    return offset


def iterative_sum():
    data = range(0, 10)
    return sum_up(0, data)


if __name__ == '__main__':
    playing_map()
    assert iterative_sum() == 45
