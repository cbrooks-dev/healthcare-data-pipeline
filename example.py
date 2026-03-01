from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.preprocessing import PolynomialFeatures
from sklearn.ensemble import HistGradientBoostingRegressor, RandomForestRegressor

housing = datasets.fetch_california_housing()

x = housing.data
y = housing.target

poly = PolynomialFeatures()
x = poly.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

LR = LinearRegression()
GBR = HistGradientBoostingRegressor()
RFR = RandomForestRegressor(n_jobs=-1)

for model in [LR, GBR, RFR]:
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    r2 = r2_score(y_test, y_pred)
    print(model, r2)
