from collections import UserDict


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
            print("Not found.")


class AddressBook(UserDict):
    
    def add_record(self, record: Record):
        if record not in self.data:
            self.data[record.name.value] = record
        else:
            print(f"Record: '{record}'' already exists.")

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
user02.add_phone('3809766555')
user02.add_phone('3809766777')


user03 = Record("No Name")
user03.add_phone('3809766314')
user03.add_phone('3809766222')
user03.add_phone('3809766333')

# Добавляю юзерів
user_list = [user01, user02, user03]
for user in user_list:
    book.add_record(user)

# Вивожу всю базу
book.print_contacts()

# Видаляємо запис
book.delete_record('No Name')

# Добавляємо існуючого користувача
print("\nAlready exists:", '-' * 10)
book.add_record('Patrick')

# Вивожу всю базу
print('\nDeleted:', '-' * 10)
book.print_contacts()

# Шукаємо в контактах
print("\nFinded:", '-' * 10)
book.find_record("Patrick")

print("\nFinded:", '-' * 10)
book.find_record("Palala")

# Змінюємо номер Патріка вводячи неправельний номер
print("\nNot Changed:", '-' * 10)
user01.edit_phone('0011223345', '00')
book.find_record("Patrick")

# Змінюємо на правельний
print("\nChanged:", '-' * 10)
user01.edit_phone('0011223345', '0000000000')
book.find_record("Patrick")

# Шукаємо номер
print("\nFinded:", '-' * 10)
user02.find_phone('3809766314')

# Шукаємо неіснуючий номер
print("\nFinded:", '-' * 10)
user02.find_phone('8803766314')
