The goal of this assignment is to extract features from data and prepare simple feature importance analysis.

The data is in file `train.json`. Each line in this file represents one ad saved in json format.
Each ad contains information like: title, description and some basic ad parameters.

Parameters:

- `title` - title of an ad
- `description` - description of an ad
- `arrival_date` - date when ad arrived to moderation system
- `category_id` - id of ad category
- `price_type` - can be price, arranged, free, exchange or None (if the ad doesn't contain price)
- `price` - value of price
- `user_created_at` - date when user was created
- `label` - 0 if the ad was accepted by moderator, 1 if the ad was rejected by moderator

Additional question:

- How would you design a good testing procedure for this data in order to prevent overfitting?


