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
            return e
        
        for p in self.phones:
            if  p.value == phone_obj.value:
                return "Phone already exist."
        else:
            self.phones.append(phone_obj)

    def remove_phone(self, phone: str):
        self.phones = list(filter(lambda p: p.value != phone, self.phones))
        
        
    def edit_phone(self, phone: str, new_phone: str):
        try:
            if not any(p.value == phone for p in self.phones):
                raise ValueError("Номер який Ви хочете змінити - не існує.")
            
            new_phone_obj = Phone(new_phone)
            for p in self.phones:
                if p.value == phone:
                    p.value = new_phone_obj.value
                    
        except ValueError as e:
            return e

    def find_phone(self, phone: str):
        for p in self.phones:
            if p.value == phone:
                return p
            else:
                return None


class AddressBook(UserDict):
    
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name: str):
        return self.data.get(name)
        
    def delete(self, name: str):
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

book.delete('No name')

print("\nПісля видалення запису: ", '-' * 10)
print(book.show_contacts())

print("\nПомилкові вводи номеру: ", '-' * 10)
print(user01.add_phone('000000000')) # Недостатньо чисел
print(user01.add_phone('000000000d')) # Містить букву

print("\nНормальний ввід номеру: ", '-' * 10)
print(user01.add_phone('0000000000')) # Додаємо існуючий
print(user01)

user01.remove_phone('8888888888')
print(user01)

print("\nМіняємо номер: ", '-' * 10)
print(user01)


print(user01.edit_phone('1000000000', '0000011111'))
user01.edit_phone('0000000000', '0000011111')

print(user01)

print("\nШукаємо номер: ", '-' * 10)
print(user01.find_phone('0000011111'))
print(user01.find_phone('0000011121'))


print("\nШукаємо запис в базі: ", '-' * 10)
print(book.find('John'))
print(book.find('Lalka'))
