import snscrape.modules.twitter as sntwitter
import pandas as pd

tweet_data=[]

username=input("Enter Username: ")
number=int(input("Enter how many tweets you want: "))

for i,tweets in enumerate(sntwitter.TwitterSearchScraper('{}'.format(username)).get_items()):
    if i>number:
        break
    tweet_data.append([tweets.date,tweets.content,tweets.user.username
                       ,tweets.url,tweets.user.followersCount,tweets.likeCount])

df=pd.DataFrame(tweet_data,columns=['Date','Tweets','Username','Url','Followers','Likes'])
df.to_csv(f'{username}.csv',index=False,encoding='utf-8')
