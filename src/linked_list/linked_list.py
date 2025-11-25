from __future__ import annotations
from typing import Any


class Node:
    def __init__(self, value) -> None:
        self.next: Node | None = None
        self.previous: Node | None = None
        self.value: Any = value


class LinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None

    def append(self, node: Node) -> None:
        # empty list
        if not self.head or not self.tail:
            self.head = node
            self.tail = node
            return
        self.tail.next = node
        node.previous = self.tail
        self.tail = node

    def remove(self) -> None:
        if not self.head or not self.tail:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        new_tail = self.tail.previous
        self.tail = new_tail
        self.tail.next = None
