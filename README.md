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
Please refer to the following chart and use numeric values of media and sleeve condition when sending json data: 
| Value | Media / Sleeve condition | 
|---|---|
| 5 | Mint |
| 4 | Near Mint (NM or M-) |
| 3 | Very Good Plus (VG+), Generic sleeve |
| 2 | Very Good (VG) |
| 1 | Good (G), Good Plus (G+) |
| 0 | Poor (P), Fair (F) |


input json format examples:
```json
{
  "artist": "DMX Krew",
  "title": "Dread It A Go EP",
  "release_format": "EP",
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
```json
{
  "artist": "Zeta Reticula",
  "title": "I Am Mensch",
  "release_format": "12\"",
  "number_of_tracks": 4,
  "release_year": 2018,
  "rating": 4.67,
  "votes": 36,
  "have": 194,
  "want": 173,
  "limited_edition": false,
  "media_condition": 5,
  "sleeve_condition": 5
}
```
```json
{
  "artist": "Junq",
  "title": "Lila Dreams EP",
  "release_format": "EP",
  "number_of_tracks": 4,
  "release_year": 2017,
  "rating": 4.64,
  "votes": 77,
  "have": 173,
  "want": 910,
  "limited_edition": false,
  "media_condition": 5,
  "sleeve_condition": 5
}
```

[^1]: A generic sleeve within the context of grading items on Discogs Marketplace refers to a type of sleeve that is not
specific to the release. It should be given a value of 3 because, in theory, it doesn't add, nor subtract the value of 
the record itself.