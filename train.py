import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

# Load data dictionary
data_dict = pickle.load(open('./data.pickle', 'rb'))

data = np.asarray(data_dict['data'])
labels = np.asarray(data_dict['labels'])

# Split into train and test with stratification
x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, shuffle=True, stratify=labels)

# Initialize and train model
model = RandomForestClassifier()
model.fit(x_train, y_train)

# Test model
y_predict = model.predict(x_test)
score = accuracy_score(y_predict, y_test)

print(f'{score * 100:.2f}% of samples were classified correctly!')

# Save model
with open('model.p', 'wb') as f:
    pickle.dump({'model': model}, f)
