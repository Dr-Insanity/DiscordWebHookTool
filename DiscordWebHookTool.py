from dhooks import Webhook, Embed
import asyncio
import urllib
from configparser import ConfigParser
from urllib import error
from urllib.request import Request, urlopen
import time
import os

config = ConfigParser()

def send():
    # start with clean terminal
    os.system("clear")

    config.read('config.ini')
    W_URL = config.get('discord_webhook_tool', 'URL')

    try:
        hook = Webhook(W_URL)
        arg = input(f"[Discord Webhook Tool] webhook> ")

        if arg != "embed": # just send text, if input was not embed
            hook.send(arg)

        elif arg == "embed": # send embeds this way (or, if you want to do it your own way, you may write your own code below)
            embed = Embed(
                description="The description of the embed",
                color=0x2f3136, # pick a color (this is a hex-based color value in this example)
                timestamp='now' # sets the timestamp to current time
                )

            embed.set_author(name='Dr-Insanity') # an author (feel free to change)
            embed.add_field(name="Google", value='[click to go to google](https://google.com/)') # this is an example of a link (with blue text on the embed)
            embed.set_footer(text='the text on the footer')

            hook.send(embed=embed)

        else:
            if arg == "x": # exit the application
                exit()
    except ValueError:
        os.system("clear")
        print(
"""
╔═─═─═─═─═─═─═─═─═─═─═─═─═─═╗                        
║ ❌ webhook URL invalid ❌ ║
╚═─═─═─═─═─═─═─═─═─═─═─═─═─═╝
""")
        # Ask for the webhook URL to use
        webhook_URL = input("specify the webhook URL> ")
        config.read('config.ini')
        config.set('discord_webhook_tool', 'URL', webhook_URL)
            
        with open('config.ini', 'w') as f:
            config.write(f)
        
    send()

def ChangeWebHookURL():
    try:
        open('config.ini', 'r')
        # Ask for the webhook URL to use
        webhook_URL = input("specify the webhook URL> ")
        config.read('config.ini')
        config.set('discord_webhook_tool', 'URL', webhook_URL)
        send()

    except FileNotFoundError: # We assume URL was never been given to use.

        # Ask for the webhook URL to use
        webhook_URL = input("specify the webhook URL> ")
        config.read('config.ini')
        config.add_section('discord_webhook_tool')
        config.set('discord_webhook_tool', 'URL', webhook_URL)
        
        with open('config.ini', 'w') as f:
            config.write(f)
        send()

def Q_ChangeHook_InvalidReply():
    os.system("clear")
    print(
"""
╔═─═─═─═─═─═─═─═─═─═─═─═─═─═╗                        
║ ❌    Invalid reply    ❌ ║
╚═─═─═─═─═─═─═─═─═─═─═─═─═─═╝
Your choices are:
- use
- change""")
    time.sleep(3)
    ConfigCheck()

def ConfigCheck():
    os.system("clear")
    try:
        open('config.ini', 'r')
        
        print(
"""
╔═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═╗
║      🔗        Discord Webhook Tool       🔗        ║
║ Hey there!   I found a webhook in the configuration ║
╚═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═╝
""")
        YesOrNo = input("Do you wish to (use) this or (change)?\nType 'use' or 'change' to make a choice> ")

        proper_replies = ['use', 'change']

        if YesOrNo.lower() in proper_replies:
            if YesOrNo.lower() == 'use':
                send()
            elif YesOrNo.lower() == 'change':
                os.system('clear')
                ChangeWebHookURL()
        else:
            Q_ChangeHook_InvalidReply()

    except FileNotFoundError: # We assume URL was never been given to use.

        InitWebhook() # continue the application

def InitWebhook():
    # start with clean terminal
    os.system("clear")

    try:
        open('config.ini', 'r')
    except FileNotFoundError: # We assume URL was never been given to use.

        # Ask for the webhook URL to use
        webhook_URL = input("specify the webhook URL> ")
        config.read('config.ini')
        config.add_section('discord_webhook_tool')
        config.set('discord_webhook_tool', 'URL', webhook_URL)
        
        with open('config.ini', 'w') as f:
            config.write(f)

    send()
def main():
    os.system("clear")
    print(
        """
        ╔═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═╗
        ║      🔗        Discord Webhook Tool       🔗        ║
        ║ Sending Embeds, links and messages with ease through║
        ║ a webhook URL of choice!                            ║
        ║                                                     ║
        ║ Not affiliated with Discord Inc. in any way         ║
        ╚═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═╝
        A moment . . .
        """)

    time.sleep(5) # give people the time to read front page of this CLI-based utility
    os.system("clear") # Clear the current terminal / CMD / Powershell Window
    
    ConfigCheck()

main()