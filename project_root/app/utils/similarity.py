from sklearn.metrics.pairwise import cosine_similarity
from .vectorization import vectorize
import numpy as np

def calculate_similarity(data):
    vectors = vectorize(data)
    similarity_matrix = cosine_similarity(vectors)
    return similarity_matrix

def find_related_documents(similarity_matrix, threshold=0.0):
    related_docs = {}
    for i in range(len(similarity_matrix)):
        for j in range(len(similarity_matrix[i])):
            if i != j and similarity_matrix[i][j] >= threshold:
                if i in related_docs:
                    related_docs[i].append(j)
                else:
                    related_docs[i] = [j]
    return related_docs

def get_similarity_score(document1, document2):
    vector1 = vectorize(document1)
    vector2 = vectorize(document2)
    similarity_score = cosine_similarity(vector1.reshape(1, -1), vector2.reshape(1, -1))
    return similarity_score[0][0]
