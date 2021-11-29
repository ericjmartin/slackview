import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Initializes your app with your bot token and socket mode handler
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))


@app.event("app_mention")
def mention_hello(message, say):
    print('mention_hello')
    say(f'Hi there')
@app.message("hello")
def message_hello(message, say):
    print('message_hello')
    say(f'Hi there')

# Start your app
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
