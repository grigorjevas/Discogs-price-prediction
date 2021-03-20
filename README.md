# Discogs price prediction API
![Discogs](assets/discogs_logo.jpg)
## Introduction
Vinyl records - new or old - retain a lot of value and some of them turn out to be a good investment as their value 
increases over time. With Electro being a timeless genre without being very much affected by trends, I have collected 
a dataset of 5000 Electro records from [Discogs](https://www.discogs.com/), the largest online music 
database and marketplace using my other project, 
[Discogs Marketplace scraper](https://github.com/grigorjevas/Discogs-marketplace-scraper) and trained a logistic 
regression model based on various features of the records.\
The model will predict the price for a provided record making it easier to decide whether it's a bargain and worthy 
addition to my collection, or overpriced meal for Discogs sharks.

## Usage
The API endpoint is a Flask app hosted on heroku https://discogs-price-prediction.herokuapp.com/ which you can access 
with any REST API client, such as Postman.
There are two main routes:
- `/predict` - takes POST requests, predicts record value by features provided.
- `/history` - takes GET requests and returns last 10 most recent requests and predictions from the database
- `/history/num_predictions` - you can supply an optional number of results to return by adding an int `num_predictions`,
for example `https://discogs-price-prediction.herokuapp.com/history/5`

Input json format example:
```json
{
  "artist": "DMX Krew",
  "title": "Dread It A Go EP",
  "release_format": "LP",
  "number_of_tracks": 8,
  "release_year": 2002,
  "rating": 4.75,
  "votes": 24,
  "have": 111,
  "want": 106,
  "limited_edition": true,
  "media_condition": 5,
  "sleeve_condition": 4
}
```
Please refer to the following chart and use numeric values of media and sleeve condition when sending json data: 
| Value | Media / Sleeve condition | 
|---|---|
| 5 | Mint |
| 4 | Near Mint (NM or M-) |
| 3 | Very Good Plus (VG+), Generic sleeve |
| 2 | Very Good (VG) |
| 1 | Good (G), Good Plus (G+) |
| 0 | Poor (P), Fair (F) |

A generic sleeve within the context of grading items on Discogs Marketplace refers to a type of sleeve that is not
specific to the release. It should be given a value of 3 because, in theory, it doesn't add, nor subtract the value of 
the record itself.

#### Using command line
You can also use `requests` module and use the API in a Jupyter notebook like so:
```python
import json
import requests
release_info = {
  "artist": "Joe McBride",
  "title": "21.12 / 30.03",
  "release_format": "LP",
  "number_of_tracks": 12,
  "release_year": 2020,
  "rating": 5.00,
  "votes": 22,
  "have": 63,
  "want": 42,
  "limited_edition": True,
  "media_condition": 5,
  "sleeve_condition": 5
}

url = "https://discogs-price-prediction.herokuapp.com/predict"
response = requests.post(url, json.dumps(release_info))
print(f"{json.loads(response.content)}")
```
And to retrieve the latest inferences
```python
url = "https://discogs-price-prediction.herokuapp.com/history"
response = requests.get(url)
print(f"{json.loads(response.content)}")
```

## Installation
If you wish to run this application yourself, you can do so easily by following these steps:
1. Create Heroku project and Heroku PostgreSQL database
1. Add your database credentials to .env file (make sure to rename `.env_template` to `.env`)
1. Run `pip install -r requirements.txt`
1. Type `flask run` to start the app


## Model 
The model was trained using Google Colab 
[notebook](https://github.com/grigorjevas/Discogs-price-prediction/blob/main/Preparing_data_and_models.ipynb) in this 
repository. Model accuracy results are provided below. They are not great but accuracy was not the main focus of this 
project.
```
Model score: 0.5254380568688232
Mean absolute error: 2.1076547256012557
```

## License
This project is licensed under [MIT license](https://tldrlegal.com/license/mit-license)