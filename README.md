# Squirtudo
A Discord helper bot for Pokemon Go communities.

Squirtudo is a Discord bot based off of FoglyOgly's popular Meowth2.0 Bot. https://github.com/FoglyOgly/Meowth

### Raid Setup Commands:

| Commands | Shortcuts | Requirements  | Description |
| -------- | --------- |:-------------:| ------------|
| **!raid** \<pkmn\> \<place\> \[minutes_remaining\] | N/A | *#raid-reports* | Creates an open raid channel. |
| **!raidegg** \<level\> \<place\> \[minutes_until_hatch\] | **!egg** \<level\> \<place\> \[minutes_until_hatch\] |*#raid-reports* | Creates a raid egg channel. |
| **!raid** \<pkmn\> | N/A | *Raid Egg Channel* | Converts raid egg to an open raid. |
| **!location new** \<place\> | **!loc new** \<place\> | *Raid Channel* | Sets the raid location. |


### Individual Status Updates:

| Commands | Shortcuts | Requirements  | Description |
| -------- | --------- |:-------------:| ------------|
| **!interested** \[number\] \[party\] | **!i** \[number\] \[party\] | *Raid Channel* | Sets your status for the raid to 'interested'. |
| **!coming** \[number\] \[party\] | **!c** \[number\] \[party\] | *Raid Channel* | Sets your status for the raid to 'coming'. |
| **!here** \[number\] \[party\]| **!h** \[number\] \[party\] | *Raid Channel* | Sets your status for the raid to 'here'. |
| **!cancel**  | **!o**, **!x** | *Raid Channel* | Cancel your status. |

Example: **!i 2 v1** - sets your status for the raid to 'interested', bringing one extra valor player.
party is logged throughout, so any new status commands will reflect the party initialized.

### Raid Status Commands:

| Commands | Shortcuts | Requirements  | Description |
| -------- | --------- |:-------------:| ------------|
| **!starttime** \[HH:MM AM/PM\] | **!st** \[HH:MM AM/PM\] | *Raid Channel* | Set approximate start time to be displayed in channel title. |
| **!location** | **!loc**, **!where**, **!map** | *Raid Channel* | Shows the raid location. |
| **!timer** | N/A | *Raid Channel* | Shows the expiry time for the raid. |
| **!timerset** \<minutes_remaining\> | **!ts** \<minutes_remaining\> | *Raid Channel* | Set the expiry time for the raid. |
| **!duplicate** | **!d** | *Raid Channel* | Reports the raid as a duplicate channel. |

### List Commands:

| Commands | Shortcuts | Requirements  | Description |
| -------- | --------- |:-------------:| ------------|
| **!list**  | **!l** | *Raid Channel* | Lists all member status' for the raid. |
| **!list interested** | **!l i** | *Raid Channel* | Lists 'interested' members for the raid. |
| **!list coming**  | **!l c** | *Raid Channel* | Lists 'coming' members for the raid. |
| **!list here** | **!l h** | *Raid Channel* | Lists 'here' members for the raid. |
| **!list teams** | **!l t** | *Raid Channel* | Lists teams of the members that have RSVPd. |
| **!list instinct**  | **!l ins**, **!l y** | *Raid Channel* | Lists Instinct members for the raid. |
| **!list mystic** | **!l mys**, **!l b** | *Raid Channel* | Lists Mystic members for the raid. |
| **!list valor** | **!l val**, **!l r** | *Raid Channel* | Lists Valor members for the raid. |

### Tag Commands:
| Commands | Shortcuts | Requirements  | Description |
| -------- | --------- |:-------------:| ------------|
| **!tag all** <message>  | N/A | *Raid Channel* | Sends message to all users who have set their status. |
| **!tag interested** <message> | **!tag i** <message> | *Raid Channel* | Sends message to all 'interested' users. |
| **!tag coming** <message> | **!tag c** <message> | *Raid Channel* | Sends message to all 'coming' users. |
| **!tag here** <message> | **!tag h** <message> | *Raid Channel* | Sends message to all 'here' users. |
| **!tag nothere** <message> | **!tag nh** <message> | *Raid Channel* | Sends message to all 'interested' or 'coming' users. |

### The Most Important Command:
| Commands | Shortcuts | Requirements  | Description |
| -------- | --------- |:-------------:| ------------|
| **!starting** | **!go** |*Raid Channel*; To be used only after start time, or once everyone is 'here' | Clears all members 'here', announce raid start. |


## General notes on Squirtudo:

Squirtudo relies completely on users for reports. Squirtudo was designed as an alternative to Discord bots that use scanners and other illegitimate sources of information about Pokemon Go. As a result, Squirtudo works only as well as the users who use it. As there are 10+ ways of interacting with Squirtudo, there can be a bit of a rough learning period, but it quickly becomes worth it.

## Known issues:

Compatibility with Python 3.6 on Mac OS X requires running "Install Certificates.command" in the Python 3.6 folder. Incompatible with discord.py 1.0
