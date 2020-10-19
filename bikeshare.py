import pandas as pd
from datetime import datetime
from datetime import timedelta
import time

# Filenames
#chicago = 'chicago.csv'
#new_york_city = 'new_york_city.csv'
#washington = 'washington.csv'
#reduce the whitespace for for readablity.

##Descrption of the Project
#The developed  program allows the user to explore an US bikeshare system database
#and retrieve statistics information from the database.
#The user is able filter the information by city, month and weekday,
#in order to visualize statistics information related to a specific subset of data.
#The user is also able to chose to view raw data and to sort this data by columns,
#in ascending or descending order.

def welcome_message(df):
    print('Hello Welcocme to the Bike Share')


def enterCity():

    cityName = ''
    while cityName.lower() not in ['chicago', 'new york', 'washington']:
        cityName = input('\nHello! Let\'s explore some US bikeshare data!\n'
                     'Would you like to see data for Chicago, New York, or'
                     ' Washington?\n')
        if cityName.lower() == 'chicago':
            return 'chicago.csv'
        elif cityName.lower() == 'new york':
            return 'new_york_city.csv'
        elif cityName.lower() == 'washington':
            return 'washington.csv'
        else:
            print('Sorry, I do not understand your input. Please input either '
                  'Chicago, New York, or Washington.')

def enterTimeFilter():

    time_filter = ''
    while time_filter.lower() not in ['month', 'day', 'none']:
        time_filter = input('\nWould you like to filter the data by month, day,'
                            ' or not at all? Type "none" for no time filter.\n')
        print('\n Entered timefilter',time_filter.lower())
        if time_filter.lower() == 'month':
            return time_filter.lower()
        elif time_filter.lower() == 'day':
            return time_filter.lower()
        elif time_filter.lower() == 'none':
            return time_filter.lower()
        else:
                print('Sorry, I do not understand your input. Please input either '
                  'month', 'day', 'none.')

    return time_filter.lower()

def enterMonth():

    month_input = ''
    months_dict = {'january': 1, 'february': 2, 'march': 3, 'april': 4,
                   'may': 5, 'june': 6}
    while month_input.lower() not in months_dict.keys():
        month_input = input('\nWhich month? January, February, March, April,'
                            ' May, or June?\n')
        if month_input.lower() not in months_dict.keys():
            print('Sorry, I do not understand your input. Please type in a '
                  'month between January and June')
    month = months_dict[month_input.lower()]
    return ('2017-{}'.format(month), '2017-{}'.format(month + 1))

def enterDay():

    day_input = ''
    day_dict = {'monday': 1, 'tuesday': 2, 'wednesday': 3, 'thursday': 4,'friday': 5, 'saturday': 6,'sunday': 7}
    this_month = enterMonth()[0]
    month = int(this_month[5:])
    print('month',month)
    while day_input.lower() not in day_dict.keys():
        day_input = input('\nWhich day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n')
        if day_input.lower() not in day_dict.keys():
            print('Sorry, I do not understand your input. Please type in a '
                  'day between Monday and Sunday')
    day = day_dict[day_input.lower()]
    #return ('2017-{}'.format(day), '2017-{}'.format(day + 1))
    day = int(day)
    try:
        start_date = datetime(2017, month, day)
        valid_date = True
    except ValueError as e:
        print(str(e).capitalize())
    end_date = start_date + timedelta(days=1)

    print('\n start date',str(start_date))
    print('\n end date', str(end_date))

    return (str(start_date), str(end_date))


def popularMonth(df):

    months = ['January', 'February', 'March', 'April', 'May', 'June']
    index = int(df['start_time'].dt.month.mode())
    most_popularMonth = months[index - 1]
    print('The most common month is {}.'.format(most_popularMonth))

def popularDay(df):

    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
                    'Saturday', 'Sunday']
    index = int(df['start_time'].dt.dayofweek.mode())
    most_popularDay = days_of_week[index]
    print('The most common day of week for start time is {}.'.format(most_popularDay))

def popularHour(df):

    most_popularHour = int(df['start_time'].dt.hour.mode())
    if most_popularHour == 0:
        am_pm = 'am'
        popularHour_readable = 12
    elif 1 <= most_popularHour < 13:
        am_pm = 'am'
        popularHour_readable = most_popularHour
    elif 13 <= most_popularHour < 24:
        am_pm = 'pm'
        popularHour_readable = most_popularHour - 12
    print('The most common hour of day  {}{}.'.format(popularHour_readable, am_pm))

def find_TripDuration(df):

    total_duration = df['trip_duration'].sum()
    print("The total travel time is: {}".format(total_duration))
    minute, second = divmod(total_duration, 60)
    hour, minute = divmod(minute, 60)
    print('The total trip duration is {} hours, {} minutes and {}''seconds.'.format(hour, minute, second))
    average_duration = round(df['trip_duration'].mean())
    m, s = divmod(average_duration, 60)
    if m > 60:
        h, m = divmod(m, 60)
        print('The average trip duration is {} hours, {} minutes and {}'
              ' seconds.'.format(h, m, s))
    else:
        print('The average trip duration is {} minutes and {} seconds.'.format(m, s))

def find_cmnStation(df):

    common_start = df['start_station'].mode().to_string(index = False)
    common_end = df['end_station'].mode().to_string(index = False)
    print('The most common start station is {}.'.format(common_start))
    print('The most common end station is {}.'.format(common_end))

