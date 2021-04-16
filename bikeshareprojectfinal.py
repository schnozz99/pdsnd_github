import time
import pandas as pd
import numpy as np

#define the valud user inputs for comparison
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
valid_months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'all']
valid_days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun', 'all']

#set user messages
try_again_message = "\nPlease enter a valid option"
exit_message = "\nTo exit programme press ctrl c\n"

Testrun = 1

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    if testrun = 1:
        valid = 1
        city = 'chicago'
        month = 'jan'
        day = 'mon'
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    #valid = 0
    options = ''
    while valid == 0:
        print("\nEnter the city you would like to explore, the options are:")
        for i in CITY_DATA.keys():
            options += i.title() + ', '
        print(options)
        city = input("City: ").lower()
        if city in CITY_DATA.keys():
            valid = 1
        else:
            print(try_again_message + exit_message)

    # TO DO: get user input for month (all, january, february, ... , june)
    #valid = 0
    options = ''
    while valid == 0:
        print("\nEnter the month you'd like to filter the data on from January to June or enter all. the options are:")
        for i in valid_months:
            options += i.title() + ', '
        print(options)
        month = input("Month: ").lower()
        if month in valid_months:
            valid = 1
        else:
            print(try_again_message + exit_message)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    #valid = 0
    options = ''
    while valid == 0:
        print("\nEnter the day of the week you'd like to filter the data on or enter all. the options are:")
        for i in valid_days:
            options += i.title() + ', '
        print(options)
        day = input("Day: ").lower()
        if day in valid_days:
            valid = 1
        else:
            print(try_again_message + exit_message)


    print('-'*40)
    print("City chosen: {}".format(city.title())+'\n')
    print("Month chosen: {}".format(month.title())+'\n')
    print("Day chosen: {}".format(day.title())+'\n')
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime and create month and day of the week columns
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.dayofweek
    df['Day of Week Name'] = df['Start Time'].dt.weekday_name
    df['Hour'] = df['Start Time'].dt.hour
    df['Start and End Station'] = df['Start Station'] + ' to ' + df['End Station']

    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = valid_months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['Month'] == month]

    if day != 'all':
        # use the index of the months list to get the corresponding int
        day = valid_days.index(day)

        # filter by month to create the new dataframe
        df = df[df['Day of Week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = valid_months[df['Month'].mode()[0] - 1]
    print("\nMost common month: {}".format(common_month.title()))

    # TO DO: display the most common day of week
    common_day = valid_days[df['Day of Week'].mode()[0]]
    print("\nMost common day of week: {}".format(common_day.title()))


    # TO DO: display the most common start hour
    print("\nMost common hour: {}:00".format(df['Hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("\nMost common start station: {}:00".format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print("\nMost common end station: {}:00".format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    print("\nMost common start to end station: {}".format(df['Start and End Station'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time, as time in seconds changing to days
    total_travel_time = round(df['Trip Duration'].sum() / 86400 , 1)
    print("\nTotal travel time: {} (days)".format(total_travel_time))

    # TO DO: display mean travel time, as time in seconds changing to minutes
    mean_travel_time = round(df['Trip Duration'].mean() / 60, 1)
    print("\nMean travel time: {} (mins)".format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("\nUser Type Counts:\n{}".format(df['User Type'].value_counts()))

    # TO DO: Display counts of gender
    print("\nGender Counts:\n{}".format(df['Gender'].value_counts()))

    # TO DO: Display earliest, most recent, and most common year of birth
    print("\nOldest traveller birth year: {}".format(int(df['Birth Year'].min())))
    print("\nYoungest traveller birth year: {}".format(int(df['Birth Year'].max())))
    print("\nMost common traveller birth year: {}".format(int(df['Birth Year'].mode())))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        valid = 0
        more_data = 0
        while valid == 0 or more_data == 0:
            data_request = input("\nWould you like to see the raw data, enter Y or N:").upper()
            if data_request in ['Y', 'N']:
                valid = 1
                if data_request == 'Y':
                    print(df.head())
                else:
                    more_data = 1
                    column_names = ''
                    for col in df.columns:
                        column_names += col + ', '
                    print("\nColumn Names: {}".format(column_names))
            else:
                print(try_again_message + exit_message)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
