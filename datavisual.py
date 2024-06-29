import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_data():
    df = pd.read_csv('STOCK_OF_STONKS_price_history.csv')

    # convert the timestamp to datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # set the timestamp as the index
    df.set_index('timestamp', inplace=True)

    # plot the buy and sell prices over time
    plt.figure(figsize=(14, 7))
    sns.lineplot(data=df, x=df.index, y='buy_price', label='Buy Price')
    sns.lineplot(data=df, x=df.index, y='sell_price', label='Sell Price')
    
    plt.title('Stock of Stonks Prices Over Time')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.legend(loc='upper right')
    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
    
    #better format
    plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%m/%d %H:%M'))
    plt.gcf().autofmt_xdate()

    plt.savefig('stock_of_stonks_prices_over_time.png')
    plt.show()

if __name__ == "__main__":
    visualize_data()
