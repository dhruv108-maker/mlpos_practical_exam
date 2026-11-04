import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv('datasets/data.csv')

categorical_columns = ['gender', 'ssc_b', 'hsc_b', 'hsc_s',
                       'degree_t', 'workex', 'specialisation']

encoders = {}

for col in categorical_columns:
    encoders[col] = LabelEncoder()
    data[col] = encoders[col].fit_transform(data[col])

x = data.drop(['sl_no', 'status', 'salary'], axis=1)
y = data['status']

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier()
model.fit(x_train, y_train)

pickle.dump(model, open('TrainedModels/model.pkl', 'wb'))
pickle.dump(encoders, open('TrainedModels/encoder.pkl', 'wb'))

print("Accuracy:", model.score(x_test, y_test))