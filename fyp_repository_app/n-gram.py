import nltk
from nltk.util import ngrams
from  nltk.metrics.distance import jaccard_distance

from fyp_repository_app.models import Projects

project = Projects.objects.all()
for projec in project:

    with open("projec.file_report", "r") as f1, open("application", "r") as f2:
        text1 = f1.read()
        text2 = f2.read()

    # convert text in to list of bigram
    bigram1 = list(ngrams(text1.split(), 2))
    bigram2 = list(ngrams(text2.split(), 2))

    # calculate jaccard distance
    jaccard_similarity = 1 - jaccard_distance(set(bigram1), set(bigram2))

    # compare jaccard with threshold
    threshold = 0.8

    if jaccard_similarity > threshold:
        print("PLagiarism is greater ")
    else:
        print("Plagiarism is minimun")
