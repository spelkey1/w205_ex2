import tweepy

consumer_key = "O5uOThh1fyaytp1nATdmVyiRW";
#eg: consumer_key = "YisfFjiodKtojtUvW4MSEcPm";


consumer_secret = "umhLLDU56oISV6ivXMuCK29wC3xWkKSqoT38K1a3slghTjjMcg";
#eg: consumer_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token = "725837135715037184-hmwcvxUKOPs3xpMZQ6JHpcDHWQmTkvF";
#eg: access_token = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token_secret = "cyZeFW5T4LL23OKds1eKNDYJszQB0XjSdGNeQbWqZfzcT";
#eg: access_token_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



