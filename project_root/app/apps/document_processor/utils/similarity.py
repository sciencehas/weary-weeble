from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def calculate_similarity(matrix):
    similarity_matrix = cosine_similarity(matrix)
    return similarity_matrix

def find_related_documents(similarity_matrix, threshold=0.0):
    related_docs = {}
    for i in range(similarity_matrix.shape[0]):
        for j in range(i+1, similarity_matrix.shape[1]):
            if similarity_matrix[i][j] >= threshold:
                if i in related_docs:
                    related_docs[i].append(j)
                else:
                    related_docs[i] = [j]
    return related_docs

def get_similarity_range(matrix, min_similarity=0.0, max_similarity=1.0):
    similarity_matrix = calculate_similarity(matrix)
    related_docs = find_related_documents(similarity_matrix, min_similarity)
    filtered_docs = {k: v for k, v in related_docs.items() if any(similarity_matrix[k][doc_index] <= max_similarity for doc_index in v)}
    return filtered_docs
