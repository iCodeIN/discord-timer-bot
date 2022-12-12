# Discord Timer Bot

A Discord timer bot, that uses ffmpeg to play a sound when the time is up! 

Code can be hosted locally on linux or on a linux server. 

![image](https://user-images.githubusercontent.com/100603074/204672021-2babe946-f60d-4376-add5-fa260312fbb9.png)

*Use as a starting reference for creating your own :) !*

*Not robust code, will break if kicked while playing sound or if multiple timers are set at the same time :)* 

## Installation

**Note:** *Run the following code as a user, **try to avoid using sudo**, see [here](https://stackoverflow.com/questions/29310688/sudo-pip-install-vs-pip-install-user) for more info.*

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
