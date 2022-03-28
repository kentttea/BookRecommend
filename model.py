from gensim.models import Word2Vec
import pandas as pd
import ast

reviews = []
df_review = pd.read_csv('book_review_list.csv', names=['Titles', 'Reviews'], index_col=0)
for review in df_review['Reviews']:
    review = ast.literal_eval(review)
    reviews.append(review)

model = Word2Vec(reviews, sg=1, vector_size=150, min_count=1, window=10, epochs=20)
model.save('book_recommend.model')

