from collections import UserDict


class CountPhoneNumberError(Exception):
    pass


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__ (self, value):
        super().__init__(value)


class Phone(Field):
    
    def __init__ (self, value):
        super().__init__(value)

    def validate_number(self):
        if len(self.value) != 10:
            print("The number must consist of the ten digits.")
            return False
        return True
    


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones: list(Phone) = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {' '.join(p.value for p in self.phones)}"

    def add_phone(self, phone: Phone):
        phone_obj = Phone(phone)
        if phone_obj.validate_number():
            self.phones.append(Phone(phone))

    def remove_phone(self, phone: str) -> None:
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)

    def edit_phone(self, phone: str, new_phone: Phone):
        new_phone_object = Phone(new_phone)
        if new_phone_object.validate_number():
            for p in self.phones:
                if p.value == phone:
                    p.value = new_phone_object.value
        return "The number is not correct."

    def find_phone(self, phone: str):
        found_phones = list(filter(lambda p: p.value == phone, self.phones))
        print(f"Users {self.name.value} phone numbers found: ")
        if found_phones:
            for found_phone in found_phones:
                print(f"{found_phone.value.ljust(5)}")
        else:
            print("Number not found.")


class AddressBook(UserDict):
    
    def add_record(self, record):
        self.data[record.name.value] = record

    def delete_record(self, name):
        del self.data[name]

    def find_record(self, name):
        if self.data.get(name):
            print(self.data.get(name))
        else:
            print("Record not found!")

    def print_contacts(self):
        for numbers in self.data.values():
            print(f"{numbers};")


book = AddressBook()


user01 = Record("Patrick")
user01.add_phone("0011223343")
user01.add_phone("0011223344")
user01.add_phone("0011223345")


user02 = Record("Alice")
user02.add_phone('3809766314')
user02.add_phone('3809766314')
user02.add_phone('3809766314')


user03 = Record("No Name")
user03.add_phone('3809766314')
user03.add_phone('3809766314')
user03.add_phone('3809766314')

# Добавляю юзерів
user_list = [user01, user02, user03]
for user in user_list:
    book.add_record(user)

# Вивожу всю базу
book.print_contacts()

# Видаляємо запис
book.delete_record('No Name')

# Вивожу всю базу
print('Deleted:', '-' * 10)
book.print_contacts()

# Шукаємо в контактах
print("Finded:", '-' * 10)
book.find_record("Patrick")

print("Finded:", '-' * 10)
book.find_record("Palala")

# Змінюємо номер Патріка
print("Not Changed:", '-' * 10)
user01.edit_phone('0011223345', '00')
book.find_record("Patrick")
print("Changed:", '-' * 10)
user01.edit_phone('0011223345', '0000000000')
book.find_record("Patrick")
