from datetime import datetime, date


class Person:
    _today = date.today()

    def __init__(
        self,
        firstName: str,
        lastName: str,
        birthday: str = None,
        street: str = None,
        zip: str = None,
        city: str = None,
        country: str = None,
        email: str = None,
        phone: str = None,
    ):
        self.firstName = firstName
        self.lastName = lastName
        self._birthday = (
            datetime.strptime(birthday, "%d.%m.%Y").date()
            if not birthday is None
            else None
        )
        self.street = street
        self.zip = int(zip) if not zip is None else None
        self.city = city
        self.country = country
        self.email = email
        self.phone = phone

    @property
    def birthday_print(self) -> str:
        if self._birthday is not None:
            return date.strftime(self._birthday, "%d.%m.%Y")
        else:
            return "n/a"

    @property
    def birthday_MMDD(self) -> int:
        if self._birthday is not None:
            return int(date.strftime(self._birthday, "%m%d"))

    @property
    def age_exact(self) -> int:
        if self._birthday is not None:
            years = self._today.year - self._birthday.year
            if self._today.month < self._birthday.month or (
                self._today.month == self._birthday.month
                and self._today.day < self._birthday.day
            ):
                years -= 1
            return years
    
    @property
    def age_this_year(self) -> int:
        if self._birthday is not None:
            return self._today.year - self._birthday.year

    @property
    def birthday_in_x_days(self) -> int:
        if self._birthday is not None:
            thisYearsBday = datetime.strptime(
                str(self._today.year) + date.strftime(self._birthday, "%m%d"),
                "%Y%m%d",
            ).date()
            delta = thisYearsBday - self._today
            return delta.days

    @property
    def birthday_today(self) -> bool:
        if self._birthday is not None:
            thisYearsBday = datetime.strptime(
                str(self._today.year) + date.strftime(self._birthday, "%m%d"),
                "%Y%m%d",
            ).date()
        return self._today == thisYearsBday

    def __repr__(self):
        return f"<Person> {self.lastName}, {self.firstName}"
