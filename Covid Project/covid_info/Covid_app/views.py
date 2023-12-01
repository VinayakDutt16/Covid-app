from django.shortcuts import render , redirect
import pandas as pd

df = pd.read_csv("C:/Users/HP/OneDrive/Desktop/Covid Project/covid_info/Covid_app/covid_toy.csv")
print(df.head())
# Create your views here.

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['gender'] = le.fit_transform(df['gender'])
df['cough'] = le.fit_transform(df['cough'])
df['city'] = le.fit_transform(df['city'])
df['cough'] = le.fit_transform(df['cough'])

x = df.iloc[:,2:4].values
y = df.iloc[:,-1].values
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.2)
from sklearn.neighbors import KNeighborsClassifier

df.head()

def home(request):
    return render(request,"index.html")

def predict(request):
    if request.method == 'POST':
        a = request.POST.get('age')
        age = int(a)
        s = request.POST.get('salary')
        salary = int(s)
        result = knn_ans.predict([[age,salary]])[0]

print(df.head())