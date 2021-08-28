"""
Name: Sameera Balijepalli
"""
import sys 
import copy

def main():
        try:
            for i in sys.argv[1:]: #reads through command line
                crimes = open_file_read(sys.argv[1])
                times = open_file_read(sys.argv[2])
                times = times[1:] #skips header
        
            #creates/sorts/updates crimes
            robbery = create_crimes(crimes)
            sort_crimes(robbery)
            update_crimes(robbery,times)
            print_outputs(robbery) 

            #writing file to robberies.tsv
            _o = open("robberies.tsv","w")
            _o.write("ID\tCategory\tDayOfWeek\tMonth\tHour\n")
            for line in robbery:
                _o.write(str(line))
        except IOError: #catch error and exit 
            print("Unable to open", i)
            sys.exit()

   
class Crime(object):
    """Represents a crime objects.    
    Attributes:        
    crime_ID(int): ID number       
    category(str): category of robbery
    day_of_week(str): day of the week 
    month(str): month of robbery 
    hour(str): hour of robbery 
    """
    def __init__(self, crime_ID:int, category: str):
        self.crime_ID = crime_ID
        self.category = category
        self.day_of_week = None
        self.month = None
        self.hour = None 
    def __eq__(self, other):
        return type(self) == type(other) and self.crime_ID == other.crime_ID
    def __repr__(self):
        return ("{}\t{}\t{}\t{}\t{}\n").format(self.crime_ID, self.category, \
            self.day_of_week, self.month, self.hour)


def open_file_read(fileName):
    """Function reads the file from command argument
    Args:
        fileName(str): command line
    Returns:
        file_open(list): list of data from file
    """
    file_open = []
    with open(fileName) as file:
        file_open = file.readlines()
    return file_open


def create_crimes(lines):
    """This function returns a list of Crime Objects 
    Args: 
        line(lst): list of crimes as a string 
    Returns: 
        robbery(lst): crime objects for each unique robbery 
    """
    list_crimes = []
    id_check = []
    robbery = []
    for i in range(len(lines)):
        line = lines[i]
        _split = line.split()
        list_crimes.append(_split)
    for i in list_crimes: #reads each line from list_crimes 
        if i[1] == 'ROBBERY' and i[0] not in id_check:#checks for ROBBERY/duplicates 
            id_check.append(i[0])
            robbery_v2 = Crime(int(i[0]),str(i[1]))#crime object for unique ID 
            robbery.append(robbery_v2)
    return robbery


def sort_crimes(crimes):#uses insertion sort
    """Function mutates the existing list
    Args:
        crimes(lst): list of crime objects 
    Returns: 
        None 
    """
    size = len(crimes)
    for i in range(1,size):
        j = i
        while j > 0 and crimes[j-1].crime_ID > crimes[j].crime_ID:
            crimes[j - 1].crime_ID, crimes[j].crime_ID = \
                crimes[j].crime_ID, crimes[j-1].crime_ID
            j -= 1


def set_crimetime(crime, day_of_week, month, hour):
    """Fuction updates attributes of Crime given three arguemnts
    Agrs: 
        crime(crime): object of crime 
        day_of_week(str): a string containing a day of the week 
        month(int): integer between 1 and 12 
        day(int): integer between 0 and 23 
    Returns: 
        Crime
    """
    new_crime = copy.copy(crime)
    months = ['January','February','March','April','May','June','July',\
        'August','September','October','November','December']
    time = ['12AM','1AM','2AM','3AM','4AM','5AM','6AM','7AM','8AM',\
        '9AM','10AM','11AM','12PM','1PM','2PM','3PM','4PM','5PM','6PM',\
            '7PM','8PM','9PM','10PM','11PM']
    new_crime.day_of_week = day_of_week
    new_crime.month = months[int(month)-1]
    new_crime.hour = time[int(hour)]
    return new_crime


def update_crimes(crimes, lines):
    """Function updates list of sorted crime objects
    Args:
        crimes(list): sorted crime objects list
        lines(list of str): strings from times.tsv
    Returns:
        None
    """
    for line in lines:
        new_list = line.split()
        _id = new_list[0]
        _found = (find_crime(crimes, _id))
        if _found != -1 or None:
            crime_found = crimes[(find_crime(crimes, _id))]
            _dayweek = new_list[1]
            _date = new_list[2]
            _month = _date[0:2]
            _clock = new_list[3]
            _hour = _clock[0:2]
            new_crime = set_crimetime(crime_found,_dayweek,_month,_hour)
            crimes[_found] = new_crime

        
def find_crime(crimes,crime_ID):#binary search
    """Function returns position of ID 
    Args:
        crimes(list): sorted crime objects list
        crime_ID(int): crime_ID integer
    Returns:
        int: index of of crime object with that ID
        -1: if crime_id not found
    """
    low, high = 0, len(crimes) - 1
    while low <= high:
        midpoint = (low + high)//2
        if crimes[midpoint].crime_ID == int(crime_ID):
            return midpoint
        if int(crime_ID) < int(crimes[midpoint].crime_ID):
            high = midpoint - 1
        else:
            low = midpoint + 1
    return -1


def print_outputs(robbery):
    """Function prints output from updated crime objects
    Args:
        robbery(list): updated crime objects 
    Returns:
        prints needed displays
    """
    total_rob = len(robbery)
    print("NUMBER OF PROCESSED ROBBERIES: {0}".format(total_rob))
    day = []
    months = []
    hours = []
    for i in robbery:#appending each value to a list 
        day.append(i.day_of_week)
        months.append(i.month)
        hours.append(i.hour)
    max_day = max(day, key = day.count)#checks for count of max value
    print("DAY WITH MOST ROBBERIES: {0}".format(max_day))
    max_month = max(months, key = months.count)
    print("MONTH WITH MOST ROBBERIES: {0}".format(max_month))
    max_hour = max(hours, key = hours.count)
    print("HOUR WITH MOST ROBBERIES: {0}".format(max_hour))


if __name__ == '__main__':
    main()
