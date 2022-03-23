from people import Person
from pathlib import Path
from datetime import datetime
import csv


def csv_to_list_of_dicts(filePath: Path) -> list[list]:
    rows = []
    with open(filePath, "r", encoding="utf-8-sig") as f:
        dialect = csv.Sniffer().sniff(f.read())
        f.seek(0)
        reader = csv.reader(f, dialect=dialect)
        header = next(reader)
        for row in reader:
            rows.append(row)
    output = []
    for row in rows:
        d = dict(zip(header, row))
        output.append(d)
    return output


def remove_empty_values(input: list[dict]) -> dict:
    output = []
    for d in input:
        # remove BOM and NaN in one go:
        cleaned = {str.replace(k, '\ufeff', ""): v for k, v in d.items() if v != ""}
        output.append(Person(**cleaned))
    return output


def get_closest_birthday_people(
    refDate: datetime, people: list[Person], margin: int
) -> list[Person]:

    ref_MMDD = int(datetime.strftime(refDate, "%m%d"))
    sortedList = sorted(people, key=Person.birthday_MMDD.fget)

    closestBirthdayPerson = min(
        sortedList, key=lambda x: abs(x.birthday_MMDD - ref_MMDD)
    )
    i = sortedList.index(closestBirthdayPerson)
    maxIndex = len(sortedList) - 1
    displayIndices = list(range((i - margin), (i + margin + 1)))

    for x, j in enumerate(displayIndices):
        if j < 0:
            displayIndices[x] += maxIndex
        elif j > maxIndex:
            displayIndices[x] -= maxIndex

    return [sortedList[i] for i in displayIndices]


def render_html(people: list[Person]) -> str:
    head = """
    <head>
    <meta charset='utf-8'>
    <title>Birthday Reminder</title>
      <style>
		body {
			font-family: Arial;
			font-size: 20px;
			padding: 10px;
            text-align: center;
			background-color: #ffd35c;
		}
        h1 {
            font-family: Tahoma;
            color: #80012e
        }
        hr {
            height:1px;
            border-width:0;
            color:#80012e;
            background-color:#80012e
        }
        .footer {
            position: fixed;
            bottom: 0;
            right: 0;
            margin: 10px;
            font-size: 70%
        }
        .bday {
            color: #80012e
            font-size: 200%;
            animation: blink 1s linear infinite;
        }
        @keyframes blink{
            0%{opacity: 1;}
            50%{opacity: .1;}
            100%{opacity: 1;}
        }
      </style>
    </head>
    """

    body = f"""
    <body>
    <h1>Birthday Reminder</h1>
    <hr>
    <div>
    <h3 class='{ 'bday' if people[0].birthday_today else '' }'>
        {people[0].birthday_print} - {people[0].firstName} {people[0].lastName} ({people[0].age_this_year})
    </h3>
    <h3 class='{ 'bday' if people[1].birthday_today else '' }'>
        {people[1].birthday_print} - {people[1].firstName} {people[1].lastName} ({people[1].age_this_year})
    </h3>
    <h3 class='{ 'bday' if people[2].birthday_today else '' }'>
        {people[2].birthday_print} - {people[2].firstName} {people[2].lastName} ({people[2].age_this_year})
    </h3>
    </div>
    <hr>
    <p>...because no one needs social media to be reminded of birthdays<p>
    <p class='footer'>© Pasci 2022</p>
    </body>
    """

    fullHTML = "<!DOCTYPE html><html>" + head + body + "</html>"
    return fullHTML
