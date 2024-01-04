import tweepy 
from wordcloud import WordCloud, STOPWORDS
from textblob import TextBlob
from geopy import OpenMapQuest
import folium
import imgkit
from html2image import Html2Image
import keys
hti = Html2Image()

def get_trend_id(country_name):
    trends_available = api.available_trends()
    for location in trends_available:
        if location['name'] == country_name:
            return location['woeid']    

# Authenticate to Twitter
consumer_key = keys.consumer_key
consumer_secret = keys.consumer_secret
access_token = keys.access_token
access_secret = keys.access_secret
mapquest_key = keys.mapquest_key

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.access_token = access_token
auth.access_token_secret = access_secret
api = tweepy.API(auth)

#Customized trend sorter due to place
while True:
    try:
        country = input("Enter place  name: ")
        trend_id = get_trend_id(country)
        trends = api.get_place_trends(trend_id)
        for trend in trends[0]["trends"]:
            print(trend["name"])
        break
    except:
        print("Please enter a valid location(ex: Turkey,Italy) ")

#Timeline wordcloud creater 
public_tweets = api.home_timeline()
all_words = ' '.join([tweet.text for tweet in public_tweets])
wordcloud = WordCloud(width=500, height=300, random_state=21, max_font_size=110).generate(all_words)
wordcloud.to_file('wordcloud.png')

# Sentiment analysis for a particular account or for the whole users from that region 
while True:
    try:
        screenName = input("Enter the username for create sentiment analysis : ")
        sentimentA = api.get_user(screen_name=screenName)
        for tweet in sentimentA.timeline():
            print(tweet.text)
            analysis = TextBlob(tweet.text)
            print(analysis.sentiment)
            print("")
        break
    except:
        print("Enter a valid username : ")

#map of the trends
trendsMap = {}
geolocator = OpenMapQuest(api_key=mapquest_key)
map = folium.Map(location=[41.0082, 28.9784], zoom_start=6)
for trend in trendsMap:
    location = geolocator.geocode(trend)
    if location is not None:
        folium.Marker([location.latitude, location.longitude], popup=trend).add_to(map)
map.save('map.html')
with open('./map.html') as f:
    hti.screenshot(f.read(), save_as='map.png')