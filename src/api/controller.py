from datetime import date

from src.api.txt_log_decorator import txt_logger


class Blacklist:
    """Класс проверки на вхождение в черный список."""

    def __init__(self, key):
        """По параметру записываем черный список."""
        self.checker = Checker()
        blacklisted_phones = [
            {'phone': '89993220000', 'expire_date': '2021-12-31'},
            {'phone': '89993220000', 'expire_date': '2022-5-9'},
            {'phone': '88005553535', 'expire_date': '2007-8-22'},
            {'phone': '80554669500', 'expire_date': '2077-9-17'},
        ]
        blacklisted_users = [
            {'username': 'Виталий Волочай', 'expire_date': '2021-12-1'},
            {'username': 'Денис Шарипов', 'expire_date': '2022-5-9'},
            {'username': 'Николай Ридтц', 'expire_date': '2007-7-5'},
            {'username': 'Магомед Халилов', 'expire_date': '2142-2-23'},
        ]
        self._key = key
        if self._key == 'phone':
            self.blacklist = blacklisted_phones
        if self._key == 'username':
            self.blacklist = blacklisted_users

    def __iter__(self):
        """Итератор позволяющий итерироваться по строке в чёрном списке Yields."""
        for blacklisted in self.blacklist:
            yield from blacklisted

    def get_list(self):
        """Метод получения черного списка, без данных с истекшим сроком давности."""
        not_expired_blacklist = []
        for seeking_data in self.blacklist:
            if self.checker.check_date(seeking_data['expire_date']):
                not_expired_blacklist.append(seeking_data)
        return not_expired_blacklist

    @txt_logger
    def check(self, blacklist_data: str) -> bool:
        """Метод проверки нахождения в чёрном списке.

        1)Проверям есть ли данные в чёрном списке.
        2)Находим в списке дату блокировки проверям срок ее годности.
        3)Возвращаем boolean.
        """
        is_blacklisted = False
        class_var = 'check'
        for seeking_data in self.blacklist:
            if seeking_data[self._key] == blacklist_data:
                checked_date = seeking_data['expire_date']
                if self.checker.check_date(checked_date):
                    is_blacklisted = True
                if not self.checker.check_date(checked_date):
                    is_blacklisted = False
        return is_blacklisted, class_var

    @txt_logger
    def add(self, blacklist_data: str, expire_date: str) -> bool:
        """Метод добавления данных в чёрный список.

        1)Проверяем наличие данных в чёрном списке.
        2)Проверям дату на валидность.
        3)Добавляем в чёрный список, записываем срок годности.
        4)Возвращаем результаты.
        """
        class_var = 'add'
        func_result = False
        if self.checker.check_date(expire_date):
            for seeking_data in self.blacklist:
                if seeking_data[self._key] != blacklist_data:
                    if self._key == 'phone':
                        if self.checker.check_phone(blacklist_data):
                            new_data = {self._key: blacklist_data, 'expire_date': expire_date}
                            self.blacklist.append(new_data)
                            func_result = True

                    if self._key == 'username':
                        if self.checker.check_fullname(blacklist_data):
                            new_data = {self._key: blacklist_data, 'expire_date': expire_date}
                            self.blacklist.append(new_data)
                            func_result = True
                if seeking_data == blacklist_data:
                    if self.checker.check_date(seeking_data['expire_date']):
                        new_data = {self._key: blacklist_data, 'expire_date': expire_date}
                        self.blacklist.append(new_data)
                        func_result = True
        return func_result, class_var

    @txt_logger
    def update(self, blacklist_data: str, new_expire_date: str) -> bool:
        """Метод обновления данных в чёрный список.

        1)Проверяем есть ли данные в чёрном списке.
        2)Проверяем новый срок годности.
        3)По результатам проверки меняем срок годности или удаляем из чёрного списка.
        """
        class_var = 'update'
        for position, matching_data in enumerate(self.blacklist):
            if matching_data[self._key] == blacklist_data:
                if self.checker.check_date(new_expire_date):
                    matching_data['expire_date'] = new_expire_date
                    return True, class_var
                if not self.checker.check_date(new_expire_date):
                    self.blacklist.pop(position)
                    class_var = 'update del'
                    return True, class_var
        return False, class_var

    @txt_logger
    def delete(self, blacklist_data) -> bool:
        """Метод удаления данных из чёрного списка.

        1)Проверяем есть ли данные в чёрном списке.
        2)Если есть удаляем данные, срок годности из чёрного списка по позиции.
        Возвращаем boolean.
        Если данных нет возвращаем boolean.
        """
        class_var = 'del'
        for position, matching_data in enumerate(self.blacklist):
            if blacklist_data == matching_data[self._key]:
                self.blacklist.pop(position)
                return True, class_var
        return False, class_var


class Checker:
    """Класс реализирующий проверку телефона, ФИ, даты на валидность."""

    def __init__(self):
        """Записываем текущую дату."""
        today = date.today()
        self.year = today.year
        self.month = today.month
        self.day = today.day

    @txt_logger
    def check_phone(self, phone_number: str) -> bool:
        """Метод проверки телефонного номера."""
        class_var = 'phone'
        checked = False
        valid_len_phone_number = 11
        if type(phone_number) is str:
            if len(phone_number) == valid_len_phone_number:
                if phone_number.isdigit():
                    if phone_number.startswith('8'):
                        checked = True
        return checked, class_var

    @txt_logger
    def check_fullname(self, fullname: str) -> bool:
        """Метод проверки фамилии имени."""
        class_var = 'fullname'
        min_len_name = 2
        check = False
        if fullname.count(' ') <= 0:
            return False, class_var
        if fullname.count(' ') > 0:
            name, second_name = fullname.split(' ')
            if name.isalpha() and second_name.isalpha:
                if len(name) >= min_len_name and len(second_name) >= min_len_name:
                    return True, class_var
        return check, class_var

    @txt_logger
    def check_date(self, check_date: str) -> bool:
        """Функция проверяющая валидность даты и возвращающая bool.

        1)Раскладываем на список вводимую дату(YYYY-MM-DD).
        2)Сравниваем с текущей датой, возвращаем boolean.
        """
        class_var = 'date'
        check = False
        if check_date.count('-') == 2:
            check_date = map(int, check_date.split('-'))
            checked_year, checked_month, checked_day = check_date
            if checked_year >= self.year:
                if checked_year > self.year:
                    check = True
                if checked_month >= self.month:
                    if checked_month > self.month:
                        check = True
                    if checked_day > self.day:
                        check = True
        return check, class_var
