class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.stack = []
        self.top = Node
        self.i = -1

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        if len(self.stack) == 0:
            temp = Node(data, None)
        else:
            temp = Node(data, self.top)
        self.top = temp
        self.stack.append(data)

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        if len(self.stack) > 0:
            data = self.stack.pop()
            if len(self.stack) == 0:
                self.top = None
            else:
                self.top = Node(self.stack[-1], self.top)
            return data
