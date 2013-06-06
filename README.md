jasta
=====

Jabber status bot

1. Install in virtualenv, `pip install -r pip_requirements.txt`
2. Install [redis](http://redis.io)
2. Copy *bot/local_config.py.dist* to *bot/local_config.py* and set up an account for bot
3. Run `python runbot.py`
4. Add bot to your roster
5. Run `python runserver.py`
6. Navigate `http://127.0.0.1:500/your_jid@server.com.html` in your browser to see your current status
7. Navigate `http://127.0.0.1:500/your_jid@server.com.json` in your browser to get status data


