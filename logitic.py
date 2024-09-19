import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score
import matplotlib.pyplot as plt

# Creating the dataset
data = {
    'Quantity': [5, 3, 2, 1, 4, 6, 7, 3, 9, 2],
    'Total Price': [50, 45, 50, 100, 80, 180, 70, 150, 108, 150],
    'Status': ['Delivered', 'Delivered', 'Delivered', 'Delivered', 'In Transit', 'In Transit', 'Delivered', 'In Transit', 'In Transit', 'In Transit']
}
df = pd.DataFrame(data)

# Converting Status to binary
status_mapping = {'Delivered': 1, 'In Transit': 0}
df['Status'] = df['Status'].map(status_mapping)

# Preparing the data
X_log = df[['Quantity']].values
Y_log = df['Status'].values

# Training the model
logistic_regressor = LogisticRegression()
logistic_regressor.fit(X_log, Y_log)

# Making predictions
Y_log_pred = logistic_regressor.predict(X_log)

# Evaluating the model
cm = confusion_matrix(Y_log, Y_log_pred)
accuracy = accuracy_score(Y_log, Y_log_pred)

# Plotting the results
plt.scatter(X_log, Y_log, color='blue')
plt.plot(X_log, logistic_regressor.predict_proba(X_log)[:, 1], color='red')
plt.title('Logistic Regression')
plt.xlabel('Quantity')
plt.ylabel('Probability of Delivery')
plt.show()

# Printing results
print(f'Confusion Matrix: \n{cm}')
print(f'Accuracy: {accuracy}')
