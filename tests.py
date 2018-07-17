import pytest
import random
import string

from trie import Trie
from bruteforce import BruteForce


@pytest.fixture
def words(n=10**5, max_length=21, min_length=1):
    bool_pair = (True, False)
    return (
        (
            random.choice(bool_pair),
            ''.join(
                random.choices(
                    string.ascii_lowercase,
                    k=random.randint(min_length, max_length),
                ))
        ) for _ in range(n)
    )


@pytest.mark.parametrize('klass', (Trie, BruteForce))
def test_add_get_words(klass):
    words = ('s', 'ss', 'sss', 'ddfg', 'd', 'dd', 'ddf', 'dzz',)
    entry = klass()
    count = 0
    for word in words:
        entry.add_word(word)
        count += 1
    assert entry.get_words_count('s') == 3
    assert entry.get_words_count('ss') == 2
    assert entry.get_words_count('sss') == 1
    assert entry.get_words_count('ssd') == 0
    assert entry.get_words_count('d') == 5
    assert entry.get_words_count('dd') == 3
    assert entry.get_words_count('dz') == 1
    assert entry.get_words_count('ddf') == 2
    assert entry.get_words_count('dx') == 0
    if klass is Trie:
        assert entry.root.number == count


def test_add_words_returned_node():
    words = ('s', 'ss', 'sss', 'ddfg', 'd', 'dd', 'ddf', 'dzz',)
    entry = Trie()
    for word in words:
        node = entry.add_word(word)
        assert node.symbol == word[-1]


def test_root_words_count():
    words = ('s',) * 100
    entry = Trie()
    for word in words:
        entry.add_word(word)
    assert entry.root.number == len(words)


def _test(cls, words):
    entry = cls()
    for add, word in words:
        if add:
            entry.add_word(word)
        else:
            entry.get_words_count(word)


def test_performance_trie(words, benchmark):
    benchmark(_test, Trie, words)


@pytest.mark.skip(reason="Too slow")
def test_performance_bruteforce(words, benchmark):
    benchmark(_test, BruteForce, words)
