from gensim.models import Word2Vec
import pandas as pd
import ast
import random

l_titles = []
l_reviews = []
df_review = pd.read_csv('book_review_list.csv', names=['Titles', 'Reviews'])


for title in df_review['Titles']:
    l_titles.append(title)
list(set(l_titles))

for review in df_review['Reviews']:
    review = ast.literal_eval(review)
    l_reviews.append(review)
l_reviews = list(map(list, set(map(tuple, l_reviews))))
   

def recommend(genre="", now="", after="", want="", excepting=""):
    l_recommend_book = []
    model = Word2Vec.load("book_recommend.model")
    recommend = model.wv.most_similar(positive=[genre, now, after, want], negative=[excepting], topn=20)
    similar_words = [t[0] for t in recommend]
    for review in l_reviews:
        count = 0
        for word in similar_words:
            if word in review:
                count += 1
        if count > 3:
            book_index = l_reviews.index(review)
            recommend_book = l_titles[book_index]
            l_recommend_book.append(recommend_book)
    if len(l_recommend_book) > 3:
        book = random.sample(l_recommend_book, 2)
        return book
        # print(book[1],book[0])
    else:
        return l_recommend_book
        # print(l_recommend_book[0])  


# now = '楽しい'
# genre = '長い'
# after = '衝撃'
# want = '感動'
# excepting = '退屈'
# recommend(genre,now, after, want, excepting)

