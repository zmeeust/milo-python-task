from datetime import datetime
import itertools


def filter_dates(dates):
    """Filter input dates for possible date format 'year-month-day'
    """
    possible_dates = []
    for date in dates:
        if len(date[0]) > 2 or len(date[1]) > 2 or len(date[1]) > 2:
            try:
                possible_dates.append(datetime.strptime("{}-{}-{}".format(date[0], date[1], date[2]), "%Y-%m-%d"))
            except Exception:
                pass
        else:
            try:
                possible_dates.append(datetime.strptime("{}-{}-{}".format(date[0], date[1], date[2]), "%y-%m-%d"))
            except Exception:
                pass
    return possible_dates

def get_earliest_possible_legal_date(date):
    """Function get date in format "A/B/C", where A,B,C are integers 
       between 0 and 2999 and output the earliest possible legal date 
       between Jan 1, 2000 and Dec 31, 2999 (inclusive)
    """
    start_date = datetime.strptime("2000-1-1", "%Y-%m-%d")
    end_date = datetime.strptime("2999-12-31", "%Y-%m-%d")
    fixed_date = ['0' + x if len(x) == 1 else x for x in date.split('/')]
    all_dates = list(itertools.permutations(fixed_date))
    possible_dates = filter_dates(all_dates)   
    possible_dates.sort()
    
    if len(possible_dates) > 0:
        if start_date < possible_dates[0] < end_date:
            return("{}".format(possible_dates[0])[:10])
        else:
            return "is illegal"
    else:
        return "is illegal"


if __name__ == '__main__':
    import unittest


    class EarliestPossibleDateTest(unittest.TestCase):
        def test_possible_dates(self):
            self.assertEqual(get_earliest_possible_legal_date("1/2/3"), "2001-02-03")
            self.assertEqual(get_earliest_possible_legal_date("3/20/1"), "2001-03-20")
            self.assertEqual(get_earliest_possible_legal_date("15/25/3"), "2015-03-25")
            self.assertEqual(get_earliest_possible_legal_date("2/1/8"), "2001-02-08")
            self.assertEqual(get_earliest_possible_legal_date("300/1/8"), "is illegal")
            self.assertEqual(get_earliest_possible_legal_date("3000/15/8"), "is illegal")
            self.assertEqual(get_earliest_possible_legal_date("13/13/13"), "is illegal")


    unittest.main()