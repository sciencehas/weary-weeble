```python
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from .cleaning import clean_data

def create_word_vector(docs):
    """
    This function creates a word vector from the given documents.
    """
    # Initialize the CountVectorizer
    vectorizer = CountVectorizer()

    # Fit and transform the vectorizer on our corpus
    word_count_vector = vectorizer.fit_transform(docs)

    return word_count_vector, vectorizer

def compute_idf(word_count_vector):
    """
    This function computes the IDF values.
    """
    # Initialize the TfidfTransformer
    tfidf_transformer = TfidfTransformer(smooth_idf=True, use_idf=True)

    # Fit the transformer on our word count vector
    tfidf_transformer.fit(word_count_vector)

    return tfidf_transformer

def create_tfidf_matrix(docs, vectorizer, tfidf_transformer):
    """
    This function creates a TF-IDF matrix from the given documents.
    """
    # Transform the count matrix to a tf-idf representation
    tf_idf_vector = tfidf_transformer.transform(vectorizer.transform(docs))

    return tf_idf_vector

def vectorize_documents(docs):
    """
    This function vectorizes the given documents.
    """
    # Clean the documents
    cleaned_docs = [clean_data(doc) for doc in docs]

    # Create word vector
    word_count_vector, vectorizer = create_word_vector(cleaned_docs)

    # Compute IDF values
    tfidf_transformer = compute_idf(word_count_vector)

    # Create TF-IDF matrix
    tfidf_matrix = create_tfidf_matrix(cleaned_docs, vectorizer, tfidf_transformer)

    return tfidf_matrix
```