# Telegram Market pAulse Bot
_****Currently a work in progress**_

**This bot is designed to be used in conjunction with Telegram. Its purpose is to analyze financial markets and send alerts to its users.**

### Here is a basic Flow Chart of its operation.
*_Note this is incomplete and will be updated continuing development_
![Basic User Flow Chart](/FlowChart_v0.01/UI.png)


## Steps To Download
1. Fork this repo
2. Create a virtual environment on your computer using Anaconda or your favorite environment package. (Optional, but recommended)
  1. To setup Anaconda, follow the official installation instructions here -> https://www.continuum.io/downloads.
  2. Run ```conda create --name telegram-market-bot python=3``` to create a new Anaconda environment for the project.
  3. Then run ```source activate telegram-market-bot``` on Linux/macOS or ```activate cryptocurrency-analysis``` if you use Windows.
3. Download the dependencies listed below


* ```conda install pandas ```

* ```conda install -c conda-forge python-telegram-bot ```
(Or follow the official installation instructions here) -> https://github.com/python-telegram-bot/python-telegram-bot


4. Once your environment is setup clone the repository with
``` git clone https://github.com/<your_name_here>/telegram_marketpulse.git```
5. To use the Bot you will need to setup your own bot and generate an authorization token through Telegram's @BotFather. Instructions can be found here -> https://core.telegram.org/bots#6-botfather
6. Once you have an authorization token, navigate to the subdirectory called "*/api_keys*" and create a file labeled ***tele_keys.py***
7. Copy and paste this code, fill in the blanks with your token and channel, then save.

        MYChannelID = "<your_channel_id>"
        Token = "<your_token_here>"
If you'd like to test your bot use this simple code inside tele_keys.py and run the script.

        import telegram
        BOT = telegram.Bot(token=Token)
        BOT.sendMessage(MYChannelID,'test')

8. You're done! Run the bot and start developing! ```python tele_message_handler.py```

## Pull Requests and Develoment
Currently, this is a solo project. If you'd like to contribute feel free to issue a pull request or message me privately. I will continue development on my own time and plan to make it available for download on PyPy when I feel it's 1.0.


## Setup Issues
If you are having trouble and followed the instructions, feel free to contact me for help.

##### Finding the channelID

If you are having trouble finding your channelID you can go to telegram and add @getidsbot for your **personal** id number.
The channelID you see is your personal channelID and any messages sent you from the bot will be private and self-directed. I use this for testing.

If you have a public telegram channel the process is a bit more convoluted.(If there's an easier way I'd love to know)

Navigate to https://web.telegram.org/ Login, and find the channel you want to use the bot on. Add your bot as an admin and note the numbers at the end of the url.

It should look something like this https://web.telegram.org/#/im?p=c1102333260_15025125804615986862

Grab the first ten digits and prepend -100 in front of them. If you use the example above your channelID should look like this.
-1001102333260

That's it! :bowtie:
