from dhooks import Webhook, Embed
from configparser import ConfigParser
import time
import os

config = ConfigParser()

class bcolors:
    magenta = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[38;5;118m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def send():
    # start with clean terminal
    os.system("clear")

    config.read('config.ini')
    w_URL = config.get('discord_webhook_tool', 'URL')

    try:
        hook = Webhook(w_URL)
        arg = input(f"[Discord Webhook Tool][CONNECTED] webhook> ")

        if arg.split()[0] != "embed": # just send text, if input was not embed
            hook.send(arg)

        elif arg.split()[0] != "embed": # send embeds this way (or, if you want to do it your own way, you may write your own code below)
            embed = Embed(
                title="Features",
                description="""⭐ Send custom made embeds
⭐ Send regular messages
⭐ Send links
⭐ Customizable configuration file
⭐ **[Future update]** *~~Embed builder web app~~*
⭐ **[Future update]** *~~GUI~~*""",
                color=0x5865F2, # pick a color (this is a hex-based color value in this example)
                timestamp='now' # sets the timestamp to current time
                )

            embed.set_author(name='By Dr-Insanity') # an author (feel free to change)
            embed.set_thumbnail(url=f"https://github.com/Dr-Insanity/DiscordWebHookTool")
            embed.add_field(name="Download (PC, not mobile)", value='[` Direct Link `](https://github.com/Dr-Insanity/DiscordWebHookTool/archive/refs/heads/main.zip) (ZIP file)') # this is an example of a link (with blue text on the embed)
            embed.set_footer(text="This embed is made with Dr-Insanity's Webhook Tool")

            hook.send(embed=embed)

    except ValueError:
        os.system("clear")
        print(
"""
╔═─═─═─═─═─═─═─═─═─═─═─═─═─═╗                        
║ ❌ webhook URL invalid ❌ ║
╚═─═─═─═─═─═─═─═─═─═─═─═─═─═╝
""")
        time.sleep(3)

        os.system("clear")

        print(
"""
╔═─═─═─═─═─═─═─═─═─═─═─═─═─═╗                        
║ 🔗   New Webhook URL   🔗 ║
╚═─═─═─═─═─═─═─═─═─═─═─═─═─═╝
""")

        # Ask for the webhook URL to use
        webhook_URL = input("specify the webhook URL> ")
        webhook_NME = input("Give this webhook a new name> ")
        config.read('config.ini')
        config.set('discord_webhook_tool', '', webhook_URL)
            
        with open('config.ini', 'w') as f:
            config.write(f)
        
    send()

def AddWebHookURL():
    try:
        open('config.ini', 'r')
        # Ask for the webhook URL to use
        webhook_URL = input("specify the webhook URL> ")
        config.read('config.ini')
        config.set('discord_webhook_tool', 'URL', webhook_URL)
        with open('config.ini', 'w') as f:
            config.write(f)
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
╔═─═─═─═─═─═─═─═─═─═─═─═─═─═─═╗
║ 🔗 Discord Webhook Tool 🔗  ║
║ WebHooks found in config !! ║
╚═─═─═─═─═─═─═─═─═─═─═─═─═─═─═╝
""")
        YesOrNo = input("Do you wish to (use) this or (change)?\nType 'use' or 'change' to make a choice> ")

        proper_replies = ['use', 'change']

        if YesOrNo.lower() in proper_replies:
            if YesOrNo.lower() == 'use':
                send()
            elif YesOrNo.lower() == 'change':
                os.system('clear')
                AddWebHookURL()
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