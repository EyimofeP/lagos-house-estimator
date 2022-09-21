from django.shortcuts import render
import pandas as pd
import joblib

# Home page
def home(request):
    return render(request, "base.html")

# Buy page
def buy(request):
    return render(request, "buy.html")

# predict buy
def predict_buy(request):
    # Fetch data from the frontend
    bedrooms = float(request.POST["Bedrooms"])
    bathrooms = float(request.POST["Bathrooms"])
    toilets = float(request.POST["Toilets"])
    newly_built = float(request.POST["Newly_Built"])
    serviced = float(request.POST["Serviced"])
    furrnished = float(request.POST["Furnished"])
    type_of = request.POST["Type"]
    city = request.POST["City"]
    neighborhood = request.POST["Neighborhood"]

    # Store data in a dictionary
    data = {
    "Bedrooms" : bedrooms,
    "Bathrooms" : bathrooms,
    "Toilets" : toilets,
    "Newly Built" : newly_built,
    "Serviced" : serviced,
    "Furnished" : furrnished,
    "Type" : type_of,
    "City" : city,
    "Neighborhood" : neighborhood}

    # Import tools for preprocessing
    encoder = joblib.load("tools/encoder_joblib")
    scaler = joblib.load("tools/scaler_joblib")

    # Import model
    model = joblib.load("tools/model_joblib")    

    # Function to predict price
    def predict_house(data):
        test = pd.DataFrame([data])
        numerical = ['Bathrooms', 'Bedrooms', 'Toilets']
        test[numerical] = scaler.transform(test[numerical]) # scale the numerical data
        test = encoder.transform(test) # encode the categorical data
        
        return model.predict(test)

    # Getting prediction and convert to integer
    prediction = int(predict_house(data))

    # Send to frontend
    context = {"prediction" : prediction,
                "Bedrooms" : int(bedrooms),
                "Bathrooms" : int(bathrooms),
                "Toilets" : int(toilets)}
    
    return render(request, "buy.html", context=context)

# rent page
def rent(request):
    return render(request, "rent.html")

# predict rent
def predict_rent(request):
    # Fetch data from the frontend
    bedrooms = float(request.POST["Bedrooms"])
    bathrooms = float(request.POST["Bathrooms"])
    toilets = float(request.POST["Toilets"])
    newly_built = float(request.POST["Newly_Built"])
    serviced = float(request.POST["Serviced"])
    furrnished = float(request.POST["Furnished"])
    type_of = request.POST["Type"]
    city = request.POST["City"]
    neighborhood = request.POST["Neighborhood"]

    # Store data in a dictionary
    data = {
    "Bedrooms" : bedrooms,
    "Bathrooms" : bathrooms,
    "Toilets" : toilets,
    "Newly Built" : newly_built,
    "Serviced" : serviced,
    "Furnished" : furrnished,
    "Property Type" : type_of,
    "City" : city,
    "Neighborhood" : neighborhood}

    # Import tools for preprocessing
    encoder = joblib.load("tools/rent_encoder_joblib")

    # Import model
    model = joblib.load("tools/rent_model_joblib")    

    # Function to predict price
    def predict_house(data):
        test = pd.DataFrame([data])
        test = encoder.transform(test) # encode the categorical data
        return model.predict(test)[0]

    # Getting prediction and convert to integer
    prediction = int(predict_house(data))

    # Send to frontend
    context = {"prediction" : prediction,
                "Bedrooms" : int(bedrooms),
                "Bathrooms" : int(bathrooms),
                "Toilets" : int(toilets)}
    
    return render(request, "rent.html", context=context)