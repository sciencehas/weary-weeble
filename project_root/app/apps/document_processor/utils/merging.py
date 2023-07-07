```python
import numpy as np

def merge_vectors(bag_of_words):
    """
    This function takes a list of bag of words and merges them into a single matrix.
    """
    return np.vstack(bag_of_words)

def merge_documents(documents):
    """
    This function takes a list of documents and merges them into a single document.
    """
    return ' '.join(documents)
```