```python
from collections import Counter
from operator import itemgetter

def rank_and_sort(dictionary):
    """
    This function ranks and sorts data from a dictionary.
    """
    word_counts = Counter(dictionary)
    sorted_word_counts = sorted(word_counts.items(), key=itemgetter(1), reverse=True)

    return sorted_word_counts
```