## Description
A bot for Jabber written in Python 3. If you send message to him, he will resend it to all contacts.

## Installation
Install [SleekXMPP](https://github.com/fritzy/SleekXMPP) package via pip3 and change the following line in the script to the actual login/password pair for bot:
```
xmpp = JabberBot('bot_name@hostname', 'password')
```
Use [supervisor](http://supervisord.org/) for running this script in the background infinitely. You can find a config file for supervisor in this repository too. Probably you need to change only one line in this config:
```
command=/usr/bin/python3 /path/to/jabber-bot.py
```
