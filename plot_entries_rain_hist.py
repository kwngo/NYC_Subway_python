from pandas import *
from ggplot import *

def plot_weather_data(turnstile_weather):
    turnstile_weather.is_copy = False

    turnstile_weather.loc[turnstile_weather.rain == 0, ['rain']] = 'Non rainy days'
    turnstile_weather.loc[turnstile_weather.rain == 1, ['rain']] = 'Rainy days'

    effect_of_rain = turnstile_weather[['rain', 'ENTRIESn_hourly']]
    plot = ggplot(effect_of_rain, aes(x='ENTRIESn_hourly', fill="rain")) + \
                  geom_histogram(binwidth = 100) + \
                  ggtitle('Comparison of subway entries (for month of May)') + \
                  ylab('Frequency count') + \
                  xlab('Number of entries') + \
                  xlim(0, 3000) + \
                  theme(text = element_text(size=25))

    return plot

def main(filename):
    turnstile_weather = pandas.read_csv(filename, parse_dates=True)
    plot_weather_data(turnstile_weather)

if __name__ == "__main__":
    main('turnstile_weather_v2.csv')

    