def common_trip(df):

    most_common_trip = df['journey'].mode().to_string(index = False)
    print('The most common trip is {}.'.format(most_common_trip))

def findUsers(df):

    subs = df.query('user_type == "Subscriber"').user_type.count()
    cust = df.query('user_type == "Customer"').user_type.count()
    print('There are {} Subscribers and {} Customers.'.format(subs, cust))

def findGender(df):

    total_count = df['gender'].value_counts()[0]
    male_count = df.query('gender == "Male"').count()[0]
    female_count = df.query('gender == "Female"').count()[0]
    print('Male count -',male_count)
    print('Female count - {}'.format(female_count))
    print('Total Male + Female count - {}'.format(total_count))

def Get_birth_years(df):

    earliest = int(df['birth_year'].min())
    latest = int(df['birth_year'].max())
    mode = int(df['birth_year'].mode())
    print('The oldest users are born in {}.\nThe youngest users are born in {}.'
          '\nThe most common birth year is {}.'.format(earliest, latest, mode))

def DispData(df):

    def is_valid(display):
        if display.lower() in ['yes', 'no']:
            return True
        else:
            return False
    head = 5
    tail = 5
    valid_input = False
    while valid_input == False:
        display = input('\n Would you like to view individual trip data? '
                        'Type \'yes\' or \'no\'.\n')
        valid_input = is_valid(display)
        if valid_input == True:
            break
        else:
            print("Sorry, I do not understand your input. Please type 'yes' or"
                  " 'no'.")
    if display.lower() == 'yes':
        # prints every column except the 'journey' column created in statistics()
        #print('\n Printing every Column-'.format(df[df.columns[0:-1]].iloc[head:tail]))
        print('\n Printing every Column-',df.head(head))
        display_more = ''
        while display_more.lower() != 'no':
            valid_input_2 = False
            while valid_input_2 == False:
                display_more = input('\nWould you like to view more individual'
                                     ' trip data? Type \'yes\' or \'no\'.\n')
                valid_input_2 = is_valid(display_more)
                if valid_input_2 == True:
                    break
                else:
                    print("Sorry, I do not understand your input. Please type "
                          "'yes' or 'no'.")
            if display_more.lower() == 'yes':
                head += 5
                tail += 5
                #print('\n Printing every Column-'.format(df[df.columns[0:-1]].iloc[head:tail]))
                print('\n Printing every Column-',df.head(head))
            elif display_more.lower() == 'no':
                break


def ComputeStats():

    # Filter by city (Chicago, New York, Washington)
    city = enterCity()
    print('Loading data...')
    df = pd.read_csv(city, parse_dates = ['Start Time', 'End Time'])


    new_labels = []
    for col in df.columns:
        new_labels.append(col.replace(' ', '_').lower())
    df.columns = new_labels


    pd.set_option('max_colwidth', 100)


    df['journey'] = df['start_station'].str.cat(df['end_station'], sep=' to ')

    # Filter by time period (month, day, none)
    time_filter = enterTimeFilter()
    print('Time_filter Entered :',time_filter),
    if time_filter == 'none':
        df_filtered = df
    elif time_filter == 'month' or time_filter == 'day':
        if time_filter == 'month':
            filter_lower, filter_upper = enterMonth()
        elif time_filter == 'day':
            filter_lower, filter_upper = enterDay()
        #print('Filtering data...time_filter :',time_filter)
        #print('filter_lower',filter_lower)
        #print('filter_upper',filter_upper)
        df_filtered = df[(df['start_time'] >= filter_lower) & (df['start_time'] < filter_upper)]
       #print('df_filtered',df_filtered)
    print("\n #1 Popular times of travel")

    if time_filter == 'none':
        start_time = time.time()


        popularMonth(df_filtered)
        print("That took %s seconds." % (time.time() - start_time))

    if time_filter == 'none' or time_filter == 'month':
        start_time = time.time()


        popularDay(df_filtered)
        print("That took %s seconds." % (time.time() - start_time))
        start_time = time.time()


    popularHour(df_filtered)
    #print("That took %s seconds." % (time.time() - start_time))
    start_time = time.time()


    find_cmnStation(df_filtered)
    print("That took %s seconds." % (time.time() - start_time))
    print('\n #2 Popular stations and trip')
    start_time = time.time()


    find_TripDuration(df_filtered)
    print("That took %s seconds." % (time.time() - start_time))
    print("\n #3 Trip duration..")
    start_time = time.time()

    common_trip(df_filtered)
    print("That took %s seconds." % (time.time() - start_time))
    print("\n Most common trip..")
    start_time = time.time()


    findUsers(df_filtered)
    print("That took %s seconds." % (time.time() - start_time))
    print("\n#4 User info");
    if city == 'chicago.csv' or city == 'new_york_city.csv':

        start_time = time.time()


        findGender(df_filtered)
        print("That took %s seconds." % (time.time() - start_time))
        start_time = time.time()


        Get_birth_years(df_filtered)
        print("\n That took %s seconds." % (time.time() - start_time))
        print("\n Earliest, most recent, most common year of birth (only available for NYC and Chicago)")


    DispData(df_filtered)
    restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    while restart.lower() not in ['yes', 'no']:
        print("Invalid input. Please type 'yes' or 'no'.")
        restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    if restart.lower() == 'yes':
        ComputeStats()


if __name__ == "__main__":
	ComputeStats()
