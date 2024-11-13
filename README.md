# PRCP-1020-HousePricePred
### Conclusion
#### 1. Linear Regression:

R' Score: 0.99999 (Very high, almost perfect fit)

Mean Absolute Error (MAE): 0.1723 (Extremely low error, suggesting very accurate predictions)

Root Mean Squared Error (RMSE): 0.2336 (Very low, consistent with low errors)

Adjusted R: 0.99999 (High, indicating the model is not overfitting)

Conclusion. Linear Regression seems to be performing excellently, with very low errors and a near-perfect R value. It's one of the top-perforrting models

#### 2. Support Vector Machine (SVM):

R Score: -0.0212438 (Negative, indicating poor performance)

* MAE 59,351 (Very high error)

RMSE 88,565.78 (Extremely high, indicating poor model fit)

Adjusted R-0.9916

Conclusion: SVM performs terribly here, with large errors and a negative R score. It is not suitable for predicting SalePrice in this case.
#### 3. K-Nearest Neighbors (KNN):

•R Score: 0.9978 (Very high fit)

* MAE 1399.12 (Low error, but higher than Linear Regression)

* RMSE: 4018.89 (Still relatively low but higher than other models)

* Adjusted R: 0.9999 (Consistently high)

Conclusion: KNN performs very well, but with slightly higher errors compared to Linear Regression. It is a good model but not the best in this comparison

#### 4. Decision Tree:

R Score: 0.9859 (Good fit, but lower than other models)

MAE 1,354.28 (Moderate error, higher than other models)

RMSE: 16,386.63 (Relatively high, suggesting a less accurate fit)

Adjusted R²: 0.9858 (Indicates potential overfitting)

Conclusion: The Decision Tree performs decently but has higher errors and lower R³ compared to the top-performing models. It may suffer from overfitting

#### 5. Random Forest:

R Score: 0.9918 (Very high fit)

MAE: 1,863.64 (Moderate error)

RMSE 6974.67 (Higher error compared to KNN and Linear Regression)

* Adjusted R: 0.9917 (Good fit, but not as high as Linear Regression or KNN)

Conclusion: Random Forest is a strong contender but has slightly higher errors compared to Linear Regression and KNN. It still performs quite well

#### 6. XGBoost:

•R Score: 0.9969 (Excellent fit)

MAE: 510.90 (Low error, close to KNN and Random Forest)

RMSE: 2,842.50 (Lower error than Random Forest but higher than Linear Regression)

Adjusted R²: 0.9968 (Excellent fit)

Conclusion: XGBoost is one of the top-performing models with very low error rates and high R values. It performs slightly worse than Linear Regression but is abil highly effective.

#### 7. Bagging:

R' Score: 0.99999 (Perfect fit)

MAE: 0.1730 (Extremely low error, on par with Linear Regression)

* RMSE 0.2336 (Very low error,Talmost identical to Linear Regression)

* Adjusted R²: 0.9916 (High fit)

Conclusion: Bagging performs on par with Linear Regression, achieving almost perfect results with extremely low errors

### Final Conclusion:

Top-performing models: Linear Regression, Bagging, and XGBoost

* Linear Regression and Bagging both have nearly perfect R and the lowest error metrics making them the best choices

XGBoost is a strong alternative with a slight increase in error but still provides excellent results. Worst-performing model: SVM, which has a negative R³ and extremely high errors, making it unsuitable for this task

If simplicity and interpretability are important, Linear Regression is likely the best choice. However, Bagging is an equally effective model for more robeat mults
