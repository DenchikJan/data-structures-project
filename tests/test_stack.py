"""Здесь надо написать тесты с использованием unittest для модуля stack."""
from src.stack import Stack, Node


class TestNode:

    def test_init(self):
        node1 = Node(8, 6)
        assert node1.data == 8
        assert node1.next_node == 6


class TestStack:

    def test_push(self):
        stack = Stack()
        assert stack.stack == []
        stack.push(2)
        stack.push(5)
        stack.push(6)
        assert stack.stack == [2, 5, 6]
        assert stack.top.data == 6
        assert stack.top.next_node.data == 5
        assert stack.top.next_node.next_node.data == 2
        assert stack.top.next_node.next_node.next_node is None

    def test_pop(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        data = stack.pop()
        assert stack.top.data == 'data1'
        assert data == 'data2'
