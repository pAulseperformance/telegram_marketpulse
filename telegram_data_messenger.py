#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Simple Bot to post Telegram channel financial alerts

import telegram, tele_keys, analysis
import logging
import matplotlib as mpl
import matplotlib.pyplot as plt
plt.style.use('ggplot')

# import cryptocompare_wrapper as ccw

# Telegram API keys
Token = tele_keys.Token
MYChannelID = tele_keys.MYChannelID
BOT = telegram.Bot(token=Token)
# BOT.sendMessage(MYChannelID,'test')



def save_plot(symbol):
    df = ccw.daily_price_historical(symbol)
    fig, ax = plt.subplots(nrows=1, figsize=(15,8))
    ax.plot(df.timestamp, df.close)
    plt.savefig('foo.png', bbox_inches='tight')

def send_image_from_disk(chat_id):
    BOT.send_photo(chat_id=chat_id, photo=open('foo.png', 'rb'))


message = analysis.poll_volume_day('btc')
BOT.sendMessage(MYChannelID, message)


# TODO: Run poll_volume_day once a day @ 2pm EST or 01800 UTC
# Build intraday volume indicator similar
# expand to all coins
# for coin in coinlist:
# poll_volume_alert(coin)
def main():
    BOT.sendMessage(MYChannelID, poll_volume_day('btc'))


if __name__ == '__main__':
    main()
