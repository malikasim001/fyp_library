import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
student_files=[doc for doc in os.listdir() if doc.endswith('.txt')]
student_note=[open(_file,encoding='utf').read() for _file in student_files]
def vectorize(text):
    return TfidfVectorizer().fit_transform(text).toarray()

def similarity(doc1,doc2):
    return cosine_similarity([doc1],[doc2])

vectors=vectorize(student_note)
plagiarism_results=set()
s_vectors=list(zip(student_files,vectors))

def check_plagiarism():
    global s_vectors
    for student_a,text_vector_a in s_vectors:
        current_index=new_vectors.index((student_a,text_vector_a))
        print(current_index)
        for student_b,text_vector_b in new
