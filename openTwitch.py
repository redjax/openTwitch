"""
A script to open multiple Twitch streams.
I made this app to help a friend gain viewers. I wanted
to create a script that would take their username as an
argument, and open a web browser to their stream.

As I was writing it, I saw a good opportunity to practice with args,
so I wrote the script to be able to take multiple usernames,
and then open the corresponding stream.

Usage: python openTwitch.py twitch_username1 twitch_username2 ...

To-do:
* Create logic to determine OS/browser
* Allow passing to specific browser
"""

import webbrowser  # For opening stream
import sys  # For argv


def createStreamList():
    """Take list of arguments passed at runtime into list."""
    # Make list out of arguments passed.
    # [1:] starts at 2nd arg, iterates to last.
    streamers = sys.argv[1:]
    for streamer in streamers:
        buildURL(streamer)  # Send username to URL builder.


def buildURL(streamer):
    """Builds Twitch URL for each argument passed."""
    twitchUrl = "https://twitch.tv/"
    url = twitchUrl + streamer  # Twitch site + username from arg.

    openpage(url)


def openpage(url):
    """Open URL built in buildURL()."""
    webbrowser.open(url)


createStreamList()
