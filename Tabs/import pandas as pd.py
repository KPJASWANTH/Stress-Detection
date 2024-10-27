import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score

# Load the dataset
data = pd.read_csv("your_dataset.csv")  # Replace "your_dataset.csv" with the path to your dataset file

# Separate features and target variable
X = data.drop(['Perceived_Stress', 'Valence', 'Arousal'], axis=1)
y_stress = data['Perceived_Stress']
y_valence = data['Valence']
y_arousal = data['Arousal']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y_stress, test_size=0.2, random_state=42)

# Initialize and train the SVM classifier for stress detection
svm_classifier = SVC(kernel='linear')  # You can choose different kernels like 'linear', 'rbf', etc.
svm_classifier.fit(X_train, y_train)

# Make predictions on the test set
y_pred = svm_classifier.predict(X_test)

# Evaluate the classifier
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
