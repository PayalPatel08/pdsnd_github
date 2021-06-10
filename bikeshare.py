import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or
        "all" to apply no month filter
        (str) day - name of the day of week to filter by, or
        "all" to apply no day filter
    """

    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city = input('Please enter name of the city you want to explore.'
                     'valid cities are Chicago, New York City, Washington.\n').lower()
        if city not in CITY_DATA.keys():
            print("Please choose a vlid city name from Chicago, New York City and Washington.")
        else:
            break

# TO DO: get user input for month (all, january, february, ... , june)

    while True:
        month = input('which month?\nPlease choose a month from January,February, March, April, May, June or Choose All Months\n(Please type full month name or type "All" for no filter.)\n').lower()
        if month not in months:
            print("Please enter a valid month name.")
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = input('Please Select a day of week or all days:(Type "All" for all days)\n')
        if day not in days:
            print('Please enter a valid day name.')
        else:
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month_name'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month_name'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month_name'].mode()[0]
    print('Most common month:', most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('Most common day of the week:', most_common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour

    most_common_hour = df['hour'].mode()[0]
    print('Most common hour of the day:', most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most commonly used Start Station:', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most commonly used End Station:', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    combination_start_end_station = df.groupby(['Start Station', 'End Station']).count().max()[0]
    print('Most frequent combination of Start and End Station:', combination_start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Duration:', total_travel_time)

    # TO DO: display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print('Aveage Travel Time:', average_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_counts = df['User Type'].value_counts()
    print('User Type:\n', user_counts)

    # TO DO: Display counts of gender
    try:
        gender_counts = df['Gender'].value_counts()
        print('\nUser Counts:\n', gender_counts)
    except:
        print("Data not available for Gender Type")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year = df['Birth Year'].min()
        print('\nEarliest Year:', earliest_year)

        recent_year = df['Birth Year'].max()
        print('Most Recent Year:', recent_year)

        most_common_year = df['Birth Year'].mode()[0]
        print('Most Common Year:', most_common_year)
    except:
        print("Data not available for Birth Year")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def view_data(df):
    raw_data = input('\nWould you like to view some data??'
                     'Enter Yes or No.\n').lower()
    while raw_data == 'yes':
        print(df.iloc[0:5])
        break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()