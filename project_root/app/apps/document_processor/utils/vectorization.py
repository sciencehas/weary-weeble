```python
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

def create_word_vector(bags_of_words):
    """
    This function creates a word vector from the bags of words.
    """
    count_vectorizer = CountVectorizer()
    word_count_vector = count_vectorizer.fit_transform(bags_of_words)
    return word_count_vector, count_vectorizer

def create_tfidf_matrix(word_count_vector):
    """
    This function creates a TF-IDF matrix from the word count vector.
    """
    tfidf_transformer = TfidfTransformer(smooth_idf=True, use_idf=True)
    tfidf_matrix = tfidf_transformer.fit_transform(word_count_vector)
    return tfidf_matrix

def vectorize_documents(bags_of_words):
    """
    This function vectorizes the documents by creating a word vector and a TF-IDF matrix.
    """
    word_count_vector, count_vectorizer = create_word_vector(bags_of_words)
    tfidf_matrix = create_tfidf_matrix(word_count_vector)
    return tfidf_matrix, count_vectorizer
```