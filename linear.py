import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Creating the dataset
data = {
    'Quantity': [5, 3, 2, 1, 4, 6, 7, 3, 9, 2],
    'Total Price': [50, 45, 50, 100, 80, 180, 70, 150, 108, 150]
}
df = pd.DataFrame(data)

# Preparing the data
X = df[['Quantity']].values
Y = df['Total Price'].values

# Training the model
linear_regressor = LinearRegression()
linear_regressor.fit(X, Y)

# Making predictions
Y_pred = linear_regressor.predict(X)

# Evaluating the model
mse = mean_squared_error(Y, Y_pred)
r2 = r2_score(Y, Y_pred)

# Plotting the results
plt.scatter(X, Y, color='blue')
plt.plot(X, Y_pred, color='red')
plt.title('Linear Regression')
plt.xlabel('Quantity')
plt.ylabel('Total Price')
plt.show()

# Printing results
print(f'Coefficients: {linear_regressor.coef_}')
print(f'Intercept: {linear_regressor.intercept_}')
print(f'Mean squared error: {mse}')
print(f'R^2 score: {r2}')
