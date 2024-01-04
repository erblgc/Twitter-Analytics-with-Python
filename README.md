# Twitter Analytics with Python

This Python script utilizes various libraries to perform Twitter analytics, including fetching trending topics for a specific location, creating a word cloud from the home timeline, conducting sentiment analysis on a user's timeline, and mapping trends.

## Requirements

Before running the script, make sure to install the required libraries. You can do this by running the following command:

```bash
pip install tweepy wordcloud textblob geopy folium imgkit html2image
```
Additionally, you need to obtain API keys for Twitter and MapQuest, which are used for authentication. Provide these keys in a separate keys.py file in the following format:
```
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_secret = 'your_access_secret'
mapquest_key = 'your_mapquest_key'
```
## Usage

Run the script using the command:
    
    python main.py

Follow the on-screen instructions to input the desired location, create a word cloud, and perform sentiment analysis.
The generated outputs (word cloud, sentiment analysis, and trend map) will be saved in the project directory.

## Important Notes

Ensure you have the necessary API keys from Twitter and MapQuest.
The script may require user interaction for input, such as entering a location or a Twitter username.
Make sure to handle any exceptions or errors gracefully, as indicated in the script.

