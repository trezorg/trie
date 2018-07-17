from __future__ import annotations # noqa
from typing import (
    Dict,
    Optional,
)


class Node:

    __slots__ = ['symbol', 'childs', 'number']

    def __init__(self, symbol: str) -> None:
        self.symbol: str = symbol
        self.childs: Dict[str, Node] = dict()
        self.number: int = 0

    def add_child(self, node: Node): # noqa
        if node.symbol not in self.childs:
            self.childs[node.symbol] = node

    def get_child_by_symbol(self, symbol: str) -> Optional[Node]: # noqa
        return self.childs.get(symbol)

    def __repr__(self) -> str:
        return f'Node({self.symbol!r})'

    def __str__(self) -> str:
        return f'{self.symbol}({self.number})'


class Trie:

    def __init__(self):
        self.root: Node = Node('')

    def add_word(self, word: str, node: Node=None) -> Node:
        """
        Returns last trie node after a word has been added.
        """
        if node is None:
            node = self.root
        node.number += 1
        if not word:
            return node
        symbol, rest_word = word[0], word[1:]
        child_node = node.get_child_by_symbol(symbol)
        if child_node is not None:
            return self.add_word(rest_word, child_node)
        else:
            new_node = Node(symbol)
            node.add_child(new_node)
            return self.add_word(rest_word, new_node)

    def get_words_count(self, word: str) -> int:
        node: Node = self.root
        for symbol in (word or ''):
            node: Node = node.get_child_by_symbol(symbol)
            if node is None:
                return 0
        return node.number


if __name__ == '__main__':
    trie = Trie()
    trie.add_word('s')
    trie.add_word('ss')
    trie.add_word('sss')
    trie.add_word('ddfg')
    trie.add_word('d')
    trie.add_word('dd')
    trie.add_word('ddf')
    trie.add_word('dzz')
    assert trie.get_words_count('s') == 3
    assert trie.get_words_count('ss') == 2
    assert trie.get_words_count('sss') == 1
    assert trie.get_words_count('ssd') == 0
    assert trie.get_words_count('d') == 5
    assert trie.get_words_count('dd') == 3
    assert trie.get_words_count('dz') == 1
    assert trie.get_words_count('ddf') == 2
