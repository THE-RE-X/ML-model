import pickle

def prediction(height):
    model=pickle.load(open('hw.pkl','rb'))
    weight = model.predict(height)
    print(weight)
    return weight