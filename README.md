# Slack View

Stream in real time a Slack channel to a web page. 

Slack View is a web app that can show mutliple Slack channels as separate Slack View pages.

# Demo

This is a live Slack View example of the Bad Actors Slack channel from https://mellican.com/badactors:

<p align="center"> 
<img src="https://mellican.com/images/badactors.png?github=slackview" width=70%><br>
These bad actors aren't from Hollywood.
</p>

## Pre-requisites

* Python 3

## Installation

```
git clone https://github.com/meltaxa/slackview.git
cd slackview
pip3 install -r requirements.txt
cp config.yml-example config.yml
```

## Configuration

Update the config.yml file is the slack_app_token and slack_bot_token values.

Further configuration and customization is available inside the config.yml file. Instructions
are provided within.

#### To obtain a Slack API and BOT token:
1. Visit https://api.slack.com/apps
1. Click "Create New App"
1. Call the App "SlackView"
1. Under Features > OAuth & Permissions > Scopes, add the following OAuth scopes:

   * channels:history
   * channels:read
   * users:read
   * emoji:read

1. Under App Level Tokens > Generate Token and Scopes > add a token name and the connections.write scope.
1. Click "Generate"
1. Copy App Token value and update it in the config.yml file.

1. Click Install App to Workspace

   Accept permissions by clicking the "Allow" button.

1. Copy the Bot User OAUTH Token value and update it in the config.yml file.

#### Add SlackView to the channel

1. The SlackView "bot" app needs to join the channel by issuing the invite command from the channel:

   ```/invite @SlackView```

# Using Slack View

1. Start Slack View from command line:

    ```python3 ./app.py```

1. The console output will display the Slack View URL to use.

# Docker version

1. Create a config directory which will be mounted as a volume for Docker.

1. Place your config.yml in the config directory.

1. Run the Docker image with the volume switch to mount your config directory as /config in the image. For example:

    ```docker run -v /path/to/config_dir:/config -p 7000:7000 -e TZ=Australia/Brisbane meltaxa/slackview```

    Note, by default the Docker container will be set in UTC timezone. Set the timezone using the ```-e TZ=...``` option.

1. The Slack View app will be running on: http://\<ip address\>:7000

# PHP version

Slack View was originally written in PHP which only provided a snapshot of the channel and a page refresh is required to display
the latest messages. For posterity, the php version of Slack View is available under the [php branch](https://github.com/meltaxa/slackview/tree/php).
