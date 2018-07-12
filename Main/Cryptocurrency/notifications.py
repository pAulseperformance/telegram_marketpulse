# Helper Functions for analysis of cryptocompareAPI
import cryptocompare_wrapper as ccw
# TODO: Add VWAP Strategy
# poll price volume of coin and compare against average volume of coin
# Send message when volume is greater than average VOLUME
# poll trade by trade volume and compare against 24 hour volume or daily

# TODO: Create function that scans all coins and posts biggest winners/losers

# Gets Daily Volume and returns notification
def poll_volume_day(symbol):

    # Get and format data from API
    df = ccw.daily_price_historical(symbol)
    limit = len(df)
    last = limit - 1

    # Compute average daily_volume and assign yesterday daily volume
    dsma_volume = df.rolling(window=30)['volumefrom'].mean()[last]
    daily_volume = df['volumefrom'][last-1] #Daily close volume (grabbing yesterday because slow update on current)
    vpc = (daily_volume - dsma_volume)/dsma_volume*100
    ppc = (df['close'][last] - df['open'][last])/df['open'][last]*100

    # TODO: build volume analysis
    # if vpc is negative and vpc > avgvpc and close > open
    #     indicate low buying volume
    # if vpc is positive and vpc > avgvpc and close > open
    #     indicate high buying volume
    # if vpc is negative and vpc > avgvpc and close < open
    #     indicate low selling pressure
    # if vpc is positive and vpc > avgvpc and close < open
    #     indicate high selling pressure #You should be selling too unless its a bottom


    # volumefrom and volumeto shows buyvolume and sell volume?
    # TODO: If so: print data highlighting a buy or sell day with VWAP

    # TODO: change volumefrom to volumeto to represent basecurrency

    if daily_volume > dsma_volume:

        output  = "ALERT!: High Daily Volume\n"
        output += "Date: {}\n".format(df['timestamp'][last])
        output += "Volume PCTChange: {:.2f}%\n".format(vpc)
        output += "Open: {}\n".format(df['open'][last])
        output += "High: {}\n".format(df['high'][last])
        output += "Low: {}\n".format(df['low'][last])
        output += "Close: {}\n".format(df['close'][last])
        output += "Price PCTChange: {:.2f}%\n\n".format(ppc)

        # TODO: Return link for tradingview?

        return output

    else:
        output  = "Date: {}\n".format(df['timestamp'][last])
        output += "Open: {}\n".format(df['open'][last])
        output += "High: {}\n".format(df['high'][last])
        output += "Low: {}\n".format(df['low'][last])
        output += "Close: {}\n".format(df['close'][last])
        output += "Price PCTChange: {:.2f}%\n\n".format(ppc)

        output += "Volume: {:.0f}\n".format(df['volumefrom'][last-1])
        output += "AvgVolume: {:.0f}\n".format(dsma_volume)
        output += "Volume PCTChange: {:.2f}%\n".format(vpc)

        return output
