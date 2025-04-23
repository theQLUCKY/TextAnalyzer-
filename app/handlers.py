from collections import defaultdict
from re import findall
from math import log10


def get_words(text: str)-> list[str]:
    """Извлекает элементы из документа у которых количество символов > 1
     и если перед элементом и после находятся пробелы"""
    words = findall(r'\b[a-zа-я]+[a-zа-я]+\b', text.lower())
    return words


def get_idf(all_words: list[list])-> dict[any, float]:
    """Высчитывает idf для каждого слова по формуле log10(n/t) где n - общее количество документов в базе,
       t - количество документов в которых содержится слово"""
    defdict = defaultdict(int)
    n = len(all_words)

    for words in all_words:
        unique_words = set(words)
        for word in unique_words:
            defdict[word] += 1
    idf = {word: log10(n / defdict[word]) for word in defdict}
    return idf

