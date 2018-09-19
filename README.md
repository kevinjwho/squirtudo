# Squirtudo
A Discord helper bot for Pokemon Go communities.

Squirtudo is a Discord bot based off of FoglyOgly's popular Meowth2.0 Bot. https://github.com/FoglyOgly/Meowth

### General Commands:

| Commands | Requirements  | Description |
| -------- |:-------------:| ------------|
| **!help** \[command\] | - | Shows bot/command help, with descriptions. |
| **!about** | - | Shows info about Squirtudo. |
| **!team** \<team\> | - | Let's users set their team role. |
| **!welcome** \[@member\] | *Owner Only* | Sends the welcome message to either user or mentioned member. |
| **!outputlog**  | *Server Manager Only* | Uploads the log file to hastebin and replies with the link. |

### Raid Commands:

| Commands | Requirements  | Description |
| -------- |:-------------:| ------------|
| **!raid** \<pkmn\> \<place\> \[timer\] | *Region Channel* | Creates an open raid channel. |
| **!exraid** \<pkmn\> \<place\> | *Region Channel* | Creates an exraid channel. |
| **!invite**  | *Region Channel* | Check attached pass for entry to exraids. |
| **!raidegg** \<level\> \<place\> \[timer\] | *Region Channel* | Creates a raid egg channel. |
| **!raid** \<pkmn\> | *Raid Egg Channel* | Converts raid egg to an open raid. |
| **!timer** | *Raid Channel* | Shows the expiry time for the raid. |
| **!timerset** \<timer\> | *Raid Channel* | Set the expiry time for the raid. |
| **!location** | *Raid Channel* | Shows the raid location. |
| **!location new** \<place/map\> | *Raid Channel* | Sets the raid location. |
| **!interested** \[number\] | *Raid Channel* | Sets your status for the raid to 'interested'. |
| **!coming** \[number\] | *Raid Channel* | Sets your status for the raid to 'coming'. |
| **!here** \[number\] | *Raid Channel* | Sets your status for the raid to 'here'. |
| **!starting** | *Raid Channel* | Clears all members 'here', announce raid start. |
| **!cancel**  | *Raid Channel* | Cancel your status. |
| **!clearstatus**  | *Server Manager<br/>Raid Channel* | Cancel everyone's status. |
| **!list** | *Region Channel* | Lists all raids from that region channel. |
| **!list**  | *Raid Channel* | Lists all member status' for the raid. |
| **!list interested** | *Raid Channel* | Lists 'interested' members for the raid. |
| **!list coming**  | *Raid Channel* | Lists 'coming' members for the raid. |
| **!list here** | *Raid Channel* | Lists 'here' members for the raid. |
| **!list teams** | *Raid Channel* | Lists teams of the members that have RSVPd. |
| **!duplicate** | *Raid Channel* | Reports the raid as a duplicate channel. |
| **!starttime** \[HH:MM AM/PM\] | *Raid Channel* | Reports the raid as a duplicate channel. |

## General notes on Squirtudo:

Squirtudo relies completely on users for reports. Squirtudo was designed as an alternative to Discord bots that use scanners and other illegitimate sources of information about Pokemon Go. As a result, Squirtudo works only as well as the users who use it. As there are 10+ ways of interacting with Squirtudo, there can be a bit of a rough learning period, but it quickly becomes worth it.

## Known issues:

Compatibility with Python 3.6 on Mac OS X requires running "Install Certificates.command" in the Python 3.6 folder. Incompatible with discord.py 1.0
