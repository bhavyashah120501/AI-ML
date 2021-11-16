import numpy as np
import pandas as pd

prior={}
marginal={}
likelihood={}

def pre_process(df):
    X = df.drop([df.columns[-1]],axis=1)
    y = df[df.columns[-1]]
    return X,y
def fit(X,y):
    for i in np.unique(y):
        prior[i] = sum(y == i)/y.shape[0]
    print(prior)
    for i in X.columns:
        for j in np.unique(X[i]):
            marginal[j]= sum(X[i] == j)/X.shape[0] 
    print(marginal)
    for i in np.unique(y):
        likelihood[i] = {}
        z = X[y==i]
        for j in X.columns:
            likelihood[i][j] = {}
            for k in np.unique(X[j]):
                likelihood[i][k] = 0
        for j in z.columns:
            for k in np.unique(z[j]):
                likelihood[i][k] = sum(z[j] == k)/z.shape[0]
    print(likelihood)

def predict(outcome,temp,humidity,windy):
    print("for yes",end=" ")
    y = "yes"
    ans = (likelihood[y][outcome]*likelihood[y][temp]*likelihood[y][humidity]*likelihood[y][windy]*prior[y])/(marginal[outcome]*marginal[temp]*marginal[humidity]*marginal[windy])
    print(ans)
    print("for no",end=" ")
    y = "no"
    ans = (likelihood[y][outcome]*likelihood[y][temp]*likelihood[y][humidity]*likelihood[y][windy]*prior[y])/(marginal[outcome]*marginal[temp]*marginal[humidity]*marginal[windy])
    print(ans)
    print("since yes is greater then no , the prediction is that they will play")

if __name__ == "__main__":
    df = pd.read_table("weather.txt")
    X,y = pre_process(df)
    fit(X,y)
    predict("Rainy","Mild","Normal","t")

