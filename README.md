# Discogs price prediction API
![Discogs](assets/discogs_logo.jpg)
## Introduction
Vinyl records - new or old - retain a lot of value and some of them turn out to be a good investment as their value 
increases over time. I have collected a dataset of 5000 Electro records from
[Discogs](https://www.discogs.com/), the largest online music database and marketplace using my other project, 
[Discogs Marketplace scraper](https://github.com/grigorjevas/Discogs-marketplace-scraper) and trained a logistic 
regression model based on various features of the records.\
The model will predict the price for a provided record making it easier to decide whether it's a bargain and worthy 
addition to my collection, or overpriced meal for Discogs sharks.

## Usage 
Sleeve and media condition conversion chart: 
| 5 | Mint |
|---|---|
| 4 | Near Mint (NM or M-) |
|---|---|
| 3 | Very Good Plus (VG+), Generic sleeve[^1]  |
|---|---|
| 2 | Very Good (VG) |
|---|---|
| 1 | Good (G), Good Plus (G+) |
|---|---|
| 0 | Poor (P), Fair (F) |


input json format example:
```json
{
  "artist": "Drexciya",
  "title": "Grava 4",
  "release_format": "LP",
  "number_of_tracks": 8,
  "release_date": 2002,
  "rating": 4.66,
  "votes": 637,
  "have": 2826,
  "want": 4676,
  "limited_edition": false,
  "media_condition": 5,
  "sleeve_condition": 4
}
```

[^1]: Generic sleeve within the context of grading items on Discogs Marketplace refers to a type of sleeve that is not
specific to the release. It should be given a value of 3 because, in theory, it doesn't add, nor subtract the value of 
the record itself.