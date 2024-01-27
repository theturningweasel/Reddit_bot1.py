import praw
import random
import time
reddit = praw.Reddit(
    client_id="m5sZph1qcs5jtssshbmLOg",
    client_secret="nLIt2DzZWcYvVeRczeQiKlP6wgJKmw",
    user_agent="<console:BotApp:1.0>",
    username = 'The_epic_Did',
    password = 'ubn23mlb')
subreddit = reddit.subreddit('ProgrammerHumor')
python_quotes = ['My favorite language for maintainability is Python.']
for submission in subreddit.hot(limit = 50):
    #print("============")
    #print(submission.title)

    for comment in submission.comments:
        if hasattr(comment, "body"):
            comment_lower = comment.body.lower()
            if " python " in comment_lower:
                print("==========")
                print(comment.body)
                random_index = random.randint(0, len(python_quotes) - 1)
                comment.reply(python_quotes[random_index])
                time.sleep(660)
