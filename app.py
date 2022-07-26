"""this module is to create a flask app to get the tweets """

from flask import Flask, render_template, request
import tweepy

auth = tweepy.OAuthHandler('iyiCjcPprba7ucHl4exaVMmUM',
                           'coEHTM8jyBTpthw8XgXL11mMy3OoRrABSyDIbMDYzADyuWFscm')
auth.set_access_token('1542129125481410561-AvA7McjQlcBPeVxTCVf77MD2zNIxDz',
                      'vdApRpPm0huNwWSUnlkdH6mJwqIlAA2CKsTxb2eVE9KuN')

api = tweepy.API(auth, wait_on_rate_limit=True)

app = Flask(__name__)
"""create flask instance"""


@app.route('/', methods=['GET', 'POST'])
def index():
    """this function is to get the required tweets"""
    if request.method == 'POST':
        search_words = request.form.get("search_word")
        until = request.form.get("until")
        keywords = request.form.get("languages")

        print("inside the post", search_words, until, keywords)

        data = tweepy.Cursor(api.search_tweets, q=search_words, until=until).items(1000)
        send_item = [[i.user.screen_name, "https://twitter.com/" + i.user.screen_name
                      + "/status/" + str(i.id), i.text, i.created_at]
                     for i in data if keywords in i.text]
        print(send_item)
    else:
        send_item = []
    return render_template('index.html', tweets=send_item)


if __name__ == '__main__':
    app.run(debug=True)
