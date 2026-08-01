import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv("fertilizer_recommendation_dataset.csv")

soil_encoder = LabelEncoder()
crop_encoder = LabelEncoder()
fert_encoder = LabelEncoder()

df["Soil"] = soil_encoder.fit_transform(df["Soil"])
df["Crop"] = crop_encoder.fit_transform(df["Crop"])
df["Fertilizer"] = fert_encoder.fit_transform(df["Fertilizer"])

X = df.drop("Fertilizer",axis=1)
y = df["Fertilizer"]

model = DecisionTreeClassifier()
model.fit(X,y)

# save everything
pickle.dump(model,open("model.pkl","wb"))
pickle.dump(fert_encoder,open("fertilizer_encoder.pkl","wb"))


# py train_model.py to run it
