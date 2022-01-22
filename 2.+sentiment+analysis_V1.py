
##########Sentiment Analysis

#Data Import
import pandas as pd
input_data = pd.read_csv("D:/Google Drive/Training/Datasets/User_Reviews/User_movie_review.csv")


#Basic Details of the data
input_data.shape
input_data.columns
input_data.head(10)

#Frequency of sentiment col
input_data['class'].value_counts()


##########
#Creating Document Term Matrix

from sklearn.feature_extraction.text import CountVectorizer

countvec1 = CountVectorizer()
dtm_v1 = pd.DataFrame(countvec1.fit_transform(input_data['text']).toarray(), columns=countvec1.get_feature_names(), index=None)
dtm_v1['class'] = input_data['class']
dtm_v1.head()

#############################################
import pandas as pd
import re
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
#####Writing a Custom Tokenizer
stemmer = PorterStemmer()
def tokenize(text):
    text = stemmer.stem(text)               #stemming
    text = re.sub(r'\W+|\d+|_', ' ', text)    #removing numbers and punctuations and Underscores
    tokens = nltk.word_tokenize(text)       #tokenizing
    return tokens

countvec = CountVectorizer(min_df= 5, tokenizer=tokenize, stop_words=stopwords.words('english'))
dtm = pd.DataFrame(countvec.fit_transform(input_data['text']).toarray(), columns=countvec.get_feature_names(), index=None)
#Adding label Column
dtm['class'] = input_data['class']
dtm.head()

###Building training and testing sets
df_train = dtm[:1900]
df_test = dtm[1900:]

################# Building Naive Bayes Model
from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB()
X_train= df_train.drop(['class'], axis=1)
#Fitting model to our data
clf.fit(X_train, df_train['class'])

#Accuracy
X_test= df_test.drop(['class'], axis=1)
clf.score(X_test,df_test['class'])

#Prediction
pred_sentiment=clf.predict(df_test.drop('class', axis=1))
print(pred_sentiment)