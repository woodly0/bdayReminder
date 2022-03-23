from pathlib import Path
from datetime import datetime
from utils import *
import traceback
import webbrowser
import time

reminderDistance = 3  # number of days
dataSource = Path("people.csv")
targetFile = Path("birthday_reminder.html")
errorLogFile = Path("error.log")
today = datetime.today()


def main():
    # load people :
    myDicts = csv_to_list_of_dicts(dataSource)
    people = remove_empty_values(myDicts)
    peopleWithDate = [p for p in people if p._birthday is not None]
    peopleToDisplay = get_closest_birthday_people(today, peopleWithDate, 1)

    # create and save html to display:
    html = render_html(peopleToDisplay)
    targetFile.write_text(html)

    # calculate the distance between birthdays and today
    deltas = [abs(p.birthday_in_x_days) for p in peopleToDisplay]

    if min(deltas) <= reminderDistance:
        # launch browser as gui:
        webbrowser.open_new(targetFile)
        print("launched")
        time.sleep(1)


if __name__ == "__main__":
    print("start")
    try:
        main()
    except Exception as ex:
        traceback.print_exc()
        errorLogFile.write_text(traceback.format_exc())
    print("exit.")
