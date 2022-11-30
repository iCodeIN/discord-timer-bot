# Discord Timer Bot

A Discord timer bot, called with `.timer`, that plays a sound when time is up! 

![image](https://user-images.githubusercontent.com/100603074/204672021-2babe946-f60d-4376-add5-fa260312fbb9.png)

## Installation

```
git clone https://github.com/A-poc/discord-timer-bot;cd discord-timer-bot;pip install -r requirements.txt
```

## Configuration

You must change the following values in timerBot.py:

```python
17: token="REDACTED" # Discord bot token
72: channel=client.get_channel("REDACTED") # Voice chat channel ID
74: source=FFmpegPCMAudio('REDACTED') # Local audio file to play once time is up
```

## Usage
### Start timer

```
.timer 1 minute
.timer 2 minutes
.timer 2 mins
.timer 1 second
.timer 1 seconds
.timer 1 secs
```

### Help

```
.help
```
