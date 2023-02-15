class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list.copy()


    def __iter__(self):
        self.cursor = -1
        self.my_list = []
        self.l = self.list_of_list
        return self

    def __next__(self):

        while self.l:
            item = self.l.pop(-1)
            if type(item) is list:
                self.l.extend(item)
            else:
                self.my_list.append(item)

        if self.cursor < len(self.my_list) - 1:
            self.list_of_list = self.my_list[::-1]
            self.cursor += 1
            return self.list_of_list[self.cursor]
        else:
            raise StopIteration


def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_3()