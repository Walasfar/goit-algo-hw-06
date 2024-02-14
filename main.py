from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        super().__init__(value)


class Phone(Field):

    def __init__(self, value):
        super().__init__(value)
        
        if not self.validate_number():
            raise ValueError("Неправельний номер телефону.")
    
    def validate_number(self):
        return len(self.value) == 10 and self.value.isdigit()


class Record:
    
    def __init__(self, name: Name):
        self.name = Name(name)
        self.phones: list(Phone) = []

    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, phone: Phone):
        
        try:
            phone_obj = Phone(phone)    
        except ValueError as e:
            return f"Error: {e}"
        
        for p in self.phones:
            if  p.value == phone_obj.value:
                return "Phone already exist."
        else:
            self.phones.append(phone_obj)

    def delete_phone(self, phone: str):
        self.phones = list(filter(lambda p: p.value != phone, self.phones))

    def edit_phone(self, phone: str, new_phone: str):
        new_phone_obj = Phone(new_phone)
        for p in self.phones:
            if p.value == phone:
                p.value = new_phone_obj.value

    def find_phone(self, phone: str):
        for p in self.phones:
            if p.value == phone:
                return f"{self.name.value}'s phone finded: {p.value}"
            else:
                return 'Number not found.'


class AddressBook(UserDict):
    
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find_record(self, name: str):
        try:
            return self.data[name]
        except KeyError:
            return f"Record '{name}' does not exist."
        
    def delete_record(self, name: str):
        del self.data[name]

    def show_contacts(self):
        result = ""
        for name, record in self.data.items():
            result += f"{record}\n"
        return result


book = AddressBook()


user01 = Record('John')
user01.add_phone('8888888888')
user01.add_phone('0000000000')
user01.add_phone('3806822212')

user02 = Record('Elena')
user02.add_phone('3809713312')
user02.add_phone('4867133150')


user03 = Record('No name')
user03.add_phone('3809722212')
user03.add_phone('4867133555')

contacts = [user01, user02, user03]

for contact in contacts:
    book.add_record(contact)
    
print(book.show_contacts())

book.delete_record('No name')

print("\nПісля видалення записуа: ", '-' * 10)
print(book.show_contacts())

print("\nПомилкові вводи номеру: ", '-' * 10)
print(user01.add_phone('000000000')) # Недостатньо чисел
print(user01.add_phone('000000000d')) # Містить букву

print("\nНормальний ввід номеру: ", '-' * 10)
print(user01.add_phone('0000000000')) # Додаємо існуючий
print(user01)

user01.delete_phone('8888888888')
print(user01)

print("\nМіняємо номер: ", '-' * 10)
print(user01)
user01.edit_phone('0000000000', '0000011111')
print(user01)

print("\nШукаємо номер: ", '-' * 10)
print(user01.find_phone('0000011111'))
print(user01.find_phone('0000011121'))


print("\nШукаємо запис в базі: ", '-' * 10)
print(book.find_record('John'))
print(book.find_record('Lalka'))




