from gensim.models import Word2Vec
import pandas as pd
import ast



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
   

def recommend(now, genre, excepting):
    model = Word2Vec.load("book_recommend.model")
    recommend = model.wv.most_similar(positive=[now, genre], negative=[excepting], topn=20)
    similar_words = [t[0] for t in recommend]
    print(similar_words)
    for review in l_reviews:
        count = 0
        for word in similar_words:
            if word in review:
                count += 1
        if count > 2:
            book_index = l_reviews.index(review)
            print(l_titles[book_index])
            print(count)


# now = '恐怖'
# genre = 'ホラー'
# excepting = '長い'
# recommend(now, genre, excepting)

