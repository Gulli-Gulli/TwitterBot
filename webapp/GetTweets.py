from multiprocessing.connection import Client
import sys,tweepy,re
from .models import tweets as Tweets

from .DBConnection import DBConnection
database = DBConnection.getConnection()

class GetTweets:

    
    def get(topic):


        try:
            tweetset = {}
            nts = 10
            bearerToken = 'AAAAAAAAAAAAAAAAAAAAAPmqcAEAAAAAvC1OmL9lWXsD5KXJPjP9FFlJ5hk%3Dqhw2OIAgwHLqhaz5oKnKf4pGmA2c3VDV2R9H1R0aMsUiORElDM'
            consumerKey = 'pdngFM526cwEROQfdblZm2OPj'
            consumerSecret = 'jBe4YW53q9LkAt0utNlKMaI5Qowc1HbzjaczTWdu4wkxnsvavz'
            accessToken = '1515959615871066112-KWe5Tg9f6fSLpweewvfZrF9GNd2EtL'
            accessTokenSecret = '0rUk2QjylTcKmY7EhvJs051eF5wqs38ktSrUDeHP25smt'
            
            #auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
            #auth.set_access_token(accessToken, accessTokenSecret)
            auth = tweepy.Client(
                return_type=dict,
                bearer_token= bearerToken,
                consumer_key=consumerKey,
                consumer_secret=consumerSecret,
                access_token=accessToken,
                access_token_secret=accessTokenSecret)
            

            api = tweepy.API(auth)
            # input for term to be searched and how many tweets to search
            
            #searchTerm =topic+ " -filter:retweets"
            searchTerm =topic
            NoOfTerms =int(nts)
            # searching for tweets
            tweets = auth.search_recent_tweets(searchTerm)

            cursor = database.cursor()
            database.commit()
            cursor = database.cursor()

            #query = "INSERT INTO  webapp_tweets(`tweet`, userid, status)  VALUES (%s,%s,%s)"

            
            Tweets.objects.all().delete()
            for tweet in tweets['data']:
                tweetset[tweet['id']]=tweet['text']
                try:
                    #val = (str(tweet['text']), str(tweet['id']), 'Legitimate')
                    #temp = "Insert into webapp_tweets(tweet, userid, status) VALUES("+"'"+str(tweet['text'])+"'"+","+"'"+str(tweet['id'])+"'"+",'Legitimate')"
                    #print(temp)
                    #cursor.execute(temp)
                    Tweets.objects.create(tweet=str(tweet['text']), userid=str(tweet['id']), status='Legitimate')
                except Exception as e:
                    print('Exception',e)
                    
            #print(tweetset) 
       
        except Exception as e:
            print('Exception',e)
        
        database.commit()
        GetTweets.insertdef(searchTerm)

        return tweetset



    def insertdef(topic):
        searchTerm =topic

        cursor2 = database.cursor()

        cursor2.execute("SELECT * FROM webapp_dtweets where tweet like '%"+searchTerm+"%' ")
        query = "INSERT INTO  webapp_tweets(tweet, userid, status)  VALUES (%s,%s,%s)"

        rows = cursor2.fetchall()
        for row in rows:
            val = (str(row[1]), str(row[2]), 'Legitimate')
            cursor2.execute(query, val)
        database.commit()





   
if __name__ == '__main__':
    p=GetTweets.get('movie')
    print(p)

