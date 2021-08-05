# bolbobot
A discord frame data bot for Absolver.
Currently running version 1.1, using Python 3.9.  
Requires the following python libraries: os, json, discord, dotenv, discord.ext

Frame data acquired from [SloClap's official frame data spreadsheet](https://docs.google.com/spreadsheets/d/137K5enErK3GuWo9dLuOe7m4teMnJuutmK8wtAZx7sW0/edit#gid=702127089), [J0ker's frame data sheet](https://drive.google.com/file/d/1XkZQ5s955sMQFkMig2lGBEh6R2JJNg9P/view), and my own personal knowledge.

This bot is inspired and based on the [old Tekken 7 frame bot](https://github.com/BKNR/mokujin) by BKNR.

## To use
The command is !bolbo get (movename) to retrieve frame data. Sword moves not done yet.
There's also a *sneaky* hidden command.

## The files
bolbobot.py - The main body of the program.  
alias.py - A giant dictionary. Used to check for move aliases so the user doesn't have to type the full name of every move and can instead type common alises or shortened names.   
movelist.json - Contains the data for every attack. Probably should have split this up into separate files cause it's a 1.5k line json now. Eh, it was easier to program this way.
