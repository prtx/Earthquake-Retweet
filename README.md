# Nepal Quake Retweet

A computerized real-time retweet mechanism using Twitter API. Analyzes tweets to filter out only those related to [April 2015 Nepal Earthquake](https://en.wikipedia.org/wiki/April_2015_Nepal_earthquake).

![Alt text](https://media.licdn.com/mpr/mpr/AAEAAQAAAAAAAAX6AAAAJDIxMDYwOWMzLTdjYzUtNDQwMi1iMWQwLTBiMzM4Yjc5MTExZg.jpg "April 2015 Nepal Earthquake")

The system associated with twitter handle [@quakeretweets](https://twitter.com/quakeretweets) was live in 2nd May, 2015 and retweeted 900+ tweets.
![Alt text](https://image.ibb.co/bRJyQm/Screenshot_from_2017_10_28_15_33_04.png "@quakeretweets in action")

## To use
- Register you Twitter app and generate access keys from [here](https://apps.twitter.com/). You will need two keys. One for streaming, next for retweeting.
- Update the keys in `keys.py`.
- Run

    $ python3 engine.py
