"""
Name: Sameera Balijepalli
"""
import unittest
from crimetime import Crime
from crimetime import create_crimes
from crimetime import sort_crimes
from crimetime import set_crimetime
from crimetime import update_crimes
from crimetime import find_crime


class MyTest(unittest.TestCase):
    def test_create_crimes(self):
        lines = ["150454719\tROBBERY\tROBBERY ON THE STREET WITH A GUN\n",\
            "150454719\tOTHER OFFENSES\tEVADING A POLICE OFFICER RECKLESSLY\n",\
            "150022065\tNON-CRIMINAL\tAIDED CASE, DOG BITE\n",\
            "150011660\tROBBERY\tROBBERY ON THE STREET, STRONGARM"]
        expected = [Crime(150454719,"ROBBERY"),Crime(150011660,"ROBBERY")]
        self.assertEqual(create_crimes(lines), expected)

    def test_sort_crimes(self):
        crimes_one = [Crime(1, "ROBBERY"), Crime(2, "ROBBERY"), Crime(3,'ROBBERY'), \
            Crime(4, "ROBBERY"), Crime(5, "ROBBERY")]
        expected_one = [Crime(1, "ROBBERY"), Crime(2, "ROBBERY"), Crime(3,'ROBBERY'), \
            Crime(4, "ROBBERY"), Crime(5, "ROBBERY")]
        crimes_two = [Crime(10, "ROBBERY"), Crime(2, "ROBBERY"), Crime(57,'ROBBERY'), \
            Crime(44, "ROBBERY"), Crime(75, "ROBBERY")]
        expected_two = [Crime(2, "ROBBERY"), Crime(10, "ROBBERY"), Crime(44,'ROBBERY'), \
            Crime(57, "ROBBERY"), Crime(75, "ROBBERY")]
        sort_crimes(crimes_one)
        sort_crimes(crimes_two)
        self.assertEqual(crimes_one, expected_one)
        self.assertEqual(crimes_two, expected_two)
    
    def test_set_crimetime(self):
        #test 1
        c1 = Crime(15046293, "ROBBERY")
        c1_e = Crime(15046293, "ROBBERY")
        c1_e.day_of_week = "Tuesday"
        c1_e.month = "May"
        c1_e.hour = "10AM"
        self.assertEqual(set_crimetime(c1, "Tuesday", 5, 22),c1_e)
        #test 2
        c1 = Crime(150160320, "ROBBERY")
        c1_e = Crime(150160320, "ROBBERY")
        c1_e.day_of_week = "Saturday"
        c1_e.month = "February"
        c1_e.hour = "1PM"
        self.assertEqual(set_crimetime(c1, "Saturday", 2, 13),c1_e)
        #test 3
        c1 = Crime(151124583, "ROBBERY")
        c1_e = Crime(151124583, "ROBBERY")
        c1_e.day_of_week = "Tuesday"
        c1_e.month = "December"
        c1_e.hour = "3AM"
        self.assertEqual(set_crimetime(c1, "Tuesday", 12, 3),c1_e)
    
    def test_update_crimes(self):
        crimes = [Crime(1, "ROBBERY"),Crime(2, "ROBBERY"),Crime(3, "ROBBERY")]
        lines = ["150017276	Tuesday	01/06/2015	16:53",\
            "150007374	Saturday	01/03/2015	14:06",\
            "150017787	Tuesday	01/06/2015	13:00"]
        update_crimes(crimes, lines)
        c1 = Crime(1, "ROBBERY")
        c1.day_of_week = "Tuesday"
        c1.month = "January"
        c1.hour = "4PM"
        self.assertEqual(crimes[0], c1)
        c1 = Crime(2, "ROBBERY")
        c1.day_of_week = "Saturday"
        c1.month = "January"
        c1.hour = "2PM"
        self.assertEqual(crimes[1], c1)
        c1 = Crime(3, "ROBBERY")
        c1.day_of_week = "Tuesday"
        c1.month = "January"
        c1.hour = "1PM"
        self.assertEqual(crimes[2], c1)

    def test_find_crime(self):
        #test 1
        crimes = [Crime(10, "ROBBERY"), Crime(20, "ROBBERY"), Crime(30, "ROBBERY")]
        self.assertEqual(find_crime(crimes, 1),-1)
        #test 2
        crimes = [Crime(1, "ROBBERY"), Crime(2, "ROBBERY"), Crime(3, "ROBBERY")]
        self.assertEqual(find_crime(crimes, 1), 0)
        #test 3
        crimes = [Crime(15, "ROBBERY"), Crime(16, "ROBBERY"), Crime(17, "ROBBERY")]
        self.assertEqual(find_crime(crimes, 17),2)


if __name__ == '__main__':
    unittest.main()
