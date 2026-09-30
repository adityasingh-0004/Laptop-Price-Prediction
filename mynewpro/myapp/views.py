from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import UserProfile
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.metrics import r2_score
import numpy as np
import pandas as pd

def ReadCSV(request):

    df = pd.read_csv('myapp/static/CSV/laptop_dataset.csv')

    X = df[["RAM", "Brand", "Processor", "Storage"]]
    y = df["Price"]

    col = ["Brand", "Processor"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.25,
        random_state=42
    )

    process = ColumnTransformer(
        transformers=[
            (
                "cat",
                OneHotEncoder(handle_unknown="ignore"),
                col
            )
        ],
        remainder="passthrough"
    )

    model = Pipeline([
        ("preprocessor", process),
        ("regressor", DecisionTreeRegressor(random_state=42))
    ])

    model.fit(X_train, y_train)

    predict = model.predict(X_test)
    accuracy = r2_score(y_test, predict)

    print("Score:", accuracy)

    if request.method == "POST":

        ram = request.POST.get("ram")
        brand = request.POST.get("brand").upper()
        processor = request.POST.get("processor").upper()
        storage = request.POST.get("storage")


        new_data = pd.DataFrame({
            "RAM": [ram],
            "Brand": [brand],
            "Processor": [processor],
            "Storage": [storage]
        })

        accuracy = r2_score(y_test, predict)   
        
        result = model.predict(new_data)

        price = result[0]

        print("Price:", price)

        return render(
            request,
            "ReadCSV.html",
            {
                "prediction": price,
                "accuracy": accuracy,
                "ram": ram,
                "brand": brand,
                "processor": processor,
                "storage": storage
            }
        )


    return render(request, "ReadCSV.html")






  
    
def housePrediction(request):
    df = pd.read_csv('myapp/static/CSV/houseP.csv')
    X = df[['bedrooms','bathrooms','sqft_living','sqft_lot','floors','waterfront', 'view', 'condition', 'sqft_above','sqft_basement', 'yr_built', 'yr_renovated', 'street', 'city','statezip', 'country']]
    y = df["price"]

    col = ["street","city","statezip","country"]
    print(df.columns)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.25,
        random_state=42
    )

    process = ColumnTransformer(
        transformers=[
            (
                "cat",
                OneHotEncoder(handle_unknown="ignore"),
                col
            )
        ],
        remainder="passthrough"
    )

    model = Pipeline([
        ("preprocessor", process),
        ("regressor", DecisionTreeRegressor(random_state=42))
    ])

    model.fit(X_train, y_train)

    predict = model.predict(X_test)
    accuracy = r2_score(y_test, predict)

    print("Score:", accuracy)

    if request.method == "POST":

        bedrooms = request.POST.get("bedrooms")
        bathrooms = request.POST.get("bathrooms")
        sqft_living = request.POST.get("sqft_living")
        sqft_lot = request.POST.get("sqft_lot")
        floors = request.POST.get("floors")
        waterfront = request.POST.get("waterfront")
        view = request.POST.get("view")
        condition = request.POST.get("condition")
        sqft_above = request.POST.get("sqft_above")
        sqft_basement = request.POST.get("sqft_basement")
        yr_built = request.POST.get("yr_built")
        yr_renovated = request.POST.get("yr_renovated")
        street = request.POST.get("street")
        city = request.POST.get("city")
        statezip = request.POST.get("statezip")
        country = request.POST.get("country")
        


        new_data = pd.DataFrame({
        'bedrooms':[bedrooms],
        'bathrooms':[bathrooms],
        "sqft_living":[sqft_living],
        'sqft_lot':[sqft_lot],
        'floors':[floors],
        'waterfront':[waterfront],
        'view':[view],
        'condition':[condition],
        'sqft_above':[sqft_above],
        'sqft_basement':[sqft_basement],
        'yr_built':[yr_built],
        'yr_renovated':[yr_renovated],
        'street':[street],
        'city':[city],
        'statezip':[statezip],
        'country':[country],
        })

        accuracy = r2_score(y_test, predict)   
            
        result = model.predict(new_data)

        price = result[0]

        print("Price:", price)
        return render(
                request,
                "housePrediction.html",
                {
                    "prediction": price,
                    "accuracy": accuracy,
                    'bedrooms':bedrooms,
                    'bathrooms':bathrooms,
                    "sqft_living":sqft_living,
                    'sqft_lot':sqft_lot,
                    'floors':floors,
                    'waterfront':waterfront,
                    'view':view,
                    'condition':condition,
                    'sqft_above':sqft_above,
                    'sqft_basement':sqft_basement,
                    'yr_built':yr_built,
                    'yr_renovated':yr_renovated,
                    'street':street,
                    'city':city,
                    'statezip':statezip,
                    'country':country,                
                }
            )


    return render(request, "housePrediction.html")





def upload_image(request):

    if request.method == "POST":

        image = request.FILES.get("profile_image")

        if image:
            UserProfile.objects.create(
                profile_image=image
            )

            return redirect("upload_image")
    
    # ML code write here.......!    

    image = UserProfile.objects.last()

    return render(
        request,
        "upload_image.html",
        {"image": image}
    )   
    











  