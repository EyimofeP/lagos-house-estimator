from django.shortcuts import render
import pandas as pd
import joblib

# Home page
def home(request):
    return render(request, "base.html")


# Predict page
def predict(request):
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
        
        return model.predict(test)[0] // 1e6 # make prediction, convert it to millions and round up to 2dp 

    # Getting prediction and convert to integer
    prediction = int(predict_house(data))

    # Send to frontend
    context = {"prediction" : prediction,
                "Bedrooms" : int(bedrooms),
                "Bathrooms" : int(bathrooms),
                "Toilets" : int(toilets),
                "Newly Built" : newly_built,
                "Serviced" : serviced,
                "Furnished" : furrnished,
                "Type" : type_of,
                "City" : city,
                "Neighborhood" : neighborhood}
    
    return render(request, "base.html", context=context)