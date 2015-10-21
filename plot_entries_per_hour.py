from pandas import *
from ggplot import *

def plot_weather_data(turnstile_weather):
    entries_per_hour = turnstile_weather.groupby(["hour"], as_index=False)["ENTRIESn_hourly"].sum()

    # Plot with day of week relabeled as abreviation
    plot = ggplot(entries_per_hour, aes('hour', 'ENTRIESn_hourly')) + \
        geom_line(stat='identity') + \
        ggtitle('Subway entries by hour of day (for the month of May)') + \
        ylab('Total entries') + \
        theme(text = element_text(size=25))

    return plot

def main(filename):
    turnstile_weather = pandas.read_csv(filename, parse_dates=True)
    plot_weather_data(turnstile_weather)

if __name__ == "__main__":
    main('turnstile_weather_v2.csv')
