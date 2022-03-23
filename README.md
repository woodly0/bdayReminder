# Bday Reminder

Very basic app that reminds you of the birthdays of people you care about. The people data can be stored and modified in a simple CSV file.

## Description

If you're thinking about quitting your Facebook or LinkedIn account but you still want to be reminded of your friend’s birthdays then you should have a look at this little app.
Follow the examples in the `people.csv` file and populate it with your friend’s personal data, most importantly names and birthdays.
The app generates an HTML file with the 3 closest birthdays. If a birthday is within the reminder distance, the default browser will pop up and show the created file.


## Getting Started

### Dependencies

* Python 3.9
* No additional Python libraries are needed
* Tested on Windows Server 2016 & Windows 10

### Installing

* Fork/Download the project
* Add data to the `people.csv` file
* In the `app.py` file you’ll find the constant ``` reminderDistance = 3``` which defines the number of days within which you would like to be reminded of a birthday. It refers basically to the absolute distance in days between today and whatever birthday.

### Executing program

* Run the app.py file
* Use a scheduler to execute once a day or similar

## Help

Check out the log file that is created on error

## Authors

Main contributors:

* [woodly0]("https://github.com/woodly0") 

## License

This project is licensed under the MIT License 2022.

## Acknowledgments

Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)