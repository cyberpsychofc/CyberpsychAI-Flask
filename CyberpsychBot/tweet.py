import os
import random
import tweepy
from generate_tweet import generate_post_text, generate_reply_text

os.environ["ACCESS_KEY"] = os.getenv("ACCESS_KEY")
os.environ["ACCESS_SECRET"] = os.getenv("ACCESS_SECRET")
os.environ["CONSUMER_KEY"] = os.getenv("CONSUMER_KEY")
os.environ["CONSUMER_SECRET"] = os.getenv("CONSUMER_SECRET")
os.environ["BEARER_TOKEN"] = os.getenv("BEARER_TOKEN")

auth = tweepy.OAuthHandler(os.environ["CONSUMER_KEY"], os.environ["CONSUMER_SECRET"])
auth.set_access_token(
    os.environ["ACCESS_KEY"],
    os.environ["ACCESS_SECRET"],
)

newapi = tweepy.Client(
    bearer_token= os.environ["BEARER_TOKEN"],
    access_token= os.environ["ACCESS_KEY"],
    access_token_secret= os.environ["ACCESS_SECRET"],
    consumer_key= os.environ["CONSUMER_KEY"],
    consumer_secret= os.environ["CONSUMER_SECRET"],
)

api = tweepy.API(auth)

rivals = ['MistralAI','ChatGPTapp','deepseek_ai','AnthropicAI','GeminiApp','github','MSFTCopilot','Apple']


def tweet():
    try:
        sampletweet = generate_post_text()
        
        post_result = newapi.create_tweet(text=sampletweet)
    
    except Exception as e:
        print(f"Tweet couldn't be posted because: {e}")

def reply():
    try:
        username = rivals[random.randint(0,len(rivals) - 1)]
        tweets = api.user_timeline(screen_name=username, count=3, tweet_mode="extended")

        if tweets:
            latest_tweet = tweets[random.randint(0,len(tweets) - 1)]
            tweet_id = latest_tweet.id
            tweet_text = latest_tweet.full_text
            api.update_status(
                status=generate_reply_text(username, tweet_text), 
                in_reply_to_status_id=tweet_id, 
                auto_populate_reply_metadata=True
            )

    except Exception as e:
        print(f"Reply couldn't be posted because: {e}")