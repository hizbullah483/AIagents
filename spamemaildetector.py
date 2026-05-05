import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

df = pd.read_csv(r'C:\Users\hp\Documents\ailabpractice\spam.csv', encoding = 'latin-1')
df = df[['v1','v2']]

x = df['v2']
y = df['v1']

vector = CountVectorizer()
x = vector.fit_transform(x)
xtrain, xtest, ytrain, ytest = train_test_split(x,y,train_size=0.8,random_state=42)

model = DecisionTreeClassifier()
model.fit(xtrain,ytrain)

ypred = model.predict(xtest)
print("decision tree accuracy: ",accuracy_score(ytest,ypred))


svc = SVC()
svc.fit(xtrain,ytrain)
ypredsvc = svc.predict(xtest)
print("svc accuracy: ",accuracy_score(ytest,ypredsvc))

