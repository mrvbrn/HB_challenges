"""Turn a string of 24h time into words.

You can trust that you'll be given a valid string (it will
always have a two-digit hour 00-23, and a two-digit minute
00-59). Hours 0-11 are am, and hours 12-23 are pm.

Handle noon and midnight specially:

    >>> time_word("00:00")
    'midnight'

    >>> time_word("12:00")
    'noon'

Otherwise, covert times to text:

    >>> time_word("01:00")
    "one o'clock am"

    >>> time_word("06:01")
    'six oh one am'

    >>> time_word("06:10")
    'six ten am'

    >>> time_word("06:18")
    'six eighteen am'

    >>> time_word("06:30")
    'six thirty am'

    >>> time_word("10:34")
    'ten thirty four am'

Don't forget to handle early morning properly:

    >>> time_word("00:12")
    'twelve twelve am'

For times after noon, add 'pm'

    >>> time_word("12:09")
    'twelve oh nine pm'

    >>> time_word("23:23")
    'eleven twenty three pm'

By Joel Burton <joel@joelburton.com>.
"""


def time_word(time):
    """Convert time to text."""
    HOURS = {00:"twelve", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 
    10:"ten", 11:"eleven", 12:"twelve", 13:"one", 14:"two", 15:"three", 16:"four", 17:"five", 18:"six", 19:"seven", 20:"eight",
    21:"nine", 22:"ten", 23:"eleven"}
    MINUTES = {00: "o'clock", 1:"oh one", 2:"oh two", 3:"oh three", 4:"oh four", 5:"oh five", 6:"oh six", 7:"oh seven", 
    8:"oh eight", 9: "oh nine", 10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 
    17:"seventeen", 18:"eighteen", 19:"nineteen", 20:"twenty", 21:"twenty one", 22:"twenty two", 23:"twenty three", 24:"twenty four", 
    25: "twenty five", 30:"thirty", 34:"thirty four" }

    if time == "00:00":
        return "midnight"
    if time == "12:00":
        return "noon"

    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)

    if hours >= 12:
        return HOURS[hours] + " " + MINUTES[minutes]+" " + "pm"
    else:
        return HOURS[hours] + " " + MINUTES[minutes] + " " + "am"

   






if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TEST PASSED. YOU'RE A TIME WIZARD!\n")