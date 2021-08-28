import sys
def main():
    crimes = get_crimes(sys.argv[1])
    robbery = create_crimes(crimes)
    print(robbery)


def get_crimes(fileName):
    crimes = []
    with open(fileName) as file:
        crimes = file.readlines()
    return crimes 

class Crime(object):
    def __init__(self, crime_ID:int, category: str):
        self.crime_ID = crime_ID
        self.category = category
        self.day_of_week = None
        self.month = None
        self.hour = None 
    def __eq__(self, other):
        return type(self) == type(other) and self.crime_ID == other.crime_ID
    def __repr__(self):
        return ("{}\t{} {} {} {}\n").format(self.crime_ID, self.category, self.day_of_week, self.month, self.hour)

def create_crimes(lines: list):
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
        if i[1] == 'ROBBERY' and i[0] not in id_check: #checks for ROBBERY and ID is not a duplicate 
            id_check.append(i[0])
            robbery_v2 = Crime(int(i[0]),str(i[1])) #creates a crime object for unique ID 
            robbery.append(robbery_v2)
    return robbery #returns list of crime objects 

if __name__ == '__main__':
    main()

(/+|\/|\+|\-|\**|\*|\%)