from data import str1, str2, str3, str4, str5, str6


class Stack:
    def __init__(self):
        self.stack_list = []

    def is_empty(self):
        if not self.stack_list:
            return True
        return False

    def push(self, item):
        self.stack_list.append(item)
        return

    def pop(self):
        self.stack_list.pop()
        if not self.stack_list:
            return None
        else:
            return self.stack_list[-1]

    def peek(self):
        return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)


def sequence_check(data):
    my_list = list(data)

    Stack_open_parenthesis = Stack()
    Stack_open_square_bracket = Stack()
    Stack_open_curly_bracket = Stack()
    for element in my_list:
        if element == "(":
            Stack_open_parenthesis.push(element)
        elif element == ")":
            if Stack_open_parenthesis.is_empty():
                return print("Несбалансировано")
            Stack_open_parenthesis.pop()
        elif element == "[":
            Stack_open_square_bracket.push(element)
        elif element == "]":
            if Stack_open_square_bracket.is_empty():
                return print("Несбалансировано")
            Stack_open_square_bracket.pop()
        elif element == "{":
            Stack_open_curly_bracket.push(element)
        elif element == "}":
            if Stack_open_curly_bracket.is_empty():
                return print("Несбалансировано")
            Stack_open_curly_bracket.pop()
    if (
        Stack_open_parenthesis.is_empty()
        and Stack_open_square_bracket.is_empty()
        and Stack_open_curly_bracket
    ):
        return print("Сбалансировано")
    else:
        return print("Несбалансировано")


if __name__ == "__main__":
    sequence_check(str1)
