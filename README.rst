OBX
===


**NAME**


``OBLX`` - object links


**SYNOPSIS**


|
| ``oblx <cmd> [key=val] [key==val]``
| ``oblx -cviw``
| ``oblx -d`` 
| ``oblx -s``
|

**DESCRIPTION**


``OBLX`` has all you need to program a unix cli program, such as disk
perisistence for configuration files, event handler to handle the
client/server connection, deferred exception handling to not crash
on an error, etc.

``OBLX`` allows for easy json save//load to/from disk of objects. It
provides an "clean namespace" Object class that only has dunder
methods, so the namespace is not cluttered with method names. This
makes storing and reading to/from json possible.

``OBLX`` is a demo bot, it can connect to IRC, fetch and display RSS
feeds, take todo notes, keep a shopping list and log text. You can
also copy/paste the service file and run it under systemd for 24/7
presence in a IRC channel.

``OBLX`` is Public Domain.


**INSTALL**


installation is done with pipx

|
| ``$ pipx install oblx``
| ``$ pipx ensurepath``
|
| <new terminal>
|
| ``$ oblx srv > oblx.service``
| ``$ sudo mv oblx.service /etc/systemd/system/``
| ``$ sudo systemctl enable oblx --now``
|
| joins ``#oblx`` on localhost
|


**USAGE**


use ``oblx`` to control the program, default it does nothing

|
| ``$ oblx``
| ``$``
|

see list of commands

|
| ``$ oblx cmd``
| ``cfg,cmd,dne,dpl,err,exp,imp,log,mod,mre,nme,``
| ``now,pwd,rem,req,res,rss,srv,syn,tdo,thr,upt``
|

start daemon

|
| ``$ oblx -d``
| ``$``
|

start service

|
| ``$ oblx -s``
| ``<runs until ctrl-c>``
|


**COMMANDS**


here is a list of available commands

|
| ``cfg`` - irc configuration
| ``cmd`` - commands
| ``dpl`` - sets display items
| ``err`` - show errors
| ``exp`` - export opml (stdout)
| ``imp`` - import opml
| ``log`` - log text
| ``mre`` - display cached output
| ``now`` - show genocide stats
| ``pwd`` - sasl nickserv name/pass
| ``rem`` - removes a rss feed
| ``res`` - restore deleted feeds
| ``req`` - reconsider
| ``rss`` - add a feed
| ``syn`` - sync rss feeds
| ``tdo`` - add todo item
| ``thr`` - show running threads
| ``upt`` - show uptime
|

**CONFIGURATION**


irc

|
| ``$ oblx cfg server=<server>``
| ``$ oblx cfg channel=<channel>``
| ``$ oblx cfg nick=<nick>``
|

sasl

|
| ``$ oblx pwd <nsvnick> <nspass>``
| ``$ oblx cfg password=<frompwd>``
|

rss

|
| ``$ oblx rss <url>``
| ``$ oblx dpl <url> <item1,item2>``
| ``$ oblx rem <url>``
| ``$ oblx nme <url> <name>``
|

opml

|
| ``$ oblx exp``
| ``$ oblx imp <filename>``
|


**FILES**

|
| ``~/.oblx``
| ``~/.local/bin/oblx``
| ``~/.local/pipx/venvs/oblx/*``
|

**AUTHOR**

|
| ``Bart Thate`` <``bthate@dds.nl``>
|

**COPYRIGHT**

|
| ``OBLX`` is Public Domain.
|
