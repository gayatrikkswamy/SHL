
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from scraper import scrape_shl

model = SentenceTransformer('all-MiniLM-L6-v2')

data = scrape_shl()

embeddings = model.encode(data)

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(np.array(embeddings))

def search(query):

    q_embedding = model.encode([query])

    D,I = index.search(np.array(q_embedding),3)

    results = []

    for i in I[0]:
        results.append(data[i])

    return results
